
# PREYANSH RASTOGI 2017176

from urllib.request import *
import datetime


# function to get weather response
def weather_response(location, API_KEY):
        url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + location +'&APPID=' + API_KEY 
        a = urlopen(url)
        json = str(a.read())
        return json
        



# function to check for valid response 
def has_error(location,json):
        x = json.index('name')
        x = x + 7
        y = len(location)
        city_name = json[x:x+y]
    
        if city_name.lower() !=  location.lower():
                return True
        else :
                return False




# function to get attributes on nth day
def get_temperature (json, n= 0 ,t= '15:00:00' ):
        x = str(datetime.date.today() + datetime.timedelta(days = n)) + ' ' + t
        a = json.index(x)
        y = json.rfind('"temp"', 0 , a )
        z = float(json[y+7: y+13])
        return z

def get_humidity(json, n=0 ,t='15:00:00' ):
        x = str(datetime.date.today() + datetime.timedelta(days = n)) + ' ' + t
        a = json.index(x)
        y = json.rfind('humidity', 0 , a )
        z  = float(json[y+10: y+12])
        return z
	

def get_pressure(json, n=0, t='15:00:00'):
       x = str(datetime.date.today() + datetime.timedelta(days = n)) + ' ' + t
       a = json.index(x)
       y = json.rfind('pressure',0, a  )
       z  = float(json[y+10: y+15])
       return z
	

def get_wind(json, n=0, t='15:00:00'):
        x = str(datetime.date.today() + datetime.timedelta(days = n)) + ' ' + t
        a = json.index(x)
        y = json.rfind('speed',0, a )
        z  = float(json[y+7: y+11])
        return z
	

def get_sealevel(json, n=0, t='15:00:00'):
       x = str(datetime.date.today() + datetime.timedelta(days = n)) + ' ' + t
       a = json.index(x)
       y = json.rfind('sea_level',0, a  )
       z  = float(json[y + 11: y+17])
       return z


	

# application script
if __name__ == '__main__':
        API_KEY = '72b4c0cb2d3091a42ae00c19743381db'
        location = input('Enter city name')
        json = weather_response(location, API_KEY)
        if json != '{"cod":"404","message":"city not found"}':
                x = has_error(location, json)
                if  x == False :
                        n = int(input('Enter nth day'))
                        t = input('HH:MM:SS')
                        x = get_temperature(json, n, t)
                        print('Temperature is',x)
                        x = get_humidity(json,n ,t)
                        print('Humidity is',x)
                        x = get_pressure(json,n ,t)
                        print('Pressure is ',x)
                        x = get_wind(json,n, t)
                        print('Wind speed is ',x)
                        x = get_sealevel(json,n, t)
                        print('Sea level is ',x)
                else:
                        print('ERROR')

        else:
                print('ERROR')




























                        

