### Flat HTML

##### Things to Remember
+ Use {{ and }} to print items in templates. Can use {{ with spaces }} or {{without spaces}}.
+ Flask looks for templates in a directory named templates by default. This directory should be in the same directory as your app script.

```python
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
  return "Hello from the {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
  return render_template("'add.html', num1=num1, num2=num2)  # References add.html


app.run(debug=True, port=8000, host='0.0.0.0')
```

```html
<!doctype html>
<html>
  <head><title>Adding!</title></head>
  <body>
    <h1>{{num1}} + {{num2}} - {{num1*num2}}</h1>
  </body>
</html>
```

##### Jinja Template Inheritance

+ {% block %}: This template tag (as they're called) defines a block in a template. In templates that are extended, these areas are overridable. In templates that extend other templates, this areas will override the parent template's block.
+ {% extends %}: This template tag specifies what template is the parent of the current template. Think of it like extended classes in Python. You can have a change of extensions if you need them.
+ {{ super() }}: This function brings in whatever content was in the same block in the parent template. Very handy if you want to include the existing content but you want to insert new content before or after the old.

```html
<!doctype html>
<html>
  <head>
    <title>{% block title %}Flask Basics{% endblock %}</title>
  </head>
  <body>
    {% block content %}{% endblock %}
    <p>Brought to you by the fine folks at Treehouse!</p>
  </body>
</html>
```

```html
{% extends "layout.html" %}

{% block title %}Howdy! | {{ super() }}{% endblock %}

{% block content %}
<h1>Hello from {{ name }}!</h1>
{% endblock %}
```

##### Will display

```html
<!doctype html>
<html>
  <head>
    <title>Howdy! | Flask Basics</title>
  </head>
  <body>
    <h1>Hello from Benjamin!</h1>
    <p>Brought to you by the fine folks at Treehouse!</p>
  </body>
</html>
```

#### Added static files / style sheets

+ The static/ directory is served automatically at /static while you're running your Flask app.
+ You also don't have to use every block in every child template. If you don't specify a new version of the block, Flask will just use whatever is there in the parent template.