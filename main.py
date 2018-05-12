from flask import Flask, render_template, request, Markup


app = Flask(__name__)  # Creating new flask app


@app.route("/1/client/", methods=['GET', 'POST'])  # Root for login page is index "/"
def client1():
    image = "static/clev.png"
    return render_template(
        "show.html", **locals())


@app.route("/1/control/<image_path>", methods=['GET', 'POST'])  # Root for login page is index "/"
@app.route("/1/control/", methods=['GET', 'POST'])  # Root for login page is index "/"
def control1():
    image = "static/clev.png"
    return render_template(
        "home.html", **locals())


# Main flask app
if __name__ == "__main__":
    # It creates https access by last argument. It is need to be give to web-page permission to microphone
    app.run(host='0.0.0.0', port=8090) #, ssl_context='adhoc')