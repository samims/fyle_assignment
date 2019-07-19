# Bank API

## Installation

Create virtualenv (Python3.6)
```bash
virtualenv -p python3.6 venv_name
```
Activate virtualenv using
```bash
source venv_name/bin/activate
```
Clone this repo to your machine using
```bash
git clone https://github.com/samims/fyle_assignment.git
```
Install requirements.txt file
```bash
pip install -r requirements.txt
```

# Run 
Go to the project directory 
where manage.py file is located.

Migrate using
```bash
python manage.py migrate
```

To run
```bash
python manage.py runserver
```

To run tests use this command
```bash
python manage.py test
```
# API documentation

Signup API http://fyle-sam.herokuapp.com/signup/ 

Provide payload(example) 
```bash
{
    "first_name": "sam",
    "last_name": "test"
    "username": "samtest",
    "email": "samtest@example.com",
    "password": "sampass"
}
```
cURL

```bash
curl -X POST -H 'Accept:application/json;' -d first_name=sam -d last_name=test -d username=samtest -d email=samtest@example.com -d password=sampass http://fyle-sam.herokuapp.com/signup/

```

Obtain token API http://fyle-sam.herokuapp.com/api-token-auth 

Example payload:
```bash
{
    "username": "samtest",
    "password": "sampass"
}

```

cURL
```bash
curl -X POST -H 'Accept:application/json;' -d username=samtest -d password=sampass http://fyle-sam.herokuapp.com/api-token-auth/

```

It will return JWT token

Token verification

```bash
curl -X POST -H 'Accept:application/json;' -d token=your auth token http://fyle-sam.herokuapp.com/api-token-verify/
```

Token refresh

```bash

curl -X POST -H 'Accept:application/json;' -d token=your auth token http://fyle-sam.herokuapp.com/api-token-refresh/
```



Search by ifsc

```bash
curl -X GET -H 'Accept:application/json' -H 'Authorization:JWT token' http://fyle-sam.herokuapp.com/banks/?ifsc=ABHY0065028

```


Search by bank name and city
```bash

curl -X GET -H 'Authorization: JWT token' 'http://fyle-sam.herokuapp.com/banks/branch/?city=Kolkata&name=State%20Bank%20of%20India'

```
