import json
file = open('H:\\pdfs\Certificates\Datascience EDYODA\Screenshots of class\Exams\Assignment 6\employee.json','r') #change the file path while running the code
data = file.read()
file.close()
user1 = json.loads(data) 
print(user1) 