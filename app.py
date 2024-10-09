from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Redirect to Instagram
@app.route('/instagram')
def instagram():
    return redirect('https://instagram.com/ig_hazard__')

# Redirect to Twitter
@app.route('/x')
def twitter():
    return redirect('https://x.com/hxxzardd')

# Redirect to LinkedIn
@app.route('/linkedin')
def linkedin():
    return redirect('https://www.linkedin.com/in/darsheel-chahar-92a4a5311/')

# Redirect to Discord
@app.route('/discord')
def discord():
    return redirect('https://discord.com/users/930055165480951809')

# Redirect to Telegram
@app.route('/telegram')
def telegram():
    return redirect('https://t.me/@hxxzardd')

# Redirect to GitHub
@app.route('/github')
def github():
    return redirect('https://github.com/Hxzardd')



if __name__ == '__main__':
    app.run(debug=True)
