import requests

base_url = "http://localhost:8080"

url = base_url + "/menu"

payload = {
    "name": "Juice",
    "amount": 100
}
headers = {"content-type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

payload = {
    "name": "Rice",
    "amount": 100
}
headers = {"content-type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

menu = response.json()


url = base_url+"/create/customer"

payload = {
    "name": "moon",
    "phone_no": "1234567890"
}
headers = {"content-type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

cust_id = response.json().get('id')

print(response.json())  


url = base_url + f"/customer/{cust_id}/create/order"

payload = { f"{menu[0].get("dish_id")}": 2 }
headers = {"content-type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

res = response.json()



url = base_url + f"/customer/{cust_id}/order/{res.get('orders')[0]}"

response = requests.get(url)

print(response.json())