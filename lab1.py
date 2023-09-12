import requests

# url = "http://www.google.com/"
# res = requests.get(url)
# print(res)

url = "https://raw.githubusercontent.com/mh575/cmput404_lab1/master/lab1.py"
res = requests.get(url)
print(res.text)

