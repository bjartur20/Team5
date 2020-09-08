[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/bjartur20/Team5">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/b/b7/Reykjavik_University_Logo.svg/1200px-Reykjavik_University_Logo.svg.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Team 5</h3>

  <p align="center">
    Habit tracking platform for nutritional information
    <br />
    <a href="https://github.com/bjartur20/Team5"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/bjartur20/Team5">View Demo</a>
    ·
    <a href="https://github.com/bjartur20/Team5/issues">Report Bug</a>
    ·
    <a href="https://github.com/bjartur20/Team5/issues">Request Feature</a>
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
git clone https://github.com/bjartur20/Team5.git
```
2. Create a virtual environment(optional)
```sh
python3 -m venv venv
```
3. Move to API folder
```sh
cd API/
```
4. Install packages with pip
```sh
pip install -r requirements.txt
```
5. Move to main app folder
```sh
cd app/
```
6. Run the API
```sh
python app.py
```
7. Open the link: http://127.0.0.1:5000/ in a web browser and try out the REST API



<!-- TESTING -->
## Testing
The current code coverage of the repository is **97%**

* Running the unit tests, with coverage
```sh
coverage run -m pytest
```
* Getting the coverage report
```sh
coverage report -m
```


<!-- LECTURE ASPECTS -->
## Lecture Aspects
For this sprint we used a layered design where the database (data) and the Rest API (domain) work as independant entities. The presentation layer will be implemented in a future sprint.
Objer-Oriented Programming was implemented in the DBapi using abstract classes and a main gateway (see more in services README.md). Encapsulation is also used is various places in the API.


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
## TA

Gunnar Jörgen Viggósson





<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/bjartur20/Team5.svg?style=flat-square
[contributors-url]: https://github.com/bjartur20/Team5/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/bjartur20/Team5.svg?style=flat-square
[forks-url]: https://github.com/bjartur20/Team5/network/members
[stars-shield]: https://img.shields.io/github/stars/bjartur20/Team5.svg?style=flat-square
[stars-url]: https://github.com/bjartur20/Team5/stargazers
[issues-shield]: https://img.shields.io/github/issues/bjartur20/Team5.svg?style=flat-square
[issues-url]: https://github.com/bjartur20/Team5/issues
[product-screenshot]: https://i.imgur.com/WP7MQJj.png
[python]: https://www.python.org/
[flask-restplus]: https://github.com/noirbizarre/flask-restplus
[psycopg2]: https://www.psycopg.org/docs/
