import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])

arr_2 = np.array([
    [5, 6],
    [7, 8]
])

arr_3 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr_4 = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

arr_5 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

arr_6 = np.array([
    [7, 8, 9],
    [1, 4, 7],
    [3, 6, 1],
    [5, 6, 7]
])

print(arr.shape)
print(arr_2.shape)
print(arr_3.shape)
print(arr_4.shape)
print(arr_5.shape)
print(arr_6.shape)

def addition(array, array_2):
    try:
        add = np.add(array, array_2)
        print(add)
    except ValueError as e:
        print(f"Error: Shape mismatch! {array.shape} and {array_2.shape} are incompatible.")

addition(arr, arr_2)
addition(arr_3, arr_4)

def subtraction(array, array_2):
    try:
        sub = np.subtract(array, array_2)
        print(sub)
    except ValueError as e:
        print(f"Error: Shape mismatch! {array.shape} and {array_2.shape} are incompatible.")

subtraction(arr, arr_5)
subtraction(arr_3, arr_4)

def scalar_multiplication(arr, num):
    multiplication = arr * num
    print(multiplication)

def elementwise_multiplication(arr, arr_2):
    try :
       multiplication = arr * arr_2
       print(multiplication)

    except ValueError as e :
        print(f"Error: Shape mismatch! {arr.shape} and {arr_2.shape} are incompatible.")



scalar_multiplication(arr_4 , 5)
scalar_multiplication(arr_5 , 2)
scalar_multiplication(arr_2 , 26)


elementwise_multiplication(arr_2 , arr)

elementwise_multiplication(arr_3, arr_4)


def matrix_multiplication(array,array_2) :

    try :
        multiplication  = array @ array_2
        print(multiplication)
    
    except Exception as e :
        print(f"Error: Shape mismatch! {array.shape} and {array_2.shape} are incompatible.")


matrix_multiplication(arr_4,arr_5)
matrix_multiplication(arr_5,arr_6)


def transpose(Array) :
    transposed = Array.T
    print(f"Shaped changed to  {transposed.shape}")
    print(f"Array after transpose : {transposed}")




transpose(arr_4)
transpose(arr_6)



def inverse_compatibility_check(array) :
    try :
       determinent = np.linalg.det(array)
       print(determinent)

       
    except np.linalg.LinAlgError:
        print("Error: The matrix must be square (same number of rows and columns).")
        return None
        

    except TypeError:
        print("Error: The matrix must contain only numbers.")
        return None


inverse_compatibility_check(arr)
inverse_compatibility_check(arr_6)



def inverse(array) :
    try :
        inversed = np.linalg.inv(array)
        print(inversed)

    except np.linalg.LinAlgError:
        print("Linear Algebra Error: Matrix is singular (determinant is 0) or not square.")
        return None
    



inverse(arr)
inverse(arr_5)

def identitys(array) :
    identity = np.eye(array)
    print(identity)


identitys(2)
identitys(4)


def traced(Array) :
    rows,columns = np.shape(Array)
    if rows == columns :
       trace = np.trace(Array)
       print(f"Trace of matrix: {trace}")
    else :
        print("Trace only works on square matrices")


traced(arr_4)
traced(arr_2)



def ranks(Array) :
    rank = np.linalg.matrix_rank(Array)
    print(f"Rank of matrix: {rank}")



ranks(arr_5)
ranks(arr_3)

