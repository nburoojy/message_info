

## Set up

xcode-select --install
sudo pip install virtualenv
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
pip install --editable .

FLASK_APP message_info flask run

http -f post 127.0.0.1:5000/ message="test mention @foo"

to test
py.test tests/

## Todo

Move url lookups into a service
Implement url cacheing
Monitoring
Logging

