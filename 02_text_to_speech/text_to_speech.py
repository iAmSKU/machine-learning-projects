# Package
# pip install gTTS

# Refernece 
# https://www.geeksforgeeks.org/convert-text-speech-python/
# https://stackoverflow.com/questions/40811540/gtts-google-text-to-speech-error-audio-gets-saved-but-does-not-play-automatic
# https://blog.finxter.com/5-ways-to-read-a-text-file-from-a-url/

from gtts import gTTS
import os
import urllib

def save():
    #myText = "Welcome to python"
    #myText = readLink("https://simple.wikipedia.org/wiki/Rama")
    myText = readText(".\inputs\data.txt")

    language = "en"

    obj = gTTS(myText, lang=language, slow=False)

    obj.save("recording.mp3")

    os.system("start recording.mp3")

def readLink(target_url):
    data = ""

    for line in urllib.request.urlopen(target_url):
        data += line.decode('utf-8') 

    return data

def readText(file_path):
    fp = open(file_path)
    data = fp.read()    
    return data

save()
