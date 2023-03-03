from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# hard-coded username and password
username = 'admin'
password = 'password'


@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
<head>
	<title>Hack Syndicate Login</title>
	<style>
		body {
			background-color: black;
			color: #00FF00;
			font-weight: bold;
		}
		form {
			margin: 50px auto;
			width: 400px;
			padding: 40px;
			border-radius: 10px;
			box-shadow: 0px 0px 10px 0px rgba(255,255,255,0.4);
			text-align: center;
		}
		h1, h2 {
			margin: 0;
		}
		input {
			display: block;
			margin: 20px auto;
			padding: 10px;
			border-radius: 5px;
			border: none;
			width: 80%;
			font-size: 18px;
		}
		button[type="submit"] {
			background-color: white;
			color: black;
			border: none;
			padding: 10px 20px;
			border-radius: 5px;
			font-size: 18px;
			cursor: pointer;
			transition: all 0.3s ease-in-out;
		}
		button[type="submit"]:hover {
			background-color: #00FF00;
			color: white;
			box-shadow: 0px 0px 10px 0px rgba(0,255,0,0.4);
		}
	</style>
</head>
<body>
	<form method="post" action="/login">
		<h1>Hack Syndicate Login</h1>
		<h2>THC-Hydra Password Cracking Demo</h2>
		<input type="text" name="username" placeholder="Username" required>
		<input type="password" name="password" placeholder="Password" required>
		<button type="submit">Login</button>
	</form>
</body>
</html>
    '''
        
@app.route('/login', methods=['POST'])
def login():
    input_username = request.form['username']
    input_password = request.form['password']
    if input_username == username and input_password == password:
        # user is authenticated
        return '''
    <!DOCTYPE html>
<html>
  <head>
    <title>Hack Syndicate Hydra Login Demo</title>
    <link rel="icon" type="image/png" href="hydra2thumbnail.png">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" />
  </head>
  <body style="background-color: black; color: white; font-weight: bold; text-align: center; padding: 20px;">
    <div style="background-color: black; color: white; font-weight: bold; text-align: center; padding: 20px;">
      <h1 style="color: #00FF00; font-size: 40px; margin-top: 0;">Successful Login!</h1>
    </div>
    <div style="background-color: black; color: #00FF00; font-weight: bold; text-align: center; padding: 50px;">
      <h1 style="font-size: 80px; margin-top: 0;">Welcome to the Hack Syndicate</h1>
    </div>
    <div style="background-color: black; color: #00FF00; font-weight: bold; text-align: center; padding: 50px;">
      <h1 style="font-size: 60px; margin-top: 0;">Check out my links:</h1>
      <a target="_blank" href="https://www.youtube.com/channel/UCkrS8x1_OWTD7KrXUg_ALiA" style="color: blue; font-size: 40px; text-decoration: none; margin-right: 30px;">YouTube</a>
      <a target="_blank" href="https://github.com/bfrisbyh92" style="color: blue; font-size: 40px; text-decoration: none; margin-right: 30px;">GitHub</a>
      <a target="_blank" href="https://brendanfrisby.live" style="color: blue; font-size: 40px; text-decoration: none; margin-right: 30px;">Website</a>
      <a target="_blank" href="https://frisbyblog.vercel.app" style="color: blue; font-size: 40px; text-decoration: none;">Blog</a>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
  </body>
</html>
			''';
    else:
        # invalid username or password
        # We will need this failure term for our Hydra command
        return '''
				<!DOCTYPE html>
<html>
  <head>
    <title>Login Failed Hack Syndicate</title>
    <link rel="icon" type="image/png" href="hydra2thumbnail.png">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
    <style>
      body {
        background-color: black;
        color: white;
        font-weight: bold;
        text-align: center;
        padding: 20px;
      }
      h1 {
        color: yellow;
        font-size: 80px;
        margin-top: 25;
      }
      h2 {
		  color: limegreen;
	  }
   	  h3 {
		  color: limegreen;
	  }
      .footer {
        position: absolute;
        bottom: 0;
        width: 100%;
        background-color: black;
        padding: 20px;
      }
      .footer a {
        color: blue;
        font-size: 40px;
        text-decoration: none;
        margin-right: 30px;
      }
      .footer a:hover {
        color: white;
      }
    </style>
  </head>
  <body>
    <h1>Login Failed</h1>
    <h2>Hack Syndicate</h2>
    <h3>Please like and subcribe if this demo is helpful. I appreciate everyone, thanks for your support!</h3>
    <div class="footer">
      <a href="https://www.youtube.com/channel/UCJ68g5Iw83LYeB22imJhZng" target="_blank">YouTube</a>
      <a href="https://github.com/bfrisbyh92" target="_blank">GitHub</a>
      <a href="https://brendanfrisby.live" target="_blank">Website</a>
      <a href="https://frisbyblog.vercel.app" target="_blank">Blog</a>
    </div>
  </body>
</html>
    '''


if __name__ == '__main__':
    app.run(debug=True)
