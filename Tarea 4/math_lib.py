#Universidad del Valle de Guatemala 
#Gráficos por computador 
#Gabriela Paola Contreras Guerra 20213
#Libreria Matematica a utilizar 

#Function use to create a matrix, these is used based on a list that conteins all the data that I want on my matrix
#also it allows me to set the size of the matrix 
def createMatrix(row, column, List):
    mat = []
    for i in range(row):
        rowList = []
        for j in range(column):
            rowList.append(List[row * i + j])
        mat.append(rowList)
    return mat

#Function use to muliply 2 matrix using a comprehenshion list 
def multiplyMatrix(A,B):
    result = [[(sum(a * b for a, b in zip(B_row, A_col)))
                            for A_col in zip(*B)]
                                for B_row in A]
    return result

#Funtion use to multiply a matrix and a vector and save the result on a list 
def matmulvec(Matrix, vector):
    if len(Matrix[0]) != len(vector):
        return None
    result = []
    
    for i in range(len(Matrix)):
        suma = 0
        for j in range(len(Matrix[0])):
            suma += Matrix[i][j]*vector[j]
        result.append(suma)

    return result


#Dot product that gets 2 vectors 
#multiply each value and add the product of each multiplication to get the product
def dotProduct(a,b):
    dotproduct =0
    for a,b in zip(a,b):
        dotproduct = dotproduct +a*b
        d = dotproduct
    return d

#Cross product of 2 vectors 
def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

#Substraction of vectors 
def subtract(a, b):
    result = [a[i] - b[i] for i in range(min(len(a), len(b)))]
    return result

#Function to get the length of the vector 
def normalize(v):
   length = pow(((v[0])**2 +(v[1])**2 +(v[2])**2 ),0.5)
   return length