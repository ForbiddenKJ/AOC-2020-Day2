from inputData import data
import os

data = data.split('\n')
counter = 0

def parseData(x):
    x = x.split(':')
    policy = x[0].split()
    range = policy[0].split('-')
    range = [int(i) for i in range]
    x = [range, policy[1], x[1].replace(' ','')]

    return x

def check(x):

    y = x[2].count(x[1])

    if y >= x[0][0] and y <= x[0][1]: return True

    return False

if __name__ == '__main__':
    data = [parseData(i) for i in data]
    for i in data:
        result = check(i)

        if result:
            counter+=1

        else:
            counter += 0


    print(counter)
