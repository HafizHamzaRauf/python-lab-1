# *********************** TASK 1 ***********************


#   MATRIX MULTIPLICATION 
def input_Matrix():
    row= int(input("enter the no of rows of the matrix"))
    column = int(input("Enter the no of column of the matrix"))
    matrix=[]
    for i in range(row):
        print("\nEnter the elements for the row ",i+1)
        row_list = []
        for i in range(column):
          row_list.append(  int(input()))
        matrix.append(row_list)
    return matrix

def matrix_multiplication(matrix1,matrix2):
    #no of columns of matrix 1 should be equal to no of rows of matrix 2 otherwise multiplication is not possible
    if(len(matrix1[0])!=len(matrix2)):
        print("matrix cannot be multiplied")
    else:
        print("matrix can be multiplied")
        rows = len(matrix1)
        columns = len(matrix2[0])
        result = []
        for i in range(rows):
            row_list = []
            for j in range(columns):
                row_list.append(0)
            result.append(row_list)
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j]+=matrix1[i][k]*matrix2[k][j]
        print(result)


matrix_multiplication(input_Matrix(),input_Matrix())




