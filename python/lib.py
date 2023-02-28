# -*- coding: utf-8 -*-
"""
@author: Edoardo Ascenzi
"""
import DB       


class Vehicle:
    def __init__(self,name:str,sensorConfig:"list of strings" = []):
        #Type error checks
        if not isinstance(name, str):
            raise TypeError ("name must be a string")
        if not isinstance(sensorConfig, list):
            raise TypeError ("sensorConfig must be a list")
        elif len(sensorConfig) > 0:
            if not isinstance(sensorConfig[0], str):
                raise TypeError ("sensorConfig must be a list of strings")
        
        if name.lower() not in DB.dfVehicle.index:
            raise RuntimeError(f"[Vehicle] {name} not found")
        self.name = name.lower()
        self.VFs = []
        self.importVehicleType() # initialize VF list according VehicleType (if present)
        self.sensors = []
        for sensor in sensorConfig:
            self.addSensor(sensor)
        self.getCapabilities()
        

    def __str__(self):
        return self.name

    def importVehicleType(self):
        import pandas
        self.vehicleType =  DB.dfVehicle.VehicleType[self.name]
        if pandas.notna(self.vehicleType): #if a vehicle type is defined for that vehicle model
            if self.vehicleType not in DB.dictVehicleType_VehicleFunction.keys(): #case insensitive
                raise RuntimeError(f"[Vehicle] {self.vehicleType} of {self.name} not found")
            else:
                for VF in DB.dictVehicleType_VehicleFunction[self.vehicleType]:
                    self.addVehicleFunction(VF)
        else:
            print(f"[Vehicle] {self.name} has no vehicle type")
            
    def addSensor(self,sensor:str): 
        sensor = sensor.lower()
        if not sensor in DB.dfVehicle.sensorAllowed[self.name]:
            raise RuntimeError(f"[Vehicle] {sensor} is not compatible with {self.name} vehicle line")
        from Sensor import Sensor
        self.sensors.append(Sensor(sensor))
        from VehicleFunction import VehicleFunction
        self.VFs.append(VehicleFunction(DB.dictSensor_VehicleFunction[sensor]))
        
    def removeSensor(self,sensor:str):
        sensorNameList = [i.name for i in self.sensors]
        if not sensor in sensorNameList:
            raise RuntimeWarning(f"[Vehicle] {sensor} sensor is not present in current vehicle configuration")
        sensorToRemove = self.sensors[sensorNameList.index(sensor)]
        self.sensors.remove(sensorToRemove)
        self.removeVehicleFunction(sensorToRemove.getVF().name)
        print(f"Sensor {sensor} removed Correctly")
        
    def removeVehicleFunction(self,VF:str):
        VFNameList = [i.name for i in self.VFs]
        if not VF in VFNameList:
            raise RuntimeWarning(f"[Vehicle] {VF} VF is not present in current vehicle configuration")
        VFToRemove = self.VFs[VFNameList.index(VF)]
        self.VFs.remove(VFToRemove)
        
        
    def addVehicleFunction(self,VF:str):
        from VehicleFunction import VehicleFunction
        self.VFs.append(VehicleFunction(VF))
     
    def getSensor(self):
        if len(self.sensors) == 0:
            print("This car has no sensor.")
            return None
        else:
            [print(i) for i in self.sensors]
            return self.sensors
        
    def getVehicleFunction(self):
        if len(self.VFs) == 0:
            print("This car has no vehicle functions.")
            return None
        else:
            [print(i) for i in self.VFs]
            return self.VFs
    
    def getCapabilities(self):
        if len(self.VFs) == 0:
            print("This Vehicle has no capabilities")
        else:
            for VF in self.VFs:
                VF.getCapabilities()
            
            
class Sensor:
    def __init__(self,name):
        #Type error checks
        if not isinstance(name, str):
            raise TypeError ("name must be a string")
        if name.lower() not in DB.dictSensor_VehicleFunction.keys():
            raise RuntimeError(f"[Sensor] {name} not found")
        else:
            self.name = name.lower()
            self.VF = VehicleFunction(DB.dictSensor_VehicleFunction[self.name])
                
    def __str__(self):
        return self.name
    
    def getVF(self):
        return self.VF
    
    def getCapabilities(self):
        return self.VF.getCapabilities()
    
    
    
class VehicleFunction:
    def __init__(self,name):
        #Type error checks
        if not isinstance(name, str):
            raise TypeError ("name must be a string")
        if name.lower() not in DB.dictVehicleFuncion_capabilites.keys(): #case insensitive
            raise RuntimeError(f"[VehicleFunction] {name} not found")
        else:
            self.name = name.lower()
            self.capabilites = DB.dictVehicleFuncion_capabilites[self.name]
     
    def __str__(self):
        return self.name
    
    def getCapabilities(self):
        print(self.capabilites)
        return self.capabilites

            