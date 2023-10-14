python3 -m venv venv  # is it must already created at deploy stage?
source ./venv/bin/activate
pip3 install -r requirements.txt # is it already created at deploy stage?
echo "=========================== user is"
whoami
echo "==========================="
pytest
deactivate