from flask import Flask, render_template, request
from flask import Flask, render_template, request

import random

app = Flask(__name__)
#this is feature-branch

# List of quotes
quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Dream big and dare to fail. – Norman Vaughan",
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
    "What we think, we become. – Buddha",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill"
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

@app.route("/base", methods=["GET", "POST"])
def base():
    message = ""
    if request.method == "POST":
        if "hello_btn" in request.form:
            message = "👋 You clicked Hello!"
        elif "goodbye_btn" in request.form:
            message = "👋 You clicked Goodbye!"
    return render_template("base.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
