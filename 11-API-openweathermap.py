from urllib import request
import json
ciudad="Ourense"
api_key = "2ad19185fe8377bb067932fc3ef66523"
unidades ="metric"
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&units=%s&appid=%s" % (ciudad, unidades, api_key)
print (url)
response = request.urlopen(url)
http_body = response.readline().decode('utf-8')
print (http_body)
#codificar la respuesta a json
data = json.loads(http_body)
#print(data)
#acceso al bloque main
main = data["main"]
#acceso a temperatura
temperatura = main["temp"]
#data = response.json()["main"]["temp"]
print ("La temperatura de " + ciudad + "es:" + str(temperatura))