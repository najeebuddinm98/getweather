# Get weather info using OpenWeather API

These scripts uses the **OpenWeather API** to get the current weather information for any city. The obtained data is in *JSON* format, so it is formatted into readable sentences. It then stores this formatted information in a file named ```weatherdata``` in a *pythonfiles folder* with the city name as well as a date and time stamp.

The API calling requires an authorization ID that can be obtained by signing up to the [OpenWeather API](https://home.openweathermap.org/users/sign_up) for free.

You can read more about the API [here](https://openweathermap.org/api).

## getweather.py

This script will ask the user for an input in the terminal window. The received information is stored on a text file called **weatherdata.txt**

## getweather_csv.py

This script will ask the user for an input in the terminal window. The received information is stored in a csv file called **weatherdata.csv**

## getweather_clip.py

This script will get the city name directly from the **clipboard**. The received information is stored on a text file called **weatherdata.txt**

Before running the script, download the ````pyperclip```` module using *pip*.

````
pip install pyperclip
````

You can read more about this module [here](https://pyperclip.readthedocs.io/en/latest/).

