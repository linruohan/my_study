from flask import Flask
from flask import request,render_template,redirect
from db import *
app=Flask(__name__)

from wtforms import Form,TextField,PasswordField,validators

class LoginForm(Form):
    username=TextField("username",[validators.Required()])
    password=PasswordField("password",[validators.Required()])

@app.route("/user",methods=['GET','POST'])
def Login():
    myForm=LoginForm(request.form)
    if request.method=='POST':
        if myForm.username.data=="xiaohan" and myForm.password.data=='123456' and myForm.validate():
            return redirect("http://www.baidu.com")
        else:
            message="login failed"
            return render_template('index.html',message=message,form=myForm)
    return render_template('index.html',form=myForm)

@app.route("/register",methods=['GET','POST'])
def register():
    myForm=LoginForm(request.form)
    if request.method=='POST':
        addUser(myForm.username.data,myForm.password.data)
        return "register successfully"
    return render_template('index.html',form=myForm)


if __name__ == '__main__':
    app.run(port=8080)
