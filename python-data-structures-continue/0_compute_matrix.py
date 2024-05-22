#!/usr/bin/python3

def compute_matrix(matrix=[]):
	if not matrix:
		print("Matrix is empty")
		return

	sq_matrix = [[x**2 for x in row] for row in matrix]    
	
	return sq_matrix


if __name__=="__main__":
    matrix = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")
