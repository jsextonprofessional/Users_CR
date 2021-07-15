from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)
app.secret_key = 'bigsecrets'

@app.route('/')
def index():
    users = User.get_all_users()
    for user in users:
        print(user.id)
    return "I work for now!"

if __name__=="__main__":
    app.run(debug=True)