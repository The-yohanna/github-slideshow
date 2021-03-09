import requests
payload = {"name": str(input())}
r = requests.get("https://jsonmock.hackerrank.com/api/countries/search", params = payload)
r_dict = r.json()
p = int(input())
num = 0
for i in r_dict['data']:
    print(i)
    if i['population'] > p:
        num += 1
    else:
        pass
print('Number of countries with population greater than ',p, ' is ', num)

