# User Interfaces
Javascript lets us manipulate the DOM, respond to user events, understand what is already in the CSS.

Now we will see some User Interfaces designs.

How can we leverage javascript?

# Single-Page Applications
Single page applications is when a entire web application is just a single page that is manipulated.

In this case, we only need to make modifications to the part of the page that is changing.

This allows us to, steady of loading an entire page when changing, load just the part of the page which is changing.

This is specially helful for applications that change frequently.

For that, we create an example of a single page:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
    </head>
    <body>
        <div id="page1">
            <h1>This is page 1.</h1>
        </div>
        <div id="page2">
            <h1>This is page 2.</h1>
        </div>
        <div id="page3">
            <h1>This is page 3.</h1>
        </div>
    </body>
</html>
```

This would show all the three pages at the same time.

We can change that by adding a display property in CSS equal to none, meaning they should not appear.

For that, we also need to create the buttons that allow us to change the CSS in order to view one or another page. Furthermore, we use "data-page" in the button to specify that the button is related to that page, which allows us to use this value later.

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
        <style>
            div {
                display: none;
            }
        </style>
    </head>
    <body>
        <button data-page="page1">Page 1</button>
        <button data-page="page2">Page 2</button>
        <button data-page="page3">Page 3</button>
        <div id="page1">
            <h1>This is page 1.</h1>
        </div>
        <div id="page2">
            <h1>This is page 2.</h1>
        </div>
        <div id="page3">
            <h1>This is page 3.</h1>
        </div>
    </body>
</html>]
```

Now, we add the function that will show the specific page, by changing the display attribute of div. The function, called `showPage` takes as argument the refered page, changes the display of every page to none and, later, change the display for that specific page to block (which actually shows the div).

After creating the function `showPage`, it is necessary to add an event listener. The event listener is to click in each of the buttons. To apply this event listener, we must assure that the buttons are loaded before. That is done by applying this event listener inside of `DOMContentLoaded`. Inside of this, we use the `querySelectorAll` and `forEach` to apply the modification to each of the buttons. There we add a function that will use `this`, which, in javascript, will refer to the object used for the function. As explained before, each button has a "page" attribute, relating it to a specific div. This "page" can be accessed by refering to the "dataset.page".

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
        <style>
            div {
                display: none;
            }
        </style>
        <script>

            function showPage(page) {
                document.querySelectorAll('div').forEach(div => {
                    div.style.display = 'none';
                })
                document.querySelector(`#${page}`).style.display = 'block';
            }

            document.addEventListener("DOMContentLoaded", function() {
                document.querySelectorAll('button').forEach(button => {
                    button.onclick = function() {
                        showPage(this.dataset.page);
                    }
                })
            })

        </script>
    </head>
    <body>
        <button data-page="page1">Page 1</button>
        <button data-page="page2">Page 2</button>
        <button data-page="page3">Page 3</button>
        <div id="page1">
            <h1>This is page 1.</h1>
        </div>
        <div id="page2">
            <h1>This is page 2.</h1>
        </div>
        <div id="page3">
            <h1>This is page 3.</h1>
        </div>
    </body>
</html>
```

In this way, we can simulate the presence of multiple pages inside a single page.

We can also create buttons to hide or show all pages:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
        <style>
            div {
                display: none;
            }
        </style>
        <script>

            function showPage(page) {
                document.querySelectorAll('div').forEach(div => {
                    div.style.display = 'none';
                })
                document.querySelector(`#${page}`).style.display = 'block';
            }
            
            function hideAll() {
                document.querySelectorAll('div').forEach(div => {
                    div.style.display = 'none';
                })
            }

            document.addEventListener("DOMContentLoaded", function() {
                document.querySelectorAll('button').forEach(button => {
                    button.onclick = function() {
                        if (this.dataset.page == 'hide'){
                            hideAll()
                        } else if (this.dataset.page == 'show') {
                            document.querySelectorAll('div').forEach(div => {
                                div.style.display = 'block';
                            })
                        } else {
                            showPage(this.dataset.page);
                        }
                    }
                })
            })

        </script>
    </head>
    <body>
        <button data-page="page1">Page 1</button>
        <button data-page="page2">Page 2</button>
        <button data-page="page3">Page 3</button>
        <button data-page="hide">Hide All</button>
        <button data-page="show">Show All</button>
        <div id="page1">
            <h1>This is page 1.</h1>
            <h3>This is an introdutory page of my website.</h3>
        </div>
        <div id="page2">
            <h1>This is page 2.</h1>
            <h3>This is the main page of my website.</h3>
        </div>
        <div id="page3">
            <h1>This is page 3.</h1>
            <h3>This is an extra credits pageo of my website.</h3>
        </div>
    </body>
