from flask import Flask, request, render_template
import os
import Storage
import Application.API.Data as Data

# Create an object of class Flask
app = Flask(__name__)
# Implement protection
app.secret_key = os.urandom(16) # Create a 16-bit random code
# Storage component
storage = Storage.Map()

# Home page


@app.route('/')
def index():
    return render_template("index.html")


# Sign up page
@app.route('/newsletter')
def newsletter():
    return render_template("newsletter.html")


@app.route('/form', methods=["POST"])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    preference = request.form.get('preference')
    # Store the values
    Storage.add(storage, email, name, preference)
    '''
    IMPORTANT:
        In future releases, newsletters would be released at
        08:00AM. However, for demo purposes, we will be
        immediately sending a newsletter.
    '''
    Data.sendMail(storage)
    return render_template("form.html")


if __name__ == "__main__":
    app.run(port=5000)