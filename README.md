# Min2 - Test Automation Engineer Scenario
Developed by Edoardo Ascenzi

## UML Class Diagram
![alt text](https://github.com/edoardoascenzi/Min2/blob/fce0189d4da82919e7554ee48861bab6f775ef75/doc/UML%20Class%20Diagram.png)

## Solution Description
In order to meet Oscar’s requirement we can create three classes: Vehicle, Sensor and VehicleFunction.

*	VehicleFunction represents what a car is able to do. It includes the name of the vehicle function (e.g. overtaking) and the capabilities it has (i.e. “The vehicle is capable of overtaking”). This object is the one Oscar will use during his tests. For example, assuming a test case is like “Drive in an highway, set a speed higher than the vehicle in front of you -> the vehicle shall perform the overtaking”; If the vehicle has the overtaking vehicle function, it will pass the test, otherwise it will not. 
The method getCapabilities() is useful to have the description of the vehicle function under test.
*	Sensor is the class that include all the feature that the sensor would have. In this case they are the name (e.g. radar) and the VehicleFunction that it brings when installed on a compatible vehicle (e.g. overtaking). 
The methods are getVF() to have the VehicleFunction object related to that sensor and getCapabilities() which describe the capabilities of it.
*	Vehicle is the main class that represents the whole car object. It is defined by its name (that is the vehicle line name e.g. Elite), the array of all the Sensor and of all the VehicleFunction it has.
The method importVehicleType(str) define the “base” vehicle function defined by the car design that vehicle is based on (in this case Ant). Since the only parameters that the customer can choose are the vehicle line and the sensor list, the vehicle type is pre-defined in a database that contain the mapping between it and the vehicle line. The same database include also the list of sensors allowed for each vehicle line, and the vehicle function connected to each sensor and vehicle type. This solution make the system easy to scale because, in order to add new sensors or vehicle lines and type, it is necessary just to add those elements to the database, leaving the code unchanged.
The methods addSensor(str) and removeSensor(str) give the possibility to add or remove a sensor from a vehicle object already created. These functions include addVehicleFunction(str) and removeVehicleFunction(str) which add or remove the VehicleFunction related to the respective sensor
The last three methods are getSensor(), getVehicleFunction() and getCapabilities() and they are getter that returns respectively: the array of Sensor objects of the vehicle, the array of VehicleFunction object of the vehicle and the list of capabilities that vehicle has.
