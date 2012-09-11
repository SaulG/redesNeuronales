import random
from sys import argv

def genera(tam, dim):
    output = open('datos.txt','w')
    for i in range(tam):
        st = ''
        for j in range(dim):
             st += str(random.uniform(-1,1))
             st += ' '
        print>>output, st
    
def main():
    print 'tamanio y dimension'
    genera(int(argv[1]),int(argv[2]))

main()
