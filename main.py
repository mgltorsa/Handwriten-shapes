from shape import Shape
import pathlib
from sklearn.datasets import load_digits
import pylab as pl
import sklearn


class Main:

    RATE=0.5
    
    """
        Inicializa la clase main
    """
    def __init__(self):
        self.array_evaluated_key = "array_evaluted"
        self.successful_key = "successful"
        self.total_evaluated_key = "total_evaluated"
        self.digits=None
        self.targets=None  


    def load_default(self):
        self.digits = load_digits()
        self.targets = self.digits.target


    def load_number_file(self,number):
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


    def list_filter(self,number1, targets):
        indices_list = []
        for i in range(0, len(targets)):
            if targets[i] == number1:
                indices_list.append(i)
        return indices_list

    # Corremos el test de un número


    def run_test(self,number: int):
        """Cargamos las matrices a comparar"""
        matrix = self.load_number_file(number)

        """Cargamos y filtramos los indices de las imagenes donde estan los digitos"""

        indices_list = self.list_filter(number, self.targets)

        """Creamos los shapes"""
        shape = Shape(matrix)

        total_evaluated = len(indices_list)
        successful = 0

        array_evaluated_indices = []

        """Preparamos cada uno de los targets con el preprocesamiento"""
        for i in indices_list:

            preprocessed_matrix = shape.preProcessing(self.digits.images[i])
            # Result es la probabilidad de que sea el número.
            result = shape.calculateLikeness(preprocessed_matrix)
            #print("%s in %s where target was %s"% (result,i,targets[i]))
            if result >= Main.RATE:
                array_evaluated_indices.append(i)
                successful += 1
            
            """print(self.digits.images[i])
            shape.print_matrix()"""

        return {
            self.array_evaluated_key: array_evaluated_indices,
            self.successful_key: successful,
            self.total_evaluated_key: total_evaluated
        }

    # PARA PINTAR MATRIX


    def print_matrix(self,matrix):
        print("[", end="")
        for i in range(0, len(matrix)-1):
            print(str(matrix[i])+",")
        print(str(matrix[len(matrix)-1]), end="")
        print("]")
        
    def test_number(self,number):
        result = self.run_test(number)
        total_evaluated = result[self.total_evaluated_key]
        successful = result[self.successful_key]
        array_evaluated = result[self.array_evaluated_key]
        rate = successful/total_evaluated
        return "Test - %s --> Rate of success was %s, with %s successful and %s evaluated " % (number,rate,successful,total_evaluated)
    


##FIN DEL MAIN CLASS


main = Main()

main.load_default()


print("Solo ingrese el 4 o el 7")

number = int(input("Ingrese número a probar: "))

print(main.test_number(number))


number = int(input("Ingrese número a probar: "))

print(main.test_number(number))
