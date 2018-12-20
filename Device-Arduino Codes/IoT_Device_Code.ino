#include <SimpleDHT.h>
int pinDHT11 = 2;
SimpleDHT11 dht11;

//For pH_Sensor:
#define SensorPin A5            //pH meter Analog output to Arduino Analog Input 5
#define Offset 0.00            //deviation compensate
#define LED 13
#define samplingInterval 20
#define printInterval 800
#define ArrayLenth  40    //times of collection
int pHArray[ArrayLenth];   //Store the average value of the sensor feedback
int pHArrayIndex=0;
float pH;


//For Soil Moisture Sensor:
int moisture_inputpin = A2;
int moisture;


//String for final Output:
String final_output;



void setup() {
  // put your setup code here, to run once:
  pinMode(LED,OUTPUT);
  
  Serial.begin(9600);

}


void loop() {
  
  // put your main code here, to run repeatedly:


  //Code for DHT11 to get Temperature and Humidity:
  byte temperature = 0;
  byte humidity = 0;
  int err = SimpleDHTErrSuccess;
  if ((err = dht11.read(pinDHT11, &temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
    //Serial.print("Read DHT11 failed, err="); Serial.println(err);
    delay(1000);
    return;
  }
  //Serial.print("Sample OK: ");
  //Serial.print((int)temperature); Serial.print(" *C, "); 
  //Serial.print((int)humidity); Serial.println(" H");
  //Code for DHT11 Ends....

  //Getting the pH_Value:
  pH = calculate_pH();
  //Serial.print("pH = ");
  //Serial.println(pH);

  //Getting the moisture percentage:
  moisture = calculate_moisture();
  //Serial.print("Moisture = ");
  //Serial.print(moisture);
  //Serial.println("%");

  final_output = String(moisture) + '|' + String(pH) + '|' + String(humidity) + '|' + String(temperature);
  Serial.print(final_output);
  delay(1000);

}

int calculate_moisture()
{
  int moisture_input = analogRead(moisture_inputpin);
  //Serial.println("Input Moisture Value = ");
  //Serial.println(moisture_input);
  moisture_input = map(moisture_input, 0, 1023, 100, 0);
  return moisture_input;
}



//Function that calculates and returns the pH
//Note that it takes a few seconds to display the actual pH Value 
float calculate_pH()
{
  static unsigned long samplingTime = millis();
  static unsigned long printTime = millis();
  static float pHValue,voltage;
  if(millis()-samplingTime > samplingInterval)
  {
      pHArray[pHArrayIndex++]=analogRead(SensorPin);
      if(pHArrayIndex==ArrayLenth)pHArrayIndex=0;
      voltage = avergearray(pHArray, ArrayLenth)*5.0/1024;
      pHValue = 3.5*voltage+Offset;
      samplingTime=millis();
  }
  if(millis() - printTime > printInterval)   //Every 800 milliseconds, print a numerical, convert the state of the LED indicator
  {
  //Serial.print("Voltage:");
        //Serial.print(voltage,2);
        //Serial.print("    pH value: ");
  //Serial.println(pHValue,2);
        digitalWrite(LED,digitalRead(LED)^1);
        printTime=millis();
        return pHValue;
  }
}

//Function required for the calculation of pH
double avergearray(int* arr, int number){
  int i;
  int max,min;
  double avg;
  long amount=0;
  if(number<=0){
    //Serial.println("Error number for the array to avraging!/n");
    return 0;
  }
  if(number<5){   //less than 5, calculated directly statistics
    for(i=0;i<number;i++){
      amount+=arr[i];
    }
    avg = amount/number;
    return avg;
  }else{
    if(arr[0]<arr[1]){
      min = arr[0];max=arr[1];
    }
    else{
      min=arr[1];max=arr[0];
    }
    for(i=2;i<number;i++){
      if(arr[i]<min){
        amount+=min;        //arr<min
        min=arr[i];
      }else {
        if(arr[i]>max){
          amount+=max;    //arr>max
          max=arr[i];
        }else{
          amount+=arr[i]; //min<=arr<=max
        }
      }//if
    }//for
    avg = (double)amount/(number-2);
  }//if
  return avg / 2.13;
}

