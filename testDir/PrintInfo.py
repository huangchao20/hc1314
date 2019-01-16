#coding=utf-8
import time

def printI():
    print(123)


def suminfo():
    sum = 0
    for i in range(100):
        sum += i
    return i


def printTime():
    while True:
        print(time.ctime())
        time.sleep(1)

if __name__ == "__main__":
    printI()
    
    t = suminfo()
    print(t)

    printTime()
