import json
from slackclient import SlackClient
from datetime import datetime
import sys

# Fixes the encoding of the male/female symbol
reload(sys)
sys.setdefaultencoding('utf8')

token = "YOUR SLACK API TOKEN HERE"
sc = SlackClient(token)
wanted_pokemon = None
unwanted_pokemon = None

# Initialize object
def init():
    global sc, wanted_pokemon, unwanted_pokemon
    
    with open('config.json') as data_file:
        data = json.load(data_file)
        # get list of pokemon to send notifications for
        if "notify" in data:
            wanted_pokemon = _str( data["notify"] ) . split(",")

            # transform to lowercase
            wanted_pokemon = [a.lower() for a in wanted_pokemon]
        #get list of pokemon to NOT send notifications for
        if "do_not_notify" in data:
            unwanted_pokemon = _str( data["do_not_notify"] ) . split(",")

            # transform to lowercase
            unwanted_pokemon = [a.lower() for a in unwanted_pokemon]
       
      
        
        

            

# Safely parse incoming strings to unicode
def _str(s):
  return s.encode('utf-8').strip()

  

  
  
# Notify user for discovered Pokemon
def pokemon_found(pokemon):
       
    pokename = _str(pokemon["name"]).lower()
    # check array
    if not sc:
        return
    elif wanted_pokemon != None and not pokename in wanted_pokemon:
        return
    elif wanted_pokemon == None and unwanted_pokemon != None and pokename in unwanted_pokemon:
        return
    # notify
    print "[+] Notifier found pokemon:", pokename

    #http://maps.google.com/maps/place/<place_lat>,<place_long>/@<map_center_lat>,<map_center_long>,<zoom_level>z
    latLon = '{},{}'.format(repr(pokemon["lat"]), repr(pokemon["lng"]))
    google_maps_link = 'http://maps.google.com/maps?q={}&{}z'.format(latLon, latLon, 20)

    disappear_time = str(datetime.fromtimestamp(pokemon["disappear_time"]).strftime("%I:%M%p").lstrip('0'))+")"
    location_text = "Location : " + google_maps_link + ". " + _str(pokemon["name"]) + " Available till " + disappear_time + "."
    

    print sc.api_call(
        "chat.postMessage", channel="#CHANNEL NAME HERE. KEEP THE HASHTAG", text="Drop what you're doing! " + _str(pokemon["name"]) + " is nearby!" + "Location : " + google_maps_link + ". " + " Available till " + disappear_time + ".",
        username='Pokebot', icon_emoji=':robot_face:'
)


init()
