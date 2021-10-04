import os
import datetime
from flask import Flask, flash, request, redirect
from flask_httpauth import HTTPBasicAuth
from collections import Counter

UPLOAD_FOLDER = '/tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

try:
    username = os.environ['USER_LOGIN']
    password = os.environ['USER_PASS']
except:
    username = "borov"
    password = "borov"

users = {
    username: password
}
unused_wallets = []
used_wallets = {}


@auth.verify_password
def verify_password(user, passw):
    if users.get(user) == passw:
        return username


@app.route('/upload', methods=['GET', 'POST'])
@auth.login_required
def upload():
    if auth.username() != username:
        return "Not an admin"
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        else:
            filename = 'tmp.csv'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r') as wallets_file:
                global unused_wallets, used_wallets
                unused_wallets = [x.strip() for x in wallets_file.readlines()]
                used_wallets = {}
            return redirect('/stats')
    else:
        return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload_users', methods=['GET', 'POST'])
@auth.login_required
def upload_users():
    if auth.username() != username:
        return "Not an admin"
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        else:
            filename = 'users.csv'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r') as users_file:
                global users
                users = {
                    username: password
                }
                for user in users_file.readlines():
                    print(user)
                    login, passw = [x.strip() for x in user.split(',')]
                    users[login]= passw
            return redirect('/stats')
    else:
        return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/get_wallet', methods=['GET'])
@auth.login_required
def get_wallet():
    if not unused_wallets:
        return "No wallets"
    else:
        print(unused_wallets)
        wallet = unused_wallets.pop()
        used_wallets[wallet] = (auth.username(), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return f'''
        <!doctype html>
        <title>Wallet</title>
        <h1>Wallet</h1>
        <input type="text" value="{wallet}" id="myInput">
        <button onclick="myFunction()">Copy Wallet</button>
        <button onClick="window.location.reload();">Next</button>
        <script>
            function myFunction() {{
              var copyText = document.getElementById("myInput");
              
              copyText.select();
              copyText.setSelectionRange(0, 99999); /* For mobile devices */
            
              document.execCommand("copy");
            
            }}
        </script>
        '''


@app.route('/stats', methods=['GET'])
@auth.login_required
def get_stats():
    if auth.username() != username:
        return "Not an admin"
    counter_str =[f"{x} : {y}" for x,y in Counter([z[0] for z in used_wallets.values()]).items()]
    wallets_to_print = [f"{x} : {used_wallets[x]}" for x in used_wallets.keys()]
    return f"""
        Users" {users}<br>
        Used wallets: {len(used_wallets)}<br>
        Unused wallets: {len(unused_wallets)}<br>
        <br>
        Used:<br>
        {"<br><br>".join(counter_str)}
        <br><br>
        {"<br><br>".join(wallets_to_print)}
    """


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
