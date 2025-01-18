# Clustered & Non-clustered Indexes


## Clustered
- Organises data "physically" on disk.
- Only 1 Clustered is possible. Since it "organises" data in 1-way. Every time you re-organise, you have a new clustered index.
- E.g Dictionary
- A primary key is usually the one which is used for clustered index. (It doesn't have to be)
- Makes queries faster as only the data/disk block is loaded which contains the clustered data. This reducing disk I/O


## Non-clustered
- Points to data directly.
- Possible to have a lot of non-clustered indexes. Since its just a "data-structure" to speed up the process of looking something up.
- E.g Appendix at the back of book.
- Better for queries like `SELECT * FROM TABLE WHERE name='bhupesh'` assuming we have a non-clustered index on column `name` and you have a bunch of rows with name as 'bhupesh'.

