import requests
from datetime import datetime

USERNAME = "yeombin"
TOKEN = "1f24w45gsd5hgsdfvv4se42f2hv"
GRAPH_ID = "graph1"

pixela_endpoint = " https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,  # 내가 생성하는 API Key
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
#     )


pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# response = requests.post(
#     url=pixel_creation_endpoint,
#     json=pixel_data,
#     headers=headers
#     )
# print(response.text)

pixel_update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

update_param = {
    "quantity": "8"
}

response = requests.put(
    url=pixel_update_endpoint,
    json=update_param,
    headers=headers
    )

print(response.text)
