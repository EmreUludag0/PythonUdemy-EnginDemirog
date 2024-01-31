import json
data ='{"firstName": "Emre", "lastName": "Uludag"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])

customer = {
    "firstName": "Emre",
    "email": "emreuldg5@gmail.com"
    }

customerJson = json.dumps(customer)
print(customer)




