from shape import Shape
import pathlib
from sklearn.datasets import load_digits
import pylab as pl
import sklearn



print(__name__)

array_evaluated_key = "array_evaluted"
successful_key= "successful"
total_evaluated_key = "total_evaluated"

digits = load_digits()
targets = digits.target

def load_number_file(number):
    file = open('./numbers/'+str(number)+'.txt')
    lines = file.read().splitlines()
    matrix = []
    for line in lines:
        pixels = line.split(',')
        array = []
        for item in pixels:
            array.append(float(item))
        matrix.append(array)
    return matrix

def list_filter(number1,targets):
    indices_list =[]
    for i in range(0,len(targets)):
        if targets[i]==number1:
            indices_list.append(i)
    return indices_list

#Corremos el test de un número
def run_test(number:int):

    """Cargamos las matrices a comparar"""
    matrix = load_number_file(number)

    """Cargamos y filtramos los indices de las imagenes donde estan los digitos"""
    
    indices_list = list_filter(number,targets)

    """Creamos los shapes"""
    shape= Shape(matrix)

    total_evaluated = len(indices_list)
    successful = 0

    array_evaluated_indices = []

    """Preparamos cada uno de los targets con el preprocesamiento"""
    for i in indices_list:
        
        preprocessed_matrix = shape.preProcessing(digits.images[i])
        result = shape.calculateLikeness(preprocessed_matrix) #Result es la probabilidad de que sea el número.
        #print("%s in %s where target was %s"% (result,i,targets[i]))
        if result >= 0.4:
            array_evaluated_indices.append(i)
            successful+=1
     
    return {
        array_evaluated_key:array_evaluated_indices,
        successful_key:successful,
        total_evaluated_key:total_evaluated
    }


result = run_test(4)
total_evaluated = result[total_evaluated_key]
successful = result[successful_key]
array_evaluated = result[array_evaluated_key]
rate = successful / total_evaluated


print("Test - 4 --> Rate of success was %s, with %s successful and %s evaluated " % (rate,successful,total_evaluated) )

result = run_test(7)
total_evaluated = result[total_evaluated_key]
successful = result[successful_key]
array_evaluated = result[array_evaluated_key]
rate = successful / total_evaluated


print("Test - 7 --> Rate of success was %s, with %s successful and %s evaluated " % (rate,successful,total_evaluated) )




    












