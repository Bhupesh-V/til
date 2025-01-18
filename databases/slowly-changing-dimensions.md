# Slowly Changing Dimensions (SCD)



Slowly Changing Dimensions (SCD) are dimensions that change slowly over time, rather than changing on a regular schedule.

## Type 0: Retain Original

- Attributes that never change.
- Ex. Date of birth.

## Type 1: Overwrite

- No history is kept.
- Overwrite the old data with new data.

## Type 2: Add New Row

- A new row is added to the table.
- Attributes like `start_date` and `end_date` are used to track the history.
- Optionally, a `current_flag` (y/n) column can be used to track the latest version of data.

## Type 3: Add New Attribute

- Maintains a limited history.
- Records the old and new values in the same row using separate columns. Hence only last 2 versions are stored.

## Type 4: Add New (history) Table

- Maintains a full history of changes.
- A new table is created to store the history of changes.
- The original table is used to store the current data.

TODO: add examples for each type and read more about type 5 and 6.

## Resources

https://www.sqlshack.com/implementing-slowly-changing-dimensions-scds-in-data-warehouses/