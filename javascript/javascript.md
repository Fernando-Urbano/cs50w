# Javascript
In web applications:

User will send http request to a server.
The server process the request and returns a response to the user.

The server will be responsible for generating some sort of response.

Javascript will allow us to run code that will happen in the computer of the user.

The computational being done in the computer side sometimes makes it faster.

Javascript will give the ability to directly manipulate the DOM: Document Object Model that has a hyerarchy that shows the webpage that the user in looking at.

How do we add javascript, we add to the html script tags:

```
<script>
    alert('Hello, World!')
</script>
```

Anything that happens inside script is part of javascript. For instance, in the hello.html file:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello</title>
        <script>
            alert('Hello, world!');
        </script>
    </head>
    <body>
        Hello!
    </body>
</html>
```

After we can open the hello.html with the command prompt:

```
open hello.html
```

We can add additional features.

# Events
With javascript, we can do "event driven programming". Events are, for instance, drop down list, login, etc...

With javascript, we can add event handlers. The events handlers run a script when an event happens.

For example, we can add a function inside html:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello</title>
        <script>

            function hello() {
                alert('Hello, world!');    
            }
            
        </script>
    </head>
    <body>
        Hello!
        <button onclick="hello()">Click here</button>
    </body>
</html>
```

The function hello() is called by using the button, that "onclick" runs the function.

# Variables
Javascript also has the data types, functions, etc... like other programming languages.

To show that, we create a program to coun in the html "counter.html":

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Counter</title>
        <script>

            let counter = 0;
 
            function count() {
                counter += 1;
                alert(counter);
            }
            
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <button onclick="count()">Click here</button>
    </body>
</html>
```

The `let counter = 0;` defines the variable counter and sets the value equal to 0.
The function than takes this value and add one everytime the count() function is called.

We do not always need to show alerts. We can also change the content of the page by manipulating the DOM.

# querySelector
The querySelector lets us select a type of html and changes it:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello</title>
        <script>

            function hello() {
                document.querySelector('h1').innerHTML = 'Goodbye!'
            }
            
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <button onclick="hello()">Click here</button>
    </body>
</html>
```

In this html, the querySelector takes the element that is a h1. If there is more than one h1, the query will take the first one that it finds.

After, the `innerHTML` will let us change the value of that h1.

Therefore, when we can change it. The innerHTML changes the property of this particular object.

Now, what if I want to everytime I press the button the h1 changes steady of just changing to Goodbye?

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello</title>
        <script>

            function hello() {
                if (document.querySelector('h1').innerHTML === 'Hello!') {
                    document.querySelector('h1').innerHTML = 'Goodbye!';
                } else {
                    document.querySelector('h1').innerHTML = 'Hello!';
                }
            }
            
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <button onclick="hello()">Click here</button>
    </body>
</html>
```

In this case, we use `===` because the equality requires the objects to have the same type.If `==` is used, it is requiring a weaker equality. The `===` is a strick equality.

Therefore, in this case, the h1 always change.

Neverthless, we can improve the efficiency of our code:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello</title>
        <script>

            function hello() {
                const heading = document.querySelector('h1')
                if (heading.innerHTML === 'Hello!') {
                    heading.innerHTML = 'Goodbye!';
                } else {
                    heading.innerHTML = 'Hello!';
                }
            }
            
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <button onclick="hello()">Click here</button>
    </body>
</html>
```

Now, we have a variable for the html. In this case, we use const when assigning it. This is used because the variable is one that will never change.

We can do that for count as well:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Counter</title>
        <script>

            let counter = 0;
 
            function count() {
                counter ++;
                document.querySelector('h2').innerHTML = counter;
            }
            
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <h2>0</h2>
        <button onclick="count()">Count here</button>
    </body>
</html>
```

We can also add an alert! In this case, we use an alert everytime the counter is a multiple of ten.

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Counter</title>
        <script>

            let counter = 0;
 
            function count() {
                counter ++;
                document.querySelector('h2').innerHTML = counter;

                if (counter % 10 === 0) {
                    alert (`Count is now ${counter}`)
                }
            }
            
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <h2>0</h2>
        <button onclick="count()">Count here</button>
    </body>
</html>
```

