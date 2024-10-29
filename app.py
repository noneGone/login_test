from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Function to read users from the text file
def read_users():
    users = {}
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
    except FileNotFoundError:
        pass
    return users

# Function to write a new user to the text file
def write_user(username, password):
    with open('users.txt', 'a') as file:
        file.write(f"{username},{password}\n")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_users()
        
        if username in users:
            return "Username already exists! Please choose another one."
        
        write_user(username, password)
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_users()
        
        if username in users and users[username] == password:
            return "Login successful!"
        else:
            return "Invalid username or password!"
    
    return render_template('login.html')

@app.route('/')
def home():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)