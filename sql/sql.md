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

Furthermore, that are many constraints:
- CHECK: check that the number is true or false, or in a certain range.
- UNIQUE: cannot repeat.
- PRIMARY: how we find the element.
- NOT NULL: not null data.

## Adding data to the table
We use the INSERT.

```
INSERT INTO flights
    (origin, destination, duration)
    VALUES ("New York", "London", 415)
```
The flight is the name of the table.

We have to specify the columns to which we are adding in the first list.

# SQL Queries
We use the SELECT query.
```
SELECT * FROM flights
```
`*` means all

## Only select some columns
```
SELECT origin, destination FROM flights
```

## Only select specific rows
```
SELECT * FROM flights WHERE id = 3;
```
Only select where id equals 3.
Can filter from any column.

## How to create a new database?
Go to terminal and:
```
touch flights.sql
```

Now we can write SQL commands in terminal using:
```
sqlite3 flights.sql
```

Now we create a table:
```
CREATE TABLE flights (
...>         id INTEGER PRIMARY KEY AUTOINCREMENT,
...>         origin TEXT NOT NULL,
...>         destination TEXT NOT NULL,
...>         duration INTEGER NOT NULL
...> );
```

To finish a query, it is necessary to add a ";" in the end.

Now we add data:
```
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 415);
```

Now we can view the query!

## Good query visualization
```
sqlite > .mode columns
sqlite > .headers yes
```

# Queries comparisons
The query can interpret many comparisons (AND, OR, >, <, >= , <=, etc).
```
SELECT * FROM flights WHERE origin IN ('New York', 'Lima')
```

LIKE is used as well:
```
SELECT * FROM flights WHERE origin LIKE "%a%";
```

The "%a%" means: %: 0 or more characters of any kind; followed by the letter "a"; followed by %: 0 or more characters of any kind

## Update data
How to update data:
```
UPDATE flights
    SET duration = 430
    WHERE origin = 'New York'
    AND destionation = 'London';
```

## Delete data
```
DELETE flights
    WHERE destination = 'Tokio'
```

## Other Clauses
LIMIT: limit the amount of results
ORDER BY: how the results will be ordered
GROUP BY: group rows by column
HAVING: constraint inside a group by

# Joining Tables
In a ".sql" we have multiple tables, that can have relationship between them.

Now lets say, that we also need the airport code.

We could add the airport code in the same table or add it in another table!

...or we can have it in another table.

From that, we can shift the table that we have right now to origin_id, and destination_id and have the id created in another table.

flights:
```
INSERT INTO flights (
    origin_id, destination_id, duration
) VALUES (
    1, 2, 415
);
```
airports:
```
INSERT INTO airports (
    id, airport, city
) VALUES (
    1, "NYC", "New York"
);
INSERT INTO airports (
    id, airport, city
) VALUES (
    2, "LDN", "London"
);
```

Later, we could add a passengers table were we can have the flights the passenger is:
```
INSERT INTO passengers (
    first_name, last_name, flight_id
) VALUES (
    "Harry", "Potter", 1
);
```
Nevertheless, this would make it impossible for the passenger to have been in more than one flight.
For that, we have one-to-many, one-to-one, many-to-many, many-to-one relationships.

For instance, if we have a flight that might have multiple passengers, and people that can be passengers in multiple flights, we could:
- have a database called people.
- have a database of flights
- have a database of passengers in which we only have two columns:
```
person_id       flight_id
---------       ---------
    1               2    
    3               2
    4               1
    1               1
    4               3
    2               7
```
This is known as an association table.

We link person_id and flight_id.

But now the tables are a little messy to look at... therefore, we got make joins!

```
SELECT
    *
FROM
    passengers
JOIN
    flights
    ON passengers.flight_id = flights.id
JOIN
    people
    ON passengers.person_id = people.id
```
We will have a good way to visualize the results.

The default jon is a INNER JOIN
There are also:
- LEFT OUTER JOIN
- RIGHT OUTER JOIN
- FULL OUTER JOIN

## More efficient queries: CREATE INDEX
We create a way to go to the right page and section.

It takes memory to construct, but it helps to achieve better results.

```
CREATE INDEX name_index ON passengers (last_name);
```

Being the last_name the name of the column. We use that because it takes memory, but becomes faster.

## Dangers: SQL Injection Attack
A danger of SQL: a security fulnerability.
In a login, if a hacker wants to use "--", the SQL will consider every thing afterwards as comments.

Therefore, he can will be able to access it!

Therefore, we have to:
- make SQL treat the "--" as literal quotation and literal -.
- use a abstraction inside of SQL so we do not have to add SQL queries at all.

## Danger: Race Condition
Another danger of SQL, which happens due to parallel threads: two people accessing and changing the tables at the same time.

