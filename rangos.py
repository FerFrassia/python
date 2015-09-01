def condense_meeting_times(array_of_tuples):
	if len(array_of_tuples) > 1:
		for index, current in enumerate(array_of_tuples[:len(array_of_tuples - 1)]):
			if current[1] >= array_of_tuples[index + 1][0]
				current[1] = array_of_tuples[index + 1][1]
				del array_of_tuples[index + 1] 

	return array_of_tuples


