#Local Web Application using Flask

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Dummy credentials
valid_username = "admin"
valid_password = "password"

# Simple login form
login_form = '''
<!doctype html>
<title>Login</title>
<h2>Login</h2>
<form method=post>
  Username: <input type=text name=username><br>
  Password: <input type=password name=password><br>
  <input type=submit value=Login>
</form>
'''

# Login endpoint
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == valid_username and password == valid_password:
            return "Login successful"
        else:
            return "Login failed"
    return render_template_string(login_form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
