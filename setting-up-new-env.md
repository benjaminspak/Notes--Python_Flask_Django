### Setting up a new Python Env

```
python -m pip install pipenv
pipenv install requests
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

+ When seeking to deploy to production:

```
# Lock the dependencies
$ pipenv lock
# On prod deploy the same env as staging.
$ pipenv install --ignore-pipfile

```

+ To generate a dependency graph

```
pipenv graph
```