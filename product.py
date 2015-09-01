def highest_product(array_of_ints):
	if len(array_of_ints) < 3:
		raise Exception('Getting a product requires at least 3 numbers')

	highest = max(array_of_ints[0], array_of_ints[1])
	lowest = min(array_of_ints[0], array_of_ints[1])

	highestProductOf2 = array_of_ints[0] * array_of_ints[1]
	lowestProductOf2 = array_of_ints[0] * array_of_ints[1]

	highestProductOf3 = array_of_ints[0] * array_of_ints[1] * array_of_ints[2]

	for current in array_of_ints[2:]:

		highestProductOf3 = max(highestProductOf3, current * highestProductOf2, current * lowestProductOf2)
		highestProductOf2 = max(highestProductOf2, current * highest, current * lowest)
		lowestProductOf2 = min(lowestProductOf2, current * highest, current * lowest)
		highest = max(highest, current)
		lowest = min(lowest, current)

	return highestProductOf3


