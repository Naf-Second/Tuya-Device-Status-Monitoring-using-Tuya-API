import csv
import datetime
import os
import schedule
import time

ACCESS_ID = "xxx"
ACCESS_KEY = "xxx"
API_ENDPOINT = "https://openapi.tuyaeu.com"

#Endpoint varies as per your data server center, mine is central europe.

from tuya_connector import TuyaOpenAPI
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

def run_code():
    try:
        response = openapi.get('/v1.0/iot-03/devices/status?device_ids=xxx')
        print(response) #printing response to check functionality 
        currentconsumption = response['result'][0]['status'][2]
        currentcurrent = response['result'][0]['status'][3]
        currentpower = response['result'][0]['status'][4]
        currentvoltage = response['result'][0]['status'][5]
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        power = currentpower['value']
        current = currentcurrent['value']
        voltage = currentvoltage['value']
        consumption = currentconsumption['value']

        # Constructing the absolute path to the CSV file
        # The csv file will be created automatically
        csv_file_path = 'C:/Users/cur_power_data.csv'  # Replace with your absolute path

        # Checking the current working directory
        print("Current Working Directory:", os.getcwd())

        # New values to add for each column
        new_data = {
            'Current Power': power,
            'Current Voltage': voltage,
            'Current Current': current,
            'Energy Consumption': consumption,
            'TimeStamp': current_time  # current timestamp
        }

        # Open the existing CSV file in append mode
        with open(csv_file_path, 'a', newline='') as csvfile:
            fieldnames = ['Current Power', 'Current Voltage', 'Current Current', 'Energy Consumption', 'TimeStamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # If the file is empty, write the header
            if csvfile.tell() == 0:
                writer.writeheader()

            # Write the new data to the CSV file
            writer.writerow(new_data)

        print("New data has been added to cur_power_data.csv")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Schedule the job to run every 2 minutes
schedule.every(5).minutes.do(run_code)

# Keep the script running to allow scheduled jobs to be executed
while True:
    schedule.run_pending()
    time.sleep(1)
