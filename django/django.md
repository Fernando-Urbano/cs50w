# Django
# Web Applications
Django will dynamically generate HTML and CSS to build web application.
Only using HTML and CSS, the page would be identical everytime we looked at it.

# HTTP
Is a protocol we use in web development: HTTP stends for Hypertext Transfer Protocol and it is the protocol by how messages are sent back and forth.

The server will contain the web application. The client will give a request and the server will return a response.

An example of a request:
```
GET / HTTP/1.1
Host: www.example.com
```

The server will give a response like that:
```
HTTP/1.1 200 OK
Content-Type: text/html
```

The Content-Type shows what should be rendered.

Common status codes:
200: ok
301: moved permanently
403: forbidden
404: not found
500: internal server error

# Django Intro
It is a framework. First think to do is install django:
```
pip3 install Django
```

To create a project:
```
django-admin startproject {project_name}
```

In the case, we created the project example, which becomes a folder with some files already.

Some files are:
`manage.py`: file to execute commands in the django project. We won`t need to touch it probably.
`settings.py`: contains configurations settings. We mind want to change some settings.
`urls.py`: table of contents which can be visited.

How to run the application:
```
python manage.py runserver
```

Will give the following result:

```
Django version 4.1.4, using settings 'example.settings'
Starting development server at http://127.0.0.1:8000/
```

Port 8000 is one of the local ports we have in the local computer.

When we paste the url in the internet, we can see it.

# Routes
One django project may have many different applications (Google maps, Google images, Google news, etc...). Django comes with this idea to create separate apps with different capacities.

To create an app we use:
```
python manage.py startapp {name of app}
```

The previous code will create a directory with the name of the app.

Now, to have the app available, we must add it in the project installed apps.

In {project name}/settings.py, go to INSTALLED_APPS and add the new project

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '{app name}'
]
```

Now, to add something in the app, we goal to the app directory and head to "views.py". There we create a function that is a view. Each view is something the user can see.

The function will take a request as a parameter.

```
def index(request):
    return HttpResponse("Hello, world!")
```

Now, it is necessary to create a url for that app.
We do that by creating a `urls.py` file inside the app name:

```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

It is composed of the path of the url and the function that is called. Finally, we use a name as well to reference it later.

Finally, we do the same in the project `urls.py` which already has a admin.site.urls:

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls")),
]
```
The `include("hello.urls")` server to include everyother path from hello (which is the name of our app).

We can create more views!
For instance, a function to say hello to brian inside the app views.py:

```
def brian(request):
    return HttpResponse("Hello, Brian!")
```

After we add it in urls:
```
urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
]
```

What if I want to create a file which can have anyname?
We add to views:
```
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
```
And we add the following to urls:
```
urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("<str:name>", views.greet, name="greet"),
]
```
Now any name will work!

# Templates
But as we go along... we cannot add the whole HTML in the HttpResponse. Steady we can:
```
def temp(request):
    return render(request, "hello/temp.html")
```

After we do that, it is important to add the temp.html.
To do that we add a folder templates and inside it a folder with the name of our app. It is a best practice to add the folder with the app name inside the template folder. In that way we can assure no conflict.

```
def temp(request):
    return render(request, "hello/temp.html")
```

Now, when we want to make it like a template (use html and also have variables), we shoudl use a dictionary inside of render:

```
def greetpage(request, name):
    return render(
        request,
        "hello/greet.html",
        {
            "name": name.capitalize()
        }
    )
```

Than, inside of the html, we can add the name using `{{ }}`:

```
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
```

Now we want to create one that uses logic.
We will create a app to check if today is new year or not.

```
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(
        request, "newyear/index.html",
        {
            "newyear": now.month == 1 and now.day == 1
        }
    )
```

Now we create a condition inside html:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Is it new year`s?</title>
    </head>
    <body>
        {% if newyear %}
            <h1>YES</h1>
        {% else %}
            <h1>NO</h1>
        {% endif %}
    </body>
</html>
```
It is necessary to define the end because the identation is not mandatory.

Now we have a non static file!

Now we want to build static files. For instance, a CSS file is an static file.

We create the static files inside the static folder which is inside the app. We do that for the same reason we add a folder with the app name in the templates folder.

After we create a `styles.css` as a static file, we add it in the html with the following format (steady of a url):
```
{% load static %}

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Is it new year`s?</title>
        <link href="{% static 'newyear/styles.css' %}" rel="stylesheet">
    </head>
    <body>
        <h1>Is it new year?</h1>
        {% if newyear %}
            <h1>YES</h1>
        {% else %}
            <h1>NO</h1>
        {% endif %}
    </body>
</html>
```

It is important to add `{% load static %}` in the beginning of the html.

# Tasks
Further use of the web applications provide the possibility to render one html if a condition is true and another one if the condition is false.

Now we create a new app. After that, it is importan to:
1. go to the project `settings.py` and add the new app to INSTALLED_APPS list.
2. go to `urls.py` to include those urls to the urlpatterns list.
3. go to the new app directory to create a urls.py and define a urlpattern. 

After, to create a list of tasks, we define a global variable with it and use it inside the views:
```
tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "task/index.html",
        {
            "tasks": tasks
        }
    )
```

Later, to render the tasks we use a for loop inside the html:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        <h1>Tasks:</h1>
        <ul>
            {% for task in tasks %}
                <li>{{ task }}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```

# Forms
Now we construct a html to add another task:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        <h1>Add Task:</h1>
        <form>
            <input type="text" name="task">
            <input type="submit">
        </form>
    </body>
