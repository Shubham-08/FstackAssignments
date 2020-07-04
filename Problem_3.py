import bisect;


def trips(N, salads, pizzas, cakes):
	elements = [0] * N
	uniqueTrips = 0
	pizzas.sort()
	cakes.sort()
	for idx in range(N - 1, -1, -1):
		temp = pizzas[idx] + 1
		index = (bisect.bisect(cakes, temp))
		if index < N:
			elements[idx] = N - index
		if idx + 1 < len(elements):
			elements[idx] += elements[idx + 1]

	for idx in range(0, N):
		temp = salads[idx] + 1
		index = (bisect.bisect(pizzas, temp))
		if index < N:
			uniqueTrips += elements[index]

	return (uniqueTrips)


answer = trips(2, [29, 29], [61, 61], [70, 70])
