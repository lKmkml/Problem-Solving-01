def main():
    line()
    sentence()
    word()
    ABC()
    big_letter()
    small_letter()
    non_letter()
    
def line():
    save = 0
    infile = open('Loop.txt','r')
    read = infile.read()
    infile.close()
    for i in read:
        if i =='\n':
            save +=1
        else:
            pass
    print("Number of line:",save)
    
def sentence():
    save = 0
    infile = open('Loop.txt','r')
    read = infile.read()
    infile.close()
    for i in read:
        if i ==".":
            save +=1
        else:
            pass
    print("Number of Sentence:",save)

def word():
    #save = 0
    infile = open('Loop.txt','r')
    read = infile.read()
    infile.close()
    read1 = read.split()
    #for i in read:
       # if i ==" ":
           # save += 1
       # else:
            #pass
    print("Number of Word:",len(read1))

def ABC():
    #ABCD =['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
    save = 0
    infile = open('Loop.txt','r')
    read = infile.read()
    infile.close()
    for i in read:
        if i.isalpha() == True:
            save += 1
        #else:
            #pass
    print("Number of Character:",save)

def big_letter():
    save = 0
    infile = open('Loop.txt','r')
    read = infile.read()
    infile.close()
    for i in read:
        if i.isupper()== True:
            save += 1
        else:
            pass
    print("Number of Big letter:",save)

def small_letter():
    save = 0
    infile = open('Loop.txt','r')
    read = infile.read()
    infile.close()
    for i in read:
        if i.islower()== True:
            save += 1
        else:
            pass
    print("Number of Small letter:",save)

def non_letter():
    non= ['.',',','/','(',')',';']
    save = 0
    infile = open('Loop.txt','r')
    read = infile.read()
    infile.close()
    for i in read:
        if i in non:
            save += 1
        else:
            pass
    print("Number of non letter:",save)
main()