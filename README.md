# KrishiSathi

A web portal for farmers integrated with ML and IoT to analyze daily crops and their growth.
The main purpose of initiating this undertaking for my "Final Year Project" was to get an insight on the integration amon hardware, software and AI (learning). 

## Description

I would like to describe each building process separately and reflect my experiences and tools that I used throughout the development phase.

#### Hardware and Mobile Application
I first started the project focusing on the hardware part (me being a Robotics enthusiast definitely helped with works related to embedded systems)
* The device was build around *Arduino* as the brain (or microcontroller) along with sensors like pH Meter (SKU: SEN0161), humidity & temperature sensor (DHT22) and soil moisture sensor (SEN-13322)
* The values obtained from the sensors acted as the feature for our machine learning model
* To collect the measured data from soil (with the help of sensors), I build an android application using the [MIT App Inventor 2](http://ai2.appinventor.mit.edu/) because I did not have proper knowledge of JAVA and Android Studio

Android Application             |  Hardware Schematics
:------------------------------:|:-------------------------:
![](https://github.com/asheeshcric/krishisathi/blob/master/images/android_application.png)  |  ![](https://github.com/asheeshcric/krishisathi/blob/master/images/hardware_schematics.png)

#### Web Application
The web application was developed in Django. It was particularly important to create an interface for a user (farmer in our case) to have an insight of over their crops and soil condition.
* The user would simply sign up using the web application and receive a user id
* Next thing is to connect the IoT device to the android app via bluetooth (we used HC-06 bluetooth module in the device for that purpose)
* Once the android app connects to the device and starts receiving real time data, the user can submit it to the web application's database.
* The submitted data gets through the trained model and different graphs and insights on the real data are shown on the web app; along with the classification of suitable crops that can be grown on the field

Web Application
:------------------------------------------------------------------------------------:
![](https://github.com/asheeshcric/krishisathi/blob/master/images/web_application.png)


#### Machine Learning
We used a classical machine learning technique involving decision trees--called *Random Forest Classifier*
* The trained model yielded 84.6% accuracy on the testing set
* The dataset was accessed and refined from the [Ministry of Agriculture, Nepal](http://www.moad.gov.np/en) with the help of our supervisor and his contacts in the soil department
* The prominent features chosen for the machine learning model were *pH*, *soil_moisture*, *temperature*, and *humidity*
* We trained the model with around 48,000 data points classifying eight major types of soils--each corresponding to their favorable crops and fruits
* The classified soil type and its corresponding suitable crops and fruits are displayed as recommendation for the user (or farmer) in the web portal 

## Getting Started

The instructions below will get you a copy of the project up and running on your local machine for development and testing purposes. To get started, clone the repository on a folder that you want.


### Prerequisites

The major things that you will need to run this application are Python3 and pip3

```
 $ sudo apt-get install python3
 $ sudo apt-get install python3-pip
```

### Installing

After you get the python3 and the pip3 installed and working, you will need to install the requirements to run your project. The django application resides inside the folder named *"krishisathi"*

For that purpose, go to the root directory of the repository and run the following command:

```
 $ pip3 install -r requirements.txt
```

**Note**: You might want to use a virtual environment for installing the python packages required for the project

```
 $ sudo pip3 install virtualenv
 $ virtualenv krishisathi
 $ source path/to/env/bin/activate
```

For database services, you can either use the provided Sqlite3 database from Django or else you can setup your own MySQL or Postgres database service. The configurations for the project is decoupled in *env.example* file. You need to copy that file to a separate file named *.env* inside krishisathi/ folder. You local configurations are the ones that go inside the *.env* file

**Note**: If you are using the pre-provided sqlite3 from Django, then please tweak the database settings in the settings.py file. You can use the default configurations instead of the one that I've used.

## Built With

* [Django](https://docs.djangoproject.com/en/2.0/) - The web framework used
* [MIT App Inventor 2](http://ai2.appinventor.mit.edu/) - Android app building tool
* [scikit-learn](https://scikit-learn.org/) - The Machine Learning library used


## Authors

* **Ashish Jaiswal** - *Initial work* - *Project Lead* - [Ashish Jaiswal](http://jashish.com.np)
* **Manish Adhikari** - *Project Member* - [Manish Adhikari](https://github.com/Manish-Adhikari)

## Acknowledgements
* To the personnel who were involved in contributing to the project from Kathmandu Engineering College, TU
