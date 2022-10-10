import time
import random

def initListWithRandomNumbers():

    rand_list=[]

    n = 1000000

    for _ in range(n):

        rand_list.append(random.randint(0,999))

    return rand_list


def calcSumm(arr):

    summ = 0

    for val in arr:

        summ = summ + val

    return summ


rand_list = initListWithRandomNumbers()



max_time = 0

min_time = 100

avg_time = 0

calc_count = 100
# starting time

for _ in range(calc_count):

    start = time.time()

    calcSumm(rand_list)

    # end time

    end = time.time()

    # total time taken

    total_time = end - start

    if total_time > max_time:

        max_time = total_time

    elif total_time < min_time:

        min_time = total_time

    avg_time += total_time

    

avg_time /= calc_count

print(f'Минимальное время работы calcSumm = {min_time}')
print(f'Максимальное время работы calcSumm = {max_time}')
print(f'Среднее время работы calcSumm = {avg_time}')

def calcHist(tdata):

#   hist is a List to store histogram. It contains [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    hist = [0]*10

    for data in tdata:

        hist[data // 100] += 1



    return hist

#   data contains List with size 1000 000 with 0 values

data = [0]*1000000

a = calcHist(rand_list)

print(a)