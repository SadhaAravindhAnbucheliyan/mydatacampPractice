height=[[54,57,58],[64,67,68],[74,75,76]]
updated=[[55,56,52],[63,62,65],[71,79,73]]
import numpy as np
np_height=np.array(height)
print(np_height+updated)
np_conversion=np.array([0.0254,0.453592,1])
print(np_height*np_conversion)