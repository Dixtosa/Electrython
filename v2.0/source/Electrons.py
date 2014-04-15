# --encoding=utf-8

import math
import copy


class Point:
	u"""უბრალოდ ელექტრონის ან პროტონის ან ნეიტრონის(ჰუ ნოვზ) კლასი"""

	K = 9 * 10**9
	def __init__(self, x, y, charge):
		self.x, self.y = x, y
		self.charge = charge

	def __eq__(self, point):
		return point.x==self.x and point.y == self.y
	def __ne__(self, point):
		return point.x != self.x or point.y != self.y

	def forceTo(self, point):
		deltaX, deltaY = point.x - self.x, point.y - self.y
		r = math.hypot(deltaX, deltaY)
		sin = deltaY / r
		cos = deltaX / r
		q1, q2 = self.charge, point.charge

		f = Point.K * (q1 * q2)/(r*r)
		return (cos * f, sin * f) #return (x,y)


class Plane:
	def __init__(self, radius):
		self.listOfPoints = []
		self.radius = radius

	def clone(self):
		return copy.deepcopy(self)
	def getPoints(self):
		return self.listOfPoints

	def addPoint(self, x, y, q):
		if self.searchNearby(x, y):
			return False
		else:
			self.listOfPoints.append(Point(x, y, q))
			return True
	def removePoint(self, x, y):
		nearPoint = self.searchNearby(x, y)
		if nearPoint:
			self.listOfPoints.remove(nearPoint)
			return True
		else:
			return False

	def searchNearby(self, x, y):
		for point in self.listOfPoints:
			if x - self.radius < point.x < x + self.radius and y - self.radius < point.y < y + self.radius:
				return point
		return None


	def size(self):
		return len(self.listOfPoints)

	def forcesOf(self, point):
		forces = []
		for curpoint in self.listOfPoints:
			if curpoint != point:
				forces.append(curpoint.forceTo(point))
		return forces

	def addedForcesOf(self, point):
		cumulatedForce = [0, 0]
		for (x, y) in self.forcesOf(point):
			cumulatedForce[0] += x
			cumulatedForce[1] += y
		return tuple(cumulatedForce)
