# Scalability and Security
IWehn deploying  web applications in the internet, it is fundamental to host the web application in a web server. This makes us deal with issues regarding scalability and security.

We deploy our webapplication by putting them on a server. A server is a dedicated machine that will listen to web requests and give responses.

As a web application becomes popular, multiple people will want to access the application and the server will have to deal with multiple requests at the same time.

A single computer can only deal with a limited amount of users at the same time.

Where these servers exist?

- Cloud: cloud is becoming more popular. Big companies loan servers.
- On Premise: servers that are inside of a company. The company owns the physical servers. In this case, the company has a very deep understanding of the machines and can physically view them.

With cloud, we cannot have the details of the physical machines, but, on the otherhand we do not have to worry about those physical machines.

Those cloud computer services allows us to scale as we get more and more users.

How many users can a server service at the same?
Depends on the service, and the time necessary to process a request.

What do we do if a service can handle 1000 users, but 1001 users are trying to access the service at the same time?

We need to scale!

Vertical scaling: we make the server better (bigger). It is basically just swaping. Neverthless, it has limitations: there is a limit to which the server can get bigger.

Horizontal scaling: we use more server.

When we have more than one server, how do users get directed to server A or server B?

There is a Load Balancer: it is another piece of hardware, which will receive the requests and the decide where it should go. It acts as a dispacher.

This can work for multiple servers as well.

This process of deciding is called load balancing.

How does the load balance decides?
- random choice.
- round robin: has an order of connections. first user to A, second to B, third to C, fourth to A again, etc... (relative easy to implement).
- fewest connections: better when requests take longer than others. so, it asks which server has the fiewest connections. this will lead to even balance, but it is more expensive to compute.

All those approachs have the Sessions problem:
Sessions allow us to store information about the previous times the user logged.

The sessions allow us to continue logged in for instance.

This might be a problem for load balancing...

If server A is used to start a session, and, for the next time I try to access the application, the same user is assigned to server B, we would have a problem. Server B would not know what the session is.

How can a load balancing "care" about the services?

Session-Aware Load Balancing:
- sessions in database: sessions are stored in database steady of in a server. in this way, servers do not matter.
- client-side sessions: the sessions are stored in the web browsers (cookies). Inside the cookie, we can store who is logged in, for instance. It is important to do ao criptography inside the cookies in order to avoid people hacking the cookies. The problem with that is that when we have heavy cookies, it becomes heavy to pass the cookies information back and forth from the client to server side.
- sticky sessions: each session to a server.

How many of those servers do we need?
We can benchmark, by looking at how many users one server can handle.

Sometimes, the organization will have a demand higher than in other times.

One quite popular solution is Autoscaling. If more people are using the server, more servers will be used. Clouds let us do that in a good way, and let us deifne a minimum and a maximum amount of servers.

There are tradeoffs: there will take sometime to start a new server. Furthermore, there will opportunities of failure. On the other hand, if one server fails, we can just go another server.

How do we know if a server is still working?

The load balancer will send a heartbit to all the servers and see which ones did not send a response back, and therefore are dead.

The load balancer can also be a point of failure. It can be a single point of failure: which means a point of failure that will make the whole application fail.

We can have multiple load balancers. Meaning another load balancer can check if the initial load balancer is working.

# Scaling Database
All the servers need to communicate with databases. Also databases can only deal with a limited amount of requests at the same time.

So, how can we scale those databases?

Database partioning: we separate bigger databases in smaller databases.

We can do that by storing references to other tables in a main table.

For instance, if we have the airline project, we could steady of putting the flights with their destinations and origins in a main database, we can assign ids to those flights and send only the ids to the main table. This is called database vertical scaling.

Furthermore, we can do a horizontal scaling: steady of having just a flights table, we can have a flights_domestic and a flights_international tables. In this case, the tables can have the same columns, but different data. Partioning database can help us represent data.

Again, we have a single point of failure: if the database fails, all fails.

To deal with that, we have Database Replication: we can have multiple identical databases.

-single-primary replication: multiple databases and one of those is the primary database. The primary database is a database from which we can read data and write data. All the other databases are only used to read. Furthermore, in this case, we need a way to assure that all those databases are kept in sinc, meeaning that when the primary database changes, all the other should be informed. Therefore, after the writing, there is an update.

There is a drawback: the database has the problem of having limitations. If a lot of people try to change the database, it will be problematic.

Furthermore, there is still a single point of failure for writing the database (not for reading).

-multi-primary replication: multiple databases can write and read data. They are all "primary". This leads to complexity: everytime a database changes, it needs to inform all other databases.

Can have an update process problem (a row can be assigned by two people), update id problem (they add a row with the same id and we need to resolve this conflict), delete and update problem (one people deleted the row and another person updated).

# Caching
Caching allows us to not necessary load all the information from the database each time we need to get information.

For instance, in a newspaper, where the headlines are always the same along the day, it seems stupid to get the headlines from the everytime a user requests.

Caching is storing a saved version of some information in a way that there is no need to request every

There are sometimes of caching:
- client-side caching: your browser is able to cach data steady of asking the server. If there is a page that does not change very often, it is interesting to have a cach in the browser. The experience becomes faster for the user.
This can be done by adding to the headers of the HTTP response:
```
Cache-Control: max-age=86400
```
When your webserver get your response, it will get the saved version. In this case, we are specifying that the cache used until 86400 seconds after the response was sent (one day in this case).

