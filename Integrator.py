from Body import Body 
from DragModel import DragModel as dm
import scipy as sp 
import fluids as fl 



class Integrator:


	def __init__(self,planet,body, time_step):
		self.body = body
		self.planet = planet
		self.time = 0
		self.time_step = time_step

	def updateTime(self):
		self.time += self.time_step
	
	def setTimeStep(self,dt):
		self.time_step = dt 

	def calculateDrag(self):
		drag_model = dm(self.body)
		rho = drag_model.getAtmopshericDensity()
		BC = self.body.getBallisticCoefficient()
		v = self.body.getVelocity()
		m = self.body.getMass()
		cDa = m/BC
		F_d = 0.5 * rho * v**2 * cDa 
		return F_d

	def addDrag(self):
		drag_force = self.calculateDrag()
		self.body.addForce(drag_force)

	def addForce(self,force):
		self.body.addForce(force)

	def calculate2Pertrubation(self):
		J2 = 0.00108263
		mu = self.body.getMu()
		r = self.body.getRadius()
		re = 6378*1000
		pos = self.body.getPosition()

		a_x = -mu/(r**3)*pos[0]-(3*mu)/(2*r**5)*R**2*J2*\
		(1-5*(pos[2]/r)**2)*pos[0]

		a_y = -mu/(r**3)*pos[1]-(3*mu)/(2*r**5)*R**2*J2*\
		(1-5*(pos[2]/r)**2)*pos[1]

		a_z = -mu/(r**3)*pos[3]-(3*mu)/(2*r**5)*R**2*J2*\
		(1-5*(pos[2]/r)**2)*pos[3]

		force = self.body.getMass() * [a_x,a_y,a_z]
		return force 

	def addJ2Pertrubation(self):
		force = self.calculate2Pertrubation()
		self.addForce(force)

	












