from flask import Flask, render_template, request, Markup


app = Flask(__name__)  # Creating new flask app


@app.route("/client/<LCD>/", methods=['GET', 'POST'])  # Root for login page is index "/"
def client(LCD):
    with open(str("./" + LCD + ".txt"), 'r') as file:
        image = file.readline()
    image = "/static/" + image
    image = Markup(image)
    return render_template(
        "display.html", **locals())


@app.route("/control/<LCD>/<image_path>", methods=['GET', 'POST'])  # Root for login page is index "/"
@app.route("/control/<LCD>/", methods=['GET', 'POST'])  # Root for login page is index "/"
def control(LCD, image_path="Frame"):
    with open(str("./" + LCD + ".txt"), "w") as file:
        file.write(image_path + ".png")
    return render_template(
        "index.html", **locals())


@app.route("/control/<LCD>/<image_path>/<DIR>/", methods=['GET', 'POST'])  # Root for login page is index "/"
@app.route("/control/<LCD>/<image_path>/", methods=['GET', 'POST'])  # Root for login page is index "/"
def controlInner(LCD, image_path="Frame", DIR = "0"):

    with open(str("./" + image_path + "files.txt"), "r") as red:
        print("Opened files")
        files = red.readlines()
        with open(str("./" + LCD + "now.txt"), "r") as red2:
            print("Opened now")
            now = int(red2.readline().replace('\n', ' ').replace('\r', ''))
        d = int(DIR) + now
        if d >= len(files) or d <= 0:
            d = 0
        with open(str("./" + LCD + "now.txt"), "w") as red3:
            red3.write(str(d))
        print(d)
        image_path2 = files[d].replace('\n', '').replace('\r', '')
        print(image_path2)
        with open(str("./" + LCD + ".txt"), "w") as file:
            file.write(image_path2 + ".jpg")


    return render_template(
        "inner.html", **locals())


# Main flask app
if __name__ == "__main__":
    ip = input("Your ip is: ")
    # It creates https access by last argument. It is need to be give to web-page permission to microphone
    app.run(host=ip, port=8090, debug=True) #, ssl_context='adhoc')


