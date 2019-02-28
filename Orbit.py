import numpy as np 


class Orbit():


	def __init__(self, e, a, i, RAAN, w, f,mu):
		self.a = a
		self.e = e 
		self.i = np.deg2rad(i) 
		self.RAAN = RAAN 
		self.w = w 
		self.f = f
		self.mu = mu


	def getCartesianState(self):
		r = self.a * \
		(1 - self.e**2)/(1 + self.e \
			* np.cos(self.f))
		E = np.arccos((1 - r / self.a)/self.a)
		p_r = r * [np.cos(self.f),np.sin(f),0]
		one_term = np.sqrt(self.mu * self.a) / r 
		p_v = one_term * [-np.sin(E),np.sqrt(1 - self.e**2) * np.cos(E),0]

		r_x = p_r[0]*(np.cos(self.w)*np.cos(self.RAAN)-\
			np.sin(self.w)*np.cos(self.i)*np.sin(self.RAAN)) -\
		p_r[1]*(np.sin(self.w)*np.cos(self.RAAN)+\
			np.cos(self.w)*np.cos(self.i)*np.sin(self.RAAN))

		r_y = p_r[0]*(np.cos(self.w)*np.sin(self.RAAN)+\
			np.sin(self.w)*np.cos(self.i)*np.cos(self.RAAN)) +\
		p_r[1]*(np.cos(self.w)*np.cos(self.i)*np.cos(self.RAAN) -\
			np.sin(self.w)*np.sin(self.RAAN))

		r_z = p_r[0]*(np.sin(self.w)*np.sin(self.i)) + \



			p_r[1]*(np.cos(self.w)*np.sin(self.i))

		radius = [r_x,r_y,r_z]

		v_x = p_v[0]*(np.cos(self.w)*np.cos(self.RAAN) -\
			np.sin(self.w)*np.cos(self.i)*np.sin(self.RAAN)) -\
		p_v[1]*(np.sin(self.w)*np.cos(self.RAAN) +\
			np.cos(self.w)*np.cos(self.i)*np.sin(self.RAAN))

		v_y = p_v[0]*(np.cos(self.w)*np.sin(self.RAAN)+\
			np.sin(self.w)*np.cos(self.i)*np.cos(self.RAAN)) +\
		p_v[1]*(np.cos(self.w)*np.cos(self.i)*np.cos(self.RAAN) -\
			np.sin(self.w)*np.sin(self.RAAN))

		v_z = p_v[0]*(np.sin(self.w)*np.sin(self.i)) +\
			p_v[1]*(np.cos(self.w)*np.sin(self.i))

		velocity = [v_x,v_y,_v_z]

		state = {'position':radius,'velcoity':velcoity}

		return state
















# Getter Setters
##
	def getSemiMajorAxis(self):
		return self.semi_major

	def getEccentricity(self):
		return self.eccentricity

	def getInclination(self):
		return np.rad2deg(self.inclination)

	def getRAAN(self):
		return self.RAAN 

	def getArgPeriapsis(self):
		return self.periapsis

	def getTrueAnomaly(self):
		return self.true_anomaly

	def setSemiMajorAxis(self, a):
		self.semi_major = a

	def setEccentricity(self,e):
		self.eccentricity = e

	def setInclination(self,i):
		self.inclination = np.deg2rad(i) 

	def setRAAN(self,Ra):
		self.RAAN = Ra 

	def setArgPeriapsis(self,w):
		self.periapsis = w 

	def setTrueAnomaly(self,f):
		self.true_anomaly = f 