</html>
```

Furthermore, if we have really heavy pages, loading it all might be a bad idea: if the user never goes to page 2, it might be better to not load the content of page 2 beforehand.

There, we can load dynamically:

## Fetch for Loading Dynamically
We can do that by using fetching to an internal response in a django project.

This is done in project "singlepage1":

```
python manage.py runserver
```

This will start running the django app.

Inside the django app. going to /sections/1 will lead me to one page, going to /sections/2 will lead me to another, etc...

What if i want to incorporate the text of those pages into one existing html page?

We use the index.html page (which is the main page). This index.html takes data from the sections/1 or sections/2, etc...

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
        <style>
        </style>
        <script>

            function showSection(section) {
                
                fetch(`/sections/${section}`)
                .then(response => response.text())
                .then(text => {
                    console.log(text);
                    document.querySelector('#content').innerHTML = text;
                });
            }

            document.addEventListener('DOMContentLoaded', function() {
                document.querySelectorAll('button').forEach(button => {
                    button.onclick = function() {
                        showSection(this.dataset.section);
                    };
                });
            });
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <button data-section="1">Section 1</button>
        <button data-section="2">Section 2</button>
        <button data-section="3">Section 3</button>
        <div id="content">
        </div>
    </body>
</html>
```

It is basically taking the html from another page.

The div is initially blank and will request info from other htmls to fill itself.

We even added a "clean" button:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
        <style>
        </style>
        <script>

            function showSection(section) {
                
                fetch(`/sections/${section}`)
                .then(response => response.text())
                .then(text => {
                    console.log(text);
                    document.querySelector('#content').innerHTML = text;
                });
            }

            document.addEventListener('DOMContentLoaded', function() {

                document.querySelector('#clean').style.display = 'none';

                document.querySelectorAll('button').forEach(button => {
                    button.onclick = function() {
                        if (this.dataset.section == 'clean'){
                            document.querySelector('#content').innerHTML = ""
                            this.style.display = 'none';
                        } else {
                            showSection(this.dataset.section);
                            document.querySelector('#clean').style.display = 'block';
                        }
                    };
                });

            });
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <button data-section="clean" id="clean">Clean</button>
        <button data-section="1">Section 1</button>
        <button data-section="2">Section 2</button>
        <button data-section="3">Section 3</button>
        <div id="content">
        </div>
    </body>
</html>
```

This can be an advantage of being more dynamic, but makes you lose the idea of each page you are on. This is because the url for it stays the same, since we are still in the same page.

## Update the URL
We can update the URL to make sure that the user views it correctly. This is basically adding a "pushState" to the history of the user.

To do that, we use the "singlepage2" in which there are more things:

```
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            const section = this.dataset.section;
            history.pushState({section: section}, "", `section${section}`);
            showSection(section);
        };
    });
});
```

In this `pushState` we specify:
- any data associated with this this space.
- title parameter (most browsers ignore, so we can just add a "")
- url that will be shown.

This will allow us to have different urls for each of the sections.

Furthermore, we want to be able to go back to different sections. We can do that by adding the:

```
window.onpopstate = function(event) {
    console.log(event.state.section);
    showSection(event.state.section);
}
```

Which allows us to go back to the previous section.

# Scroll
The window object is quite powerful. It represents the physical window that we are looking at.

The window has some attributes:
- window.innerHeight: height of th physical window.
- window.innerWidth: height of th physical window.

Furthermore, we have the document: the document is the whole page, while the window is only the visible part of the page at any given time.

Part of the document might be below or above the window. This leads to other attributes of the window:
- window.scrollY: shows how many pixels down we have scrolled. At the top of the page, it is 0.
- window.scrollX: shows how many pixels right we have scrolled.

Furthermore:
- document.body.offsetHeight: the whole height of the page.

How can we detect when the user has reached the bottom of the document?
When window.scrollY + window.innerHeight = document.body.offsetHeight

For this, we use the "scroll.html":

```
window.onscroll = () => {

    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        document.querySelector('body').style.background = 'green';
    } else {
        document.querySelector('body').style.background = 'white';
    }

};
```

In this, we have create an event listener that will do something when we have arrived to the bottom of the page.
In this case, we change the body of the page to green.

This is really useful for websites that load more when we get to the bottom (like news articles or social networks).

For instance, the news article can fetch new information when we arrive to the end of the page. This would be an infinite scrool.

## Infinite Scroll
The infinite scroll is done inside the folder "scroll".

Inside scroll, we go in posts > urls.py. The urls shows multiple urls.

After, we go to views. Inside views, we see an index, which will just show an index.html, and a posts. The posts require two arguments.

By doing that, it will generate posts for you to see.

By running the django app and going to the url "http://127.0.0.1:8000/posts?start=1&end=10", it will show json with the posts I want.

In other words, we have generated an API.

Now, how to make the infinite scroll?

We see that in index. Everytime, we scroll to the end of the page, it creates new divs and add those new divs inside the body.


# Animation
To make things more interesting, we can add animation to the webpage.

There, we create an "animate0.html":

```
h1 {
    animation-name: grow;
    animation-duration: 2s;
    animation-fill-mode: forwards;
}
```

The h1 will grow in a forward direction.

Furthermore, we define what grow means:

```
@keyframes grow {
    from {
        font-size: 20px;
    }
    to  {
        font-size: 100px;
    }
}
```

It is liking specifyin the function "grow".

We can do the opposite as well:

```
@keyframes shrink {
    from {
        font-size: 100px;
    }
    to  {
        font-size: 20px;
    }
}

