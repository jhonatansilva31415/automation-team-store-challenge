# Automation Challenge

## About

For this challenge, a fasion-related resource needed to be chosen, in the spirt of a previous mentioned product from the automation team, I went with some spiders to make a parser of, lo and behold, Dafiti itself. You can checkout the spider at the crawler folder. 

The idea is quite simple, why not leave the API open to more fashion-related resources over time? So to not carve it in stone a specific resource, a "product" was born. In this way, for future improvements on this API, we could only change the product model to require a new category relationship, that could be something like shoes, pants, shirts and so on.

For this crawler in specific, I went with shoes, it goes over the first page on the Dafiti search for "shoes" and stores the url of the image, brand, title and price (from and to, but only from is used in this project) in a dafiti.csv file. 

To run this project, you don't need to run the spider, because a .csv is provided for you to test it out. But if you are interested in some spiders, there's a section on the documentation that goes over how to run the spider, have fun. 

### How to run the code 

To run this app, you need to ensure that you have this installed on your system

- Docker

Annnnd, that's pretty much it, this is the magic of Docker, no dreadfull list of requirements :D

If you would like to use the magic that is behind the Makefile, it's good to use a Linux system

You can go and see all the commands in the Makefile if you like to skip ahead and try things on your own, the Makefile
is pretty much self explanatory, but, nontheless, if you preffer a more step 1, 2 approach, let's move on :D. 

---

## About the Tech 

### Backend 

- [Docker] As the container service to isolate the environment.
- [Flask RESTx] As the API layer
- [Postgre SQL] As the database layer
- [pytest] As the main TDD module
- [SQLAlchemy] As the "ORM" / model layer

### Frontend 

- [React] As the only start 


### Features

- Swagger - Import a CSV with products to the database
- Swagger - CRUD for the products
- Front to list, edit and search products 


# Getting Started

After installing docker, you pretty much need 3 steps to run the backend 

- Clone the repository
- Run  `make run-app`  in the root of the project, if on Linux, else `docker-compose up`

With this, the API should spin up, but you still need to create the tables for the database

Linux

`make local-createdb`

Windows

`docker-compose exec api python manage.py recreate_db`

You can now go to http://localhost:5000 and you should see the Swagger for the API.

If you experience any problems with postgres setup, you may need to clean up your system, sometimes it happens, mostly if you have other APIs that use the same name conventions. You can try `make stop` and `docker system prune`, it's a bit harsh, but it'll clean up your docker system. After that everything should run smoothly.

## Swagger
Now that you have access to the Swagger of the API, you'll have access to the following namespaces
- test
- data
- products

### The test namespace

This is just a dummy endpoint to get things started, if you never used the Swagger before, 
you can click on the test namespace, "test For test purposes only", click on the GET /test/echo, 
and press the button "Try it out", then the button "Execute", you will see the response body
```json
{
  "echo": "echo"
}
```
Now you are ready to explore the rest of the API

### The data namespace

