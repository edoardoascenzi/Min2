# -*- coding: utf-8 -*-
"""
@author: Edoardo Ascenzi
"""

from lib import Vehicle

#%%
car1 = Vehicle("gentry",["camera"])
car1.removeSensor("camera")
car1.getCapabilities()


#%%
car2 = Vehicle("volvo",["radar"])



#%%
car3  = Vehicle("classic")

#%%

car4 = Vehicle("Paragon",["camera","radar"])


#%%
car5 = Vehicle("ELITE",["Camera","RADAR","lidar"])