Strategies:
- work with a lock: while someone is using the database, another person cannot use it.
- use django

## Starting one project
```
> django-admin startproject airline
> cd airline
> python manage.py startapp flights
```

After that, we:
- add the flights app in the settings.
- add the include("flights.urls") in the urls.py in the project
- add a urls.py file in flights app.

# Modules
Now, to use databases, we use models.py.

The models.py is present in every application.

In that, we define which models are going to exist in our application.

We can thing as having one model for each of the tables we think about storing information.

```
from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
```

# Migrations
Now that we have created the database, we can tell Django to use the models created to include information about the models. We call that process migration:
changes I would like to apply to the database. Take those changes and apply them to the database.

We use that as:
```
python manage.py makemigrations
```

The following will happen:
```
Migrations for 'flights':
  flights\migrations\0001_initial.py
    - Create model Flight
```
In flights (the app) there will be a migrations directory with a python file: 0001_initial.py

```
# Generated by Django 4.1.4 on 2023-01-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=64)),
                ('destination', models.CharField(max_length=64)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
```
After that, it is necessary to apply the migrations:
```
python manage.py migrate
```
This leads to:
```
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying flights.0001_initial... OK
  Applying sessions.0001_initial... OK
```
Where we can see that the flights migration was applied.
Now, there will be a "db.sqlite3" file that will contain a table that will store all the flights.

Now, we can:
- use the SQL to write the queries and construct the table, or...
- we can use django abstraction to be able to do so by using Python classes, methods, etc...

# Shell
For that, we use in the terminal:
```
python manage.py shell
```
Shell is a command location and a way for us to write python commmands that get executed.

After that:
```
from flights.models import Flight
```

Now we can create new flights!!

```
f = Flight(origin="New York", destination="London", duration=415)
```

After we create it, we must save it inside the table by using:
```
f.save()
```

To query those objects:
```
Flights.objects.all()
```
which will return:
```
<QuerySet [<Flight: Flight object (1)>]>
```

To represent the flight in a nicer way, we can have a string representation of the flight inside of the model created:

````
from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.origin} to {self.destination}"
```

Now if we go back to the shell and press Crtl + D, we exit the shell in a way to make the changes work.

After we enter in the shell again the command `Flights.objects.all()` returns:
```
In [2]: from flights.models import Flight

In [3]: Flight.objects.all()
Out[3]: <QuerySet [<Flight: 1. New York to London>]>
```

To get for instance the first flight, we use:
```
In [6]: flights = Flight.objects.all()

In [7]: flight = flights.first()
```
We can view the attributes of the flight as any other python object.

```
flight.duration
flight.destination
```

Furthermore, to delete the flight:
```
flight.delete()
```

Nevertheless, as we saw before, we wanted to use it in another way: linking by the id.

Therefore, we should create:

```
from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="departures"
    )
    destination = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="arrivals"
    )
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.origin} to {self.destination}"
```

- we create an Airport class with city and code.
- we use the `models.ForeignKey` to reference to the Airport class.
- we use `on_delete=models.CASCADE`, which references the idea that, if an airport is deleted from the database Airport, the Flights that contain that airport should all be deleted.
- we use `related_name="departures"` which is used by us to make relations from the Flight to the airport. In other words, a way for us to later views all the flights that have an origin in that airport. The same is done for destinations.

Now... we need to make migrations again.
```
>python manage.py makemigrations

flights\migrations\0002_airport_alter_flight_destination_alter_flight_origin.py
    - Create model Airport
    - Alter field destination on flight
    - Alter field origin on flight
```

And than migrate...
```
>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, flights, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying flights.0001_initial... OK
  Applying flights.0002_airport_alter_flight_destination_alter_flight_origin... OK
  Applying sessions.0001_initial... OK
```

Now we use shell again to create an airport.

```
In [2]: from flights.models import *
In [3]: jfk = Airport(code="JFK", city="New York")
In [4]: jfk.save()
```
```
In [5]: lhr = Airport(code="LHR", city="London")
In [6]: lhr.save()
In [7]: cdg = Airport(code="CDG", city="Paris")
In [8]: cdg.save()
In [9]: nrt = Airport(code="NRT", city="Tokyo")
In [10]: nrt.save()
```

Now we can create a flight!
```
f = Flight(origin=jfk, destination=lhr, duration=415)
f.save()
```

For instance, the flight origin is an attribute which is another object:
```
In [14]: f.origin
Out[14]: <Airport: New York (JFK)>

In [15]: f.origin.city
Out[15]: 'New York'
```

Now, we use as well the related_name:
```
In [19]: jfk.departures.all()
Out[19]: <QuerySet [<Flight: 1. New York (JFK) to London (LHR)
```

This give us the hability to manipulate the objects and their relation to SQL.