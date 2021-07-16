from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)
app.secret_key = 'bigsecrets'

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def read():
    users = User.get_all_users()
    return render_template('read.html', users = users)

@app.route('/users/create', methods=['POST', 'GET'])
def create_user():
    # if request.method == 'POST':
        # return User.create_user(request.form)
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)