from flask import Flask, render_template, redirect, url_for, session, request
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = 'random_secret_key'

# OAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='YOUR_GOOGLE_CLIENT_ID',
    client_secret='YOUR_GOOGLE_CLIENT_SECRET',
    access_token_url='https://oauth2.googleapis.com/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params={
        'access_type': 'offline',
        'prompt': 'consent',
    },
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://www.googleapis.com/oauth2/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/')
def index():
    user_email = session.get('email')
    return render_template('index.html', user_email=user_email)

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    session['email'] = user_info['email']
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/<page>')
def secure_pages(page):
    if 'email' not in session:
        return redirect('/login')
    return render_template(f'{page}.html', user_email=session.get('email'))

if __name__ == '__main__':
    app.run(debug=True)
