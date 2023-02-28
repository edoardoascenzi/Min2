# -*- coding: utf-8 -*-
"""
@author: Edoardo Ascenzi
"""

import pandas as pd

#dict <VehicleFunction name>: <VehicleFunction capabilites description>
dictVehicleFuncion_capabilites = {"brake":"The vehicle is capable of breaking",
                        "auto pilot": "The vehicle has the auto pilot",
                        "avoid obstacles": "The vehicle is capable of avoiding obstacles",
                        "intersections navigation": "The vehicle is capable of navigating intersections",
                        "overtaking" : "The vehicle is capable of overtaking",
                        "lane changing": "The vehicle is capable of changing lane",                
                        }

# dict <Sensor name>: <VehicleFuncion name>
dictSensor_VehicleFunction = {"lidar": "intersections navigation",
                "radar": "overtaking",
                "camera": "lane changing",
                }

#dict <VehicleType name> : <VehicleFunction list>
dictVehicleType_VehicleFunction = {"ant": ["brake" , "auto pilot" , "avoid obstacles"],
                                   }

import numpy
dataVehicle = { "name" : ["elite" , "classic" ,"paragon" ,"gentry","test"],
            "sensorAllowed" : [["camera", "radar", "lidar"], #Elite
                              ["radar"], #Classic
                              ["camera"], #Paragon
                              ["camera","radar"], #Gentry
                              [], # test
                               ],
            "VehicleType" : ["ant", "ant", "ant", "ant",numpy.NaN]
            }

dfVehicle = pd.DataFrame(data = dataVehicle).set_index("name") #use name as index of the df

