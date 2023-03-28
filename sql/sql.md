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

```
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

It is now possible to interact with process and modules of the classes.

Now we can start to really create a django application based on that.

First, we change the "urls.py" to add this new address:

```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index')
]
```

After, we add a views:
```
from django.shortcuts import render

try:
    from sql.airline.flights.models import Flight
except:
    from flights.models import Flight

# Create your views here.
def index(request):
    return render(
        request, "flights/index.html",
        {"flights": Flight.objects.all()}
    )
```

Finally, we need to construct the index.html inside the templates files, which will have a basic html format in the "layout:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Flights</title>
    </head>
    <body>
        {% block body %}
        {% endblock %}
    </body>
</html>
```
To which we will add a body:
```
{% extends "flights/layout.html" %}

{% block body %}

    <h1>Flights</h1>
    <ul>
        {% for flight in flights %}
            <li>Flight {{ flight.id }}: {{ flight.origin }} to {{ flight.destination }}</li>
        {% endfor %}
    </ul>

{% endblock %}
```

Finally, we can run  http://127.0.0.1:8000/flights and get the results!

Now, lets look at the airports of the database:
```
python manage.py shell
```

```
from flights.model import *
Airport.objects.all()
```

will  return:
```
<QuerySet [<Airport: New York (JFK)>, <Airport: London (LHR)>, <Airport: Paris (CDG)>, <Airport: Tokyo (NRT)>]>
```

We can also filter the query:
```
Airport.objects.filter(city="New York")
```

Than, to make sure we get only one object, we use `get` steady of filter:
```
Airport.objects.get(city="New York")
```
There, we can set that to an object and use it to create a flight:
```
jfk = Airport.objects.get(city="New York")
cdg = Airport.objects.get(city="Paris")
f = Flight(origin=jfk, destination=cdg, duration=435)
f.save()

f = Flight(origin=cdg, destination=jfk, duration=415)
f.save()
```

But we do not need to do that for every time we want to manipulate and add database.

Django has an admin app.

In the urls.py, we have already seen the "urlpatterns" with this admin:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', include("flights.urls")),
]
```
To use this, we need to create a admin account.

To do that, we use:

```
python manage.py createsuperuser
```
From there, we need to add a user, email and password.

```
python manage.py createsuperuser
Username (leave blank to use 'furbano'): fernando-urbano
Email address: fernando.rocha.urbano@gmail.com
Password:
Password (again):
Superuser created successfully.
```

Now, we have to work in the 'admin.py', in which we can register the classes we create to manipulate those from the admin app. The changes done in the admin app are:
```
from django.contrib import admin

try:
    from sql.airline.flights.models import Flight
except:
    from flights.models import Flight, Airport

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
```

Now, if we run the server and go the "admin" part of the app:
```
python manage.py runserver
```
http://127.0.0.1:8000/admin/login/?next=/admin/

There, we can change the sql tables and modify the underlying models.

We have just added more airports and flights to the database.

Now we want every flight to have its own page. To do that, we need to add the link of the flight to the "urlpatterns":

```
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:flight_id>", views.flight, name="flight")
]
```

After that, we must create a function in views.py to reference this urlpattern. The function must have the same name as the "name" in the urlpattern:

```
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight
    })
```
We can also use "pk", which stends for "primary key", steady of id:

```
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight
    })
```

After that, we must create the html that has those urls, which will have the named specified above (flight.html):

```
{% extends "flights/layout.html" %}

{% block body %}

    <h1>Flights {{ flight.id }}</h1>
    <ul>
        <li>Origin: {{ flight.origin }} </li>
        <li>Destination: {{ flight.destination }} </li>
        <li>Duration: {{ flight.duration }} </li>
    </ul>

