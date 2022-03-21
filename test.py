import requests

BASE = 'http://127.0.0.1:5000/'

# data = [{'likes': 13, 'name': 'How to Boil water', 'views': 1000000000},
#         {'likes': 17, 'name': 'Benzema Crazy Skills', 'views': 25000000},
#         {'likes': 820, 'name': 'Alien Sitings', 'views': 1000}]

# for i in range(len(data)):
#     response = requests.put(BASE + 'video/' + str(i), data[i])
#     print(response.json())

# input()
# response = requests.delete(BASE + 'video/0')
# print(response)

# input()
# for u in range(len(data)):
#     response = requests.get(BASE + 'video/' + str(u))
#     print(response.json())

response = requests.patch(BASE + 'video/2', {'views': 120000, 'likes': 101})
print(response.json())