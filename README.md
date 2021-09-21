# Dev Ops Assignment
[![Docker Image CI](https://github.com/Frodan/DevOps_flask/actions/workflows/docker-image.yml/badge.svg)](https://github.com/Frodan/DevOps_flask/actions/workflows/docker-image.yml)

This is a small web application, written on Python 3 for my friend, that is used for massive registration in crypto events.

## Usage
1. Go to /upload. Login and upload a csv file with wallets addresses.
2. After upload, workers can get wallet address for registration account by hands on /get_wallet.
Every wallet address shows only once.
3. Authenticated user can see some stats, used and unused wallets in /stats. 

## Installation
Install docker.

Build:
```bash
docker build -t flask_app .
docker run -e USER_LOGIN=<user> -e USER_PASS=<pass>  -p 8000:8000 flask_app
```
Or you can use ready image from docker hub:
```bash
docker run -e USER_LOGIN=<user> -e USER_PASS=<pass>  -p 8000:8000 frodan/dev_ops
```

Tests:
```bash
python test.py
```
## Routes
- Port: 8000
- /upload - upload csv to site
- /stats - stats of used wallets
- /get_wallet - show wallet

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)