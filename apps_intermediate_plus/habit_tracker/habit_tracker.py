
# https://pixe.la/
# https://docs.pixe.la/
# https://pixe.la/@forestfires

import datetime
import requests

USERNAME = "forestfires"
TOKEN = ""  # Add token from pixe.la to run this code again.
GRAPHID = "graph2"

today = datetime.datetime.now()
yesterday = datetime.datetime(year=2022, month=3, day=10).strftime("%Y%m%d")

pixela_endpoint_create_user = "https://pixe.la/v1/users"
pixela_endpoint_create_graph = f"https://pixe.la/v1/users/{USERNAME}/graphs"
pixela_endpoint_post_pixel = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}"
pixela_endpoint_put = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{yesterday}"

headers = {
    "X-USER-TOKEN": TOKEN
}


# CREATE USER
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint_create_user, json=user_params)
# print(response.text)


# CREATE GRAPH
# graph_config = {
#     "id": "graph2",
#     "name": "runninggraph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai",
# }
# response = requests.post(url=pixela_endpoint_create_graph, json=graph_config, headers=headers)
# print(response.text)
# This created:
# https://pixe.la/v1/users/forestfires/graphs/graph2.html


# POST PIXEL
# post_pixel_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "7",
# }
# response = requests.post(url=pixela_endpoint_post_pixel, json=post_pixel_config, headers=headers)
# print(response.text)


# PUT PIXEL
# put_pixel_config = {
#     "quantity": "8",
# }
# response = requests.put(url=pixela_endpoint_put, json=put_pixel_config, headers=headers)
# print(response.text)

# DELETE PIXEL
response = requests.delete(url=pixela_endpoint_put, headers=headers)
print(response.text)
