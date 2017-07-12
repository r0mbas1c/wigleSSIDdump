# wigleSSIDdump
Dumps text file of SSIDs in a given geolocation using Wigle API

Using Wigle API2, bounds a given geographic area by two lats and two longs and retrieves up to 500 Wigle database entries for that region, then parses just the BSSID to a named text file (one SSID per line).

## Dependencies
Python package "pygle" - https://pypi.python.org/pypi/pygle/0.20

## Configuration
Configure pygle with your Wigle API credentials.
1. Register for Wigle account -- https://wigle.net
2. In top menu of website, click TOOLS, then click the YOUR ACCOUNT PAGE under the "Via the API" section
3. Click SHOW MY TOKEN
4. API NAME at bottom is the username (encoded) and API TOKEN is the password (encoded)
5. Copy and paste API NAME into "username" (in between the quotes) in the pywiglenet.py file
6. Copy and paste API TOKEN into "password" in the pywgilenet.py file

## Usage 
`python wigleSSIDdump.py`


