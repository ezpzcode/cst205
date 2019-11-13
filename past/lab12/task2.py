import json
import urllib.request 
loca=""
url='http://api.openweathermap.org/data/2.5/weather?q=Monterey,US&appid=92562cc79201859c94e8638e881a00ef' 

with urllib.request.urlopen(url) as url: data = url.read() 
j = json.loads(data)

main = j["main"]
temp = main["temp"]
tmp = int(round(temp-273))
print(tmp) 

weather = j["weather"]
temp = weather[0]
main = temp["main"]
description = temp["description"]
print(main) 
print(description) 

sys = j['sys']
country= sys['country']
print(country) 

name = j['name']
print(name) 