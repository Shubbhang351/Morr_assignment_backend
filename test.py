import requests
from requests.auth import HTTPBasicAuth

BASE = "http://127.0.0.1:5000/"

data = [{"name" : "Shubhang", "email" : "shubh@gmail.com","phone" : 8273932426},
        {"name" : "hitesh", "email" : "hitesh@gmail.com","phone" : 8273832426},
        {"name" : "jai", "email" : "jai@gmail.com","phone" : 8273942426},
        {"name" : "Shubhang","email" : "shubh1@gmail.com","phone" : 8273932426},
        {"name" : "yash","email" : "yash@gmail.com","phone" : 9319607753},
        {"name" : "yash","email" : "yash1@gmail.com","phone" : 8273632426},
        {"name" : "yash","email" : "yash2@gmail.com","phone" : 8273632426},
        {"name" : "aman","email" : "aman@gmail.com","phone" : 8273632421},
        {"name" : "yash","email" : "yash3@gmail.com","phone" : 8273632426},
        {"name" : "yash","email" : "yash4@gmail.com","phone" : 8273632426},
        {"name" : "simran","email" : "simran@gmail.com","phone" : 7573632426},
        {"name" : "samer","email" : "samer@gmail.com","phone" : 7586632426},
        {"name" : "samer","email" : "samer1@gmail.com","phone" : 7586639426},
        {"name" : "ishank","email" : "ishank@gmail.com","phone" : 7586639426},
        {"name" : "ishank1","email" : "ishank1@gmail.com","phone" : 7586663426},
        {"name" : "pulkit","email" : "pulkit@gmail.com","phone" : 7586639426},
        {"name" : "pulkit","email" : "pulkit1@gmail.com","phone" : 7586639426},
        {"name" : "pulkit","email" : "pulkit2@gmail.com","phone" : 7586639426},
        {"name" : "somya","email" : "somya@gmail.com","phone" : 7586699426},
        {"name" : "rishi","email" : "rishi@gmail.com","phone" : 7586633326},
        {"name" : "kesar","email" : "kesar@gmail.com","phone" : 7776639426}]

username = "admin"
password = "SecretPwd"


print("ADD all data in data base")
for i in range(len(data)):
    response = requests.put(BASE + "/contact/",data = data[i],auth = HTTPBasicAuth(username, password))
    print(response.json())

print("\n")
print("GET request with name")
res = requests.get(BASE + "/contact/",auth = HTTPBasicAuth(username, password))
print(res.json())