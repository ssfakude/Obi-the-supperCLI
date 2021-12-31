# obi
obi is a cli tool to bring together all my utilities into a centralised place.


## How to Install
1. `git clone https://github.com/ssfakude/Obi-the-supperCLI.git`
2. `cd obi`
3. `pip install --editable .`
4. `obi [cmd]` See [API](#API) section for commands to run.


## Weather
The `weather` commands use [OpenWeatherMap](https://openweathermap.org/) under the hood.

It is intended to be used for querying and viewing weather information.

Below, is a list of currently supported commands.


```commandline
Usage: obi weather [OPTIONS] COMMAND [ARGS]...

  Weather information

Options:
  -l, --location TEXT  Weather at this location.  [default: London]
  --help               Show this message and exit.

Commands:
  current   Current weather at a location
  forecast  Forecast for a location
```

___options___
* `-l` `--location` - override the default location. `obi weather -l <mytown> current`


***`current`***

The `current` command gives you information for weather at a location right now.

```commandline
Usage: obi weather current [OPTIONS]

  Current weather at a location

Options:
  --help  Show this message and exit.
```

```commandline
$ obi weather current

========= Cape Town ZA - BROKEN CLOUDS =========
🔥 Temp: 22.84 - 21.67/23.89 (min/max)
🌪 Wind: 12.8
💧 Rain: {}
🌕 Sunrise: 05:08 - Sunset: 20:08 🌑
```

***`forecast`***

The `forecast` command displays weather for the upcoming days.

```commandline
Usage: obi weather forecast [OPTIONS]

  Forecast for a location

Options:
  --help  Show this message and exit.
```

```commandline
$ obi weather forecast
================================ Cape Town ZA ===============================
📅 Date:  Sat 01 Jan    Sun 02 Jan    Mon 03 Jan    Tue 04 Jan    Wed 05 Jan  
🔥 Temp:    16.93         20.12         20.11         20.23         20.91     
🌪  Wind:     8.64         16.45         20.12         14.11         11.52     
💧 Rain: {'3h': 1.25}       No            No            No            No 
```