This endpoint is mainly for uploading a CSV file with product data
into the API database. You can checkout a [CSV sample](https://github.com/jhonatansilva31415/automation_challenge/blob/main/data.csv.sample) (the endpoint will not accept this file though, you'll need to remove the .sample, but more on this later) in the root of the project 

But the main idea looks like this 
| url  | brand | title | from | to |
| ---- | ----- | ----- | ---- | -- |
| url 1  | brand 1  | title 1  | R$ x.xx  | R$ x.xx 
| url 2  | brand 2  | title 2  | R$ x.xx  | R$ x.xx

You can try it out upload a file from [the crawler](https://github.com/jhonatansilva31415/automation_challenge/blob/main/crawler/dafiti.csv)


### The Product namespace

Now that you tested the echo and uploaded some data into the API, you're ready to explore the CRUD functionality.

#### POST
If you try it out, you'll see that the payload for this endpoint looks like this
```json
{
  "id": 0,
  "url": "string",
  "brand": "string",
  "title": "string",
  "price": 0
}
```

You can edit the values and execute that you'll add a new product to the database. (the id is more for response marshalling and serialization, you can change it or leave it at zero that it won't matter)

#### GET 

The GET method is pretty much straight forward, you have a 
- `/crud/products` for all products
- `/crud/products/{product_id}` for a specific product

You can test out the `/crud/products` to see the product that you added in the previous section, with the ID of the product, you can make another request to `/crud/products/{product_id}` to see the specific product that you've added.


#### PUT 

As the post, the PUT expects
```json
{
  "url": "string",
  "img_url":"string",
  "brand": "string",
  "title": "string",
  "price": 0
}
```
And a required `product_id`, you try updating the product that you've created in the `POST` section

### DELETE 

The "delete" endpoint, does not actually delete the product, 
it sets it's is_active flag to `False`, it only expects the `product_id`, you can `DELETE` the product that you've created, and if you try to use the `/crud/products/` you'll see that your product is no longer listed, 
but you still can query him with `/crud/products/{product_id}`

--- 

## TDD 

Annnnnnd now, for the part that I know everyone is expecting, because every developer loves to test his application (I kid you not, but I actually like to write tests hahaha).

Writing tests for an API is usually more straight forward than writing tests for the frontend. 

You basically start at the `src/tests` folder, if you are going to update an endpoint, or write a new one, you can go to the specific file, e.g, for the `products`, you go to the `src/apis/product.py` and `src/tests/test_products.py`. You can now create a new test, or add functionality to an existing one. 

To run the tests, you can use

`make run-tests`, or `docker-compose exec api python -m pytest "src/tests"`

If x of y tests fail, and you want to run first the ones that fail, you can run 

`make run-fftests` or `docker-compose exec api python -m pytest "src/tests" --ff`

To run a specific and only test you can go for 

`docker-compose exec api python -m pytest "src/tests" -k "test_add_product"`

--- 

## Quality Checks 

You can also ensure the code quality (feel free to improve the script as you wish)
To run (this is a Linux script only, but you could run each command or create a script for windows) first you need to
change the exec permission with 

`chmod +x ./quality_check.sh` from the root of the project

This will run the follow 

- `docker-compose exec api isort src` for sorting out the imports (you may see some exclusions from isort in the code, this is due to circular import issues)
- `docker-compose exec api black src` for formatting the code, like deleting empty spaces and adding lines
- `docker-compose exec api flake8 src` for checking the code quality with flake8, you might want to add more conditions in the `setup.cfg` file
- `docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src"` for running tests and measuring the test coverage of the project (99% today, don't let us down, keep those tests going!)
- `sudo chown -R $(whoami) .` for Linux sake, sometimes the commands above mess up the file permissions of the folder, this only ensures that in the end, you still own your stuff.

--- 


## Frontend 

For the frontend, a simple React interface was created, as the Swagger API already satisfied the requirement for a interface that has a list of all resources and has the hability to consume it, the React side of it, was built more towards visualization and searching. It would be a nice feature in the future to add ElasticSearch to make a more robust search engine, today it's only using Javascript basic functions to make a filter.

To run the frontend, go to the front folder, and as the API, run `make run-app`, and that's pretty much it, feel free to play around now.

---

## Crawler

This project also has a specific spider to make a simple request, it goes to the first page of "shoes" on the dafiti website and scrapes data like

- URL
- Image URL
- Brand
- Title
- Price

If you want to see the spider in action, you need to have py3 installed on your system, then in the crawler folder run `make setup`. This will install all the requirements, you can make a python env before doing this. After installing the dependencies, you can run the crawler with `make run-app`, this will append data to the dafiti.csv file.

---


## Logging 

This project has no logging system built into it, but it would be a nice addition to add Sentry to capture all the errors

## Deploy on Heroku and Netlify 

The backend was deployed to Heroku, you can follow the Makefile, around `hcreate` to see the steps to deploy flask into Heroku with a PostgreSQL database.

https://murmuring-beyond-76885.herokuapp.com/

As for the frontend, it was a simple matter of uploading the "build" folder to Netlify, you can run make run-build to create the deploy folder, but you need to have yarn or npm to do it so.

https://gracious-ptolemy-44bdd9.netlify.app/

---

## Good resources for learning 

### Flask RESTx

- https://flask-restx.readthedocs.io/en/latest/
  
#### Sanitization for uploads
- https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask

#### Fields in flask 
https://flask-restx.readthedocs.io/en/latest/_modules/flask_restx/fields.html?highlight=stringmixin#

#### HTTPS deploy Heroku
https://flask-dance.readthedocs.io/en/v0.13.0/proxies.html

### Docker

- https://docs.microsoft.com/en-us/visualstudio/docker/tutorials/docker-tutorial

### TDD

- https://cucumber.io/docs/gherkin/reference/
- https://medium.com/@mvwi/story-writing-with-gherkin-and-cucumber-1878124c284c