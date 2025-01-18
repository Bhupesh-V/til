# Getting JSON data from PostgreSQL



To extract data in json from a table without specifying column names

```sql
select to_json(t) from table t where id=34;
```

From [docs](https://www.postgresql.org/docs/13/functions-json.html)

> Converts any SQL value to json or jsonb. Arrays and composites are converted recursively to arrays and objects (multidimensional arrays become arrays of arrays in JSON). Otherwise, if there is a cast from the SQL data type to json, the cast function will be used to perform the conversion;[a] otherwise, a scalar JSON value is produced. For any scalar other than a number, a Boolean, or a null value, the text representation will be used, with escaping as necessary to make it a valid JSON string value.
