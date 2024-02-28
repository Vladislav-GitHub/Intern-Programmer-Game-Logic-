# Вопрос №1
# На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 
# Пример: 
# def isEven(value):
#       return value % 2 == 0

def isEven(value):
    return value & 1 == 0


# Вопрос №2
# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
# Оценивается:
#     Полнота и качество реализации
#     Оформление кода
#     Наличие сравнения и пояснения по быстродействию

class Queue:
    def __init__(self):
        self.array = list()
        self.idx = 0
        
    def push(self, elem):
        self.array.append(elem)

    def pull(self):
        if self.array and any(self.array):
            elem = self.array[self.idx]
            self.array[self.idx] = None
            self.idx = (self.idx + 1) % len(self.array)
            return elem
        else:
            print("Пустая очередь, запушьте число.")

class FIFO(object):
    def __init__(self, size):
        self.idx = 0
        self.size = size
        self._array = []

    def push(self, elem):
        if len(self._array) == self.size:
            self._array[self.idx] = elem
        else:
            self._array.append(elem)
        self.idx = (self.idx + 1) % self.size

    def __getitem__(self, key):
        return(self._array[key])

    def __repr__(self):
        return self._array.__repr__()
    

# Вопрос №3
# На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция соответствует заданным критериям.

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        L, R = array[:mid], array[mid:]
        
        mergeSort(L)
        mergeSort(R)
        
        i, j, k = 0, 0, 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    
def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
    