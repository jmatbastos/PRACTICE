from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

from flask import Flask
from flask_mail import Mail
from flask_mail import Message
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 25
mail = Mail(app)

from .db_auth import (
    register_user,login_user,activate_user
)

from .form import RegisterUserForm

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    pass

@bp.route('/login', methods=('GET', 'POST'))
def login():
    pass

@bp.route('/logout')
def logout():
    session.clear()    
    return render_template('careers/message.html', message="Bye, see you back soon!")


@bp.route('/activate/<token>')
def activate(token):
    activate_user(token)
    return render_template('careers/message.html', message="Account activated, you can now login.")


def send_email(email, activation_digest):
    msg = Message(
    subject="Registration activation",
    sender="webmaster@josebastos.eu",
    recipients=[email],
    )
    msg.html = render_template('auth/email.html',activation_digest=activation_digest)
    mail.send(msg)
    return





