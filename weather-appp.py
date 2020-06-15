import tkinter as tk

import requests

HEIGHT = 500
WIDTH = 600


# 0a2102fd9a5f5d7f417c73a08b40c441
# pro.openweathermap.org/data/2.5/forecast/
# name, temp_c, condition, humidity, feelslike_c,

def get_weather(city):
    weather_key = '9f56fc31c7bb456d82b125045201306'
    url = 'http://api.weatherapi.com/v1/current.json'
    params = {'key': weather_key,'q': city}
    response = requests.get(url,params = params)
    print(response.json())
    weather = response.json()

    label['text'] = format_response(weather)


def format_response(weather):
    try:
        name = weather['location']['name']
        temp = weather['current']['temp_c']
        feels = weather['current']['feelslike_c']
        desc = weather['current']['condition']['text']
        humidity = weather['current']['humidity']
        final_str = 'City: %s \nConditions: %s \nTemperature(°C): %s \nFeels like: %s \nHumidty: %s \n' % (
            name,desc,temp,feels,humidity)

    except:
        final_str = 'There was a problem retrieving that information.'

    return final_str


root = tk.Tk()

canvas = tk.Canvas(root,height = HEIGHT,width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file = 'landscape.png')
background_label = tk.Label(root,image = background_image)
background_label.place(x = 0,y = 0,relwidth = 1,relheight = 1)

frame = tk.Frame(root,bg = "#1ac6ff",bd = 5)
frame.place(relx = 0.5,rely = 0.1,relheight = 0.1,relwidth = 0.75,anchor = 'n')

entry = tk.Entry(frame,bg = "white",font = 40)
entry.place(relwidth = 0.65,relheight = 1)

button = tk.Button(frame,text = "Get Weather",bg = "#b3ffd9",
                   activebackground = "#4dd5ff",
                   command = lambda: get_weather(entry.get()),font = 40)
button.place(relx = 0.70,rely = 0.05,relwidth = 0.3,relheight = 1)

lower_frame = tk.Frame(root,bg = "#1ac6ff",bd = 10)
lower_frame.place(relx = 0.5,rely = 0.25,relheight = 0.6,relwidth = 0.75,anchor = 'n')

label = tk.Label(lower_frame,bg = "white",font = ('Calibri Light',18),anchor = 'nw',justify = 'left')
label.place(relheight = 1,relwidth = 1)

weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
