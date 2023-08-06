import folium
from geopy import Nominatim
import os

while True:
    mest = input("Write your city(For example: Moscow, Russia): ")

    nominaltim = Nominatim(user_agent="user")

    location = nominaltim.geocode(mest).raw

    a = []
    for i in location.values():
        a.append(i)
    shir = a[5]
    dolg = a[6]

    m = folium.Map(location=[shir, dolg], zoom_start=8)

    folium.Marker([shir, dolg], popup=mest, tooltip=mest).add_to(m)

    m.save("Map.html")

    dt = ""
    ft = ""

    if float(shir) > 0:
        dt = f"{shir} с.ш."
    else:
        dt = f"{shir} ю.ш."

    if float(dolg) > 0:
        ft = f"{dolg} в.д."
    else:
        ft = f"{dolg} з.д."

    print(dt, ft)

    os.system("Map.html")
a = input()
