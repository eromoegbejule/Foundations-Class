{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# WeatherAPI (Weather)\n",
    "\n",
    "Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.\n",
    "\n",
    "Be sure to take advantage of both the documentation and the API Explorer!\n",
    "\n",
    "## 0) Import any libraries you might need\n",
    "\n",
    "- *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*\n",
    "- *Tip: Remember you only need to import requests once!*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).\n",
    "\n",
    "- *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*\n",
    "- *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*\n",
    "- *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*\n",
    "- *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* \n",
    "- *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"http://api.weatherapi.com/v1/current.json?key=ea62b294238944a09bd05542200411&q=Lagos\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get('http://api.weatherapi.com/v1/current.json?key=ea62b294238944a09bd05542200411&q=Lagos')\n",
    "data = response.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'location': {'name': 'Lagos', 'region': 'Lagos', 'country': 'Nigeria', 'lat': 6.45, 'lon': 3.4, 'tz_id': 'Africa/Lagos', 'localtime_epoch': 1604887756, 'localtime': '2020-11-09 3:09'}, 'current': {'last_updated_epoch': 1604886313, 'last_updated': '2020-11-09 02:45', 'temp_c': 25.0, 'temp_f': 77.0, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 4.3, 'wind_kph': 6.8, 'wind_degree': 160, 'wind_dir': 'SSE', 'pressure_mb': 1014.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 94, 'cloud': 25, 'feelslike_c': 26.9, 'feelslike_f': 80.5, 'vis_km': 10.0, 'vis_miles': 6.0, 'uv': 1.0, 'gust_mph': 10.3, 'gust_kph': 16.6}}\n"
     ]
    }
   ],
   "source": [
    "print (data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2) What's the current wind speed? How much warmer does it feel than it actually is?\n",
    "\n",
    "- *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*\n",
    "- *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['location', 'current'])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'last_updated_epoch': 1604886313,\n",
       " 'last_updated': '2020-11-09 02:45',\n",
       " 'temp_c': 25.0,\n",
       " 'temp_f': 77.0,\n",
       " 'is_day': 0,\n",
       " 'condition': {'text': 'Partly cloudy',\n",
       "  'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png',\n",
       "  'code': 1003},\n",
       " 'wind_mph': 4.3,\n",
       " 'wind_kph': 6.8,\n",
       " 'wind_degree': 160,\n",
       " 'wind_dir': 'SSE',\n",
       " 'pressure_mb': 1014.0,\n",
       " 'pressure_in': 30.4,\n",
       " 'precip_mm': 0.0,\n",
       " 'precip_in': 0.0,\n",
       " 'humidity': 94,\n",
       " 'cloud': 25,\n",
       " 'feelslike_c': 26.9,\n",
       " 'feelslike_f': 80.5,\n",
       " 'vis_km': 10.0,\n",
       " 'vis_miles': 6.0,\n",
       " 'uv': 1.0,\n",
       " 'gust_mph': 10.3,\n",
       " 'gust_kph': 16.6}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['current']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-7-f4d9b200a568>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-7-f4d9b200a568>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    print(\"The wind speed is,\" wind-mph \"but it feels warmer by:\" humidity)\u001b[0m\n\u001b[0m                               ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "print(\"The wind speed is,\" wind-mph \"but it feels warmer by:\" humidity)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Difference in warmth"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# UNFINISHEDDD"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible on next Thursday?\n",
    "\n",
    "- *Tip: Check the documentation!*\n",
    "- *Tip: If you aren't sure what something means, ask in Slack*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Endpoint for today is below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"http://api.weatherapi.com/v1/astronomy.json?key=ea62b294238944a09bd05542200411&q=Lagos&dt=2020-11-07\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "astronomy = requests.get('http://api.weatherapi.com/v1/astronomy.json?key=ea62b294238944a09bd05542200411&q=Lagos&dt=2020-11-07')\n",
    "data = astronomy.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(astronomy.json())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Endpoint for next Thursday, November 9 (since we have no money to pay for license for November 12) is below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"http://api.weatherapi.com/v1/astronomy.json?key=ea62b294238944a09bd05542200411&q=Lagos&dt=2020-11-09\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "moon_illumination = requests.get('http://api.weatherapi.com/v1/astronomy.json?key=ea62b294238944a09bd05542200411&q=Lagos&dt=2020-11-09')\n",
    "free_limit = moon_illumination.json()\n",
    "print(moon_illumination.json())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4) What's the difference between the high and low temperatures for today?\n",
    "\n",
    "- *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Pulling data from Forecast\n",
    "url = \"http://api.weatherapi.com/v1/forecast.json?key=ea62b294238944a09bd05542200411&q=Lagos&days=1\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Present difference between both sets of temperatures\n",
    "temp_diff = requests.get('http://api.weatherapi.com/v1/forecast.json?key=ea62b294238944a09bd05542200411&q=Lagos&days=1')\n",
    "temp = temp_diff.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(temp_diff.json())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "temp.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "temp['forecast']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# UNFINISHED"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## 4.5) How can you avoid the \"oh no I don't have the data any more because I made another request\" problem in the future?\n",
    "\n",
    "What variable(s) do you have to rename, and what would you rename them?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rename data variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Data = Temp"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5) Go through the daily forecasts, printing out the next week's worth of predictions.\n",
    "\n",
    "I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).\n",
    "\n",
    "- *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"http://api.weatherapi.com/v1/forecast.json?key=ea62b294238944a09bd05542200411&q=Lagos&days=7\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'date': '2020-11-09', 'date_epoch': 1604880000, 'day': {'maxtemp_c': 32.8, 'maxtemp_f': 91.0, 'mintemp_c': 26.6, 'mintemp_f': 79.9, 'avgtemp_c': 29.0, 'avgtemp_f': 84.2, 'maxwind_mph': 10.5, 'maxwind_kph': 16.9, 'totalprecip_mm': 1.1, 'totalprecip_in': 0.04, 'avgvis_km': 9.9, 'avgvis_miles': 6.0, 'avghumidity': 70.0, 'daily_will_it_rain': 1, 'daily_chance_of_rain': '75', 'daily_will_it_snow': 0, 'daily_chance_of_snow': '0', 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'uv': 10.0}, 'astro': {'sunrise': '06:35 AM', 'sunset': '06:26 PM', 'moonrise': '01:09 AM', 'moonset': '01:51 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': '34'}, 'hour': [{'time_epoch': 1604876400, 'time': '2020-11-09 00:00', 'temp_c': 27.9, 'temp_f': 82.2, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 7.6, 'wind_kph': 12.2, 'wind_degree': 206, 'wind_dir': 'SSW', 'pressure_mb': 1013.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 77, 'cloud': 24, 'feelslike_c': 31.7, 'feelslike_f': 89.1, 'windchill_c': 27.9, 'windchill_f': 82.2, 'heatindex_c': 31.7, 'heatindex_f': 89.1, 'dewpoint_c': 23.4, 'dewpoint_f': 74.1, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 10.3, 'gust_kph': 16.6}, {'time_epoch': 1604880000, 'time': '2020-11-09 01:00', 'temp_c': 27.7, 'temp_f': 81.9, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 7.2, 'wind_kph': 11.5, 'wind_degree': 211, 'wind_dir': 'SSW', 'pressure_mb': 1013.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 79, 'cloud': 23, 'feelslike_c': 31.5, 'feelslike_f': 88.7, 'windchill_c': 27.7, 'windchill_f': 81.9, 'heatindex_c': 31.5, 'heatindex_f': 88.7, 'dewpoint_c': 23.6, 'dewpoint_f': 74.5, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 9.6, 'gust_kph': 15.5}, {'time_epoch': 1604883600, 'time': '2020-11-09 02:00', 'temp_c': 27.5, 'temp_f': 81.5, 'is_day': 0, 'condition': {'text': 'Patchy light rain with thunder', 'icon': '//cdn.weatherapi.com/weather/64x64/night/386.png', 'code': 1273}, 'wind_mph': 6.0, 'wind_kph': 9.7, 'wind_degree': 231, 'wind_dir': 'SW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.2, 'precip_in': 0.01, 'humidity': 79, 'cloud': 44, 'feelslike_c': 31.3, 'feelslike_f': 88.3, 'windchill_c': 27.5, 'windchill_f': 81.5, 'heatindex_c': 31.3, 'heatindex_f': 88.3, 'dewpoint_c': 23.6, 'dewpoint_f': 74.5, 'will_it_rain': 0, 'chance_of_rain': '22', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 8.3, 'gust_kph': 13.3}, {'time_epoch': 1604887200, 'time': '2020-11-09 03:00', 'temp_c': 27.4, 'temp_f': 81.3, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 5.1, 'wind_kph': 8.3, 'wind_degree': 251, 'wind_dir': 'WSW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.3, 'precip_in': 0.01, 'humidity': 80, 'cloud': 65, 'feelslike_c': 31.0, 'feelslike_f': 87.8, 'windchill_c': 27.4, 'windchill_f': 81.3, 'heatindex_c': 31.0, 'heatindex_f': 87.8, 'dewpoint_c': 23.7, 'dewpoint_f': 74.7, 'will_it_rain': 0, 'chance_of_rain': '43', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 6.7, 'gust_kph': 10.8}, {'time_epoch': 1604890800, 'time': '2020-11-09 04:00', 'temp_c': 27.2, 'temp_f': 81.0, 'is_day': 0, 'condition': {'text': 'Patchy light rain with thunder', 'icon': '//cdn.weatherapi.com/weather/64x64/night/386.png', 'code': 1273}, 'wind_mph': 4.0, 'wind_kph': 6.5, 'wind_degree': 271, 'wind_dir': 'W', 'pressure_mb': 1012.0, 'pressure_in': 30.3, 'precip_mm': 0.5, 'precip_in': 0.02, 'humidity': 81, 'cloud': 86, 'feelslike_c': 30.8, 'feelslike_f': 87.4, 'windchill_c': 27.2, 'windchill_f': 81.0, 'heatindex_c': 30.8, 'heatindex_f': 87.4, 'dewpoint_c': 23.7, 'dewpoint_f': 74.7, 'will_it_rain': 0, 'chance_of_rain': '65', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 5.4, 'gust_kph': 8.6}, {'time_epoch': 1604894400, 'time': '2020-11-09 05:00', 'temp_c': 27.0, 'temp_f': 80.6, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 4.0, 'wind_kph': 6.5, 'wind_degree': 284, 'wind_dir': 'WNW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.5, 'precip_in': 0.02, 'humidity': 82, 'cloud': 81, 'feelslike_c': 30.5, 'feelslike_f': 86.9, 'windchill_c': 27.0, 'windchill_f': 80.6, 'heatindex_c': 30.5, 'heatindex_f': 86.9, 'dewpoint_c': 23.6, 'dewpoint_f': 74.5, 'will_it_rain': 0, 'chance_of_rain': '68', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.7, 'vis_miles': 6.0, 'gust_mph': 5.1, 'gust_kph': 8.3}, {'time_epoch': 1604898000, 'time': '2020-11-09 06:00', 'temp_c': 26.8, 'temp_f': 80.2, 'is_day': 0, 'condition': {'text': 'Patchy light rain with thunder', 'icon': '//cdn.weatherapi.com/weather/64x64/night/386.png', 'code': 1273}, 'wind_mph': 3.8, 'wind_kph': 6.1, 'wind_degree': 297, 'wind_dir': 'WNW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.6, 'precip_in': 0.02, 'humidity': 82, 'cloud': 77, 'feelslike_c': 30.2, 'feelslike_f': 86.4, 'windchill_c': 26.8, 'windchill_f': 80.2, 'heatindex_c': 30.2, 'heatindex_f': 86.4, 'dewpoint_c': 23.5, 'dewpoint_f': 74.3, 'will_it_rain': 1, 'chance_of_rain': '72', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.3, 'vis_miles': 5.0, 'gust_mph': 5.1, 'gust_kph': 8.3}, {'time_epoch': 1604901600, 'time': '2020-11-09 07:00', 'temp_c': 26.6, 'temp_f': 79.9, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 3.8, 'wind_kph': 6.1, 'wind_degree': 309, 'wind_dir': 'NW', 'pressure_mb': 1013.0, 'pressure_in': 30.4, 'precip_mm': 0.6, 'precip_in': 0.02, 'humidity': 83, 'cloud': 72, 'feelslike_c': 29.9, 'feelslike_f': 85.8, 'windchill_c': 26.6, 'windchill_f': 79.9, 'heatindex_c': 29.9, 'heatindex_f': 85.8, 'dewpoint_c': 23.4, 'dewpoint_f': 74.1, 'will_it_rain': 1, 'chance_of_rain': '75', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 4.9, 'gust_kph': 7.9}, {'time_epoch': 1604905200, 'time': '2020-11-09 08:00', 'temp_c': 27.9, 'temp_f': 82.2, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 3.8, 'wind_kph': 6.1, 'wind_degree': 287, 'wind_dir': 'WNW', 'pressure_mb': 1013.0, 'pressure_in': 30.4, 'precip_mm': 0.4, 'precip_in': 0.02, 'humidity': 76, 'cloud': 59, 'feelslike_c': 31.3, 'feelslike_f': 88.3, 'windchill_c': 27.9, 'windchill_f': 82.2, 'heatindex_c': 31.3, 'heatindex_f': 88.3, 'dewpoint_c': 22.9, 'dewpoint_f': 73.2, 'will_it_rain': 0, 'chance_of_rain': '50', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.3, 'vis_miles': 5.0, 'gust_mph': 4.7, 'gust_kph': 7.6}, {'time_epoch': 1604908800, 'time': '2020-11-09 09:00', 'temp_c': 29.1, 'temp_f': 84.4, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 3.8, 'wind_kph': 6.1, 'wind_degree': 265, 'wind_dir': 'W', 'pressure_mb': 1014.0, 'pressure_in': 30.4, 'precip_mm': 0.2, 'precip_in': 0.01, 'humidity': 68, 'cloud': 45, 'feelslike_c': 32.6, 'feelslike_f': 90.7, 'windchill_c': 29.1, 'windchill_f': 84.4, 'heatindex_c': 32.6, 'heatindex_f': 90.7, 'dewpoint_c': 22.5, 'dewpoint_f': 72.5, 'will_it_rain': 0, 'chance_of_rain': '25', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.7, 'vis_miles': 6.0, 'gust_mph': 4.7, 'gust_kph': 7.6}, {'time_epoch': 1604912400, 'time': '2020-11-09 10:00', 'temp_c': 30.4, 'temp_f': 86.7, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 3.8, 'wind_kph': 6.1, 'wind_degree': 243, 'wind_dir': 'WSW', 'pressure_mb': 1014.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 61, 'cloud': 32, 'feelslike_c': 34.0, 'feelslike_f': 93.2, 'windchill_c': 30.4, 'windchill_f': 86.7, 'heatindex_c': 34.0, 'heatindex_f': 93.2, 'dewpoint_c': 22.0, 'dewpoint_f': 71.6, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 4.5, 'gust_kph': 7.2}, {'time_epoch': 1604916000, 'time': '2020-11-09 11:00', 'temp_c': 31.2, 'temp_f': 88.2, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 4.9, 'wind_kph': 7.9, 'wind_degree': 223, 'wind_dir': 'SW', 'pressure_mb': 1013.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 58, 'cloud': 28, 'feelslike_c': 35.0, 'feelslike_f': 95.0, 'windchill_c': 31.2, 'windchill_f': 88.2, 'heatindex_c': 35.0, 'heatindex_f': 95.0, 'dewpoint_c': 21.9, 'dewpoint_f': 71.4, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 5.8, 'gust_kph': 9.4}, {'time_epoch': 1604919600, 'time': '2020-11-09 12:00', 'temp_c': 32.0, 'temp_f': 89.6, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 6.0, 'wind_kph': 9.7, 'wind_degree': 204, 'wind_dir': 'SSW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 55, 'cloud': 24, 'feelslike_c': 35.9, 'feelslike_f': 96.6, 'windchill_c': 32.0, 'windchill_f': 89.6, 'heatindex_c': 35.9, 'heatindex_f': 96.6, 'dewpoint_c': 21.7, 'dewpoint_f': 71.1, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 6.9, 'gust_kph': 11.2}, {'time_epoch': 1604923200, 'time': '2020-11-09 13:00', 'temp_c': 32.8, 'temp_f': 91.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 7.2, 'wind_kph': 11.5, 'wind_degree': 185, 'wind_dir': 'S', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 52, 'cloud': 19, 'feelslike_c': 36.9, 'feelslike_f': 98.4, 'windchill_c': 32.8, 'windchill_f': 91.0, 'heatindex_c': 36.9, 'heatindex_f': 98.4, 'dewpoint_c': 21.6, 'dewpoint_f': 70.9, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 8.3, 'gust_kph': 13.3}, {'time_epoch': 1604926800, 'time': '2020-11-09 14:00', 'temp_c': 32.2, 'temp_f': 90.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 8.3, 'wind_kph': 13.3, 'wind_degree': 191, 'wind_dir': 'SSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 54, 'cloud': 17, 'feelslike_c': 36.2, 'feelslike_f': 97.2, 'windchill_c': 32.2, 'windchill_f': 90.0, 'heatindex_c': 36.2, 'heatindex_f': 97.2, 'dewpoint_c': 21.6, 'dewpoint_f': 70.9, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 9.6, 'gust_kph': 15.5}, {'time_epoch': 1604930400, 'time': '2020-11-09 15:00', 'temp_c': 31.7, 'temp_f': 89.1, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 9.4, 'wind_kph': 15.1, 'wind_degree': 197, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 56, 'cloud': 14, 'feelslike_c': 35.4, 'feelslike_f': 95.7, 'windchill_c': 31.7, 'windchill_f': 89.1, 'heatindex_c': 35.4, 'heatindex_f': 95.7, 'dewpoint_c': 21.7, 'dewpoint_f': 71.1, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 10.7, 'gust_kph': 17.3}, {'time_epoch': 1604934000, 'time': '2020-11-09 16:00', 'temp_c': 31.1, 'temp_f': 88.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 10.5, 'wind_kph': 16.9, 'wind_degree': 203, 'wind_dir': 'SSW', 'pressure_mb': 1009.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 58, 'cloud': 11, 'feelslike_c': 34.7, 'feelslike_f': 94.5, 'windchill_c': 31.1, 'windchill_f': 88.0, 'heatindex_c': 34.7, 'heatindex_f': 94.5, 'dewpoint_c': 21.7, 'dewpoint_f': 71.1, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 12.1, 'gust_kph': 19.4}, {'time_epoch': 1604937600, 'time': '2020-11-09 17:00', 'temp_c': 30.2, 'temp_f': 86.4, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 10.5, 'wind_kph': 16.9, 'wind_degree': 203, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 62, 'cloud': 11, 'feelslike_c': 33.8, 'feelslike_f': 92.8, 'windchill_c': 30.2, 'windchill_f': 86.4, 'heatindex_c': 33.8, 'heatindex_f': 92.8, 'dewpoint_c': 22.0, 'dewpoint_f': 71.6, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 12.5, 'gust_kph': 20.2}, {'time_epoch': 1604941200, 'time': '2020-11-09 18:00', 'temp_c': 29.4, 'temp_f': 84.9, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 10.5, 'wind_kph': 16.9, 'wind_degree': 203, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 66, 'cloud': 10, 'feelslike_c': 32.8, 'feelslike_f': 91.0, 'windchill_c': 29.4, 'windchill_f': 84.9, 'heatindex_c': 32.8, 'heatindex_f': 91.0, 'dewpoint_c': 22.4, 'dewpoint_f': 72.3, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 13.0, 'gust_kph': 20.9}, {'time_epoch': 1604944800, 'time': '2020-11-09 19:00', 'temp_c': 28.5, 'temp_f': 83.3, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 10.5, 'wind_kph': 16.9, 'wind_degree': 204, 'wind_dir': 'SSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 71, 'cloud': 10, 'feelslike_c': 31.9, 'feelslike_f': 89.4, 'windchill_c': 28.5, 'windchill_f': 83.3, 'heatindex_c': 31.9, 'heatindex_f': 89.4, 'dewpoint_c': 22.7, 'dewpoint_f': 72.9, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 13.4, 'gust_kph': 21.6}, {'time_epoch': 1604948400, 'time': '2020-11-09 20:00', 'temp_c': 28.2, 'temp_f': 82.8, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 10.3, 'wind_kph': 16.6, 'wind_degree': 207, 'wind_dir': 'SSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 73, 'cloud': 10, 'feelslike_c': 31.6, 'feelslike_f': 88.9, 'windchill_c': 28.2, 'windchill_f': 82.8, 'heatindex_c': 31.6, 'heatindex_f': 88.9, 'dewpoint_c': 22.8, 'dewpoint_f': 73.0, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 13.6, 'gust_kph': 22.0}, {'time_epoch': 1604952000, 'time': '2020-11-09 21:00', 'temp_c': 27.9, 'temp_f': 82.2, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 10.3, 'wind_kph': 16.6, 'wind_degree': 210, 'wind_dir': 'SSW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 75, 'cloud': 10, 'feelslike_c': 31.3, 'feelslike_f': 88.3, 'windchill_c': 27.9, 'windchill_f': 82.2, 'heatindex_c': 31.3, 'heatindex_f': 88.3, 'dewpoint_c': 23.0, 'dewpoint_f': 73.4, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 13.9, 'gust_kph': 22.3}, {'time_epoch': 1604955600, 'time': '2020-11-09 22:00', 'temp_c': 27.6, 'temp_f': 81.7, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 10.1, 'wind_kph': 16.2, 'wind_degree': 214, 'wind_dir': 'SW', 'pressure_mb': 1013.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 76, 'cloud': 10, 'feelslike_c': 31.0, 'feelslike_f': 87.8, 'windchill_c': 27.6, 'windchill_f': 81.7, 'heatindex_c': 31.0, 'heatindex_f': 87.8, 'dewpoint_c': 23.1, 'dewpoint_f': 73.6, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 14.1, 'gust_kph': 22.7}, {'time_epoch': 1604959200, 'time': '2020-11-09 23:00', 'temp_c': 27.5, 'temp_f': 81.5, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 9.4, 'wind_kph': 15.1, 'wind_degree': 214, 'wind_dir': 'SW', 'pressure_mb': 1013.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 78, 'cloud': 13, 'feelslike_c': 31.0, 'feelslike_f': 87.8, 'windchill_c': 27.5, 'windchill_f': 81.5, 'heatindex_c': 31.0, 'heatindex_f': 87.8, 'dewpoint_c': 23.3, 'dewpoint_f': 73.9, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 13.0, 'gust_kph': 20.9}]}, {'date': '2020-11-10', 'date_epoch': 1604966400, 'day': {'maxtemp_c': 30.8, 'maxtemp_f': 87.4, 'mintemp_c': 26.5, 'mintemp_f': 79.7, 'avgtemp_c': 28.3, 'avgtemp_f': 82.9, 'maxwind_mph': 10.3, 'maxwind_kph': 16.6, 'totalprecip_mm': 3.7, 'totalprecip_in': 0.15, 'avgvis_km': 9.6, 'avgvis_miles': 5.0, 'avghumidity': 75.0, 'daily_will_it_rain': 1, 'daily_chance_of_rain': '85', 'daily_will_it_snow': 0, 'daily_chance_of_snow': '0', 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'uv': 9.0}, 'astro': {'sunrise': '06:35 AM', 'sunset': '06:26 PM', 'moonrise': '02:03 AM', 'moonset': '02:40 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': '28'}, 'hour': [{'time_epoch': 1604962800, 'time': '2020-11-10 00:00', 'temp_c': 27.4, 'temp_f': 81.3, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 8.7, 'wind_kph': 14.0, 'wind_degree': 215, 'wind_dir': 'SW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 80, 'cloud': 15, 'feelslike_c': 31.0, 'feelslike_f': 87.8, 'windchill_c': 27.4, 'windchill_f': 81.3, 'heatindex_c': 31.0, 'heatindex_f': 87.8, 'dewpoint_c': 23.6, 'dewpoint_f': 74.5, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 11.9, 'gust_kph': 19.1}, {'time_epoch': 1604966400, 'time': '2020-11-10 01:00', 'temp_c': 27.3, 'temp_f': 81.1, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 8.1, 'wind_kph': 13.0, 'wind_degree': 215, 'wind_dir': 'SW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 81, 'cloud': 18, 'feelslike_c': 31.0, 'feelslike_f': 87.8, 'windchill_c': 27.3, 'windchill_f': 81.1, 'heatindex_c': 31.0, 'heatindex_f': 87.8, 'dewpoint_c': 23.8, 'dewpoint_f': 74.8, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 10.7, 'gust_kph': 17.3}, {'time_epoch': 1604970000, 'time': '2020-11-10 02:00', 'temp_c': 27.1, 'temp_f': 80.8, 'is_day': 0, 'condition': {'text': 'Cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/119.png', 'code': 1006}, 'wind_mph': 7.4, 'wind_kph': 11.9, 'wind_degree': 226, 'wind_dir': 'SW', 'pressure_mb': 1012.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 82, 'cloud': 40, 'feelslike_c': 30.7, 'feelslike_f': 87.3, 'windchill_c': 27.1, 'windchill_f': 80.8, 'heatindex_c': 30.7, 'heatindex_f': 87.3, 'dewpoint_c': 23.8, 'dewpoint_f': 74.8, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 10.1, 'gust_kph': 16.2}, {'time_epoch': 1604973600, 'time': '2020-11-10 03:00', 'temp_c': 26.9, 'temp_f': 80.4, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 6.9, 'wind_kph': 11.2, 'wind_degree': 237, 'wind_dir': 'WSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 83, 'cloud': 61, 'feelslike_c': 30.5, 'feelslike_f': 86.9, 'windchill_c': 26.9, 'windchill_f': 80.4, 'heatindex_c': 30.5, 'heatindex_f': 86.9, 'dewpoint_c': 23.8, 'dewpoint_f': 74.8, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 9.2, 'gust_kph': 14.8}, {'time_epoch': 1604977200, 'time': '2020-11-10 04:00', 'temp_c': 26.7, 'temp_f': 80.1, 'is_day': 0, 'condition': {'text': 'Cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/119.png', 'code': 1006}, 'wind_mph': 6.3, 'wind_kph': 10.1, 'wind_degree': 248, 'wind_dir': 'WSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 84, 'cloud': 83, 'feelslike_c': 30.2, 'feelslike_f': 86.4, 'windchill_c': 26.7, 'windchill_f': 80.1, 'heatindex_c': 30.2, 'heatindex_f': 86.4, 'dewpoint_c': 23.8, 'dewpoint_f': 74.8, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 8.5, 'gust_kph': 13.7}, {'time_epoch': 1604980800, 'time': '2020-11-10 05:00', 'temp_c': 26.6, 'temp_f': 79.9, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 6.5, 'wind_kph': 10.4, 'wind_degree': 254, 'wind_dir': 'WSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 84, 'cloud': 72, 'feelslike_c': 30.0, 'feelslike_f': 86.0, 'windchill_c': 26.6, 'windchill_f': 79.9, 'heatindex_c': 30.0, 'heatindex_f': 86.0, 'dewpoint_c': 23.6, 'dewpoint_f': 74.5, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 8.9, 'gust_kph': 14.4}, {'time_epoch': 1604984400, 'time': '2020-11-10 06:00', 'temp_c': 26.6, 'temp_f': 79.9, 'is_day': 0, 'condition': {'text': 'Cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/119.png', 'code': 1006}, 'wind_mph': 6.7, 'wind_kph': 10.8, 'wind_degree': 260, 'wind_dir': 'W', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 83, 'cloud': 61, 'feelslike_c': 29.8, 'feelslike_f': 85.6, 'windchill_c': 26.6, 'windchill_f': 79.9, 'heatindex_c': 29.8, 'heatindex_f': 85.6, 'dewpoint_c': 23.5, 'dewpoint_f': 74.3, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 9.4, 'gust_kph': 15.1}, {'time_epoch': 1604988000, 'time': '2020-11-10 07:00', 'temp_c': 26.5, 'temp_f': 79.7, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 6.9, 'wind_kph': 11.2, 'wind_degree': 266, 'wind_dir': 'W', 'pressure_mb': 1012.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 83, 'cloud': 50, 'feelslike_c': 29.6, 'feelslike_f': 85.3, 'windchill_c': 26.5, 'windchill_f': 79.7, 'heatindex_c': 29.6, 'heatindex_f': 85.3, 'dewpoint_c': 23.3, 'dewpoint_f': 73.9, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 9.8, 'gust_kph': 15.8}, {'time_epoch': 1604991600, 'time': '2020-11-10 08:00', 'temp_c': 27.4, 'temp_f': 81.3, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 6.3, 'wind_kph': 10.1, 'wind_degree': 261, 'wind_dir': 'W', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 78, 'cloud': 58, 'feelslike_c': 30.7, 'feelslike_f': 87.3, 'windchill_c': 27.4, 'windchill_f': 81.3, 'heatindex_c': 30.7, 'heatindex_f': 87.3, 'dewpoint_c': 23.1, 'dewpoint_f': 73.6, 'will_it_rain': 0, 'chance_of_rain': '28', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 8.5, 'gust_kph': 13.7}, {'time_epoch': 1604995200, 'time': '2020-11-10 09:00', 'temp_c': 28.3, 'temp_f': 82.9, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 5.6, 'wind_kph': 9.0, 'wind_degree': 257, 'wind_dir': 'WSW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.1, 'precip_in': 0.0, 'humidity': 73, 'cloud': 66, 'feelslike_c': 31.8, 'feelslike_f': 89.2, 'windchill_c': 28.3, 'windchill_f': 82.9, 'heatindex_c': 31.8, 'heatindex_f': 89.2, 'dewpoint_c': 22.9, 'dewpoint_f': 73.2, 'will_it_rain': 0, 'chance_of_rain': '57', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 6.9, 'gust_kph': 11.2}, {'time_epoch': 1604998800, 'time': '2020-11-10 10:00', 'temp_c': 29.2, 'temp_f': 84.6, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 4.9, 'wind_kph': 7.9, 'wind_degree': 253, 'wind_dir': 'WSW', 'pressure_mb': 1013.0, 'pressure_in': 30.4, 'precip_mm': 0.1, 'precip_in': 0.0, 'humidity': 68, 'cloud': 74, 'feelslike_c': 32.9, 'feelslike_f': 91.2, 'windchill_c': 29.2, 'windchill_f': 84.6, 'heatindex_c': 32.9, 'heatindex_f': 91.2, 'dewpoint_c': 22.7, 'dewpoint_f': 72.9, 'will_it_rain': 1, 'chance_of_rain': '85', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 5.6, 'gust_kph': 9.0}, {'time_epoch': 1605002400, 'time': '2020-11-10 11:00', 'temp_c': 29.7, 'temp_f': 85.5, 'is_day': 1, 'condition': {'text': 'Light rain shower', 'icon': '//cdn.weatherapi.com/weather/64x64/day/353.png', 'code': 1240}, 'wind_mph': 5.6, 'wind_kph': 9.0, 'wind_degree': 240, 'wind_dir': 'WSW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.3, 'precip_in': 0.01, 'humidity': 66, 'cloud': 68, 'feelslike_c': 33.6, 'feelslike_f': 92.5, 'windchill_c': 29.7, 'windchill_f': 85.5, 'heatindex_c': 33.6, 'heatindex_f': 92.5, 'dewpoint_c': 22.7, 'dewpoint_f': 72.9, 'will_it_rain': 1, 'chance_of_rain': '85', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 6.7, 'gust_kph': 10.8}, {'time_epoch': 1605006000, 'time': '2020-11-10 12:00', 'temp_c': 30.3, 'temp_f': 86.5, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 6.3, 'wind_kph': 10.1, 'wind_degree': 228, 'wind_dir': 'SW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.5, 'precip_in': 0.02, 'humidity': 64, 'cloud': 63, 'feelslike_c': 34.4, 'feelslike_f': 93.9, 'windchill_c': 30.3, 'windchill_f': 86.5, 'heatindex_c': 34.4, 'heatindex_f': 93.9, 'dewpoint_c': 22.7, 'dewpoint_f': 72.9, 'will_it_rain': 1, 'chance_of_rain': '84', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 7.6, 'gust_kph': 12.2}, {'time_epoch': 1605009600, 'time': '2020-11-10 13:00', 'temp_c': 30.8, 'temp_f': 87.4, 'is_day': 1, 'condition': {'text': 'Light rain shower', 'icon': '//cdn.weatherapi.com/weather/64x64/day/353.png', 'code': 1240}, 'wind_mph': 6.9, 'wind_kph': 11.2, 'wind_degree': 216, 'wind_dir': 'SW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 0.7, 'precip_in': 0.03, 'humidity': 62, 'cloud': 57, 'feelslike_c': 35.1, 'feelslike_f': 95.2, 'windchill_c': 30.8, 'windchill_f': 87.4, 'heatindex_c': 35.1, 'heatindex_f': 95.2, 'dewpoint_c': 22.7, 'dewpoint_f': 72.9, 'will_it_rain': 1, 'chance_of_rain': '83', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 8.7, 'gust_kph': 14.0}, {'time_epoch': 1605013200, 'time': '2020-11-10 14:00', 'temp_c': 30.5, 'temp_f': 86.9, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 8.1, 'wind_kph': 13.0, 'wind_degree': 213, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 0.9, 'precip_in': 0.04, 'humidity': 63, 'cloud': 67, 'feelslike_c': 34.7, 'feelslike_f': 94.5, 'windchill_c': 30.5, 'windchill_f': 86.9, 'heatindex_c': 34.7, 'heatindex_f': 94.5, 'dewpoint_c': 22.7, 'dewpoint_f': 72.9, 'will_it_rain': 1, 'chance_of_rain': '75', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.7, 'vis_miles': 6.0, 'gust_mph': 10.5, 'gust_kph': 16.9}, {'time_epoch': 1605016800, 'time': '2020-11-10 15:00', 'temp_c': 30.3, 'temp_f': 86.5, 'is_day': 1, 'condition': {'text': 'Light rain shower', 'icon': '//cdn.weatherapi.com/weather/64x64/day/353.png', 'code': 1240}, 'wind_mph': 9.2, 'wind_kph': 14.8, 'wind_degree': 211, 'wind_dir': 'SSW', 'pressure_mb': 1009.0, 'pressure_in': 30.3, 'precip_mm': 1.1, 'precip_in': 0.04, 'humidity': 64, 'cloud': 76, 'feelslike_c': 34.4, 'feelslike_f': 93.9, 'windchill_c': 30.3, 'windchill_f': 86.5, 'heatindex_c': 34.4, 'heatindex_f': 93.9, 'dewpoint_c': 22.8, 'dewpoint_f': 73.0, 'will_it_rain': 0, 'chance_of_rain': '67', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.3, 'vis_miles': 5.0, 'gust_mph': 12.3, 'gust_kph': 19.8}, {'time_epoch': 1605020400, 'time': '2020-11-10 16:00', 'temp_c': 30.0, 'temp_f': 86.0, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 10.3, 'wind_kph': 16.6, 'wind_degree': 209, 'wind_dir': 'SSW', 'pressure_mb': 1009.0, 'pressure_in': 30.3, 'precip_mm': 1.3, 'precip_in': 0.05, 'humidity': 65, 'cloud': 85, 'feelslike_c': 34.0, 'feelslike_f': 93.2, 'windchill_c': 30.0, 'windchill_f': 86.0, 'heatindex_c': 34.0, 'heatindex_f': 93.2, 'dewpoint_c': 22.8, 'dewpoint_f': 73.0, 'will_it_rain': 0, 'chance_of_rain': '59', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 14.1, 'gust_kph': 22.7}, {'time_epoch': 1605024000, 'time': '2020-11-10 17:00', 'temp_c': 29.4, 'temp_f': 84.9, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 9.8, 'wind_kph': 15.8, 'wind_degree': 207, 'wind_dir': 'SSW', 'pressure_mb': 1009.0, 'pressure_in': 30.3, 'precip_mm': 1.3, 'precip_in': 0.05, 'humidity': 69, 'cloud': 83, 'feelslike_c': 33.4, 'feelslike_f': 92.1, 'windchill_c': 29.4, 'windchill_f': 84.9, 'heatindex_c': 33.4, 'heatindex_f': 92.1, 'dewpoint_c': 23.0, 'dewpoint_f': 73.4, 'will_it_rain': 0, 'chance_of_rain': '64', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 13.4, 'gust_kph': 21.6}, {'time_epoch': 1605027600, 'time': '2020-11-10 18:00', 'temp_c': 28.9, 'temp_f': 84.0, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 9.4, 'wind_kph': 15.1, 'wind_degree': 206, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 1.3, 'precip_in': 0.05, 'humidity': 72, 'cloud': 81, 'feelslike_c': 32.8, 'feelslike_f': 91.0, 'windchill_c': 28.9, 'windchill_f': 84.0, 'heatindex_c': 32.8, 'heatindex_f': 91.0, 'dewpoint_c': 23.2, 'dewpoint_f': 73.8, 'will_it_rain': 0, 'chance_of_rain': '70', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 13.0, 'gust_kph': 20.9}, {'time_epoch': 1605031200, 'time': '2020-11-10 19:00', 'temp_c': 28.3, 'temp_f': 82.9, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 8.9, 'wind_kph': 14.4, 'wind_degree': 205, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 1.3, 'precip_in': 0.05, 'humidity': 75, 'cloud': 79, 'feelslike_c': 32.2, 'feelslike_f': 90.0, 'windchill_c': 28.3, 'windchill_f': 82.9, 'heatindex_c': 32.2, 'heatindex_f': 90.0, 'dewpoint_c': 23.4, 'dewpoint_f': 74.1, 'will_it_rain': 1, 'chance_of_rain': '75', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 12.3, 'gust_kph': 19.8}, {'time_epoch': 1605034800, 'time': '2020-11-10 20:00', 'temp_c': 28.0, 'temp_f': 82.4, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 9.4, 'wind_kph': 15.1, 'wind_degree': 206, 'wind_dir': 'SSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 1.0, 'precip_in': 0.04, 'humidity': 76, 'cloud': 79, 'feelslike_c': 31.7, 'feelslike_f': 89.1, 'windchill_c': 28.0, 'windchill_f': 82.4, 'heatindex_c': 31.7, 'heatindex_f': 89.1, 'dewpoint_c': 23.3, 'dewpoint_f': 73.9, 'will_it_rain': 1, 'chance_of_rain': '71', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 13.2, 'gust_kph': 21.2}, {'time_epoch': 1605038400, 'time': '2020-11-10 21:00', 'temp_c': 27.6, 'temp_f': 81.7, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 9.8, 'wind_kph': 15.8, 'wind_degree': 207, 'wind_dir': 'SSW', 'pressure_mb': 1012.0, 'pressure_in': 30.3, 'precip_mm': 0.6, 'precip_in': 0.02, 'humidity': 77, 'cloud': 80, 'feelslike_c': 31.2, 'feelslike_f': 88.2, 'windchill_c': 27.6, 'windchill_f': 81.7, 'heatindex_c': 31.2, 'heatindex_f': 88.2, 'dewpoint_c': 23.3, 'dewpoint_f': 73.9, 'will_it_rain': 0, 'chance_of_rain': '67', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 13.9, 'gust_kph': 22.3}, {'time_epoch': 1605042000, 'time': '2020-11-10 22:00', 'temp_c': 27.3, 'temp_f': 81.1, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 10.3, 'wind_kph': 16.6, 'wind_degree': 208, 'wind_dir': 'SSW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.3, 'precip_in': 0.01, 'humidity': 78, 'cloud': 80, 'feelslike_c': 30.7, 'feelslike_f': 87.3, 'windchill_c': 27.3, 'windchill_f': 81.1, 'heatindex_c': 30.7, 'heatindex_f': 87.3, 'dewpoint_c': 23.2, 'dewpoint_f': 73.8, 'will_it_rain': 0, 'chance_of_rain': '63', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 14.8, 'gust_kph': 23.8}, {'time_epoch': 1605045600, 'time': '2020-11-10 23:00', 'temp_c': 27.3, 'temp_f': 81.1, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 9.8, 'wind_kph': 15.8, 'wind_degree': 208, 'wind_dir': 'SSW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.2, 'precip_in': 0.01, 'humidity': 78, 'cloud': 60, 'feelslike_c': 30.7, 'feelslike_f': 87.3, 'windchill_c': 27.3, 'windchill_f': 81.1, 'heatindex_c': 30.7, 'heatindex_f': 87.3, 'dewpoint_c': 23.2, 'dewpoint_f': 73.8, 'will_it_rain': 0, 'chance_of_rain': '42', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.3, 'vis_miles': 5.0, 'gust_mph': 13.9, 'gust_kph': 22.3}]}, {'date': '2020-11-11', 'date_epoch': 1605052800, 'day': {'maxtemp_c': 31.8, 'maxtemp_f': 89.2, 'mintemp_c': 27.0, 'mintemp_f': 80.6, 'avgtemp_c': 28.6, 'avgtemp_f': 83.4, 'maxwind_mph': 10.1, 'maxwind_kph': 16.2, 'totalprecip_mm': 5.4, 'totalprecip_in': 0.21, 'avgvis_km': 9.6, 'avgvis_miles': 5.0, 'avghumidity': 73.0, 'daily_will_it_rain': 1, 'daily_chance_of_rain': '88', 'daily_will_it_snow': 0, 'daily_chance_of_snow': '0', 'condition': {'text': 'Moderate rain', 'icon': '//cdn.weatherapi.com/weather/64x64/day/302.png', 'code': 1189}, 'uv': 10.0}, 'astro': {'sunrise': '06:35 AM', 'sunset': '06:26 PM', 'moonrise': '02:57 AM', 'moonset': '03:28 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': '21'}, 'hour': [{'time_epoch': 1605049200, 'time': '2020-11-11 00:00', 'temp_c': 27.3, 'temp_f': 81.1, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 9.2, 'wind_kph': 14.8, 'wind_degree': 208, 'wind_dir': 'SSW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.1, 'precip_in': 0.0, 'humidity': 78, 'cloud': 39, 'feelslike_c': 30.6, 'feelslike_f': 87.1, 'windchill_c': 27.3, 'windchill_f': 81.1, 'heatindex_c': 30.6, 'heatindex_f': 87.1, 'dewpoint_c': 23.2, 'dewpoint_f': 73.8, 'will_it_rain': 0, 'chance_of_rain': '21', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.7, 'vis_miles': 6.0, 'gust_mph': 13.2, 'gust_kph': 21.2}, {'time_epoch': 1605052800, 'time': '2020-11-11 01:00', 'temp_c': 27.3, 'temp_f': 81.1, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 8.7, 'wind_kph': 14.0, 'wind_degree': 208, 'wind_dir': 'SSW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 78, 'cloud': 19, 'feelslike_c': 30.6, 'feelslike_f': 87.1, 'windchill_c': 27.3, 'windchill_f': 81.1, 'heatindex_c': 30.6, 'heatindex_f': 87.1, 'dewpoint_c': 23.2, 'dewpoint_f': 73.8, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 12.3, 'gust_kph': 19.8}, {'time_epoch': 1605056400, 'time': '2020-11-11 02:00', 'temp_c': 27.3, 'temp_f': 81.1, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 7.8, 'wind_kph': 12.6, 'wind_degree': 207, 'wind_dir': 'SSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.8, 'precip_in': 0.03, 'humidity': 79, 'cloud': 40, 'feelslike_c': 30.6, 'feelslike_f': 87.1, 'windchill_c': 27.3, 'windchill_f': 81.1, 'heatindex_c': 30.6, 'heatindex_f': 87.1, 'dewpoint_c': 23.2, 'dewpoint_f': 73.8, 'will_it_rain': 0, 'chance_of_rain': '25', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.7, 'vis_miles': 6.0, 'gust_mph': 11.2, 'gust_kph': 18.0}, {'time_epoch': 1605060000, 'time': '2020-11-11 03:00', 'temp_c': 27.2, 'temp_f': 81.0, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 6.7, 'wind_kph': 10.8, 'wind_degree': 207, 'wind_dir': 'SSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 1.5, 'precip_in': 0.06, 'humidity': 79, 'cloud': 60, 'feelslike_c': 30.6, 'feelslike_f': 87.1, 'windchill_c': 27.2, 'windchill_f': 81.0, 'heatindex_c': 30.6, 'heatindex_f': 87.1, 'dewpoint_c': 23.3, 'dewpoint_f': 73.9, 'will_it_rain': 0, 'chance_of_rain': '49', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.3, 'vis_miles': 5.0, 'gust_mph': 10.1, 'gust_kph': 16.2}, {'time_epoch': 1605063600, 'time': '2020-11-11 04:00', 'temp_c': 27.2, 'temp_f': 81.0, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 5.8, 'wind_kph': 9.4, 'wind_degree': 206, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 2.3, 'precip_in': 0.09, 'humidity': 79, 'cloud': 81, 'feelslike_c': 30.6, 'feelslike_f': 87.1, 'windchill_c': 27.2, 'windchill_f': 81.0, 'heatindex_c': 30.6, 'heatindex_f': 87.1, 'dewpoint_c': 23.3, 'dewpoint_f': 73.9, 'will_it_rain': 1, 'chance_of_rain': '74', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 8.9, 'gust_kph': 14.4}, {'time_epoch': 1605067200, 'time': '2020-11-11 05:00', 'temp_c': 27.1, 'temp_f': 80.8, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 5.6, 'wind_kph': 9.0, 'wind_degree': 213, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 1.9, 'precip_in': 0.07, 'humidity': 79, 'cloud': 81, 'feelslike_c': 30.5, 'feelslike_f': 86.9, 'windchill_c': 27.1, 'windchill_f': 80.8, 'heatindex_c': 30.5, 'heatindex_f': 86.9, 'dewpoint_c': 23.2, 'dewpoint_f': 73.8, 'will_it_rain': 1, 'chance_of_rain': '78', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 8.3, 'gust_kph': 13.3}, {'time_epoch': 1605070800, 'time': '2020-11-11 06:00', 'temp_c': 27.1, 'temp_f': 80.8, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 5.6, 'wind_kph': 9.0, 'wind_degree': 219, 'wind_dir': 'SW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 1.5, 'precip_in': 0.06, 'humidity': 79, 'cloud': 81, 'feelslike_c': 30.3, 'feelslike_f': 86.5, 'windchill_c': 27.1, 'windchill_f': 80.8, 'heatindex_c': 30.3, 'heatindex_f': 86.5, 'dewpoint_c': 23.2, 'dewpoint_f': 73.8, 'will_it_rain': 1, 'chance_of_rain': '82', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 7.8, 'gust_kph': 12.6}, {'time_epoch': 1605074400, 'time': '2020-11-11 07:00', 'temp_c': 27.0, 'temp_f': 80.6, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 5.4, 'wind_kph': 8.6, 'wind_degree': 226, 'wind_dir': 'SW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 1.1, 'precip_in': 0.04, 'humidity': 79, 'cloud': 81, 'feelslike_c': 30.2, 'feelslike_f': 86.4, 'windchill_c': 27.0, 'windchill_f': 80.6, 'heatindex_c': 30.2, 'heatindex_f': 86.4, 'dewpoint_c': 23.1, 'dewpoint_f': 73.6, 'will_it_rain': 1, 'chance_of_rain': '86', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 7.2, 'gust_kph': 11.5}, {'time_epoch': 1605078000, 'time': '2020-11-11 08:00', 'temp_c': 27.9, 'temp_f': 82.2, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 5.8, 'wind_kph': 9.4, 'wind_degree': 221, 'wind_dir': 'SW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.7, 'precip_in': 0.03, 'humidity': 75, 'cloud': 63, 'feelslike_c': 31.3, 'feelslike_f': 88.3, 'windchill_c': 27.9, 'windchill_f': 82.2, 'heatindex_c': 31.3, 'heatindex_f': 88.3, 'dewpoint_c': 22.9, 'dewpoint_f': 73.2, 'will_it_rain': 0, 'chance_of_rain': '57', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.3, 'vis_miles': 5.0, 'gust_mph': 7.2, 'gust_kph': 11.5}, {'time_epoch': 1605081600, 'time': '2020-11-11 09:00', 'temp_c': 28.8, 'temp_f': 83.8, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 6.0, 'wind_kph': 9.7, 'wind_degree': 216, 'wind_dir': 'SW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.4, 'precip_in': 0.02, 'humidity': 70, 'cloud': 45, 'feelslike_c': 32.3, 'feelslike_f': 90.1, 'windchill_c': 28.8, 'windchill_f': 83.8, 'heatindex_c': 32.3, 'heatindex_f': 90.1, 'dewpoint_c': 22.6, 'dewpoint_f': 72.7, 'will_it_rain': 0, 'chance_of_rain': '29', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.7, 'vis_miles': 6.0, 'gust_mph': 7.4, 'gust_kph': 11.9}, {'time_epoch': 1605085200, 'time': '2020-11-11 10:00', 'temp_c': 29.7, 'temp_f': 85.5, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 6.5, 'wind_kph': 10.4, 'wind_degree': 211, 'wind_dir': 'SSW', 'pressure_mb': 1012.0, 'pressure_in': 30.4, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 65, 'cloud': 27, 'feelslike_c': 33.4, 'feelslike_f': 92.1, 'windchill_c': 29.7, 'windchill_f': 85.5, 'heatindex_c': 33.4, 'heatindex_f': 92.1, 'dewpoint_c': 22.4, 'dewpoint_f': 72.3, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 7.4, 'gust_kph': 11.9}, {'time_epoch': 1605088800, 'time': '2020-11-11 11:00', 'temp_c': 30.4, 'temp_f': 86.7, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 7.2, 'wind_kph': 11.5, 'wind_degree': 207, 'wind_dir': 'SSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 62, 'cloud': 22, 'feelslike_c': 34.3, 'feelslike_f': 93.7, 'windchill_c': 30.4, 'windchill_f': 86.7, 'heatindex_c': 34.3, 'heatindex_f': 93.7, 'dewpoint_c': 22.4, 'dewpoint_f': 72.3, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 8.3, 'gust_kph': 13.3}, {'time_epoch': 1605092400, 'time': '2020-11-11 12:00', 'temp_c': 31.1, 'temp_f': 88.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 7.8, 'wind_kph': 12.6, 'wind_degree': 204, 'wind_dir': 'SSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 60, 'cloud': 18, 'feelslike_c': 35.2, 'feelslike_f': 95.4, 'windchill_c': 31.1, 'windchill_f': 88.0, 'heatindex_c': 35.2, 'heatindex_f': 95.4, 'dewpoint_c': 22.3, 'dewpoint_f': 72.1, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 8.9, 'gust_kph': 14.4}, {'time_epoch': 1605096000, 'time': '2020-11-11 13:00', 'temp_c': 31.8, 'temp_f': 89.2, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 8.5, 'wind_kph': 13.7, 'wind_degree': 200, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 57, 'cloud': 13, 'feelslike_c': 36.1, 'feelslike_f': 97.0, 'windchill_c': 31.8, 'windchill_f': 89.2, 'heatindex_c': 36.1, 'heatindex_f': 97.0, 'dewpoint_c': 22.3, 'dewpoint_f': 72.1, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 9.8, 'gust_kph': 15.8}, {'time_epoch': 1605099600, 'time': '2020-11-11 14:00', 'temp_c': 31.2, 'temp_f': 88.2, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 8.9, 'wind_kph': 14.4, 'wind_degree': 201, 'wind_dir': 'SSW', 'pressure_mb': 1009.0, 'pressure_in': 30.3, 'precip_mm': 0.6, 'precip_in': 0.02, 'humidity': 60, 'cloud': 32, 'feelslike_c': 35.4, 'feelslike_f': 95.7, 'windchill_c': 31.2, 'windchill_f': 88.2, 'heatindex_c': 35.4, 'heatindex_f': 95.7, 'dewpoint_c': 22.5, 'dewpoint_f': 72.5, 'will_it_rain': 0, 'chance_of_rain': '23', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.7, 'vis_miles': 6.0, 'gust_mph': 11.4, 'gust_kph': 18.4}, {'time_epoch': 1605103200, 'time': '2020-11-11 15:00', 'temp_c': 30.5, 'temp_f': 86.9, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 9.6, 'wind_kph': 15.5, 'wind_degree': 201, 'wind_dir': 'SSW', 'pressure_mb': 1009.0, 'pressure_in': 30.3, 'precip_mm': 1.3, 'precip_in': 0.05, 'humidity': 63, 'cloud': 52, 'feelslike_c': 34.7, 'feelslike_f': 94.5, 'windchill_c': 30.5, 'windchill_f': 86.9, 'heatindex_c': 34.7, 'heatindex_f': 94.5, 'dewpoint_c': 22.7, 'dewpoint_f': 72.9, 'will_it_rain': 0, 'chance_of_rain': '46', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.3, 'vis_miles': 5.0, 'gust_mph': 13.2, 'gust_kph': 21.2}, {'time_epoch': 1605106800, 'time': '2020-11-11 16:00', 'temp_c': 29.9, 'temp_f': 85.8, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 10.1, 'wind_kph': 16.2, 'wind_degree': 202, 'wind_dir': 'SSW', 'pressure_mb': 1008.0, 'pressure_in': 30.2, 'precip_mm': 1.9, 'precip_in': 0.07, 'humidity': 66, 'cloud': 72, 'feelslike_c': 34.0, 'feelslike_f': 93.2, 'windchill_c': 29.9, 'windchill_f': 85.8, 'heatindex_c': 34.0, 'heatindex_f': 93.2, 'dewpoint_c': 22.9, 'dewpoint_f': 73.2, 'will_it_rain': 0, 'chance_of_rain': '69', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.0, 'vis_miles': 5.0, 'gust_mph': 14.8, 'gust_kph': 23.8}, {'time_epoch': 1605110400, 'time': '2020-11-11 17:00', 'temp_c': 29.3, 'temp_f': 84.7, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 9.4, 'wind_kph': 15.1, 'wind_degree': 203, 'wind_dir': 'SSW', 'pressure_mb': 1009.0, 'pressure_in': 30.3, 'precip_mm': 1.3, 'precip_in': 0.05, 'humidity': 70, 'cloud': 54, 'feelslike_c': 33.3, 'feelslike_f': 91.9, 'windchill_c': 29.3, 'windchill_f': 84.7, 'heatindex_c': 33.3, 'heatindex_f': 91.9, 'dewpoint_c': 23.1, 'dewpoint_f': 73.6, 'will_it_rain': 0, 'chance_of_rain': '46', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.3, 'vis_miles': 5.0, 'gust_mph': 13.4, 'gust_kph': 21.6}, {'time_epoch': 1605114000, 'time': '2020-11-11 18:00', 'temp_c': 28.6, 'temp_f': 83.5, 'is_day': 1, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 8.9, 'wind_kph': 14.4, 'wind_degree': 204, 'wind_dir': 'SSW', 'pressure_mb': 1009.0, 'pressure_in': 30.3, 'precip_mm': 0.6, 'precip_in': 0.02, 'humidity': 73, 'cloud': 36, 'feelslike_c': 32.5, 'feelslike_f': 90.5, 'windchill_c': 28.6, 'windchill_f': 83.5, 'heatindex_c': 32.5, 'heatindex_f': 90.5, 'dewpoint_c': 23.3, 'dewpoint_f': 73.9, 'will_it_rain': 0, 'chance_of_rain': '23', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 9.7, 'vis_miles': 6.0, 'gust_mph': 11.9, 'gust_kph': 19.1}, {'time_epoch': 1605117600, 'time': '2020-11-11 19:00', 'temp_c': 28.0, 'temp_f': 82.4, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 8.3, 'wind_kph': 13.3, 'wind_degree': 205, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 77, 'cloud': 17, 'feelslike_c': 31.8, 'feelslike_f': 89.2, 'windchill_c': 28.0, 'windchill_f': 82.4, 'heatindex_c': 31.8, 'heatindex_f': 89.2, 'dewpoint_c': 23.5, 'dewpoint_f': 74.3, 'will_it_rain': 0, 'chance_of_rain': '0', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 10.5, 'gust_kph': 16.9}, {'time_epoch': 1605121200, 'time': '2020-11-11 20:00', 'temp_c': 27.8, 'temp_f': 82.0, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 8.3, 'wind_kph': 13.3, 'wind_degree': 205, 'wind_dir': 'SSW', 'pressure_mb': 1010.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 78, 'cloud': 36, 'feelslike_c': 31.6, 'feelslike_f': 88.9, 'windchill_c': 27.8, 'windchill_f': 82.0, 'heatindex_c': 31.6, 'heatindex_f': 88.9, 'dewpoint_c': 23.6, 'dewpoint_f': 74.5, 'will_it_rain': 0, 'chance_of_rain': '29', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 10.5, 'gust_kph': 16.9}, {'time_epoch': 1605124800, 'time': '2020-11-11 21:00', 'temp_c': 27.7, 'temp_f': 81.9, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 8.1, 'wind_kph': 13.0, 'wind_degree': 204, 'wind_dir': 'SSW', 'pressure_mb': 1011.0, 'pressure_in': 30.3, 'precip_mm': 0.1, 'precip_in': 0.0, 'humidity': 79, 'cloud': 54, 'feelslike_c': 31.5, 'feelslike_f': 88.7, 'windchill_c': 27.7, 'windchill_f': 81.9, 'heatindex_c': 31.5, 'heatindex_f': 88.7, 'dewpoint_c': 23.7, 'dewpoint_f': 74.7, 'will_it_rain': 0, 'chance_of_rain': '59', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 10.7, 'gust_kph': 17.3}, {'time_epoch': 1605128400, 'time': '2020-11-11 22:00', 'temp_c': 27.5, 'temp_f': 81.5, 'is_day': 0, 'condition': {'text': 'Patchy rain possible', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 8.1, 'wind_kph': 13.0, 'wind_degree': 204, 'wind_dir': 'SSW', 'pressure_mb': 1012.0, 'pressure_in': 30.3, 'precip_mm': 0.1, 'precip_in': 0.0, 'humidity': 80, 'cloud': 73, 'feelslike_c': 31.3, 'feelslike_f': 88.3, 'windchill_c': 27.5, 'windchill_f': 81.5, 'heatindex_c': 31.3, 'heatindex_f': 88.3, 'dewpoint_c': 23.8, 'dewpoint_f': 74.8, 'will_it_rain': 1, 'chance_of_rain': '88', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 10.7, 'gust_kph': 17.3}, {'time_epoch': 1605132000, 'time': '2020-11-11 23:00', 'temp_c': 27.4, 'temp_f': 81.3, 'is_day': 0, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 8.1, 'wind_kph': 13.0, 'wind_degree': 211, 'wind_dir': 'SSW', 'pressure_mb': 1012.0, 'pressure_in': 30.3, 'precip_mm': 0.1, 'precip_in': 0.0, 'humidity': 81, 'cloud': 54, 'feelslike_c': 31.1, 'feelslike_f': 88.0, 'windchill_c': 27.4, 'windchill_f': 81.3, 'heatindex_c': 31.1, 'heatindex_f': 88.0, 'dewpoint_c': 23.8, 'dewpoint_f': 74.8, 'will_it_rain': 0, 'chance_of_rain': '59', 'will_it_snow': 0, 'chance_of_snow': '0', 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 10.7, 'gust_kph': 17.3}]}]\n"
     ]
    }
   ],
   "source": [
    "response = requests.get('http://api.weatherapi.com/v1/forecast.json?key=ea62b294238944a09bd05542200411&q=Lagos&days=7')\n",
    "week_forecast = response.json()\n",
    "print(week_forecast['forecast']['forecastday'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "If the high temperature of the day is 32.8 degrees Celsius, it will be a warm day on 2020-11-09.\n",
      "If the high temperature of the day is 30.8 degrees Celsius, it will be a warm day on 2020-11-10.\n",
      "If the high temperature of the day is 31.8 degrees Celsius, it will be a warm day on 2020-11-11.\n"
     ]
    }
   ],
   "source": [
    "for forecast in week_forecast['forecast']['forecastday']:\n",
    "    if forecast['day']['maxtemp_c'] >= 35:\n",
    "        print(f\"If the high temperature of the day is {forecast['day']['maxtemp_c']} degrees Celsius, it will be a hot day on {forecast['date']}.\")\n",
    "    elif forecast ['day']['maxtemp_c'] >= 15:\n",
    "        print(f\"If the high temperature of the day is {forecast['day']['maxtemp_c']} degrees Celsius, it will be a warm day on {forecast['date']}.\")\n",
    "    else:\n",
    "        print(f\"If the high temperature of the day is {forecast['day']['maxtemp_c']} degrees Celsius, it will be a cold day on {forecast['date']}.\")\n",
    "              "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 6) What will be the hottest day in the next week? What is the high temperature on that day?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?\n",
    "\n",
    "I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say \"{temperature} and cloudy\" instead of just the temperature. \n",
    "\n",
    "- *Tip: You'll only need one day of forecast*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?\n",
    "\n",
    "- *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['location', 'current', 'forecast', 'alert'])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url=\"http://api.weatherapi.com/v1/forecast.json?key=ea62b294238944a09bd05542200411&q=Miami&days=1\"\n",
    "miamitwentyfour=requests.get(url)\n",
    "miamidata=miamitwentyfour.json()\n",
    "miamidata.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(miamidata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#50% is same as 0.5\n",
    "#Got stuck trying to figure out how to finish this"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Declare variables\n",
    "n_hours_day=0\n",
    "miamidata['forecastday']['date_epoch']\n",
    "for count in miamidata['forecastday']['date_epoch']:\n",
    "    if miamidata['forecastday']['date_epoch'] > 0.5:\n",
    "        print(\"The temperature when it is hour\",n_hours_day+1,\"is\",miamidata['hourly']['data'][n_hours_day]['temperature'],\"degrees F and cloudy.\")\n",
    "    else:\n",
    "        print(\"The temperature when it is hour\",n_hours_day+1,\"is\",miamidata['hourly']['data'][n_hours_day]['temperature'],\"degrees F.\")\n",
    "    n_hours_day=n_hours_day+1\n",
    "    \n",
    "    if n_hours_day>23:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9) What was the temperature in Central Park on Christmas Day, 2015? How about 2012? 2007? How far back does the API allow you to go?\n",
    "\n",
    "- *Tip: You'll need to use latitude/longitude. You can ask Google, it knows*\n",
    "- *Tip: Remember when latitude/longitude might use negative numbers*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['error'])\n"
     ]
    }
   ],
   "source": [
    "url = \"http://api.weatherapi.com/v1/history.json?key=ea62b294238944a09bd05542200411&q=New York&dt=2015-12-25\"\n",
    "response = requests.get(\"http://api.weatherapi.com/v1/history.json?key=ea62b294238944a09bd05542200411&q=New York&dt=2015-12-25\") \n",
    "forecast_2010 = response.json()\n",
    "print(forecast_2010.keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Central Park showed an error when inputted as a place, so try longitude and latitude of 40.785091 and -73.968285\n",
    "#Also, year 2015"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"http://api.weatherapi.com/v1/history.json?key=ea62b294238944a09bd05542200411&q=q=40.785091,-73.968285&dt=2010-12-25\"              "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['error'])\n"
     ]
    }
   ],
   "source": [
    "response = requests.get(\"http://api.weatherapi.com/v1/history.json?key=ea62b294238944a09bd05542200411&q=q=40.785091,-73.968285&dt=2010-12-25\")\n",
    "forecast_2015 = response.json()\n",
    "print(forecast_2015.keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#API still refusing to back to 2015...or even 2020-11-01"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
