#print the weather of the city from clipboard using OpenWeather API

import json, requests, datetime, os, pyperclip

def get_json_from_api(link):
    #DO: return JSON data by calling the API
    response=requests.get(link)
    response.raise_for_status()
    #DEBUG: print(response.text+'\n')
    data=json.loads(response.text)
    return data

def format_weather_data(data):
    #DO: return the json data in a paragraphed and clear format
    timeStamp=str(datetime.datetime.now())
    lat=str(data['coord']['lat'])
    lon=str(data['coord']['lon'])
    coor='Coordinates of '+data['name']+': '+'lat='+lat+' '+'lon='+lon
    desc='Weather description: '+data['weather'][0]['description']
    tempCelsius=round(data['main']['temp']-273,2)
    temp='Temperature in Celsius: '+str(tempCelsius)+' degrees'
    presAtm=round(data['main']['pressure']/1000, 2)
    pres='Air pressure: '+str(presAtm)+' atm'
    hum='Humidity: '+str(data['main']['humidity'])+'%'
    wind='Wind speed: '+str(data['wind']['speed'])+' m/s'
    name='\n'+data['name']+' weather at '+timeStamp
    total='\n'.join([name,coor,desc,temp,pres,hum,wind])
    #DEBUG: print(totalData)
    return total
    
if __name__=="__main__":
    try:
        userLoc=pyperclip.paste()
        location=userLoc.lower().replace(' ','+') #convert the entered location into url-ready form
        
        # UPDATE below (get your id by signing up to OpenWeatherAPI
        apiId='<Enter_your_API_ID_here>' #IMP: edit this before runnning
        # UPDATE above
        
        url='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' %(location, apiId)
        
        jsonData=get_json_from_api(url)
        formattedData=format_weather_data(jsonData)
        
        #DO: store in a text file

        currentDir=os.getcwd()
        mainDir=currentDir+'\\pythonfiles'
        if not os.path.exists(mainDir): #checking if folder already exists
            os.mkdir(mainDir)
        
        filePath=mainDir+'\\weatherdata.txt'
        file=open(filePath,'a') #append mode so that previous data isnt overwritten
        file.write('\n')
        file.write(formattedData)
        file.close()
        print('The file weatherdata.txt has been updated in the pythonfiles directory in the path '+currentDir)

    except ModuleNotFoundError:
        print("You haven't downloaded the pyperclip module. Try again after downloading.")

    finally:
        os.system('cmd /k "pause"')

