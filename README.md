# Python Telegram Services

It has been developed to register the participants of telegram groups in the database, written in Python.

### Install

1. Change current directory
    - `cd /home/ubuntu/python_telegram_services`

2. Create virtual environment and install requirements into it
    - `python3 -m venv venv3`
    - `source venv3/bin/activate`
    - `pip install --upgrade pip`
    - `pip install -r requirements.txt`

3. Create environment variables
    - `export MONGO_USERNAME='<username>'`
    - `export MONGO_USERNAME='<password>'`
    - `export TELEGRAM_API_ID='<api_id>'`
    - `export TELEGRAM_API_ID='<api_hash>'`

4. Start the scripts
    - `nohup python3 -u python_telegram_services/<script_name>.py > <script_name>.log &`

You can now see its logs with `tail -f <script_name>.log`.

### Note

At the moment, the `requirements.txt` is not necessary. The project doesn't
use any packages outside of the Python standard library. Eventually, I plan
to show some more advanced features that will use packages from PyPI.