# Device-Status-Monitoring-using-Tuya-API

1. In order to get the Access ID and Access KEY, you need to make a project on Tuya IOT website, as well as link your device to the project 
using your preferred method.

2. Make sure you have installed all the dependencies before importing them.

3. Use your own device ID in the GET response call.

4. You can print the response separately.
   https://eu.iot.tuya.com/cloud/explorer
   Go through the doc to see the return structure to get your required status data.

5. The CSV file path should be the same path as the folder your main.py file is in.

6. The program is scheduled to run every 10 minutes, you can unschedule or reschedule as per your need.

#Print the new_data dictionary separately to see if your program is running properly. 

