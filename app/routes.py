from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import Login


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    # validate_on_submit判断用户的请求方式，验证数据
    if form.validate_on_submit():
        flash(f"Login requested for use {form.username.data}, "
              f"remember_me={form.remember_me.data}")

        # url_for绑定视图函数，返回视图函数的url
        return redirect(url_for("index"))

    return render_template("login.html", title="Sign In", form=form)