# Website
New website with better UI written in Django.

## Requirements
- entr is required to use live reload `style.scss` compilation
- scss is required to compile stylesheets
- python3 and pip (of course)

### Installing python server dependencies
#### Use requirements.txt
_**NOTE**: It is recommended to install using pipenv_
```
python3 -m pip install --user -r requirements.txt
```
#### Use Pipenv
This is the recommended way of installing python dependencies.  
__Pipenv is required__
```
python3 -m pipenv install
python3 -m pipenv shell
```

## Usage
By default every time you start the server with `python pitv/manage.py runserver` it uses different key. In order to change that, make `local_settings.py` in `pitv/pitv/`.

First, create database with:
```
./manage.sh migrate
```
Second, create admin user:
```
./manage.sh createsuperuser
```
Finally, run the server:
```
./run.sh
```

## Contributing
Feel free to open issue or pull request.  
Usually `grep  -i "TODO" -r .` will reveal things that should be changed
