from flask import (Flask, render_template, request, flash, session,
                   redirect)

app = Flask(__name__)
# app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Homepage displaying navigation and intro."""

    return render_template("home.html")

@app.route('/contact')
def contact_page():
    """displaying contact info, links and projects."""

    return render_template("contact.html")




if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)