import json
Indian_States = {
        "Hyderabad":"Telangana",
        "Amaravathi":"Andhra Pradesh",
        "Chennai":"Tamilnadu",
        "Jaipur":"Rajasthan",
        "New Delhi":"Delhi",
        "Mumbai":"Maharastra",
        "Bangalore":"Karnataka"}

#with open("Indian_States.json","w") as outfile:
#json.dump(Indian_States,outfile, indent=1)
#print("JSON got Appended :\n",Indian_States)
                  ##OR##
data= json.dumps(Indian_States)
file = open('indian_States.json','w')
file.write(data)
file.close()