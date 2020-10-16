[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/UlfurOrn/Team5">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/b/b7/Reykjavik_University_Logo.svg/1200px-Reykjavik_University_Logo.svg.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Team 5</h3>

  <p align="center">
    Habit tracking platform for nutritional information
    <br />
    <a href="https://github.com/UlfurOrn/Team5"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/UlfurOrn/Team5">View Demo</a>
    ·
    <a href="https://github.com/UlfurOrn/Team5/issues">Report Bug</a>
    ·
    <a href="https://github.com/UlfurOrn/Team5/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Testing](#testing)
* [Lecure Aspects](#lecture-aspects)
  * [Sprint 1](#sprint-1)
  * [Sprint 2](#sprint-2)
  * [Sprint 3](#sprint-3)
* [Team Members](#team-members)
* [Teacher](#teacher)
* [TA](#ta)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Swagger UI Screen Shot][product-screenshot]](https://i.imgur.com/WP7MQJj.png)

This is the Github repository for Team 5's project in T-302-HONN.
We created a habit tracking platform for nutritional information.


### Built With

* [Python][python]
* [Flask][flask]
* [Flask-restplus][flask-restplus]
* [Psycopg2][psycopg2]



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* pip
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/UlfurOrn/Team5.git
```
2. Create a virtual environment(optional)
```sh
python3 -m venv venv
```


API:


1. Move to API folder
```sh
cd API/
```
2. Install packages with pip
```sh
pip install -r requirements.txt
```
3. Move to main app folder
```sh
cd app/
```
4. Run the API
```sh
python app.py
```
5. Open the link: http://127.0.0.1:8000/ in a web browser and try out the REST API


WebApp:


1. Move to the Project folder
```sh
cd
```
2. Export the environmental variables:
```sh
Terminal: export FLASK_APP=WebApp
Windows: set FLASK_APP=Webapp
```
3. Run the Flask app
```sh
flask run
```
4. Open the link: http://127.0.0.1:5000 in a web browser and try out the WebApp


Serve up the WebApp and the REST api at the same time:
1. run the run.py file in the root directory after previous environment variable setup
```sh
python run.py
```


Mail Service:

1. Move to MailService folder
```sh
cd MailService/
```
2. Install packages with pip
```sh
pip install -r requirements.txt
```
3. Move to main src folder
```sh
cd src/
```
4. Run the MailService Api
```sh
python app.py
```
5. Open the link: http://127.0.0.1:8001/ in a web browser and try out the Mail Service

**Note:** The mail api service we were using closed our account for exposing an api key.
          The service was working but unfortunately not anymore. Hopefully this is alright
          for this sprint, and this will be fixed by the end of the next one.


<!-- TESTING -->
## Testing
### API testing
The current code coverage of the API is **97%**. The tests should be run from with in API/app with the commands below
* Running the unit tests, with coverage
```sh
coverage run -m pytest
```
* Getting the coverage report
```sh
coverage report -m
```

### WebApp testing
Our current code coverage of the WebApp is **59%**. To run the tests you should be positioned in the root directory and run:
Before running these tests you need to first start both the REST API and the WebApp. See instructions above.
* Running the unit tests, with coverage
```sh
coverage run -m pytest WebAppTests
```
* Getting the coverage report
```sh
coverage report -m
```

<!-- LECTURE ASPECTS -->
## Lecture Aspects

### Sprint 1
For this sprint we used a layered design where the database (data) and the Rest API (domain) work as independant entities. The presentation layer will be implemented in a future sprint.
Objer-Oriented Programming was implemented in the DBapi using abstract classes and a main gateway (see more in services README.md). Encapsulation is also used is various places in the API.

### Sprint 2
The six of the eight Base Design Patterns we decided on implementing for our system are the following:

* Registry: 
The registry design pattern is used to implement a global sole instance logger that we use for error logging, 
this introduces logging to our system.

* Plug-in: 
The Plug-in pattern is used to read a config file for the logger, aka output format, output file and more

* Mapper:
The Mapper design pattern is implemented to make changing between the rest api bodies and database structure easier. 
This also makes changes to the models easier.

* Layer Supertype:
For the Layer Supertype we created a Mapper interface with some methods to implement which the other Mapper classes inherit from.

* Gateway:
To implement the Gateway pattern we introduced a small external service into our project, a mail service, 
and we created a more basic api for said service.

* Service Stub:
For the service stub we created a fake mail service to remove the dependency on the mail service during unit tests.

### Sprint 3
The Single Responsibility Principle:
* The first place where we implement this principle is in our Mapper classes. These classes have only one reason to change and that
reason is if the underlying tables in the database change. That is if we where to, f.x. add a new column to a table or rename an existing
column we would change it but that is the only reason these classes have to change.
* The second place where we implement this principle is in the DBapi class. The only reason this class has to change is if we add/remove 
a table that we want to query from the database.
* The third place where we implement this principle is in our controller classes for the REST api. These classes/modules have only one
reason to change which is the addition/removal of a REST api function/route. These classes do not concern themselves with anything else.

The Dependency Injection:
To get the dependency injection we did a little bit of refactoring. We decided to create a new DBapi class that takes in the 5 IO classes.
These IO classes get assigned to instance variables named after the tables. This means that each call to f.x. users changes from DBapi.users("GET")
to DBapi.users.get(). This allows us to change out the DBapi that is used in the REST api by simply changing what IO classes we use allowing for
a swift transfer between f.x. different databases while still maintaining the same code that uses the DBapi (i.e. with dependency injection). We do
realize that this depends on the IO classes to implement the same types of interfaces which is just something that needs to be done when implementing
new IO classes.

### Sprint 4
Conway´s Law: 
* Our team has a unique structure to it. We are a team of eight, we split our tasks in a way where one team member does database work, another works on the REST API, a few members on the Flask web application, another few on design for our website, and the rest on lecture aspects, amongst giving their opinions on improvements on various things in our system. This kind of team structure has resulted in a system where our database, REST API, and web application function as individual systems, while still offering an outside perspective when implementing each service for our system.
* The communication amongst our team can sometimes be quite difficult, with the current status of the world we must communicate solely online.This has proven to have it’s challenges, it would be much easier to meet together in-person to discuss our problems, help each other with our tasks, create diagrams and documents and so on.
* We do however, not believe this has had a large impact on our specific system, perhaps working on our project took slightly more time than it should have, we could have, for example, implemented more functionality to our system, but in reality we probably would have just finished out tasks sooner in the sprint, resulting in not having to crunch the final weekend to get the last few tasks done.

Components:

Non-Functional requirements and constraints:

Logs:

Risk management:


<!-- TEAM MEMBERS -->
## Team Members

The members of Team-5 include RU students from the Computer Science department. We are a mixture of second and third year computer science and software engineering students.

* Annija Apine, Computer Science - annija17@ru.is
* Bent Gunnarsson, Software Engineering - bent19@ru.is
* Bjartur Þórhallsson, Software Engineering - bjartur19@ru.is
* Erla Óskarsdóttir, Computer Science - erla19@ru.is
* Guðjón Ingi Valdimarsson, Software Engineering - gudjonv18@ru.is
* Magnús Konráð Sigurðsson, Software Engineering - magnusks19@ru.is
* Páll Þorsteinsson Sonnentag, Computer Science - pallt18@ru.is
* Úlfur Örn Björnsson, Software Engineering - ulfur19@ru.is



<!-- TEACHER -->
## Teacher

Gerardo Reynaga



<!-- TA -->
## TAs

* Gunnar Jörgen Viggósson
* Svanur Jóhannesson
* Þórður Friðriksson





<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/UlfurOrn/Team5.svg?style=flat-square
[contributors-url]: https://github.com/UlfurOrn/Team5/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/UlfurOrn/Team5.svg?style=flat-square
[forks-url]: https://github.com/UlfurOrn/Team5/network/members
[stars-shield]: https://img.shields.io/github/stars/UlfurOrn/Team5.svg?style=flat-square
[stars-url]: https://github.com/UlfurOrn/Team5/stargazers
[issues-shield]: https://img.shields.io/github/issues/UlfurOrn/Team5.svg?style=flat-square
[issues-url]: https://github.com/UlfurOrn/Team5/issues
[product-screenshot]: https://i.imgur.com/WP7MQJj.png
[python]: https://www.python.org/
[flask]: https://flask.palletsprojects.com/en/1.1.x/
[flask-restplus]: https://github.com/noirbizarre/flask-restplus
[psycopg2]: https://www.psycopg.org/docs/
