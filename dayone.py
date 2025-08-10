numbers = [2,4,4,3,6,1,1]

def mean_cal(numbers):
    mean = sum(numbers)/len(numbers)
    return mean


def median_cal(numbers):
    sort = sorted(numbers)
    num = len(numbers)
    if num % 2 == 0:
        median = (sort[num//2-1]+sort[num//2])/2
    else:
        median =sort[num//2]
    return median


def mode_cal(numbers):
    freq ={}
    for n in numbers:
        freq[n] = freq.get(n,0)+1
    
    mode = max(freq,key=freq.get)
    return mode

def std_cal(numbers):
    mean = mean_cal(numbers)
    diff =[(x - mean)** 2 for x in numbers]
    varience = sum(diff)/(len(numbers)-1)
    std = varience ** 0.5
    return std

mean = mean_cal(numbers)
median = median_cal(numbers)
mode = mode_cal(numbers)
std = std_cal(numbers)

print('Mean value is',mean)
print('Median value :',median)
print('mode is',mode)
print('Standard deviation is :',std)