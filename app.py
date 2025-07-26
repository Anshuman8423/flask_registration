from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not name or not email or not password:
            message = 'All fields are required!'
        else:
            message = f'Registration successful for {name}!'
    return render_template('register.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
