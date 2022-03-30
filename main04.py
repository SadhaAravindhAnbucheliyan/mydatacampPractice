height=[54,65,36,98,87,95]
weight=[15,45,25,36,24,34]
import numpy as np
np_height_m=np.array(height)
np_weight_kg=np.array(weight)*0.453592
bmi=np_weight_kg/np_height_m**2
print(bmi)