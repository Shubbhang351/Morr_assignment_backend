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
        {"name" : "yash","email" : "yash4@gmail.com","phone" : 8273632426}]

username = "admin"
password = "SecretPwd"

#put request
print("PUT request without auth")
response = requests.put(BASE + "/contact/",data = data[0])
print(response.json())

print("\n")
print("PUT request with auth")
response = requests.put(BASE + "/contact/",data = data[0],auth = HTTPBasicAuth(username, password))
print(response.json())

print("\n")
print("ADD all data in data base")
for i in range(len(data)):
    response = requests.put(BASE + "/contact/",data = data[i],auth = HTTPBasicAuth(username, password))
    print(response.json())


print("\n")
#GET Request
print("GET request without auth")
response = requests.get(BASE + "/contact/?email=" + data[0]['email'])
print(response.json())

print("\n")
print("GET request with auth")
#only email
res = requests.get(BASE + "/contact/?email=" + data[0]['email'],auth = HTTPBasicAuth(username, password))
print(res.json())

print("\n")
print("GET request with both name and emial")
res = requests.get(BASE + "/contact/?email=" + data[0]['email'] +"&name=" + data[0]['name'],auth = HTTPBasicAuth(username, password))
print(res.json())


print("\n")
print("GET request with name")
res = requests.get(BASE + "/contact/?name=" + data[0]['name'],auth = HTTPBasicAuth(username, password))
print(res.json())


print("\n")
print("GET request with wrong auth")
res = requests.get(BASE + "/contact/?name=" + data[0]['name'],auth = HTTPBasicAuth('admin1', password))
print(res.json())

print("\n")
print("UPDATE request without auth")
response = requests.patch(BASE + "/contact/" + "jai@gmail.com",{"name" : "jai sharma"})
print(response.json())


print("\n")
print("UPDATE request with auth")
response = requests.patch(BASE + "/contact/" + "jai@gmail.com",{"name" : "jai sharma"},auth = HTTPBasicAuth(username, password))
print(response.json())

print("check for changes")
res = requests.get(BASE + "/contact/?email=" + "jai@gmail.com",auth = HTTPBasicAuth(username, password))
print(res.json())

print("\n")
print("DELETE request without auth")
response = requests.delete(BASE + "/contact/jai@gmail.com")
print(response.json())

print("\n")
print("DELETE requset with auth")
response = requests.delete(BASE + "/contact/jai@gmail.com",auth = HTTPBasicAuth(username, password))
print(response.json())

print("check contact deleted or not")
res = requests.get(BASE + "/contact/?email=" + "jai@gmail.com",auth = HTTPBasicAuth(username, password))
print(res.json())