
import numpy as np 



# Create drag model for earth 

class EarthModel:
	
	SELF_RADIUS = 6378 * 1000
	SCALE_HEIGHT = 8570
	SEA_DENSITY = 1.225


	def getAtmosphericDensity(r):
		h = r - cls.EARTH_RADIUS
		rho = cls.SEA_DENSITY * np.exp(-cls.SCALE_HEIGHT/h)
		return rho 

	





