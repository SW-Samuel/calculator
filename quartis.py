import numbers
import statistics
import numpy as np

quartis_number = []

def reset():
    global second_quartis
    
    second_quartis = 0
    quartis_number.clear()

def list_treatment(numbers):
    half = int((len(numbers)/2))

    if len(numbers)%2 != 0:
        numbers.pop(half)

    return numbers
   

def calculation_quartis(numbers):

    half_numbers = np.array_split(numbers,2)

    print(f"\n{half_numbers[0]}\t{half_numbers[1]}\n")
    
    for element in half_numbers:
        n = statistics.median(element)
        quartis_number.append(n)
    
    return quartis_number

def print_screen(quartis2, quartis13):
    print(f" Quartis 1: {quartis13[0]}")
    print(f" Quartis 2: {quartis2}")
    print(f" Quartis 3: {quartis13[1]}")

def operation_quartis(numbers):
    numbers.sort()
    print(numbers)

    second_quartis = statistics.median(numbers)

    numbers = list_treatment(numbers)

    quartis = calculation_quartis(numbers)

    print_screen(second_quartis,quartis)
