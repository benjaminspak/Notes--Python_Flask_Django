### Flask Basics

```
pip install flask
```

+ Flask scripts are called apps.

##### Key terms:
+ View: A view is a function that returns an HTTP response. This response has to be a string but can be any string you want.
+ Route: A route is the URL path to a view. They always start with a forward slash / and can end with one if you want.
+ dunder: A quick way of saying "double underscore". Ex: '__name__'

##### Building a response

```python
from flask import Flask

# Create a new flask instance in the local name space
app = Flask(__name__)

# Create a decorator/view/response function for the '/' url
@app.route('/')
def index(name="Treehouse"):
  return "Hello from the {}!".format(name)

app.run(debug=True, port=8000, host='0.0.0.0')
```

#### Building a request / response

##### Key Terms

+ global: A global is a variable that exists outside of the normal Python scopes. It is available everywhere.
+ query string: The part of a URL that comes after the ?. You'll notice that the information after this looks like keyword arguments.
+ request: request is a Flask global that represents the request that the client has made to your application. This contains things like cookies, the path, and, in our usage, the query string.

```python
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name="Treehouse"):
  name = request.args.get('name', name)  # Accept a query string 
  return "Hello from the {}".format(name)

app.run(debug=True, port=8000, host='0.0.0.0')
```

##### Sample Query

```
/?name=Benjamin
```

#### Doing away with query strings

+ Views can have more than one route

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')  # Capture the incoming sting value
def index(name="Treehouse"):
  return "Hello from the {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')  # Specify input type int
def add(num1, num2):
  return '{} + {} = {}'.format(num1, num2, num1+num2)
app.run(debug=True, port=8000, host='0.0.0.0')
```

```
/benjamin  # returns benjamin
```

```
/add/5/2  # returns 7
```