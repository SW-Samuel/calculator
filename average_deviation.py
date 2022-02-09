import math

#global variable
sum_numbers = 0
average = 0
dm = []
variance_pot = []
desviationM = 0
variance = 0
desviationP = 0

def reset():
    global sum_numbers, average,  desviationM, variance, desviationP
    sum_numbers = 0
    average = 0
    dm.clear()
    variance_pot.clear()
    desviationM = 0
    variance = 0
    desviationP = 0

#
def calc_DM(numbers, amount):
    global desviationM
    global sum_numbers
    sum_numbers = 0

    for i in numbers:
        num = i - average
        
        if num < 0: num = num * -1
        
        sum_numbers = sum_numbers + num
        num = round(num,2)
        dm.append(num)

    desviationM = float(sum_numbers/amount)

def calc_variance(amount):
    global variance
    global sum_numbers
    sum_numbers = 0
    i=0
    
    while i<amount:
        pot = dm[i]*dm[i]
        pot = round(pot,2)
        variance_pot.append(pot)
        sum_numbers = sum_numbers + variance_pot[i]
        i+=1
    
    variance = sum_numbers/amount

def standard_deviation():
    global desviationP

    desviationP = float(variance ** 0.5)

def print_results(numbers,amount):
    i=0
    
    print(f"Média = {numbers}/{amount} = {average}")
    print("-----------------------------------")
    print(f"---------Desvio Médio-------------")
    print("-----------------------------------")
    while i<amount:
        print(f"DM = | {numbers[i]} - {average} | = {dm[i]:.2f}")
        i+=1

    print(f"Desvio médio = {dm}/{amount} = {desviationM:.2f}")

    print("-----------------------------------")
    print(f"------------Variância-------------")
    print("-----------------------------------")

    print(f"Variância = {variance_pot}/{amount} = {variance:.2f}")

    print("-----------------------------------")
    print(f"---------Desvio Padrão------------")
    print("-----------------------------------")

    print(f"+/- {desviationP:.2f}")


def operation_deviation(numbers, amount):
    global sum_numbers
    global average

    numbers.sort()

    for i in numbers:
        sum_numbers = sum_numbers + i
    
    average = sum_numbers/amount
    calc_DM(numbers, amount)
    calc_variance(amount)
    standard_deviation()
    print_results(numbers,amount)

    