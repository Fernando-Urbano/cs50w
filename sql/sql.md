# SQL
Is a database language.

When we deal with relational databases, we store data in tables.
Each table has rows and columns.
Now, we will use an example of flights and the table will contain: origin, destination and length of the flight.

There are multiple database management systems:
- MySQL and PostgreSQL are generally used on more large scale. Permits to have the database server separated from the application server, for instance, which facilitates debugging and testing.
- SQLite only has one table and is often used for smaller applicatations. It will make it easier to start.

## Types in SQL
Each database system has a different variety of types. SQLite has:
- TEXT
- NUMERIC (other numeric)
- INTEGER
- REAL 
- BLOB (binary large object): files, image, etc...

MySQL has a longer list of types that it supports:
- CHAR(size): takes an argument of size. Advantageous when we know the ammount of characters. Will make it more efficient.
- VARCHAR(size): takes an arguement of maximum size. Sometimes it will be fewer characters.
- SMALLINT: use different number of bytes.
- INT
- BIGINT
- FLOAT
- DOUBLE: stores floats with more information (more precision because it uses more bytes).
- etc

## Create a table inside a database
Syntax for creating a table in SQLite:
```
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL,
)
```
The name of the table will be "flight". After we are creating the structure of the table.

The "id" is a identifier and it is a way to make sure we can access each of the observations.

Furthermore:

