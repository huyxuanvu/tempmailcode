import re
import requests
import time
repone = requests.session()
request000 = repone.get("https://10minutemail.net/address.api.php?new=1")
get_mail = request000.json()["mail_get_mail"]
print(get_mail)
time.sleep(20)
count = 0
list = []
while True :  
    
    request000 = repone.get("https://10minutemail.net/address.api.php")   
 
    mail_list = request000.json()["mail_list"]
    for mail in mail_list :         
        if mail["from"] == '"Instagram" <no-reply@mail.instagram.com>' :
            sub = mail['subject']           
    if count == 30:
        break
    time.sleep(0.8)
    count += 1
    

print(sub)
regex  = re.findall(r'\d{1}',sub)
code = ""
for i in regex:
    code += str(i)
print(f'this is code :{code}')
time.sleep(200)

# [
# {'mail_id': 'xFJSJl',
#  'from': '"Instagram" <no-reply@mail.instagram.com>',
#   'to': 'hqr17954@xcoxc.com', 
#   'subject': '143057 is your Instagram code', 
#   'datetime': '2022-12-04 06:07:32',
#    'datetime2': 'just now', 'timeago': 30, 
#    'isread': '0'},
#     {'mail_id': 'welcome', 
#    'from': 'no-reply@10minutemail.net', 
#    'subject': 'Hi, Welcome to 10 Minute Mail', 
#    'datetime': '2022-12-04 06:07:10 UTC',
#     'datetime2': '52 seconds ago',
#      'timeago': 52, 
#      'isread': False}
# ]