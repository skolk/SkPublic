import time
from datetime import datetime as dt
import os


hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","gmail.com","www.gmail.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print(1)
        time.sleep(5)
