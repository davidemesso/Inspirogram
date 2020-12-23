import inspirobot  # Import the libary
from requests import get
import time
from instabot import Bot 
import os

def generateImage():
    image = inspirobot.generate()
    response = get(image.url)
    with open('output.png', 'wb') as file:
        file.write(response.content)

def init_bot():  
    bot = Bot() 
    bot.login(username = "youremail@provider.dom",  
            password = "yourpassword123") 
    return bot

if __name__ == "__main__":
    bot = init_bot()
    while True:
        for filename in os.listdir('./'):
            if filename.endswith('.REMOVE_ME'):
                os.remove(filename)
        generateImage()
        print("got")
        bot.upload_photo("output.png", 
            caption ="All credits to inspirobot.me #inspiring#deep#quotes") 
        time.sleep(300)
