import requests as req

''' Test function to access api data and fetch them! '''
#print(dir())

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

url = 'https://api.nytimes.com/svc/topstories/v2/us.json?api-key=GaKSQ76kFF7NJv2tGexv0S1cGGGIawaO'

requestForApi = req.get(url)
#print(requestForApi.status_code)
result = []
for data in requestForApi.json()['results']:
    result.append({data['section'],data['item_type']})

print(result)