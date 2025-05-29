from flask import Flask, redirect, url_for, session, request, render_template
from authlib.integrations.flask_client import OAuth
import sqlite3

app = Flask(__name__)
app.secret_key = 'RANDOM_SECRET_KEY'
oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id='617626641717-h7id283c974boc59t4fim555j0qpsguu.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://oauth2.googleapis.com/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params={'access_type': 'offline'},
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://www.googleapis.com/oauth2/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login')
def login():
    return google.authorize_redirect(redirect_uri=url_for('auth', _external=True))

@app.route('/auth')
def auth():
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()
    session['email'] = user_info['email']
    return redirect(url_for('get_name'))

@app.route('/get_name', methods=['GET', 'POST'])
def get_name():
    if request.method == 'POST':
        name = request.form.get('name')
        email = session.get('email')

        conn = sqlite3.connect('datrfe.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (email TEXT, name TEXT)''')
        c.execute("INSERT INTO users (email, name) VALUES (?, ?)", (email, name))
        conn.commit()
        conn.close()

        return f"<h3>Name '{name}' saved for {email}!</h3>"

    return render_template('get_name.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('homepage'))
