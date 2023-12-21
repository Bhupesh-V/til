# Google's Golang UUID package has a nice side effect for handling UUID Arrays on PostgreSQL
**_Posted on 21 Dec, 2023_**

Ever seen this error while scanning a Postgres column containing an array of UUIDs when using an ORM with Go?

```
sql: Scan error on column index 15, name \"column_uuids\": unsupported Scan, storing driver.Value type string into type *[]uuid.UUID
```

If you work with Golang, you will know that while reading a list of UUIDs from a Postgres column, you might have to implement a custom scanner to handle the conversion to `[]uuid.UUID` type.

Here's a sample implementation of the scanner interface for the `[]uuid.UUID` type.

```go
package uuid

import (
	"fmt"
	"strings"

	"github.com/google/uuid"
)

type UUIDSlice []uuid.UUID

// Implementing the Scanner interface for the UUIDSlice type
func (u *UUIDSlice) Scan(value interface{}) error {
	if value == nil {
		*u = make(UUIDSlice, 0)
		return nil
	}
	strValue, ok := value.(string)
	if !ok {
		return fmt.Errorf("unsupported Scan, storing driver.Value type %T into type UUIDSlice", value)
	}

	if strValue == "{}" {
		// Check for an empty UUID array representation in the database
		*u = make(UUIDSlice, 0)
		return nil
	}

	uuidStrings := strings.Split(strValue, ",") // Assuming UUIDs are stored as a comma-separated string
	result := make(UUIDArray, len(uuidStrings))

	for i, uuidStr := range uuidStrings {
		parsedUUID, err := uuid.Parse(uuidStr)
		if err != nil {
			return err
		}
		result[i] = parsedUUID
	}

	*u = result
	return nil
}
```

> It would be nice if it was available on pq just like [`pq.StringArray`](https://pkg.go.dev/github.com/lib/pq#StringArray)

If you notice, this piece of code would look bugy at the first glance.

```go
	uuidStrings := strings.Split(strValue, ",") // Assuming UUIDs are stored as a comma-separated string
	result := make(UUIDArray, len(uuidStrings))

	for i, uuidStr := range uuidStrings {
		parsedUUID, err := uuid.Parse(uuidStr)
		if err != nil {
			return err
		}
	...
	}
```

What happens if the `strValue` is `{5d80b766-7b0b-4638-8315-e1d58cd42996}`? I forgot to strip the curly braces from the string, right?. So the `len(uuidStrings)` will return `36 + 2` and ideally this code should fail while parsing the UUID on `uuid.Parse(uuidStr)`. But it doesn't.

The reason is that `uuid.Parse()` method assumes it's a ["Microsoft GUID"](https://learn.microsoft.com/en-us/dynamicsax-2012/developer/guids#string-representations-of-a-guid) and parses it accordingly. So the above code will work even if the curly braces are not stripped from the string, and you will get a `uuid.UUID` type.

See `uuid.Parse()` method's implementation [here](https://github.com/google/uuid/blob/master/uuid.go#L81-L83)