This has the advantages already mentioned, but at the same time, makes changes unavailable for users until the cache is finished (unless there is a "forced refresh").
From that, we can add a ETag:
```
Cache-Control: max-age=86400
ETag: "746291702072037E0271032"
```

The ETag is a mark of the version of the CSS and HTML and Javascript that is being passed. If the ETag changes, meaning the version changed, which says that the cache should not be used, the client should make a new request.

- server-side caching: cache is done on the server side. Therefore, the server can talk to the database or to a "cache database". Django has some specific built-in caches:

- per-view caching: cach a particular view. In this way, the view will be used in the same way it was loaded before.
- template fragment caching: a part of the template can be cached (a side bar, a h1, etc...)
- low-level cache API: you can save the information of the API.

# Security
There is a bunch of security consideration to take a look at. It can be implemented and inherance in every part of the code we viewed before.

## Security: Git
Open source software: git is generally related to open source code. This is good, but it has drawdown: you cannot put passwords, for instance. Making the repository available for everyone also comes with the idea to assure that credentials and passwords must never be put inside a push to a branch. That is particularly important because in an open source code, people can view not only the current version of the application but older ones as well.

## Security: HTML
HTML is often related to "pishing attack", meaning that I say I have a link to one particular url, but go to another one:

```
<a href="url1">
    url2
<\a>
```

Or, in a more practical way:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>My Website</title>
    </head>
    <body>
        <a href="https://cs50.harvard.edu/extension/web">https://www.google.com/</a>
    </body>
</html>
```

This leaves the possibility of being tricked. Anyone can look at the HTML from any page.

If I want to create a fake version of a website. I can just copy the whole html from there and get a similar website.

I can say them that I am linking to a page of a bank and actually be linking to a copied fake version of that bank's page.

Is good to be mindfull that HTML is really vunerable!

## Security: HTTPS
The whole internet is based on the idea of using HTTP and specially HTTPS to communicate between client and server side.

How do we know that the information being passed back and forth is secure?

I want that the path towards going to the server and back to the client is secure, in a way that passwords, credentials, and others do not leak.

For that, we use cryptography!

If I pass it along without cryptography, everyone will be able to view it.

For that, we use *secret-key cryptography*: everytime I pass information, I pass along a secret key, which can be used to encrypt or decrypt the information sent. Therefore, we want to send the `Ciphertext`. The cyphertext and the key will be used to convert the cyphertext to plaintext.

Therefore, the key is the way to send and receive.

Neverthless, it would be stupid to send the key via internet, because it would be the way to understand all the information, and would generate the same unsecure outcome of just sending the plaintext.

If I could send the secret key in secret, we could solve this problem, but that is not possible.

Therefore, for the internet, we have a *public-key criptography*, which uses a private key and a public key. The private key should not be shared with other people.

The public key is used to encript information and the private key is used to decrypt the information.

If I want to communicate information to another person, I can send the public key via internet and the other person will use this public key to encrypt the information. When the information is sent back to me, I use the private key to decrypt the information.

We can say that a key capable of encrypting the information might not be able to decrypt the information.

## Security: SQL
For instance, security is particularly useful to store password.

For that, we use a "hashed" version of the password. The hash function makes the password be transformed into a sequence of hashs. The function is made in a way that is very easy to transform from password to hash, but really hard to transform from hash to plain text again.

The company wont actually know to the users passwords.

That is why a company wont be able to tell you your password.

For instance, another problem is making sure that when letting people reset their passwords by providing their e-mail, you do not send a message saying that the e-mail does not exist in the database. This would leak informatiosaying which users have an account.

## Security: SQL Injections
A user can try to imply SQL into login.

For instance, a user login-in would use this query to do so:
```
SELECT * FROM users WHERE username = 'harry' AND password "123"
```

This could lead to a problem if a hacker writes `'harry' --'`

That is because everything after the `--` is considered as a comment.

## Security: APIs
There are a number of ways that the APIs can become more secure as well:
- rate limiting: limiting the amount of requests a particular user can send in an amount of time. The requests can shut the system or be trying to leak information by doing that.
- route authentication: only let users with an API key to see some data.

The API keys should not be on the source code as well!

One common solution for that is to use from the Environment variables. The server will have the keys steady of in the source code. The server can take the information from the environment.

Many APIs have API keys.

## Security: JavaScript
JavaScript is particularly vunerable due to to the fact that is programming in the client side.

One particular vulnerability is "Cross-Site Scripting", meaning that one can run JavaScript in the webpage besides the JavaScript from that webpage. A webpage always wants that the JavaScript running is only the one written by the application.

If someone else can write, they can manipulate the users experience.

Therefore, leaves the possibility of changing the DOM.

You will want to detect that there is someone writing and make a way to avoid it.

This comes together with the idea that we do not want the user to be able to write SQL code to access our queries.

 Django is particularly good at detecting those by making "Cross-Site Request Forgery", meaning it fakes a request to the website while not intending to make this request.

 To avoid this, we only want a POST request to be send to access the database.

 The {% csrf_token %} is a way to avoid that. 

 ```
<form action="/transfer" method="post">
    {% csrf_token %}
    <input name="to" value="brian">
    <input name="amt" value="2800">
    <input name="submit" value="Transfer">
</form>
 ```


