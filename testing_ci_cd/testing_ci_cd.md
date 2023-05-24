# Testing and CI/CD

We look at testing and CI/CD, which are best practices.

# Testing
Makes sure that the written code is correct.
Tests that make sure that we have the program working as expected.
`assert` is used to do that.

```
def square(x):
    return x * x

assert square(10) == 100
```

If we run this statement and python code, it will show nothing. If there is no problem in assert, the assert will ignore the statement.

Steady, if there is an error, we can see an "AssertionError", seeing where the problem is.

This is specially valiable when program becomes bigger.

How can I test the following?

```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, ceiling(n ** .5)):
        if n % i == 0:
            return False
    return True
```

We create a "test0.py", and than add a "shell" script that I can run inside my terminal.


```
python3 -c "from tests0 import test_prime; test_prime(1, False)"
python3 -c "from tests0 import test_prime; test_prime(2, True)"
python3 -c "from tests0 import test_prime; test_prime(8, False)"
python3 -c "from tests0 import test_prime; test_prime(11, True)"
python3 -c "from tests0 import test_prime; test_prime(25, False)"
python3 -c "from tests0 import test_prime; test_prime(28, False)"
```

Will run python commands by using: `./tests0.sh`

If there are errors, we can check.

Furthermore, there are libraries that allow us to write tests. For instance, "unittests".

It is automated to make it easier to test.

In "tests1.py", we define a class that defines a bunch of functions. Those functions will use the method assertTrue or assertFalse.

We use `unittest.main()` to run all tests.

in this case: `python test1.py`.

It is necessary for the tests to comprehend the whole project.

# Django
We can validate that a object is a valid object.

We can validate, for instance, the flight.

For that, we create a function that does this validation:

```
def is_valid_flight(self):
    return self.origin != self.destination and self.duration > 0
```

Whenever we create an application in django, it gives us a "tests.py" file. It is used to create the files we want to create.

For that, we create a class that will do the tests.

```
class FlightTestCase(TestCase):

    def setUp(self):

        # Create airports.
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        # Create flights.
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100)

    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)
```

When we use, this TestCase, we have the advantage of not actually interacting with the real database. It will just interact with a database made for testing.

In this case, we are trying to create objects and assure that those objects behave as expected.

The database actually changes. So, if one test function changes our database, the changes also necessarily implied for other test functions.

After, we can run the tests with manage.py:

```
python manage.py test
```

Docstring should help us understand the tests.

The test database is created and destroyed when using it.

It should say how many of the tests passed.

Furthermore, we can simulate how web requests work to see if they are behaving as well as expected.

That is done in airline0.py.

```
def test_index(self):
    c = Client()
    response = c.get("/flights/")
    print(response)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context["flights"].count(), 3)
```

In this case, we create a client, and we use the client to access the url "/flights/".

We can than, check that the response status_code is 200 and the flights in the index are currently 3.

The context in the response. This is a python dictionary that has all the info that was passed.

Furthermore, if we try to access an index higher than the number of flights, it should give an 404 error:

```
def test_invalid_flight_page(self):
    max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]

    c = Client()
    response = c.get(f"/flights/{max_id + 1}")
    self.assertEqual(response.status_code, 404)
```

We can also check for passangers, planes, etc...

Therefore, we can simulate a get request. We can verify that the context is correct.

Again, we verify with the python manage.py.

Until now, we have been able to test things that happen in the server size, but not what happens on the browser.

Sometimes, we could want to simulate the front-end.

Now, we will create a "counter.html".

We will create a way to increase and decrease a number.

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Counter</title>
        <script>
            document.addEventListener('DOMContentLoaded', () => {

                let counter = 0;

                document.querySelector('#increase').onclick = () => {
                    counter++;
                    document.querySelector('h1').innerHTML = counter;
                }

                document.querySelector('#decrease').onclick = () => {
                    counter--;
                    document.querySelector('h1').innerHTML = counter;
                }


            });
        </script>
    </head>
    <body>
        <h1>0</h1>
        <button id="increase">+</button>
        <button id="decrease">-</button>
    </body>
</html>
```

Now, we would still need to fo there and apply the changes.

Neverthless, to efficiently test the html and javascript, we should work with libraries that are able to do so.

One of the most popular ones is Selenium.

# Selenium
For that, we use a webdriver that will allow us to interact.

To do that, we use the shell inside the "selenium" folder starting a python interpreter:
```
from tests import *
```
It will generate a webbroser (in this case Chrome, but it can be another). There, we need to assure that we go to the url of our application.

```
uri = fiel_uri("counter.html")
driver.get(uri)
```

With that, I have the hability to see the same things that the user sees by looking at "driver.title", "driver.page_source". The page_source shwows a messy code.

Now, if I want to simulate something, I can "find_element".

```
increase = driver.find_element_by_id("increase")
```
It will create a variable that is a button (because our "increase" element was a button in the counter.html).

After, we can simulate clicking on that button.

```
increase.click()
```

This will automatically execute the button.

We could also do it multiple times:

```
for i in range(25):
    increase.click()
```

The tests are way quicker doing that!

After learning that, we go back to unittests.

```
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element_by_id("decrease")
        decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")