In this case, we use the equivalent of f-string for javascript. For that we use "``" and $:
```
alert (`Count is now ${counter}`)
```

We can also add an event listener.

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Counter</title>
        <script>

            let counter = 0;
 
            function count() {
                counter ++;
                document.querySelector('h2').innerHTML = counter;

                if (counter % 10 === 0) {
                    alert (`Count is now ${counter}`)
                }
            }

            document.querySelector('button').onclick = count;
            
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <h2>0</h2>
        <button>Count here</button>
    </body>
</html>
```

In that, we use the querySelector to find a buttom and set its "onclick" property to te function count.

Furthermore, it is worth to mention that the function is not being called, just assigned to the buttom.

We call that "function programming", where functions are handled as values.

Neverthless, the previous code would do nothing.

We can check in the javascript console where the error is coming from.

There, we can find that theere is an error:

Uncaught TypeError: Cannot set properties of null (setting 'onclick')

We can see that is not finding a button: the problem is that the browser will run from top to bottom. Therefore, the value is used before assigned.

How can we solve it? We can use a couple of strategies:
- put the script tag at the end of the html.
- add another event listener (shown below)

We use addEventListener('DOMContentLoaded'):

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Counter</title>
        <script>

            let counter = 0;
 
            function count() {
                counter ++;
                document.querySelector('h2').innerHTML = counter;

                if (counter % 10 === 0) {
                    alert (`Count is now ${counter}`)
                }
            }

            document.addEventListener('DOMContentLoaded', function() {
                document.querySelector('button').onclick = count;
            });
            
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <h2>0</h2>
        <button>Count here</button>
    </body>
</html>
```

We now have added an "addEventListener". The event listener has two parameters: first the event it will listen to. In this case, it is listening to "DOMContentLoaded", which is finishing to load the whole page. The second parameter is a function that will be executed when the event happens. We do not need to define the function previously. Javascript allows the function to be defined inside. Therefore, in this scenario, we ask that the page is loaded before assigning the function count to the property "onclick" of the button.

To make it more organized, it is useful to separate the code of the javascript and the code of the html. Sometimes, the person working with the javascript will not be the same as the one working with the html.

We do that by reference of the javascript inside the html:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Counter</title>
        <script src="counter.js"></script>
    </head>
    <body>
        <h1>Hello!</h1>
        <h2>0</h2>
        <button>Count here</button>
    </body>
</html>
```

The same javascript can be used in more than one library.

Let's work a bit more... with forms.

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello</title>
        <script>

            document.addEventListener('DOMContentLoaded', function() {
                
                document.querySelector('form').onsubmit = function() {
                    const name = document.querySelector("#name").value;
                    alert(`Hello, ${name}!`)
                };

            });
            
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <form>
            <input autofocus id="name" placeholder="Name" type="text">
            <input type="submit">
        </form>
    </body>
</html>
```

In this case, we define a form. Inside the form, the "autofocus" already loads the page focusing on the form.

Furthermore, we create an event listener that calls the function we passed when the page finished loading ("DOMContentLoaded").

Inside the event listener, the second element passed is the function that will be used.

The function assigns a value to the form html on submit.

Inside it, we want to get the name pased in the "input". Nonethless, there is more than one input. Therefore, we use the same sintax as CSS to specify what we are talking about. Due to the fact that we are talking about a specific input which has the id "name", we use this last id to reference it. From that input, we take the value and a assign it to a constant variable called name. This variable is later used to raise an alert with the name of the user.

Furthermore... we can change the CSS by using javascript. We can use that by using style:

