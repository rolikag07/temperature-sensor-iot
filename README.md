
# Temperature Sensor IoT
This project is made using Bolt IoT Wi-Fi Module and Python . In this project temperature data can also be pushed to the  Bolt Cloud. Basically this project senses room temperature and if the temperature crosses the threshold an alert message will sent to you on telegram in regular intervals. 

## Installation

    git clone https://github.com/rolikag07/temperature-sensor-iot
    cd temperature-sensor-iot
    pip install -r requirements.txt

## How to run
Execution of this code is easy. You simply need to execute the command below:

    python3 telegram_alert.py

Note: Kindly edit the conf.py file with your own device configurations. 

## Features

 - Temperature sensing using LM35 
 - Telegram message alert 
 - Google Area Chart Generation
 
 ## Demo Chart 
 
Temperature Chart is  [here](https://cloud.boltiot.com/control?utm_viewer_subscription=bolt_cloud&utm_owner_subscription=bolt_cloud&name=BOLT13168999)
 


For any queries please raise an issue. 
Happy Coding :)

