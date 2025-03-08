from flask import Flask, render_template, redirect, request, url_for, flash
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False


app.config["SECRET_KEY"] = "Your secret key"




ALLOWED_EXTS = {"txt", "jpeg", "jpg", "png","TXT","JPEG","JPG","PNG"}

def check_file(file):
    return file.endswith(tuple(ALLOWED_EXTS))


@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    error = None
    filename = None

    if request.method == "POST":
        if "file" not in request.files:
            error = "File not selected"
            return render_template("form.html", error = error)
        
        file = request.files['file']
        filename = file.filename

        if filename =='':
            error = "File name is empty."
            return render_template("form.html", error = error)
        
        if check_file(filename) == False:
            error = "This file is not supported."
            return render_template("form.html",error = error)
        
        file.save(os.path.join("/coding/something/uploads",filename))

    return render_template("form.html", error=error,filename = filename)


if __name__ == "__main__":
    app.run(debug=True)