{% endblock %}
```

Now we check specific flights!

Now we are going to add Passengers to the flights!

This is a many-to-many relationship.
The many-to-many relationship allows for a passenger to be in multiple flights and for a flight to have multiple passengers.

For that, is necessary to have this kind of class inside the models.py:

```
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
```

In this way, we can add multiple flights to a passenger.
The `blank=True` refers to the fact that a passenger can have no flights.
The `related_name="passengers"` refers to the fact that we can access the passangers of a flight using this attribute to the flight.

After we finished creating this change, we must apply the migrations:
```
python manage.py makemigrations
python manage.py migrate
```
```
python manage.py makemigrations
Migrations for 'flights':
  flights\migrations\0004_passenger.py
    - Create model Passenger
PS C:\Users\furbano\Desktop\personal\cs50w\sql\airline> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, flights, sessions
Running migrations:
  Applying flights.0004_passenger... OK
```

The changes are made and we should add Passengers to the admin.py! We go the admin.py and add the Passenger:

``from django.contrib import admin

try:
    from sql.airline.flights.models import Flight
except:
    from flights.models import Flight, Airport, Passenger

# Register your models here.
```
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)`
```

Now, to view the passengers in the flights url, we can add in "views.py":
```
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })
```
Than, we should modify the html to have:
```
{% extends "flights/layout.html" %}

{% block body %}

    <h1>Flight {{ flight.id }}</h1>
    <ul>
        <li>Origin: {{ flight.origin }} </li>
        <li>Destination: {{ flight.destination }} </li>
        <li>Duration: {{ flight.duration }} </li>
    </ul>

    <h2>Passengers</h2>
    <ul>
        {% for passenger in passengers %}
            <li>{{ passenger }}</li>
        {% empty %}
            <li>No passengers.</li>
        {% endfor %}
    </ul>


{% endblock %}
```
The `{% empty %}` is used if the list of passengers is empty.

To not need to manually change pages, we can add a link to go back to the page we want. Therefore, we add the hyperlink in the end of the page:

```
{% extends "flights/layout.html" %}

{% block body %}

    <h1>Flight {{ flight.id }}</h1>
    <ul>
        <li>Origin: {{ flight.origin }} </li>
        <li>Destination: {{ flight.destination }} </li>
        <li>Duration: {{ flight.duration }} </li>
    </ul>

    <h2>Passengers</h2>
    <ul>
        {% for passenger in passengers %}
            <li>{{ passenger }}</li>
        {% empty %}
            <li>No passengers.</li>
        {% endfor %}
    </ul>

    <a href="{% url 'index' %}">Back to Flight List</a>

{% endblock %}
```

Furthermore, in the Flight List, we add hypterlinks as well, specifying the flight id:

```
{% extends "flights/layout.html" %}

{% block body %}

    <h1>Flights</h1>
    <ul>
        {% for flight in flights %}
            <li>
                <a href="{% url 'flight' flight.id %}">
                    Flight {{ flight.id }}: {{ flight.origin }} to {{ flight.destination }}
                </a>
            </li>
        {% endfor %}
    </ul>

{% endblock %}
```

Now we have linked the pages together!

Now, we want to be able to add a passenger to a particular flight. We will do that by adding a new url to he "urlpatterns". For that, we add a "book" inside each flight:

```
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),
]
```

Now it is important to separate: we can request a webpage with a get message or a post message. A get message is used to "get the page", while the post message is used to manipulate data and do something in the system.

Inside the page, for this particular example, we assume that the input field used is inside a post json with key "passenger".

After that, we use this key to get the row of the table Passenger that has this id and create the object.
The object automatically has the the possibility to add a flight (a method).
Finally, the "return" part of the function is used to update the page. The "reverse" makes it happen.

```
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id, )))
```

Now we have to add the form that will make this post request! We will do it inside the "flight.html":

```
    {% extends "flights/layout.html" %}

    {% block body %}

        <h1>Flight {{ flight.id }}</h1>
        <ul>
            <li>Origin: {{ flight.origin }} </li>
            <li>Destination: {{ flight.destination }} </li>
            <li>Duration: {{ flight.duration }} </li>
        </ul>

        <h2>Passengers</h2>
        <ul>
            {% for passenger in passengers %}
                <li>{{ passenger }}</li>
            {% empty %}
                <li>No passengers.</li>
            {% endfor %}
        </ul>

        <h2>Add Passenger</h2>

        <form action="{% url 'book' flight.id %}" method="post">
            {%  csrf_token %}
            <select name="passenger">
                {% for passenger in non_passengers %}
                    <option value="{{ passenger.id }}">{{ passenger }}</option>
                {% endfor %}
            </select>
            <input type="submit">
        </form>

        <a href="{% url 'index' %}">Back to Flight List</a>

    {% endblock %}
```

