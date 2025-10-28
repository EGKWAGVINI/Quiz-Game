from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-me"  # replace this in production

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form.get("full_name", "")
        email = request.form.get("email", "")
        # password = request.form.get("password", "")
        flash(f"Welcome, {full_name or email}! (demo only)", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # TODO: authenticate user here if needed
        email = request.form.get("email", "")
        flash(f"Signed in as {email} (demo only)", "success")
        # redirect to main page after sign-in
        return redirect(url_for("main_page"))
    return render_template("login.html")

@app.route("/guest")
def guest():
    flash("Continuing as Guest (demo route).", "info")
    # redirect to main page after guest login
    return redirect(url_for("main_page"))

@app.route("/main_page")
def main_page():
    return render_template("main_page.html")

if __name__ == "__main__":
    app.run(debug=True)
