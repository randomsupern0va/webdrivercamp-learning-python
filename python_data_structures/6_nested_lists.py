#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def print_mat(matrix):
	for row in matrix:
		for item in row:  
			print(item, end=' ')
		print('\n')
				
	 
	
print_mat(matrix)
