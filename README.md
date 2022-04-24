# yezza-project
Create Basic API using Django REST

## Requirements
- Python 3
- PostgreSQL 

## How to Run
- Clone this project: `git clone https://github.com/mridho2828/yezza-project.git`
- Setup database

    - Run postgresql locally
    - Create new database yezza `createdb postgres`
    - Enter postgresql database as superuser `psql yezza -U [your-user]`
    - Create user "yezza" with password "foobar" `CREATE USER yezza with password 'foobar';`
    - Grant all privileges of the database to the user `GRANT ALL ON DATABASE yezza TO yezza;`
- Go to project directory. Before installing the requirements and run the project, it is recommended to create virtual environment
- Install requirements: `pip install -r requirements.txt`
- Run migration first:
  
    - `python manage.py makemigrations`
    - `python manage.py migrate`
    
- Run server to use the APIs: `python manage.py runserver`. The server should now be running on localhost port 8000

## How to test

- Create superuser: `python manage.py createsuperuser` and then enter the desired credential.
- Login to django admin `http://127.0.0.1:8000/admin/` using your superuser. You can then add another user.
- You can see the result of GET request via endpoint `http://127.0.0.1:8000/notes/`, however you should not be able to create, delete, or update notes.
- To perform create, delete, or update request you should be authenticated first. Since the project uses token authentication, you have to obtain auth token first before sending your request.
To get auth token, you can do POST request via url `http://127.0.0.1:8000/notes/` by entering corresponding user and password:
  `http POST http://127.0.0.1:8000/token-auth/ username=[user] password=[password].` Alternatively, you can also use curl
- You can now perform create, delete, or update request by providing the auth token. For example to create a new note you can do a POST request.
```
 http POST http://127.0.0.1:8000/notes/ "Authorization: Token [AUTH_TOKEN]" \
 author='author' \
 text='something here' \
 attachments:=`[1,2,3]`
 ```