# Define the neccesary information for a body in orbit 
import numpy as np 
from numpy import linalg as LA 
from Orbit import Orbit as orb 


class Body():

	# initalize body in orbit with instantenous classic orbit elements at any time
	# include orbit 
	def __init__(self,r,v,f,mu,mass,BC):
		self.position = r
		self.velocity = v
		self.force = f 
		self.mass = mass 
		self.ballisticCoefficent = BC
		self.mu = mu 
		# def __init__(self, e, a, i, RAAN, w, f,mu):
		self.orbit = orb(.5,100,45,45,0.2,1000)



	## Getters and Setters for Force

	def setForce(self,force):
		self.force = force 

	def getForce(self):
		return self.force 

	def addForce(self,force):
		self.force = [sum(x) for x in zip(self.force, force)]

	def getMu(self):
		return self.mu


	## ACCESS POSITIONS

	def getRadiusVector(self):
		return self.position 

	def getVelocityVector(self):
		return self.velcoity 

	def getRadius(self):
		return LA.norm(self.position)

	def getVelocity(self):
		return LA.norm(self.velocity)

	def getAngularMomentumVector(self):
		h = np.cross(self.position,self.velocity)

	def getNodeVector(self):
		h = self.getAngularMomentumVector()
		n = np.cross([0,0,1], h) 
		return n

	def getEccentricityVector(self):
		n = self.getNodeVector()
		v = self.getVelocity()
		r = getRadius()
		e = (v**2/self.mu - 1/r) * self.position - (np.dot(self.position,self.velocity)/self.mu) * self.velocity
		return e 

	## METHODS TO UPDATE ORBIT

	def getEccentricity(self):
		e = self.getEccentricityVector()
		return LA.norm(e)


	def getInclination(self):
		h = self.getAngularMomentumVector()
		i = np.arccos(h[2]/LA.norm(h))
		return np.rad2deg(i)

	def getTrueAnomaly(self):
		r = self.getRadius()
		v = self.getVelocity()
		e = self.getEccentricityVector()
		f = 0
		if np.dot(r,v) >= 0:
			f = np.arccos(np.dot(e,r)/(LA.norm(e)*LA.norm(r)))
		else:
			f = 2*np.pi-np.arccos(np.dot(e,r)/(LA.norm(e)*LA.norm(r)))
		return f 


	def getRAAN(self):
		n = self.getNodeVector()
		RAAN = 0
		if n[1] >= 0:
			RAAN = np.arccos(n[0]/LA.norm(n))
		else:
			RAAN = 2*np.pi-np.arccos(n[0]/LA.norm(n))
		return np.rad2deg(RAAN)



	def getArgPeriapsis(self):
		n = self.getNodeVector()
		e = self.getEccentricityVector()
		w = 0
		if e[2] >= 0:
			w = np.arccos(np.dot(n,e)/(LA.norm(n)*LA.norm(e)))
		else:
			w = 2*pi-np.arccos(np.dot(n,e)/(LA.norm(n)*LA.norm(e)))
		return w

	def getSemiMajorAxis(self):
		v = LA.norm(self.velocity)
		r = LA.norm(self.position)
		a = (2/r - v**2/self.mu)**-1
		return a


	def updateOrbit(self):
		e = self.getEccentricity()
		a = self.getSemiMajorAxis()
		i = self.getInclination()
		w = self.getArgPeriapsis()
		f = self.getTrueAnomaly()
		RAAN = self.getRAAN()

		# def __init__(self, e, a, i, RAAN, w, f,mu):
		self.orbit.setSemiMajorAxis(a)
		self.orbit.setEccentricity(e)
		self.orbit.setInclination(i)
		self.orbit.setRAAN(RAAN)
		self.orbit.setArgPeriapsis(w)
		self.orbit.setTrueAnomaly(f)






































		.....................................

	## DRAG CALC METHODS

	def getBallisticCoefficient(self):
		return self.ballisticCoefficent

	def getMass(self):
		return self.mass



	












