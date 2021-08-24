import os
from flask import Flask, flash, request, redirect
from flask_httpauth import HTTPBasicAuth


UPLOAD_FOLDER = '/tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

username = os.environ['USER_LOGIN']
password = os.environ['USER_PASS']
unused_wallets = []
used_wallets = []


@auth.verify_password
def verify_password(user, passw):
    if user == username and passw == password:
        return username


@app.route('/upload', methods=['GET', 'POST'])
@auth.login_required
def upload():
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
                used_wallets = []
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


@app.route('/', methods=['GET'])
def get_wallet():
    if not unused_wallets:
        return "No wallets"
    else:
        print(unused_wallets)
        wallet = unused_wallets.pop()
        used_wallets.append(wallet)
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
    return f"""
        Used wallets: {len (used_wallets)}<br>
        Unused wallets: {len(unused_wallets)}<br>
        <br>
        Used:<br> 
        {"<br>".join(used_wallets)}
    """


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
