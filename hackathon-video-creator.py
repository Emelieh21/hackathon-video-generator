# General dependencies
import json
import urllib
import random
import subprocess
import sys
import fnmatch

# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# To read in the config yaml
import yaml

# Read in the yaml
with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

# The text that you want to convert to audio 
language = config['language']

# generate base URL
baseUrl = str("https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl="+language+"&dt=t&q=")

# Translation function
def getTranslation(baseUrl, text):
    url = str(baseUrl+text).replace(" ", "+")
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print data
    speech = data[0][0][0]
    return(speech)

# Introduction text 
text = "Hello we are "+config["team"]+" and we present to you our project "+config['name']
introduction = getTranslation(baseUrl, text)

# Introduction slide...

# Objective text
text = 'The goal of our project is to '+config['objective']
goal = getTranslation(baseUrl, text)

# three steps text
text = "This is how "+config['name']+" works First "+config['steps']['step_one']+' then '+ config['steps']['step_two']+' finally '+config['steps']['step_three']
steps = getTranslation(baseUrl, text)

# Demo time
text = "And now it is time for a demo! Let's see how it works..."
demo = getTranslation(baseUrl, text)

# Combine all
mytext = introduction+". "+goal+". "+steps+". "+demo

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("welcome.mp3") 

# Pick a random bensound song, I have them in a local folder because I don't want to push the mp3s to git
songList = fnmatch.filter(os.listdir("local"),"*.mp3")
subprocess.Popen(["afplay", "local/"+random.choice(songList)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print('Continuing script...')
# Playing the converted file 
os.system("afplay -v 10 -r 1.2 welcome.mp3") 

