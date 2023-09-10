import os
from flask import app
from flask import render_template, flash, redirect, url_for
from forms import LoginForm
from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Запрошен логин для пользователя {}, Запомните меня={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True)