```
<!DOCTYPE html>
<html>
    <head>
        <title>Colors</title>
        <script>
            document.addEventListener('DOMContentLoaded', function() {

                // Change font color to red
                document.querySelector("#red").onclick = function () {
                    document.querySelector("#hello").style.color = "red";
                }
                // Change font color to blue
                document.querySelector("#blue").onclick = function () {
                    document.querySelector("#hello").style.color = "blue";
                }
                // Change font color to green
                document.querySelector("#green").onclick = function () {
                    document.querySelector("#hello").style.color = "green";
                }

            })
        </script>
    </head>
    <body>
        <h1 id="hello">Hello!</h1>
        <button id="red">Red</button>
        <button id="blue">Blue</button>
        <button id="green">Green</button>
    </body>
</html>
```

To better specify that is:

```
<!DOCTYPE html>
<html>
    <head>
        <title>Colors</title>
        <script>
            document.addEventListener('DOMContentLoaded', function() {

                document.querySelectorAll('button').forEach(function(button){
                    button.onclick = function() {
                        document.querySelector('#hello').style.color = button.dataset.color; 
                    }
                });

            });
        </script>
    </head>
    <body>
        <h1 id="hello">Hello!</h1>
        <button id="red" data-color="red">Red</button>
        <button id="blue" data-color="blue">Blue</button>
        <button id="green" data-color="green">Green</button>
    </body>
</html>
```

In this case, we use "data-" to specify data about each of the htmls.

After, we use `querySelectorAll` which will return every element of this type in a NodeList. After, for each of the buttons that comes back, we change the color.

This "for" is done using the "forEach" method. This method applies a function to each of the elements of a list. Therefore, the parameter is the function which must show the element as a parameter. Inside, we use the button.dataset.color attribute to change it.

More recent of javascript has the arrow function, which does the same as function, but using an "arrow":

```
document.querySelectorAll('button').forEach(button => {
    button.onclick = function() {
        document.querySelector('#hello').style.color = button.dataset.color; 
    }
});
```

If the function has no parameter it can be represented with `() =>`

To make it even better, we can make a dropdown:

```
<!DOCTYPE html>
<html>
    <head>
        <title>Colors</title>
        <script>
            document.addEventListener('DOMContentLoaded', () => {

                document.querySelector('select').onchange = function() {
                    document.querySelector('#hello').style.color = this.value;
                }

            });
        </script>
    </head>
    <body>
        <h1 id="hello">Hello!</h1>
        <select>
            <option value="black">Black</option>
            <option value="blue">Blue</option>
            <option value="red">Red</option>
            <option value="green">Green</option>
        </select>
    </body>
</html>
```

The "this" is used to refer to the object of the event. In this case, it refers to the select.

The events that we generally work with are:
- onclick: when clicked.
- onmouseover: when the mouse goes by the button, select, etc.
- onkeydown: when you press key down on the keyboard.
- onkeyup: when you press key up on the keyboard.
- onload,
- onblur,
- etc...

## To-do list only with JavaScript
```
<!DOCTYPE html>
<html>
    <head>
        <title>Tasks</title>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                document.querySelector('form').onsubmit = () => {
                    const task = document.querySelector('#tasks').value;
                    console.log(task);

                    // Stop form from submitting
                    return false;
                }
            })
        </script>
    </head>
    <body>
        <h1>Tasks</h1>
        <ul id="tasks">
        </ul>
        <form>
            <input id="task" placeholder="New Task" type="text">
            <input type="submit">
        </form>
    </body>
</html>
```


We are using script to see the submission. The `console.log` is the equivalent of python print. This is useful for debugging:

```
<!DOCTYPE html>
<html>
    <head>
        <title>Tasks</title>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                document.querySelector('form').onsubmit = () => {
                    const task = document.querySelector('#tasks').value;
                    console.log(task);

                    const li = document.createElement('li');
                    li.innerHTML = task;

                    document.querySelector('#tasks').append(li)

                    // Stop form from submitting
                    return false;
                }
            })
        </script>
    </head>
    <body>
        <h1>Tasks</h1>
        <ul id="tasks">
        </ul>
        <form>
            <input id="task" placeholder="New Task" type="text">
            <input type="submit">
        </form>
    </body>
</html>
```

Now we have created a constant list item and assigned the value task to it.
Later, we append this list element to the unordered list created.

























