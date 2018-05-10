import time
from datetime import datetime as dt
import os

#hosts_temp="hosts"
working_hours=[14,17] #24 hour clock
hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","gmail.com","www.gmail.com",www.reddit.com,reddit.com]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,working_hours[0]) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,working_hours[1]):
        print("working hours")
        with open(hosts_path,'r+') as file:
            content=file.read()
            #print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("go forth and prospoer")
    time.sleep(5)
