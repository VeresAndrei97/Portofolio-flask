from flask import Flask, redirect, url_for, render_template, request, flash
from flask_mail import Mail,Message
import os

app = Flask(__name__,static_url_path="",static_folder="img")


app.config['MAIL_SERVER']='smtp.gmail.com',
app.config['MAIL_PORT']=465,
app.config['MAIL_USE_SSL']=True,
app.config['MAIL_USERNAME'] = 'veresandrei97@gmail.com',
app.config['MAIL_PASSWORD'] = '07453082romania1'

mail=Mail(app)

@app.route("/", methods=['GET','POST'])
def home():
    return render_template("Index.html")

@app.route("/project")
def project():
    return render_template("Projects.html")

@app.route("/Resume")
def resume():
    return render_template("Resume.html")

@app.route("/Contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        email = request.form["email_user"]
        actual_msg = request.form["body_message"]
        msg= mail.send_message(subject="send mail message",
        sender='veresandrei97@gmail.com', 
        recipients=['veresandrei97@gmail.com'],body="Trying to send an email")
        mail.send(msg)
        flash("Your mail has been sent")
        
    else :
        return render_template("Contact.html") 



if __name__=="__main__":
    app.run(debug=True)