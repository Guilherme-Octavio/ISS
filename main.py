import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

# O Tutorial que me serviu como base:  https://youtu.be/5UWeOfdESZE?t=534

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url) # returna a api
result  = json.loads(response.read()) # carrega em json o valor 

with open("iss.txt", 'w') as file:
    # criando a txt e colocando o que vai dentro dele
    file.write(f"Temos {result['number']} astronautas no ISS agora: \n \n")

    people = result["people"]
    for i in people:
        file.write(f"{ i['name'] } - a bordo\n") # pega o nome das pessoas abordo 1 por 1
        
    #mostra longitude e latitude
    g = geocoder.ip('me')

    file.write(f"\n Sua localização autal Lat / Long é: {str(g.latlng)}") #escreve sua long e lat
    file.close() # fecha o arquivo. Não nesseçario pois estou utilizando o with mas por segurança coloquei
webbrowser.open("iss.txt") # abre o arquivo para nós

#preparando o Mapa mundi com turtle

screen = turtle.Screen()
screen.setup(1280, 720) # pode ser tambem 700:720
screen.setworldcoordinates(-180,-90,180,90)

# carrega a imagem mapa mundi
screen.bgpic("img/WorldMap.gif") # backgorund 
screen.register_shape("img/iss.gif") 
iss= turtle.Turtle()
iss.shape("img/iss.gif")
iss.setheading(45)
iss.penup()

while True:
    #mosta onde esta a Estação em tempo real
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    #pega a localização
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']
    
    lat = float(lat)
    lon = float(lon)
        
    print("\nlongitude: " + str(lon)) # transforma o valorem float depois em string 
    print("\nLatitude: " + str(lat))# mesma coisa
    
    #carregar a posição da iss
    iss.goto(lon, lat)
    
    # tempo para refresh
    time.sleep(1)