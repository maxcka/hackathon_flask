from flask import Flask, render_template, request

@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'myusername' and password == 'mypassword': 
            return 'You have logged in succesfully!'
        else:
            return 'Username or password error, please try again'
    if ".edu" not in username:
            return 'Please enter a valid email address containing ".edu"'
            
    return render_template('login.html')
