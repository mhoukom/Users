from flask import render_template, redirect, request

from flask_app import app

from flask_app.models.user import User


@app.route("/")
def index():
    all_users = User.get_all()
    return render_template("index.html", all_users = all_users)


@app.route("/users/new")
def new_user_form():
    return render_template("new_user.html")


@app.route("/users/create", methods = ["POST"])
def create_user():
    User.create(request.form)
    return redirect("/")


@app.route("/users/<int:user_id>")
def display_user(user_id):
    return render_template("user.html", user = User.get_one({"id": user_id}))


@app.route("/users/<int:user_id>/edit")
def edit_user_form(user_id):
    return render_template("edit_user.html", user = User.get_one({"id": user_id}))


@app.route("/users/<int:user_id>/update", methods = ["POST"])
def update_user(user_id):
    print(request.form)
    data= {
        **request.form,
        "id": user_id
    }
    User.update(data)
    return redirect(f"/users/{user_id}")


@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    User.delete({"id":user_id})
    return redirect("/")