```

After that, we only need to use:

```
python tests.py
```

If one of the tests failed, we would get an error (AssertionError) and show how the assertion did not work.

Some unittest methods:
```
assertEqual
assertNotEqual
assertTrue
assertFalse
assertIn
assertNotIn
```

When using those, it is easier to get a message showing error.

Therefore, we can use Django Testing and Browser Testing. The Browser testing can be done in python!

# CI/CD
CI: Continuous Integration
- continuous merges to main branch
- automated unit tests

Leads to less problem of having different projects, and makes easier to change things and assure that the pathway works well.
Particuarly for large codes, it is impossible that one person knows everything about that code. The unittests help tremendously in this case.

CD: Continuous Delivery
- short release schedules

Continuous delivery leads to incremental changes steady of making big changes. This is particularly helpful to understand what went wrong in the new delivery, vis-a-vis a project that delivery multiple new features and corrections at the same time. Furthermore, it helps the user to addapt to one change at a time. 

In the ideal project, continuous deployment leads to continuous integration.

# GitHub Actions
Github actions allows us to automatize some elements of deployment. For instance, with github actions we can check it the deployment was correctly done.

To achieve that, we create a github page inside of our application and create a command to be followed in an yaml:

```
name: Testing
on: push

jobs:
  test_project:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run Django unit tests
      run: |
        pip3 install --user django
        python3 manage.py test
```

- name: name of the command
- on: when will it be activated?
- jobs: the jobs it will do
- runs-on: in which machine it will run. in this case the latest 
- name: name of the specific part of the job
- run: what this specific part of the job will do. In this case, it install django (other dependencies might be necessary to install for more complex systems) and runs the tests.

Therefore, everytime we push, automatically, the tests will run in a github virtual machine.

From github repository we can look at a tab which shows the recent pushs and if they were successful.

# Docker
Docker is a way to make containerization software. Steady of running in the computer, we will run it inside of a container in the computer.

Each container will contain its own configurations.

As long as you provide the right instructions, everyone in a team will work on identical environment.

This works well with the idea of continuous delivery.

In this way, we assure that the right versions and the right packages are installed.

A VM (Virtual Machine) is running a virtual machine, having its own Guest OS. VMs are generally heavy. On the other hand, Containers do not have their own Guest OS. They rely on Docker, which provides environments with specifics bins/libs. The Docker layer is keeping track of the containers and the environments.

How do we configure those Docker containers?

We do that by writing a docker file.

The docker file we have created is in "airline1". 

```
FROM python:3
COPY .  /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

The Dockerfile describes the instructions for creating a docker image.

The docker image represents all the libraries and versions which allows us to created containers based on the same material.

This docker file allows me to create an image.

The `FROM python:3` means that we are taking configurations from the python:3 image. We will be basing our image in another one. Specifically, this image is responsible for installing python:3 and other packages which might be helpful.

Often times, we will base a docker file in another docker file.

The `COPY . /usr/src/app` will copy everything I have in the current directory and paste it in usr/src/app. This will include everything into the container: settings, requirements, etc...

The `WORKDIR /usr/src/app` will change my working directory to the usr/src/app. Therefore, this new working directory will have everything that is necessary.

Finally, the `CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]` specifies what should run when I start my container.
The sintax shows that each word is separated by a comma. `0.0.0.0:8000` is the portal in which I want to run the container. We could have chosen another portal as well.

Therefore, any user can base their code on the same configurations.

Until now, we have been using SQL Lite database, being a file -based database that allows us to create tables, insert rows into it, etc...

Neverthless, SQL Lite does not scale as well for larger applications and we want the SQL to be hosted in a separated server. Postgress or MySQL work better in this case.

How can I change it?

We should create another server. We do that in production by running the SQL in another container.

Docker Compose is the way to do that: Docker Compose allows us to run multiple containers together. We can run a Postgress database in one container and the application in another container and have they communicating.

Having Postgress installed, we create a file in "airline1" called docker-compose.yml.

The docker-compose.yml is a yml file that describes the services that will be part of my application. Ecah service is going to be its own container that could be based on a different docker image.

```
version: '3'

services:
    db:
        image: postgres

    web:
        build
        volumes:
            - .:/usr/src/app
        ports:
            - "8000:8000"
```

In this case, we have the `db` service that is based on the image `postgres`, which is an already built image of how to start postgres container.

Furthermore, for the web application, we base it on the docker file I have written. This can be specified by `build: .`, meaning I am building from the current directory. In addition, I specify that my current directory should correspond to the app directory, in the `volumes: - .:/usr/src/app`. Finally, we specify that the port 8000 on my computer should correspond to port 8000 on docker, from `ports: - "8000:8000"`.

So, with that, we can create our containers!

From there, we go the airline1 directory, and in commmand prompt:

```
docker-compose up
```

This will start the services.

This will start the application in port 8000. Therefore, going to "0.0.0.0:8000/flights" will take me to flights page.

This is not running only on my computer, but in the docker container.

Now, lets say we have logins in the app and we want to create a super user.

We cannot do as before, by using the the `python manage.py createsuperuser`. This would create a superuser in the local computer steady of in the docker.

To do that, we start by writing: `docker ps` in the command prompt.

This will show all the containers that are current running. From there, we can make a configuration to run the previous sheel command inside of a container.

To do that, we look at the containers that are currently running. One of those will be the web container. With this specific container id, we use in command prompt:

`docker exec -it d5b80cf9991d bash -l`

The previous command specifies that we want to execute a command inside the container with the passed id. `-it` specifies that we want to make the execution interactive, and the `bash` is the command we want to execute. Therefore, we are saying that we want to 
run a bash prompt, meaning I want to be able to interact with a sheel (to be able to run command inside the container).

From there, after running this, we go inside a sheel in the directory that contains the web application.

From there, we can do a secretuser in the same way we would do before. After, by pressing ctrl + B, we logout of the container.

The superuser will be created.


 





