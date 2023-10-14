python3 -m venv venv  # already created of deploy stage
source ./venv/bin/activate
pip3 install -r requirements.txt # already created of deploy stage
echo "=========================== user is"
whoami
echo "==========================="
pytest
deactivate