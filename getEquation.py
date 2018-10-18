# Equation 
import re
def getEquation(e,dicName):
    operater = '[\+|\-|\/|\*|\(|\)]+'
    operaters=re.findall(operater,e)
    variables=re.split(operater, e)
    # print(operaters)    
    # print(variables)    
    ee=""
    if len(variables) >0 :
        # print(re.search("^"+operater,e))
        if re.search("^"+operater,e):
            ee=operaters.pop(0)
            variables.pop(0)
            print(variables)

        ee=ee+dicName+"[\""+variables.pop(0)+"\"]"

        for i in variables:
            if len(i)>0 :
                ee=ee+operaters.pop(0)+dicName+"[\""+i+"\"]"
        for i in operaters:
            ee=ee+i
    else:
        return "Fail : no operand"
    return ee
# 

if __name__ == '__main__':
    print(getEquation("(a+b)*c","rr"))  