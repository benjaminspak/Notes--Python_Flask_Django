### Dunder
+ If a script is imported the whole script will run.
+ Using dunder ensures that the full script only runs if directly called.
+ Importing a script after using dunder will stop all imported scripts from automatically running.
+ Importing will dunder will give you greater control; requiring you to call each of the imported script's methods you want to run.

#### Dunder name main conditional
+ Only allows execution of code block, if not imported.

##### app.py
```python
def print_hello():
    print("Hello from app.")

if __name__  == '__main__':
    print_hello()

```

#### Structed imports with dunder
##### second_app.py

```python
import app

print("Hello from second app")
app.print_hello()

```