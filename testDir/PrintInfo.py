#coding=utf-8

def printI():
    print(123)


def suminfo():
    sum = 0
    for i in range(100):
        sum += i
    return i

if __name__ == "__main__":
    printI()
    
    t = suminfo()
    print(t)
