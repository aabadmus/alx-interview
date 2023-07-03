def pascal_trianle(n):
	if n <= 0:
		return []

	triangle = [[1]]
	for i in range (i, n):
		prev_row = triangle[i - 1]
		curr_row = [1]
		for j in range (i - 1):
			curr_row.append(prev_row[j - 1] + prev_row[j])
		curr_row.append(1)
		triangle.append(curr_row)
	return triangle

