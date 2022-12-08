# apiflask by joel
## readme


apiflask is a api rest to registering, loging, verify email by received code and login is authby the basic auth .

##summary
- 1 project architecture schema
- 2 instruction to run and test this application
- 3 github link to access sources code

## 1 project architecture schema (principal folder and file)

- app(folder)
  - config(folder)
    - conf(file)
  - crud(folder)
    - userscrud(file)
  - models(folder)
    - users(file)
  - services(folder)
     - utils(file)
  - app(file)
  - wsgi(file)
  - __init__(file)
  - 
- env(folder)
- .env(file)
- .env.prod(file)
- .flaskenv(file)
- docker-compose(file)
- dockerfile(file)
- readme.md(file)
- requirements

__app__ is the pricipale folder to put all project manuel resources.
__crud__ is a database folderto create my sql request to get or put information since my db. i contain the file usercrud only because i have single table in my database
__models__ is a folder to rang a request shema. i contain a single file named users.
__services__ is for my custom method and  my reused function in all application. the file who contain my custom function isnamed utils
__app__ file is the main of my application. i import my apiflask packages in this file.
__wsgi__ it's the entry point of my application to run my application in production environnement with gunicorn.
other file is the configuration file


## 2 instruction to run and test this application

- you can clone my application the git repos in the end of this documentation or the reception end project email you're receive 
- open the project in you're favorite code editor
- you can run ``` pip install -r requirements.txt ``` cmd to install all project dependencies if you excecute in localy without docker
- if you use docker . run ```docker-compose --env-file=.env.prod up -d``` in docker commande print to create image, create your container and build all microservice app i created in dockercompose file
- normally the application run and you can verify in your browser __localhost:5000/docs__
- if it's ok , all endpoints of this application is show now
- you can test all endpoints directly in swagger and if you want to seethe application redocs you can excecute this __localhost:5000/redoc__
- i make my application test with postman and swagger
- i deploy my application in unbuntu server

## 3 github link to access sources code

my github link to clone or see my code sources is  :

| repos github |
| ------ |
| [https://github.com/XcoderDJOUE/apiflask] |


for run application in dev mode you can change it in .flaskenv file in the application root

commande to run it on local dev environment
```sh
cd apiflask
pip install -r requirements.txt
flask run --reload --host=0.0.0.0 --port=5000
```
__NB: not forget to install localserveur or SGBD. me i'm used xampp to my local dev__
--- 
For production environments...

```sh
#use gunicorn to run in production and change .flaskenv file FLASK_ENV=production
gunicorn -w 4 -b=0.0.0.0:5000 app.wsgi:app
#gunicorn work in linux environment only
```

