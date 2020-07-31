### This project no longer supported, as Niantic broke the Pokemon Go API.  I'm leaving this project up in case the API is made public again and someone would like to use this code.  


# Pokemon Go Notification System

This is a modification of [PokemonGo-Finder](https://github.com/jxmorris12/PokemonGo-Finder), 
which is a fork of [the popular PokemonGo-Map repository](https://github.com/AHAAAAAAA/PokemonGo-Map) 
with the purpose of allowing users to passively know if specific Pokemon are nearby without having to 
constantly monitor the map. This allows users to set a list of sought-after Pokemon and receive 
notifications through [Slack](https://slack.com/).

## Configure Slack
Generate a token for sending yourself notifications using the Slack API.  [Go here](https://api.slack.com/docs/oauth-test-tokens), log in, and generate your "token for testing."  Copy down this token code and save it for the ##Notifications section
## Config File
Instead of from the command-line, all arguments are read from a `config.json` file. Jxmorris12 introduced a required field to this config: `notify`, a comma-separated list of the Pokemon that you'd like to receive Pushbullet notifications for.
As an alernative to 'notify', you may also make use of a field called 'do_not_notify'. If the 'do_not_notify' field is present and the 'notify' field is not present, you will be notified for ALL pokemon except the ones in the 'do_not_notify' field.

Here's a sample `config.json` using the 'notify' field:

```
{
  "auth_service": "google",
  "username": "myemailuser",
  "password": "pikachu123",
  "step_limit": 5,
  "location": "742 Evergreen Terrace, Arlington, VA",
  "notify": "dratini,magnemite,electabuzz,hitmonchan,hitmonlee,chansey,lapras,snorlax,porygon,mew,mewtwo,moltres,zapdos,articuno,ditto,seel,gyarados,cubone"
 }
```

Here's a sample `config.json` using the 'do_not_notify' field:

```
{
  "auth_service": "google",
  "username": "myemailuser",
  "password": "pikachu123",
  "step_limit": 5,
  "location": "742 Evergreen Terrace, Arlington, VA",
  "do_not_notify": "rattata,raticate,pidgey,pidgeotto,venonat,zubat,golbat,magikarp,weedle,kakuna,caterpie,metapod"
  }
```

## Install

Install the necessary dependencies (including the slack client) by running `pip install --upgrade -r requirements.txt`.
Open config.json in a text editor and fill in your user info. 
 I recommend using a dummy google account that isnt tied to your main pokemon account in case they decide to ban people.
 Once you have the config file saved, run the main script using `python main.py`.

*Using this software is against the ToS and can get you banned. Use at your own risk.*

## Notifications
You'll have to set up notifications and the slack channel you'd like to receive them.
 Open notifier.py
Replace "YOUR SLACK API TOKEN HERE" with your slack api token. Duh. 
 Then scroll down to the bottom and replace where it says "#YOUR CHANNEL NAME HERE"  with the channel that you want the 
notifications to go to. Keep the # before the name.  This channel has to exist within the slack team that the API token 
was generated from.  

##Catch 'em All!!
Run the main script using `python main.py` and get catching!
 

