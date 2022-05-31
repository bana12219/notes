class Solution(object):
	#no pueden ser peso 0, hay que validar la lista
	#hay 3 casos:
	#1. cuando los asteroides son signos iguales ambos son finalistas
	#2. cuando son signos diferentes prevalece el mayor
	#3. cuando son signos diferentes pero igual peso se eliminan
	def asteroidCollision(self,asteroids):
		"""
		:type asteroids: List[int]
		:rtype: List[int]
		"""
		final_asteroids=list()
		asteroid2compare=list()
		while asteroids:
			asteroid2compare.clear()
			asteroid2compare.insert(0,asteroids.pop(-1))
			if not asteroids:
				#si solo tiene un elemento del par a evaluar, regresalo
				final_asteroids.insert(0,asteroid2compare[0])
				return final_asteroids
			asteroid2compare.insert(1,asteroids.pop(-1))
			#signos iguales
			if asteroid2compare[0]<0 and asteroid2compare[1] <0 or asteroid2compare[0]>0 and asteroid2compare[1] >0:
				#agrega ambos
				for elemento in asteroid2compare:
					final_asteroids.insert(0,elemento)
				continue
			#signos diferentes, pesos iguales se eliminan
			if abs(asteroid2compare[0])==abs(asteroid2compare[1]):
				continue
			#signos diferentes, pesos diferentes: primero mayor
			if abs(asteroid2compare[0])>abs(asteroid2compare[1]):
				#reinsertalo para volver a comparar
				asteroids.append(asteroid2compare[0])
				continue
			#signos diferentes, pesos diferentes: segundo mayor
			#reinsertalo para volver a comparar
			asteroids.append(asteroid2compare[1])
		return final_asteroids

if __name__ == "__main__":
	s=Solution()
	s.asteroidCollision([5, 10, -5])
		

	