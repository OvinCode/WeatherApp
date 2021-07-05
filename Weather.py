from tkinter import *
# from PIL import ImageTK,Image
import requests
import json

root = Tk()
root.title('Ovin WeatherMap')
root.iconbitmap('C:/WeatherApp/Ovin.ico')
root.geometry("550x50")
#
def cityLookup():

    city.get()
    cityLabel = Label(root, text=city.get())
    cityLabel.grid(row=1, column=0, columnspan=2)
    try:
        api_requests = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + city.get() +"&appid=fbe750623016a38c58911bb32d39a7e9")
        api = json.loads(api_requests.content)
        place = api["name"]
        temp = api["main"]['temp']
        temp = round((temp - 273),2)
        temp_min = api["main"]['temp_min']
        temp_min = round((temp_min - 273),2)
        temp_max = api["main"]['temp_max']
        temp_max = round((temp_max - 273),2)
        humidity = api["main"]['humidity']

        myLabel = Label(root, text=str(place) + " -->  "
                                   + "Current Temp : " + str(temp) + " °C     "
                                   + "Min Temp : " + str(temp_min) + " °C     "
                                   + "Max Temp : " + str(temp_max) + " °C     "
                                   + "Humidity : " + str(humidity) + " % ")
        myLabel.grid(row=1,column =0,columnspan =2)

    except Exception as e:
        api = "Error..."

city = Entry(root)
city.grid(row=0, column=0,stick=W+E+N+S)
#
cityButton = Button(root, text="Search City", command=cityLookup)
cityButton.grid(row=0, column=1,stick=W+E+N+S)


root.mainloop()