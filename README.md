# KrishiSathi

A web portal for farmers integrated with ML and IoT to analyze daily crops and their growth.
The main purpose of initiating this undertaking for my "Final Year Project" was to get an insight on the integration amon hardware, software and AI (learning). 

## Description

I would like to describe each building process separately and reflect my experiences and tools that I used throughout the development phase.

### Hardware and Mobile Application
I first started the project focusing on the hardware part (me being a Robotics enthusiast definitely helped with works related to embedded systems)
* The device was build around *Arduino* as the brain (or microcontroller) along with sensors like pH Meter (SKU: SEN0161), humidity & temperature sensor (DHT22) and soil moisture sensor (SEN-13322)
* The values obtained from the sensors acted as the feature for our machine learning model
* To collect the measured data from soil (with the help of sensors), I build an android application using the [MIT App Inventor 2](http://ai2.appinventor.mit.edu/) because I did not have proper knowledge of JAVA and Android Studio

![alt text](https://github.com/asheeshcric/krishisathi/blob/master/images/android_application.png)
![alt text](https://github.com/asheeshcric/krishisathi/blob/master/images/hardware_schematics.png)
