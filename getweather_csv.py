#store the weather of the given city using OpenWeather API in a csv file

import json, requests, datetime, os, csv

def get_json_from_api(link):
    #DO: return JSON data by calling the API
    response=requests.get(link)
    response.raise_for_status()
    #DEBUG: print(response.text+'\n')
    data=json.loads(response.text)
    return data

def format_weather_data(data):
    #DO: return the json data in a clear and divided format
    name=data['name']
    ctime=str(datetime.datetime.now())
    lat=data['coord']['lat']
    lon=data['coord']['lon']
    desc=data['weather'][0]['description']
    tempCelsius=round(data['main']['temp']-273,2)
    temp=tempCelsius
    presAtm=round(data['main']['pressure']/1000, 2)
    pres=presAtm
    hum=data['main']['humidity']
    wind=data['wind']['speed']
    total=[name,ctime,lat,lon,desc,temp,pres,hum,wind]
    #DEBUG: print(total)
    return total


if __name__=="__main__":

    #DO: get user input and retrieve data from the API accordingly
    userLoc=input('Enter the city name: \n')
    location=userLoc.lower().replace(' ','+') #convert the entered location into url-ready form

    # UPDATE below (get your id by signing up to OpenWeatherAPI
    apiId='<Enter_your_API_ID_here>' #IMP: edit this before runnning
    # UPDATE above

    url='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' %(location, apiId)

    jsonData=get_json_from_api(url)
    formattedData=format_weather_data(jsonData)

    #DO: store in a csv file
    currentDir=os.getcwd()
    mainDir=currentDir+'\\pythonfiles'
    if not os.path.exists(mainDir): #checking if folder already exists
        os.mkdir(mainDir)

    filePath=mainDir+'\\weatherdata.csv'
    fileExists=os.path.isfile(filePath)
    headers=['City','Date','Latitude','Longitude','Description','Temperature','Pressure','Humidity','Wind speed']

    file=open(filePath,'a') #append mode so that previous data isnt overwritten
    writeObj=csv.DictWriter(file, fieldnames=headers) #our csv writer object

    if not fileExists:
        writeObj.writeheader() #write header if a new csv file is created

    writeObj.writerow({
        'City':formattedData[0],
        'Date':formattedData[1],
        'Latitude':formattedData[2],
        'Longitude':formattedData[3],
        'Description':formattedData[4],
        'Temperature':formattedData[5],
        'Pressure':formattedData[6],
        'Humidity':formattedData[7],
        'Wind speed':formattedData[8]
        }) #send the appropriate data to the respective columns

    file.close()
    
    print('The file weatherdata.csv has been updated in the pythonfiles directory in the path '+currentDir)
    os.system('cmd /k "pause"')

