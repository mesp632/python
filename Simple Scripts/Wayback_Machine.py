#open website using Wayback Machine
#input should request URL and Timestamp
import webbrowser
import json
from urllib.request import urlopen

print("Let's use the Wayback Machine.")
site = input("Type a website URL: ")
datetime = input("Type a year, month, and a day formatted like YYYYMMDD: ")
url = "http://archive.org./wayback/available?url=%s&timestamp=%s" % (site,datetime)
url_response = urlopen(url)
url_contents = url_response.read()
url_text = url_contents.decode("utf-8")
url_data = json.loads(url_text)

try:
    old_url = url_data["archived_snapshots"]["closest"]["url"]
    print("Found this: ", old_url)
    print("Opening Browser to view: ")
    webbrowser.open(old_url)
except:
    print("Unable to find: ", old_url)