
b = "00110"

def parsePackedBCDS(inputBits):
    n = 4
    binvalues = [inputBits[i:i+n] for i in range(0, len(inputBits), n)]
    operators = {'1010' : '+', '1101' : '/'}     
    for binvalue in binvalues:
        if operators.get(binvalue) != None:
          print('\n',end ="")
          print(operators.get(binvalue))
        else:
          print(int(binvalue,2), end ="")

parsePackedBCDS('011000100000110100100000')
