from flask import Flask, request, redirect, render_template, send_from_directory



app = Flask(__name__)

# Supongamos que estos son los datos de inicio de sesión correctos
correct_username = "admin"
correct_password = "password"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != correct_username or request.form['password'] != correct_password:
            error = 'Usuario o contraseña erronea'
        else:
            return redirect('/')
    return render_template('login.html', error=error)

@app.route('/')
def home():
    
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)