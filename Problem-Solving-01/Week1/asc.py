import time

def V1(n):
    b = 0
    for i in n:
        if i == " ":
            pass
        else:
            a = ord(i)
            b += a
    return b
n = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

start = time.time()
print('answerV1:', V1(n))
print('timeV1:',(time.time()-start)*1000)