Looking specifically at the "Add Passenger", we have:
- an action, which specifies that the method is a post
- a csrf_token, which specifies that is a security token specifying that the request comes from inside the application.
- a list to select from: in this list the new passenger can be any passenger who is not already in this flight, which is a data available in the "non_passengers". The non_passenger variable had to be passed in "views" in the same way as every other. In the following code, the "Passenger.objects.exclude" excludes the rows of the table passenger which have the flight.id equal to the refered id.
```
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight.id).all()
    })
```
- an input, which will submit the post request.

## Building Extra Functionalities for Admin
The admin page can be configure to make it nicer to see or to edit.
For instance, we can change the list_display

```
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
    
class PassengersAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights", )

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengersAdmin)
```

This changes the way the classes are presented.
For instance the "list_display" shows how the admin will view the attributes of the class.

# Users
To build users, we need to craate another app called "users". First, inside the commmand prompt we add:
```
python manage.py startapp users
```
Second, we need to add this app in the settings.py:
```
INSTALLED_APPS = [
    'flights',
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
Third, we need to add the users in "urlpatterns" inside the "urls.py" of the project folder:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', include("flights.urls")),
    path('users/', include("users.urls")),
]
```
Fourth, we need to create a urlpatterns for the app, which will be inside the app. We create the "urls.py" and add this script:

```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]
```
In this case, we are already adding three different urls.
Fifth, we work with the app's views. Inside, we first look at the index. Inside the index, we want to make sure that the user is authenticated. To assure that the user is authenticated, we check if the attribute user in the request has an attribute authenticated equals to True. It is worth to mention that the request always has the user attribute.

```
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
```
So if the user is not authenticated, we require an authentication from the user. We use the same function as before, redirects the user to a login url (which has not yet been created).

...now we create the login views:
```
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    

def login_request(request):
    return render(request, "users/login.html")
```

...and now we create a template folders, which will have a folder with the name of the app inside in which we will have the html files. The first html file will be the layout:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Users</title>
    </head>
    <body>
        {% block body %}
        {% endblock %}
    </body>
</html>
```
Later, we create the login.html which will extend the layout.html:

```
{% extends "users/layout.html" %}

{% block body %}

    <form action="{% url 'login' %}" method="post">
        {%  csrf_token %}
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">  
        <input type="login" value="Login">
    </form>

{% endblock %}
```

From there, we run the server again and start to add users. The users can have different level of access.

After, we go to "users/login" where we can make the login with any of the users.

Now we need to to implement what the login will do. To this kind of request, we must implement a POST method, because we cannot have the password inside the url.

We can authenticate the user using `from django.contrib.auth import authenticate, login, logout`:
```
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "users/login.html")
```
Furthermore, we add an optional "message". If it exists in the render html, it is displayed. For that, we add in the login.html:

```
{% extends "users/layout.html" %}

{% block body %}

    {% if message %}
        <div>{{ message }}</div>
    {% endif %}

    <form action="{% url 'login' %}" method="post">
        {%  csrf_token %}
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">  
        <input type="submit" value="Login">
    </form>

{% endblock %}
```

Now, if the user is authenticated, the login will return to "index", but the index has not yet been created. We must create it.

First we change the index to render an html:

```
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")
```
Than we create, inside the templates/users the "user.html":
```
{% extends "users/layout.html" %}

{% block body %}

    <h1>Welcome, {{ request.user.first_name }}</h1>
    <h4>Username: {{ request.user.username }}</h4>

{% endblock %}
```

Finally, we create the logout that just returns to the login page:
```

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
```

Finally, we craete a hyperlink in the user.html that gives the request of this last function:

```

```



































