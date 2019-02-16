import copy
import math
class Shape:
    MAXVALUE = 12

    def __init__(self,matrix):
        self.__shape=matrix
        self.__sumValues=0
        for row in matrix:
            for column in row:
                self.__sumValues+=column
            

    def preProcessing(self, matri):
        max = -1
        matrix=copy.deepcopy(matri)
        for row in matrix:
            for column in row:
                if column > max:
                    max = column
        increment = (Shape.MAXVALUE-max)/max
        increment += 1
        
        for row in matrix:
            for  i in range(0,len(row)):
                row[i] *= increment
                row[i]=int(row[i])
        return matrix
    
    """
    calcula la semejanza entre las matrices matrix y self.__shape
    calculando la matriz diferencia entre ellas, luego se suman los
    valores de esta matriz, para finalmente dividirlo por la suma de
    los valores en self.__shape
    """
    def calculateLikeness(self,matrix):
        matrixSubst=0
        for row in range(0,len(matrix)):
            for column in range(len(matrix[0])):
                matrixSubst+=math.fabs(matrix[row][column]-self.__shape[row][column])
        tmp= matrixSubst/self.__sumValues
        return 1-tmp
    """
        pinta la matriz de la forma 
        [
            [item,...,item-n],
            .
            .
            [item,...,item-n],
        ]
    """
    def print_matrix(self):
        print("[", end="")
        for i in range(0, len(self.__shape)-1):
            print(str(self.__shape[i])+",")
        print(str(self.__shape[len(self.__shape)-1]), end="")
        print("]")
            
        

"""def test():
    matrix=[
        [10,10,10],
        [1,10,1],
        [1,10,1]
    ]
    matrix1=[
        [9,3,8],
        [1,6,3],
        [0,7,1]
    ]
    shape=Shape(matrix)
    var=shape.preProcessing(matrix1)
    result=shape.calculateLikeness(var)
    print(result)

test()"""
