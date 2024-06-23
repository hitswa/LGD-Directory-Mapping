python3 --version
pip install --upgrade pip
python3 -m venv .
source ./bin/activate
pip freeze > requirements.txt
python3 -m pip install -r requirements.txt