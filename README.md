# Python Telegram Services

It has been developed to register the participants of telegram groups in the database, written in Python.

### Install 

1. Clone repository
    - `cd /home/ubuntu`
    - `git clone https://github.com/barisariburnu/python_telegram_services.git`

2. Change current directory
    - `cd /home/ubuntu/python_telegram_services`

3. Create virtual environment and install requirements into it
    - `python3 -m venv venv3`
    - `source venv3/bin/activate`
    - `pip install --upgrade pip`
    - `pip install -r requirements.txt`

4. Create environment variables
    - `export MONGO_USERNAME='<username>'`
    - `export MONGO_USERNAME='<password>'`
    - `export TELEGRAM_API_ID='<api_id>'`
    - `export TELEGRAM_API_ID='<api_hash>'`
    - `export TELEGRAM_BOT_TOKEN='<bot_token>'`

### Configuration for Get Member Services 

1. Start the scripts
    - `sudo cp service.conf /etc/supervisor/conf.d/get_members_for_amazon.conf`
    - `sudo cp service.conf /etc/supervisor/conf.d/get_members_for_udemy.conf`
    - `sudo cp service.conf /etc/supervisor/conf.d/get_members_for_crypto.conf`
    - `sudo supervisorctl reread`
    - `sudo supervisorctl reload`
    - `sudo supervisorctl start get_members_for_amazon`
    - `sudo supervisorctl start get_members_for_udemy`
    - `sudo supervisorctl start get_members_for_crypto`

You can now see its logs with `tail -f logs/<service-name>.log`. You can stop its services with `sudo supervisorctl stop all`

### Configuration for Send Message Services

1. Install and enable cron
    - `sudo apt install cron`
    - `sudo systemctl enable cron`

2. Edit crontab
    - `crontab -e`

3. Add to bottom line 
    - `30 * * * * /home/ubuntu/python_telegram_services/service.sh -f send_message_for_udemy.py`

4. Save and exit.

### Note

At the moment, the `requirements.txt` is not necessary. The project doesn't
use any packages outside of the Python standard library. Eventually, I plan
to show some more advanced features that will use packages from PyPI.