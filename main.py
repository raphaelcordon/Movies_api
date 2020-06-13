

'''
import requests
data = requests.get(f'http://www.omdbapi.com/?s=star+wars&apikey=c60ebd9f')
data = data.json()
#print(data)

for d in range(0, len(data['Search'])):
    print(data['Search'][d])

+++++++


result = []
for d in range(0, len(data['Search'])):
    result.append(data['Search'][d])


for d in result:
    print(d['Title'], d['Year'])



'''