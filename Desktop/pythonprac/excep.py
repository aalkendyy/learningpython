matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



def get_element(arr,r,c):
    try:
        return matrix[r][c]
    except IndexError:
        return "index error"



print(get_element(matrix, 1, 2)) 
print(get_element(matrix, 2, 3)) 






