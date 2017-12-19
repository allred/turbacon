# turbacon

This software was developed using Python 3.6.3 and Flask.

To run the server (inside a virtualenv):

```
git clone https://github.com/allred/turbacon.git
cd turbacon
pyenv virtualenv 3.6.2 turbacon
pyenv activate turbacon
pip install -r requirements.txt
pip install --editable .
API_KEY_TURBACON=YourApiKeyHere ./runme
```

Then visit http://localhost:5000 (or whichever URL is listed in the command output)
