## Flask Application Design

### HTML Files

**index.html:**
- The main page of the application.
- Contains the HTML structure for displaying the input fields, submit button, and a section for displaying the results.
- Includes the necessary JavaScript for handling form submission and AJAX requests.
```html
<!DOCTYPE html>
<html>
  <head>
    <title>AI Query Application</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ZENh88jZCj6kh9l82SEna3JD727m1n3397gZ3sE49F2iVC0nkTl3sa4g7z36ttA6" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2JKwGw4j5xx2nCTd3hGsd9x1sF4k yes9efii0aUtKcu4l6N2896JEYLk" crossorigin="anonymous"></script>
  </head>
  <body class="container">
    <h1>AI Query Application</h1>
    <form id="query-form">
      <div class="mb-3">
        <label for="serial-numbers" class="form-label">Serial Numbers (separate by comma):</label>
        <input type="text" class="form-control" id="serial-numbers">
      </div>
      <div class="mb-3">
        <label for="attachment-names" class="form-label">Attachment Names (separate by comma):</label>
        <input type="text" class="form-control" id="attachment-names">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    <div class="results mt-3 border rounded p-3">
      <h3>AI Response:</h3>
      <p id="response"></p>
    </div>
  </body>
</html>
```

### Routes

**main.py:**
- The main Flask application file.
- Defines the routes and handles HTTP requests.

```python
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        serial_numbers = request.form.get("serial-numbers")
        attachment_names = request.form.get("attachment-names")

        # Query the database and get AI response
        response = make_query(serial_numbers, attachment_names)

        return jsonify({"response": response})
    return render_template('index.html')

def make_query(serial_numbers, attachment_names):
    # Replace with your actual query logic
    return "AI response for serial numbers: {}, attachment names: {}".format(serial_numbers, attachment_names)

if __name__ == '__main__':
    app.run(debug=True)
```

In this Flask application design:

- **index.html** is the main user interface, featuring input fields, a submit button, and a section for displaying the AI response.
- **main.py** handles the routing and HTTP request processing. It receives the input from the form, queries the database to get the AI response, and displays it on the index page.