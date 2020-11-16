from flask import Flask , render_template, request, redirect, url_for
from flask_mail import Mail, Message
from config import mail_username, mail_password

app = Flask(__name__) 

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": mail_username,
    "MAIL_PASSWORD": mail_password
}

app.config.update(mail_settings)
mail = Mail(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("structure.html")

@app.route("/send", methods=['GET', 'POST'])
def send():
    if request.method == "POST":
        name = request.form.get('user_name')
        email = request.form.get('user_email')
        text = request.form.get('user_text')
        
        msg = Message(subject=f"Mail from {name}",sender=email,recipients=[mail_username])
        msg.body = f"Name: {name}\nE-Mail: {email}\n\n\n{text}"
        mail.send(msg)

    elif request.method == "GET":
        return redirect(url_for('structure.html', **kwargs))

    return render_template("structure.html", success=True)

if __name__ == "__main__":
    app.run(debug=True)