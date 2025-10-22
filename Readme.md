step 1: create a docker container
command: docker run --name postgres-db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres

step 2: check if docker container is running
command: docker ps

step 3: open pgadmin and creat a new server
note: give the same credentials given while creating a docker container.

step 4: open vscode and create a virtual environment
commands
4.1 installing venv : pip3 install virtualenv
4.2 creating a virtual environment: python -m venv nameOfTheEnvironment
4.3 activating the virtual environment : venv\Scripts\Activate

step 5: Install flask SQl alchemy orm and pyjwt
command: pip3 install Flask Flask-SQLAlchemy PYJWT

step 6: freeze all dependencies in a requiriments.txt file
command: pip3 freeze > requiriments.txt

step 7: initialize everything in init.py file like db, flask app.

setp 8: initialize the database models in models.py file.


