from collections import deque

Origin = deque()
Aux = deque()
Destiny = deque()
Origin.extend(range(0,4))

print 'origin: ', Origin
print 'aux: ', Aux
print 'destiny: ', Destiny
print 'solving'

def hanoi(origin, aux, destiny):
	if len(origin) == 1:
		firstElement = origin.popleft()
		destiny.appendleft(firstElement)
		return
	else:
		largestDisc = origin.pop()
		hanoi(origin, destiny, aux)
		destiny.appendleft(largestDisc)
		hanoi(aux, origin, destiny)
		return

hanoi(Origin, Aux, Destiny)

print 'solved'
print 'origin: ', Origin
print 'aux: ', Aux
print 'destiny: ', Destiny