</html>
```

Nevertheless, the previous html is really similar to the index.html for the task app. So... how do we find a way to not need to copy and paste the html?

## Template Inheritance
The files will inherit from my layout all the structure of the page, and all that will need to be written will be what differs from one page to another.

For that, we create a layout.html which will have the basic portion of the layout and a block:
The block can have 
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        {% block body %}
        {% endblock %}
    </body>
</html>
```

The "body" is the name of the block we want to use.

In that way we do not have to add the whole html for every render html we do.

From that, we can change the index and the add htmls. For instance, the add.html becomes:

```
{% extends "task/layout.html" %}

{% block body %}
<h1>Add Task:</h1>
<form>
    <input type="text" name="task">
    <input type="submit">
</form>
{% endblock %}
```

## Add a link which goes from one page to another
The first way to do that would be to:
```
<body>
    <h1>Tasks:</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
    <a href="/task/add">Add a New Task</a>
</body>
```
Nevertheless, this would make it difficult for us to handle modifications. We would need to modify every link in every script to change if necessary. The name makes it way easier to handle it! The better solution is:

```
<body>
    <h1>Tasks:</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'add' %}">Add a New Task</a>
</body>
```

That works because Django uses the urls.py file to find the link.

To avoid collision, we use the name of the app before in the html:
```
<a href="{% url 'task:add' %}">Add a New Task</a>
```
and new to add the app_name in the `urls.py`:

```
from django.urls import path

from . import views

app_name = 'task'
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]
```

## Add Action to Form
Add an action will be done like this:
```
{% block body %}
<h1>Add Task:</h1>
<form accept="{% url 'task:add' %}" method="post">
    <input type="text" name="task">
    <input type="submit">
</form>
<a href="{% url 'task:index' %}">Return to Tasks</a>
{% endblock %}
```

The method to go another page is called "get" in going from one page to another. Now we are using a post method. A post method is used when the method has a capacity to change the application. Post will give us a capacity to send data.

The current submit status would be: Forbidden (403) with a CSRF verification failed. CSRF stands for Cross Site Forgery and it is useful specially for restrictive data.

To remove this problem, we add a CSRF token, which is generated for every session and is available every time a user visits that site.

If the token is valid, the form can send data. This CSRF is by default active in Django in MiddleWare in settings of the project:

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

The following is the one used: `'django.middleware.csrf.CsrfViewMiddleware'`.

For that, we add the csrf_token:
```
{% extends "task/layout.html" %}

{% block body %}
<h1>Add Task:</h1>
<form accept="{% url 'task:add' %}" method="post">
    {% csrf_token %}
    <input type="text" name="task">
    <input type="submit">
</form>
<a href="{% url 'task:index' %}">Return to Tasks</a>
{% endblock %}
```

## Django Forms
Django gave us the hability to add forms in the django way.
We start that with creating a class and add it in the request:
```
from django.shortcuts import render
from django import forms

tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
```

```
def adddjango(request):
    return render(
        request, "task/adddjango.html",
        {
            "form": NewTaskForm()
        }
    )
```

After it is done, we add the form in `{{}}` to the html and Django will automatically generate the html:
```
{% block body %}
<h1>Add Task:</h1>
<form accept="{% url 'task:add' %}" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit">
</form>
<a href="{% url 'task:index' %}">Return to Tasks</a>
{% endblock %}
```

If I change the class, I do not need to change the html to make a change in the application:
```
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
```

Django will automatically to a client validation if the values are wrongly written.

Furthermore, we want to check the server validation, because it is easy to innactivate the client side validation and it.

To create a server validation and add to the tasks:

```
def adddjango(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(
                request,
                "task/adddjango.html",
                "form": form
            )

    return render(
        request, "task/adddjango.html",
        {
            "form": NewTaskForm()
        }
    )
```
Now we can do a server validation that will show the mistake even if the client side validation is disabled.

Now, to be redirectory to the tasks page:
```
def adddjango(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("task:index"))
```
For that, we need to import the HttpResponseRedirect and we use the reverse to specify the page with its name.

Nevertheless, we still have a problem: the tasks list is a global variable. Therefore, anyone how access the application can view this same list of tasks.

What if everyone has a different task? What if I want a "per user" task.

# Session
It allows django to remember who you are and deal with specific variables related to you. Furthermore, it can store data about you!

To do that, we use the feature of the request:
```
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(
        request, "task/index.html",
        {
            "tasks": request.session["tasks"] 
        }
    )
```
When we do that, we will encounter a problem: "no such table: django_session". That is because django will store data in tables, by default.

To create a table, it is necessary to run the following in the terminal:

```
python manage.py migrate
```
Will allow us to migrate default databases that it wants to create and this will allow it to happen.

After that we need to make some changes in the views.py because the tasks are directly vinculated to the request:

```
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(
        request, "task/index.html",
        {
            "tasks": request.session["tasks"] 
        }
    )

def add(request):
    return render(request, "task/add.html")

def adddjango(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(
                request,
                "task/adddjango.html",
                {
                    "form": form
                }
            )

    return render(
        request, "task/adddjango.html",
        {
            "form": NewTaskForm()
        }
    )
```

We make a change to the index.html as well in order to show no tasks if the list is empty:

```
<body>
    <h1>Tasks:</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% empty %}
            <li>No tasks.</li>
        {% endfor %}
    </ul>
    <a href="{% url 'task:adddjango' %}">Add a New Task</a>
</body>
```

The sessions are determinated by cookies.

