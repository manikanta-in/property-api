#sstring: XYZ

#x, Y, Z
#xy,xz,yz
#xyz

def findSubstring(input):
    for i in range(len(input)):
        print(input[i])
        for j in range(len(input)):  
            if (j > i and j < len(input)) :
                print(input[i]+input[j])
    print(input)
        
      
            
findSubstring('xyz')


deploy 