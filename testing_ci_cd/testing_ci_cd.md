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

In the ideal project, continuous deployment leads to continuous