h1 {
    animation-name: shrink;
    animation-duration: 2s;
    animation-fill-mode: forwards;
}
```

In animate1, we show it going from the left to the center. We do that in animate1.html:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Animation</title>
        <style>

            @keyframes move {
                from {
                    left: 0%;
                }
                to  {
                    left: 50%;
                }
            }

            h1 {
                position: relative;
                animation-name: move;
                animation-duration: 10s;
                animation-fill-mode: forwards;
            }

        </style>
    </head>
    <body>
        <h1>Welcome!</h1>
    </body>
</html>
```

Furthermore, we can specify more points than just the beginning and the end of the animation.

We do that in animate2.html:

```
<!DOCTYPE html>
<html>
    <head>
        <title>Animation</title>
        <style>

            @keyframes move {
                0% {
                    left: 0%;
                }
                50% {
                    left: 50%;
                }
                100% {
                    left: 0%;
                }
            }

            h1 {
                position: relative;
                animation-name: move;
                animation-duration: 3s;
                animation-fill-mode: forwards;
            }

        </style>
    </head>
    <body>
        <h1>Welcome!</h1>
    </body>
</html>
```

We can even add the amount of times the animation will happen, which can be a number or infinite:

```
h1 {
    position: relative;
    animation-name: move;
    animation-duration: 3s;
    animation-fill-mode: forwards;
    animation-iteration-count: infinite;
}
```

Finally, in animate3.html, we make in a way that the animation is a consequence of javascript.

We do that by using a script:

```
document.addEventListener('DOMContentLoaded', () => {
    const h1 = document.querySelector('h1');

    // Stop animation initially
    h1.style.animationPlayState  = 'paused';

    // Toggle animation on click
    document.querySelector('button').onclick = () => {
        if (h1.style.animationPlayState  === 'paused')
            h1.style.animationPlayState = 'running';
        else
            h1.style.animationPlayState  = 'paused';
    };
});
```

What if we want to add an animation to the project we did with posts?
We want to be able to hide the posts. We do that in the "hide" folder.

For that, inside the hide > index.html:

```
// If hide button is clicked, delete the post
document.addEventListener('click', event => {
    const element = event.target;
    if (element.className === 'hide') {
        element.parentElement.style.animationPlayState = 'running';
        element.parentElement.addEventListener('animationend', () =>  {
            element.parentElement.remove();
        });
    }
});
```

We have a event listener that will be done in clicking. It can be clicking in any part of the website.

Inside this event, by default we have a variable (called event in this case) that is the thing which was clicked (we do that by specifying the target).

After, we check if the element clicked has was a hide button. This was possible because we created every hide button with the hide class.

Neverthless, after finding out if that element is a hide, we cannot just "remove" that element: this would remove the hide button. The correct way to do that would be to check for the "parentElement". Therefore, we remove the parentElement of the hide button.

Neverthless, hiding the element is a bit strange and adding an animation would help to understand we will be hiddind it.

Therefore, we add an animation to the post:

```
.post {
    background-color: #77dd11;
    padding: 20px;
    margin-bottom: 10px;
    animation-name: hide;
    animation-duration: 2s;
    animation-fill-mode: forwards;
    animation-play-state: paused;
}
```

Furthermore, we need to define what "hide" means:

```
@keyframes hide {
    0% {
        opacity: 1;
        height: 100%;
        line-height: 100%;
        padding: 20px;
        margin-bottom: 10px;
    }
    75% {
        opacity: 0;
        height: 100%;
        line-height: 100%;
        padding: 20px;
        margin-bottom: 10px;
    }
    100% {
        opacity: 0;
        height: 0px;
        line-height: 0px;
        padding: 0px;
        margin-bottom: 0px;
    }
}
```

Finally, we add an event listener to see when the animation is over. Therefore, we remove the element only when the animation is over.

# React
As applications get more complex, it becomes necessary to add organization to the javascript code.



