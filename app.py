from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    dolls = [
        {
            "name": "Barbie Doll",
            "description": "Classic fashion doll.",
            "image": "https://i.imgur.com/6X4Y5Qm.jpg"
        },
        {
            "name": "Princess Doll",
            "description": "Beautiful princess toy.",
            "image": "https://i.imgur.com/0y8Ftya.jpg"
        },
        {
            "name": "Baby Doll",
            "description": "Cute baby doll.",
            "image": "https://i.imgur.com/UPrs1EW.jpg"
        }
    ]

    return render_template("index.html", dolls=dolls)

if __name__ == "__main__":
    app.run(debug=True)