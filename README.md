# Dev Ops Assignment

This is a small web application, written on Python 3 for my friend, that is used for massive registration in crypto events.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage
Build:
```bash
docker build -t flask_app .
docker run -e USER_LOGIN=<user> -e USER_PASS=<pass> flask_app
```
Or you can use ready image from docker hub:
```bash
docker run -e USER_LOGIN=<user> -e USER_PASS=<pass> frodan/dev_ops
```

## Routes
- Port: 8000
- /uploads - upload csv to site
- /stats - stats of used wallets
- / - show wallet

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)