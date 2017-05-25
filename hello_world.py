from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

# @app.route("/hello/<name>")
# def hi_person(name):
#     return "Hello {}!".format(name.title())

@app.route("/hello/<name>")
def hello_person(name):
    return render_template('template.html', my_name=name)

@app.route("/jedi/<firstname>/<lastname>")
def hi_person(firstname, lastname):
    jediname = lastname[:3] + firstname[:2]
    return "Hello {}!".format(jediname.title())

@app.template_filter()
def title_format(word):
    """Convert first letter to uppercase"""
    formatted_word = word[0].upper()
    new_word = formatted_word + word.split(word[0])[1]
    return new_word

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888)
