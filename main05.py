height=[56,89,9,89,78,65]
weight=[23,43,54,4,23,31]
import numpy as np
np_height_m=np.array(height)*0.0254
np_weight_kg=np.array(weight)*0.453592
bmi=np_weight_kg/np_height_m**2
print(bmi)
light=bmi>21
print(light)