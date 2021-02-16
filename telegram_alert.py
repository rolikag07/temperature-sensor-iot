import requests
import json
import time

from boltiot import Bolt
import conf

mybolt = Bolt(conf.bolt_api_key, conf.device_id)

def get_sensor_value_from_pin(pin):
    """Returns the sensor value. Returns -999 if request fails"""
    try:
        response = mybolt.analogRead(pin)
        data = json.loads(response)
        if data["success"] != 1:
            print("Request not successfull")
            print("This is the response->", data)
            return -999
        sensor_value = int(data["value"])
        return sensor_value
    except Exception as e:
        print("Something went wrong when returning the sensor value")
        print(e)
        return -999


def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/bot" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("This is the Telegram URL")
        print(url)
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False


while True:
    # Step 1
    sensor_value = get_sensor_value_from_pin("A0")
    Temperature = round( (100*sensor_value)/1024)    
    print("Currently your room temperature is:", Temperature)
    
    # Step 2
    if sensor_value == -999:
        print("Request was unsuccessfull. Skipping.")
        time.sleep(10)
        continue
    
    # Step 3
    if sensor_value >= 287:
       print("Room temperature risen up")
       message = "Alert! the room temperature has risen to " + str(Temperature) + ". Kindly lower down the room temperature for the baby"
       telegram_status = send_telegram_message(message)
       print("This is the Telegram status:", telegram_status)

    # Step 4
    if sensor_value >= conf.threshold:
       print("Room temperature is normal ")
       message = "The room temperature " + str(Temperature) + " is okay for the baby. "
       telegram_status = send_telegram_message(message)
       print("This is the Telegram status:", telegram_status)

    # Step 5
    if sensor_value <= conf.threshold:
       print("Room temperature is lowered ") 
       message = "Alert! the room temperature has been lowered to " + str(Temperature) + " .kindly warm up the room a bit for the baby."
       telegram_status = send_telegram_message(message)
       print("This is the Telegram status:", telegram_status)
         
    # Step 6
    time.sleep(1800)


	
