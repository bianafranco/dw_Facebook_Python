import urllib, json
from pprint import pprint

token = 'CAACEdEose0cBAIaoZAXK3kTZBCBW9ZAqyEfQw2HzY0eZArJdmFQeYU8xD0DcMiZBZByMZBuKiATrSZBznbsJzCoB8DlQrLIrGrSKF0SZAscXmiNyipa63pX3Irfo0E9Tg2RPgiQvB34wPSYECYjWnyUZAY5tQiWaj3NZAPAcjp77OeZBPjbPzyN7rksNmZCmGmUFZAgqWh8ZCgaIt2FKNVMU688IVtp'

idUser = '100000404613490'

url = 'https://graph.facebook.com/v2.3/' + idUser + '?access_token='+token

resp = urllib.urlopen(url).read()

dados = json.loads(resp.decode('utf-8'))

##pprint(dados)
print dados.keys()
