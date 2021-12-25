import numpy as np
import random as r
import matplotlib.pyplot as plt
from random import randint
import math as m
#import plotly.express as px

def randomsearch():
    def genfunct(equation):
        signs = ["+","-","*","/","m.sin","m.cos","x"]
        a2 = randint(0,1000) % randint(1,5)
        equation[1] = signs[a2]

        for i in range(513):
            #print(i)
            if (equation[i] != "+" and equation[i] != "-" and equation[i] != "*" and equation[i] != "/" and equation[i] != "m.sin" and equation[i] != "m.cos"):
                continue
            if (equation[i] == "m.sin" or equation[i] == "m.cos"):
                if (i >= 128 and i <= 255):
                    a3 = randint(0,1000) % 2
                    if (a3 == 0):
                        equation[i*2] = "x"
                    else:
                        value = randint(0,10000) % randint(1,7000)
                        digit = float(value/1000.000)
                        num = str(digit)
                        equation[i*2] = num
                else:
                    a1 = randint(0,1000) % randint(1,4)
                    if a1 < 2:
                        a2 = randint(0,1000) % randint(1,6)
                        #print("the random digit is ",a2)
                        equation[i*2] = signs[a2]
                    else:
                        a3 = randint(0,1000) % 2
                        #print("the random digit is ",a3)
                        if a3 == 0:
                            equation[i*2] = "x"
                        else:
                            value = randint(0,10000) % randint(1,7000)
                            digit = float(value/1000.000)
                            num = str(digit)
                            equation[i*2] = num
            else:
                if (i >= 128 and i <= 255):
                    for j in range(2):
                        a3 = randint(0,1000) % 2
                        #print("the random digit is ",a3)
                        if a3 == 0:
                            equation[i*2+j] = "x"
                        else:
                            value = randint(0,10000) % randint(1,7000)
                            digit = float(value/1000.000)
                            num = str(digit)
                            equation[i*2+j] = num
                else:
                    for j in range(2):
                        a1 = randint(0,1000) % randint(1,4)
                        #print("the random digit is ",a2)
                        if a1 < 2:
                            a2 = randint(0,1000) % randint(1,6)
                            #print("the random digit is ",a1)
                            equation[i*2+j] = signs[a2]
                        else:
                            a3 = randint(0,1000) % 2
                            #print("the random digit is ",a3)
                            if a3 == 0:
                                equation[i*2+j] = "x"
                            else:
                                value = int(randint(0,1000)) % randint(1,7000)
                                digit = float(value/1000.000)
                                num = str(digit)
                                equation[i*2+j] = num

    def showfunct(i, funct):
        closepar = ")"
        openpar = "("
    
        if funct[i] == "":
            True
        elif funct[i] == "m.sin" or funct[i] == "m.cos":
            actfunc.append(funct[i])
            actfunc.append(openpar)
            showfunct(i*2, funct)
            actfunc.append(closepar)
        elif (funct[i] == "+" or funct[i] == "-" or funct[i] == "*" or funct[i] == "/"):
            actfunc.append(openpar)
            showfunct(i*2,funct)
            actfunc.append(funct[i])
            showfunct(i*2+1,funct)
            actfunc.append(closepar)
        else:
            actfunc.append(funct[i])
        return actfunc

    def calcfunct(value,funct):
        calc = []
        for j in range(513):
            calc.append(float(1.00))

        i = 512
        while i > 0:
            if funct[i] == "":
                i -= 1
                continue
            elif funct[i] == "x":
                calc[i] = value
            elif funct[i] == "m.sin":
                temp = float(np.sin(calc[i*2]))
            elif funct[i] == "m.cos":
                temp = float(np.cos(calc[i*2]))
            elif funct[i] == "+":
                temp = float(calc[i*2] + calc[i*2+1])
                calc[i] = temp
            elif funct[i] == "-":
                temp = float(calc[i*2] + calc[i*2+1])
                calc[i] = temp
            elif funct[i] == "*":
                temp = float(calc[i*2] * calc[i*2+1])
                calc[i] = temp
            elif funct[i] == "/":
                if calc[i*2+1] == 0:
                    calc[i] = 10000
                else:
                    temp = float(calc[i*2] / calc[i*2+1])
                    calc[i] = temp       
            else:
                num = str(funct[i])
                temp = float(num)
                calc[i] = temp
        
            i -= 1
        return calc[1]

    def removebranch(i, funct):
        if funct[i] == "":
            True
        elif (funct[i] == "m.sin" or funct[i] == "m.cos"):
            removebranch(i*2, funct)
            funct[i] = ""
        elif (funct[i] == "+" or funct[i] == "-" or funct[i] == "*" or funct[i] == "/"):
            removebranch(i*2, funct)
            removebranch(i*2+1, funct)
            funct[i] = ""
        else:
            funct[i] = ""

    def evalfunct(xvalue, yvalue, length, funct):
        add = 0
        for i in range(length):
            ypoint = float(calcfunct(xvalue[i], funct))
            diff = float(yvalue[i]-ypoint)
            add += diff * diff
        return add/length

    length = 1000
    xpoints = []
    ypoints = []
    equation = []
    optequation = []
    optiter = 0
    opterr = float(1000)
    actfunc = []
    errors = []
    iterations = 10
    xiter = []
    converror = 20
    convind = 0
    convx = []
    convperc = []

    file = open(r'data.txt')

    for i in file:
        row = i.split(', ')
        xcoord = float(row[0])
        ycoord = float(row[1])
        xpoints.append(xcoord)
        ypoints.append(ycoord)

    for i in range(513):
        equation.append("")

    for i in range(513):
        optequation.append("")

    print("Starting Random Search")
    for k in range(10):
        optiter = 0
        opterr = float(50.00)
        for i in range(iterations):
            removebranch(1,equation)
            genfunct(equation)
            err = float(evalfunct(xpoints,ypoints,length,equation))
            convx.append(convind)
            convind += 1
            if err > converror:
                convperc.append(0)
            else:
                convperc.append(1)
                converror = 5E25
            if err < opterr:
                opterr = err
                optiter = i+1
                errors.append(err)
                print(err)
                for j in range(513):
                    optequation[j] = equation[j]
            else:
                errors.append(opterr)
            
            xiter.append(i)
            
        realfunc = showfunct(1,optequation)

    eqfit = ''

    for i in range(0,len(realfunc)-1):
        if realfunc[i] == "/" and realfunc[i+1] == "0":
            realfunc[i] = "+"

    for i in realfunc:
        eqfit += i
    
    print("RS Optimum equation:", eqfit)
    print(" Found at iteration " + str(optiter) + " with err " + str(opterr))
    yfitted = []  

    for x in xpoints:
        yfitted.append(eval(str(eqfit)))
    
    return xpoints, ypoints, yfitted, errors, xiter, convx, convperc, iterations

def RHMC():
    def genfunct(equation):
        signs = ["+","-","*","/","m.sin","m.cos","x"]
        a2 = randint(0,1000) % randint(1,5)
        equation[1] = signs[a2]

        for i in range(513):
            if (equation[i] != "+" and equation[i] != "-" and equation[i] != "*" and equation[i] != "/" and equation[i] != "m.sin" and equation[i] != "m.cos"):
                continue
            if (equation[i] == "m.sin" or equation[i] == "m.cos"):
                if (i >= 128 and i <= 255):
                    a3 = randint(0,1000) % 2
                    if (a3 == 0):
                        equation[i*2] = "x"
                    else:
                        value = randint(0,10000) % randint(1,7000)
                        digit = float(value/1000.000)
                        num = str(digit)
                        equation[i*2] = num
                else:
                    a1 = randint(0,1000) % randint(1,4)
                    if a1 < 2:
                        a2 = randint(0,1000) % randint(1,6)
                        #print("the random digit is ",a2)
                        equation[i*2] = signs[a2]
                    else:
                        a3 = randint(0,1000) % 2
                        #print("the random digit is ",a3)
                        if a3 == 0:
                            equation[i*2] = "x"
                        else:
                            value = randint(0,10000) % randint(1,7000)
                            digit = float(value/1000.000)
                            num = str(digit)
                            equation[i*2] = num
            else:
                if (i >= 128 and i <= 255):
                    for j in range(2):
                        a3 = randint(0,1000) % 2
                        #print("the random digit is ",a3)
                        if a3 == 0:
                            equation[i*2+j] = "x"
                        else:
                            value = randint(0,10000) % randint(1,7000)
                            digit = float(value/1000.000)
                            num = str(digit)
                            equation[i*2+j] = num
                else:
                    for j in range(2):
                        a1 = randint(0,1000) % randint(1,4)
                        #print("the random digit is ",a2)
                        if a1 < 2:
                            a2 = randint(0,1000) % randint(1,6)
                            #print("the random digit is ",a1)
                            equation[i*2+j] = signs[a2]
                        else:
                            a3 = randint(0,1000) % 2
                            #print("the random digit is ",a3)
                            if a3 == 0:
                                equation[i*2+j] = "x"
                            else:
                                value = int(randint(0,1000)) % randint(1,7000)
                                digit = float(value/1000.000)
                                num = str(digit)
                                equation[i*2+j] = num

    def showfunct(i, funct):
        closepar = ")"
        openpar = "("
    
        if funct[i] == "":
            True
        elif funct[i] == "m.sin" or funct[i] == "m.cos":
            actfunc.append(funct[i])
            actfunc.append(openpar)
            showfunct(i*2, funct)
            actfunc.append(closepar)
        elif (funct[i] == "+" or funct[i] == "-" or funct[i] == "*" or funct[i] == "/"):
            actfunc.append(openpar)
            showfunct(i*2,funct)
            actfunc.append(funct[i])
            showfunct(i*2+1,funct)
            actfunc.append(closepar)
        else:
            actfunc.append(funct[i])
        return actfunc

    def calcfunct(value,funct):
        calc = []
        for j in range(513):
            calc.append(float(1.00))

        i = 512
        while i > 0:
            if funct[i] == "":
                i -= 1
                continue
            elif funct[i] == "x":
                calc[i] = value
            elif funct[i] == "m.sin":
                temp = float(np.sin(calc[i*2]))
            elif funct[i] == "m.cos":
                temp = float(np.cos(calc[i*2]))
            elif funct[i] == "+":
                temp = float(calc[i*2] + calc[i*2+1])
                calc[i] = temp
            elif funct[i] == "-":
                temp = float(calc[i*2] + calc[i*2+1])
                calc[i] = temp
            elif funct[i] == "*":
                temp = float(calc[i*2] * calc[i*2+1])
                calc[i] = temp
            elif funct[i] == "/":
                if calc[i*2+1] == 0:
                    calc[i] = 10000
                else:
                    temp = float(calc[i*2] / calc[i*2+1])
                    calc[i] = temp       
            else:
                num = str(funct[i])
                temp = float(num)
                calc[i] = temp
        
            i -= 1
        return calc[1]

    def removebranch(i, funct):
        if funct[i] == "":
            True
        elif (funct[i] == "m.sin" or funct[i] == "m.cos"):
            removebranch(i*2, funct)
            funct[i] = ""
        elif (funct[i] == "+" or funct[i] == "-" or funct[i] == "*" or funct[i] == "/"):
            removebranch(i*2, funct)
            removebranch(i*2+1, funct)
            funct[i] = ""
        else:
            funct[i] = ""

    def evalfunct(xvalue, yvalue, length, funct):
        add = 0
        for i in range(length):
            ypoint = float(calcfunct(xvalue[i], funct))
            diff = float(yvalue[i]-ypoint)
            add += diff * diff
        return add/length

    print("Starting Random Search")

    length = 1000
    xpoints = []
    ypoints = []
    equation = []
    optequation = []
    optiter = 0
    opterr = float(100000)
    actfunc = []
    errors = []
    iterations = 10
    population = []
    binarytrees = []
    xiter = []
    poperrs = []
    complengths = []


    file = open(r'data.txt')

    for i in file:
        row = i.split(', ')
        xcoord = float(row[0])
        ycoord = float(row[1])
        xpoints.append(xcoord)
        ypoints.append(ycoord)

    for i in range(513):
        equation.append("")

    for i in range(513):
        optequation.append("")

    for k in range(10):
        optiter = 0
        opterr = float(50.00)
        for i in range(iterations):
            removebranch(1,equation)
            genfunct(equation)
            err = float(evalfunct(xpoints,ypoints,length,equation))
            if err < opterr:
                poperrs.append(err)
                eqlen = 0
                for x in range(0,len(equation)):
                    if equation[x] != '':
                        eqlen += 1
                complengths.append(eqlen)
                opterr = err
                optiter = i+1
                errors.append(err)
                print(err)
                for j in range(513):
                    optequation[j] = equation[j]
            else:
                errors.append(opterr)
            
            xiter.append(i)

        binarytrees.append(optequation)
        realfunc = showfunct(1,optequation)
        population.append(realfunc)


    eqfit = ''
    for i in range(0,len(realfunc)-1):
        if realfunc[i] == "/" and realfunc[i+1] == "0":
            realfunc[i] = "+"

    for i in realfunc:
        eqfit += i
        
    yfitted = []  

    print("The RS Optimum Equation for HC is: ", eqfit)
    print(" Found at iteration " + str(optiter) + " with err " + str(opterr))

    for x in xpoints:
        yfitted.append(eval(str(eqfit)))
        

    print("Starting Hill Climber")

    hclength = len(optequation)
    hciterations = 10
    hcoptequation = []
    hcxiter = []
    hcerrors = []
    hceqfit = ""
    hcopterr = float(1000)
    actfunc = []
    stderror = 20


    for i in range(513):
        hcoptequation.append("")

    for k in  range(hciterations):
        ind = 0
        for i in optequation:
            if "1" in i:
                i = float(i)
                choice = r.randint(0,1)
                if choice == 0:
                    i = i - r.uniform(0,0.2)
                else:
                    i = i + r.uniform(0,0.2)
                i = str(i)
                optequation[ind] = i
                ind += 1  
            elif "3" in i:
                i = float(i)
                choice = r.randint(0,1)
                if choice == 0:
                    i = i - r.uniform(0,0.2)
                else:
                    i = i + r.uniform(0,0.2)
                i = str(i)
                optequation[ind] = i
                ind += 1  
            elif "5" in i:
                i = float(i)
                choice = r.randint(0,1)
                if choice == 0:
                    i = i - r.uniform(0,0.2)
                else:
                    i = i + r.uniform(0,0.2)
                i = str(i)
                optequation[ind] = i
                ind += 1  
            elif "7" in i:
                i = float(i)
                choice = r.randint(0,1)
                if choice == 0:
                    i = i - r.uniform(0,0.2)
                else:
                    i = i + r.uniform(0,0.2)
                i = str(i)
                optequation[ind] = i
                ind += 1  
            elif "9" in i:
                i = float(i)
                choice = r.randint(0,1)
                if choice == 0:
                    i = i - r.uniform(0,0.2)
                else:
                    i = i + r.uniform(0,0.2)
                i = str(i)
                optequation[ind] = i
                ind += 1   
            else:
                ind += 1
                

        hcerr = float(evalfunct(xpoints,ypoints,length,optequation))
        
        if hcerr < stderror:
            poperrs.append(err)
            eqlen = 0
            for x in range(0,len(optequation)-1):
                if optequation[x] != '':
                    eqlen += 1
            complengths.append(eqlen)

        if hcerr < hcopterr:
            hcopterr = hcerr
            optiter = k+1
            hcerrors.append(hcerr)
            print("The HC error is: ", hcerr)
            for j in range(513):
                hcoptequation[j] = optequation[j]
        else:
            hcerrors.append(hcopterr)
            
        hcxiter.append(k)
     

    hcrealfunc = showfunct(1,hcoptequation)

    for i in range(0,len(hcrealfunc)-1):
        if hcrealfunc[i] == "/" and hcrealfunc[i+1] == "0":
            hcrealfunc[i] = "+"

    for i in hcrealfunc:
        hceqfit += i

    print("The HC Optimum Equation is: ", hceqfit)


    hcyfitted = []
    for x in xpoints:
        hcyfitted.append(eval(str(hceqfit)))

    return xpoints, ypoints, hcyfitted, hcerrors, hcxiter, poperrs, complengths, hciterations

def GA():
    def crossover(population, bintree):
    # population is ordered, bintree is binary tree ordered
        popcount = len(population)
        for i in range(0, popcount - 1):
            if i % 2 == 1:
                continue
            else:
                # Selecting random index for operator and checking
                treelength1 = len(population[i])
                treelength2 = len(population[i])
            
                for e in range(0, treelength1):
                    rind1 = r.randint(0, treelength1)
                    print(population[e])
                    if population[e][rind1] == "+" or population[e][rind1] == "-" or population[e][rind1] == "*" or population[e][rind1] ==  "/":
                        ind1 = rind1            # operator found, stop searching and send index
                        break
                    else:
                        continue
                
                for j in range(0, treelength2):
                    rind2 = r.randint(0, treelength2)
                    if population[j][rind2] == "+" or population[j][rind2] == "-" or population[j][rind2] == "*" or population[j][rind2] ==  "/":
                        ind2 = rind2            # operator found, stop searching and send index
                        break
                    else:
                        continue
                
                # add original equations of children up to index for error calculations
                # bin1, bin2 = binary tree array of children 1 and 2
                # child1 = init1 + final2, child2 = init2 + final1
            
                bin1, bin2 = [], []
                for x in range(0, ind1-1): 
                    bin1.append(bintree[i][x])
                
                for x in range(0, ind2-1):
                    bin2.append(bintree[i][x])
                
                for y in range(ind1, len(bintree[i])):
                    bin2.append(bintree[i][y])
                    
                for y in range(ind2, len(bintree[i+1])):
                    bin1.append(bintree[i][y])
                
                bintree.append(bin1)
                bintree.append(bin2)
            
                

                # Get ordered equation, split into before (init) and after (final) operator index
                init1, final1, opind1 = diverge(population[i], ind1)
                init2, final2, opind2 = diverge(population[i+1], ind2)
            
                # Crossover, child1 = init1 + final2, child2 = init2 + final1
                child1, child2 = [], []
                for i in range(0, len(init1)):
                    child1.append(init1[i])
                    
                for i in range(0, len(final2)):
                    child1.append(final2[i])
                    
                for i in range(0, len(init2)):
                    child2.append(init2[i])
            
                for i in range(0, len(final1)):
                    child2.append(final1[i])
                
                # children are ordered arrays, add them to population
                population.append(child1)
                population.append(child2)
            
                # return new ordered population and binary tree population        
        return population, bintree

    def diverge(equation, index):
    
    # input binary tree array equation, output 2 ordered halfs
        init, index = orderedstop(0, equation, index - 1)
        final = showfunct(index,equation)
    
        return init, final, index
    
    def orderedstop(i, funct, endindex):
        if i == endindex:
            return actfunc
    
        orderindex = 0
        closepar = ")"
        openpar = "("
    
        if funct[i] == "":
            True
        elif funct[i] == "m.sin" or funct[i] == "m.cos":
            actfunc.append(funct[i])
            orderindex += 1
            actfunc.append(openpar)
            orderindex += 1
            orderedstop(i*2, funct, endindex)
            actfunc.append(closepar)
            orderindex += 1
        elif (funct[i] == "+" or funct[i] == "-" or funct[i] == "*" or funct[i] == "/"):
            actfunc.append(openpar)
            orderindex += 1
            orderedstop(i*2, funct, endindex)
            actfunc.append(funct[i])
            orderindex += 1
            orderedstop(i*2+1, funct, endindex)
            actfunc.append(closepar)
            orderindex += 1
        else:
            actfunc.append(funct[i])
            orderindex += 1
            
        return actfunc, orderindex


    def genfunct(equation):
        signs = ["+","-","*","/","m.sin","m.cos","x"]
        a2 = randint(0,1000) % randint(1,5)
        equation[1] = signs[a2]

        for i in range(513):
            if (equation[i] != "+" and equation[i] != "-" and equation[i] != "*" and equation[i] != "/" and equation[i] != "m.sin" and equation[i] != "m.cos"):
                continue
            if (equation[i] == "m.sin" or equation[i] == "m.cos"):
                if (i >= 128 and i <= 255):
                    a3 = randint(0,1000) % 2
                    if (a3 == 0):
                        equation[i*2] = "x"
                    else:
                        value = randint(0,10000) % randint(1,7000)
                        digit = float(value/1000.000)
                        num = str(digit)
                        equation[i*2] = num
                else:
                    a1 = randint(0,1000) % randint(1,4)
                    if a1 < 2:
                        a2 = randint(0,1000) % randint(1,6)
                        #print("the random digit is ",a2)
                        equation[i*2] = signs[a2]
                    else:
                        a3 = randint(0,1000) % 2
                        #print("the random digit is ",a3)
                        if a3 == 0:
                            equation[i*2] = "x"
                        else:
                            value = randint(0,10000) % randint(1,7000)
                            digit = float(value/1000.000)
                            num = str(digit)
                            equation[i*2] = num
            else:
                if (i >= 128 and i <= 255):
                    for j in range(2):
                        a3 = randint(0,1000) % 2
                        #print("the random digit is ",a3)
                        if a3 == 0:
                            equation[i*2+j] = "x"
                        else:
                            value = randint(0,10000) % randint(1,7000)
                            digit = float(value/1000.000)
                            num = str(digit)
                            equation[i*2+j] = num
                else:
                    for j in range(2):
                        a1 = randint(0,1000) % randint(1,4)
                        #print("the random digit is ",a2)
                        if a1 < 2:
                            a2 = randint(0,1000) % randint(1,6)
                            #print("the random digit is ",a1)
                            equation[i*2+j] = signs[a2]
                        else:
                            a3 = randint(0,1000) % 2
                            #print("the random digit is ",a3)
                            if a3 == 0:
                                equation[i*2+j] = "x"
                            else:
                                value = int(randint(0,1000)) % randint(1,7000)
                                digit = float(value/1000.000)
                                num = str(digit)
                                equation[i*2+j] = num

    def showfunct(i, funct):
        closepar = ")"
        openpar = "("
    
        if funct[i] == "":
            True
        elif funct[i] == "m.sin" or funct[i] == "m.cos":
            actfunc.append(funct[i])
            actfunc.append(openpar)
            showfunct(i*2, funct)
            actfunc.append(closepar)
        elif (funct[i] == "+" or funct[i] == "-" or funct[i] == "*" or funct[i] == "/"):
            actfunc.append(openpar)
            showfunct(i*2,funct)
            actfunc.append(funct[i])
            showfunct(i*2+1,funct)
            actfunc.append(closepar)
        else:
            actfunc.append(funct[i])
        return actfunc

    def calcfunct(value,funct):
        calc = []
        for j in range(513):
            calc.append(float(1.00))

        i = 512
        while i > 0:
            if funct[i] == "":
                i -= 1
                continue
            elif funct[i] == "x":
                calc[i] = value
            elif funct[i] == "m.sin":
                temp = float(np.sin(calc[i*2]))
            elif funct[i] == "m.cos":
                temp = float(np.cos(calc[i*2]))
            elif funct[i] == "+":
                temp = float(calc[i*2] + calc[i*2+1])
                calc[i] = temp
            elif funct[i] == "-":
                temp = float(calc[i*2] + calc[i*2+1])
                calc[i] = temp
            elif funct[i] == "*":
                temp = float(calc[i*2] * calc[i*2+1])
                calc[i] = temp
            elif funct[i] == "/":
                if calc[i*2+1] == 0:
                    calc[i] = 10000
                else:
                    temp = float(calc[i*2] / calc[i*2+1])
                    calc[i] = temp       
            else:
                num = str(funct[i])
                temp = float(num)
                calc[i] = temp
        
            i -= 1
        return calc[1]

    def removebranch(i, funct):
        if funct[i] == "":
            True
        elif (funct[i] == "m.sin" or funct[i] == "m.cos"):
            removebranch(i*2, funct)
            funct[i] = ""
        elif (funct[i] == "+" or funct[i] == "-" or funct[i] == "*" or funct[i] == "/"):
            removebranch(i*2, funct)
            removebranch(i*2+1, funct)
            funct[i] = ""
        else:
            funct[i] = ""

    def evalfunct(xvalue, yvalue, length, funct):
        add = 0
        for i in range(length):
            ypoint = float(calcfunct(xvalue[i], funct))
            diff = float(yvalue[i]-ypoint)
            add += diff * diff
        return add/length

    print("Starting Random Search")

    length = 1000
    xpoints = []
    ypoints = []
    equation = []
    optequation = []
    optiter = 0
    opterr = float(100000)
    actfunc = []
    errors = []
    iterations = 10
    population = []
    xiter = []
    poperrs = []
    complengths = []


    file = open(r'data.txt')

    for i in file:
        row = i.split(', ')
        xcoord = float(row[0])
        ycoord = float(row[1])
        xpoints.append(xcoord)
        ypoints.append(ycoord)

    for i in range(513):
        equation.append("")

    for i in range(513):
        optequation.append("")

    for k in range(10):
        optiter = 0
        opterr = float(50.00)
        for i in range(iterations):
            removebranch(1,equation)
            genfunct(equation)
            err = float(evalfunct(xpoints,ypoints,length,equation))
            if err < opterr:
                poperrs.append(err)
                eqlen = 0
                for x in range(0,len(equation)):
                    if equation[x] != '':
                        eqlen += 1
                complengths.append(eqlen)
                opterr = err
                optiter = i+1
                errors.append(err)
                print(err)
                for j in range(513):
                    optequation[j] = equation[j]
            else:
                errors.append(opterr)
            
            xiter.append(i)

        population.append(optequation)
        realfunc = showfunct(1,optequation)


    eqfit = ''
    for i in range(0,len(realfunc)-1):
        if realfunc[i] == "/" and realfunc[i+1] == "0":
            realfunc[i] = "+"

    for i in realfunc:
        eqfit += i
        
    yfitted = []  

    print("The RS Optimum Equation for HC is: ", eqfit)
    print(" Found at iteration " + str(optiter) + " with err " + str(opterr))

    for x in xpoints:
        yfitted.append(eval(str(eqfit)))
        

    print("Starting Hill Climber")

    hclength = len(optequation)
    hcoptequation = []
    hciterations = 10
    hcxiter = []
    hcerrors = []
    hceqfit = ""
    hcopterr = float(1000)
    actfunc = []
    stderror = 20


    for i in range(513):
        hcoptequation.append("")

    for k in  range(hciterations):
        ind = 0
        for i in optequation:
            if "1" in i:
                i = float(i)
                choice = r.randint(0,1)
                if choice == 0:
                    i = i - r.uniform(0,0.2)
                else:
                    i = i + r.uniform(0,0.2)
                i = str(i)
                optequation[ind] = i
                ind += 1  
            elif "3" in i:
                i = float(i)
                choice = r.randint(0,1)
                if choice == 0:
                    i = i - r.uniform(0,0.2)
                else:
                    i = i + r.uniform(0,0.2)
                i = str(i)
                optequation[ind] = i
                ind += 1  
            elif "5" in i:
                i = float(i)
                choice = r.randint(0,1)
                if choice == 0:
                    i = i - r.uniform(0,0.2)
                else:
                    i = i + r.uniform(0,0.2)
                i = str(i)
                optequation[ind] = i
                ind += 1  
            elif "7" in i:
                i = float(i)
                choice = r.randint(0,1)
                if choice == 0:
                    i = i - r.uniform(0,0.2)
                else:
                    i = i + r.uniform(0,0.2)
                i = str(i)
                optequation[ind] = i
                ind += 1  
            elif "9" in i:
                i = float(i)
                choice = r.randint(0,1)
                if choice == 0:
                    i = i - r.uniform(0,0.2)
                else:
                    i = i + r.uniform(0,0.2)
                i = str(i)
                optequation[ind] = i
                ind += 1   
            else:
                ind += 1
                

        hcerr = float(evalfunct(xpoints,ypoints,length,optequation))
        
        if hcerr < stderror:
            poperrs.append(err)
            eqlen = 0
            for x in range(0,len(optequation)-1):
                if optequation[x] != '':
                    eqlen += 1
            complengths.append(eqlen)

        if hcerr < hcopterr:
            hcopterr = hcerr
            optiter = k+1
            hcerrors.append(hcerr)
            print("The HC error is: ", hcerr)
            for j in range(513):
                hcoptequation[j] = optequation[j]
        else:
            hcerrors.append(hcopterr)
            
        hcxiter.append(k)
     

    hcrealfunc = showfunct(1,hcoptequation)

    for i in range(0,len(hcrealfunc)-1):
        if hcrealfunc[i] == "/" and hcrealfunc[i+1] == "0":
            hcrealfunc[i] = "+"

    for i in hcrealfunc:
        hceqfit += i

    print("The HC Optimum Equation is: ", hceqfit)


    hcyfitted = []
    for x in xpoints:
        hcyfitted.append(eval(str(hceqfit)))
        
    # Send a population of 10 to create 10 more children and add them
    population, bintree = crossover(population, binarytrees)

    # Remove 10 biggest errors from population
    poperrs = []
    for i in length(0,len(bintree)):
        err = float(evalfunct(xpoints,ypoints,length,bintree[i]))
        poperrs.append(err)
    
    print(poperrs)

    # order population from lowest error to greatest
    sortedpop = [i[0] for i in sorted(enumerate(poperrs), key=lambda x:x[1])]
    print(sortedpop)

    # keep 5 best errors in population
    for i in range(len(sortedpop)-1,4,-1):
        del sortedpop[i-1]

    print(sortedpop)

    ind = 0

    for i in sortedpop:
        bintree[ind] = bintree[i]
        population[ind] = population[i]
        ind +=1
   
    #print(population)

    for i in range(len(population),5,-1):
        del population[i-1]
        del bintree[i-1]
        
    print(population)

    return xpoints, ypoints, hcyfitted, hcerrors, hcxiter, poperrs, complengths, hciterations

xpoints, ypoints, yfitted, rserrors, rsxiter, convx, convperc, rsiterations = randomsearch()
xpoints, ypoints, hcyfitted, hcerrors, hcxiter, poperrs, complengths, hciterations = RHMC()
xpoints2, ypoints2, hcyfitted2, hcerrors2, hcxiter2, poperrs2, complengths2, hciterations = RHMC()

RS_yval = []
HC_yval = []
RS_stdss = []
HC_stdss = []
GA_yval = []
GA_stdss = []




############ Calculating the errors for each method ##############
for i in range(0,int(rsiterations/10)-1):
    RS_stdss.append(rserrors[i])

RS_std = np.std(RS_stdss)
#print(RS_std)
RS_error = (RS_std/(np.sqrt(rsiterations)))
print(RS_error)

xval = np.arange(0.1,rsiterations,rsiterations/10)
for i in range(rsiterations):
    if i % (rsiterations/10) == 0:
        RS_yval.append(rserrors[i])

for i in range(0,int(hciterations/10)-1):
    HC_stdss.append(hcerrors[i])

HC_std = np.std(HC_stdss)
#print(HC_std)
HC_error = 20*(HC_std/(np.sqrt(hciterations)))
print(HC_error)
for i in range(hciterations):
    if i % (hciterations/10) == 0:
        HC_yval.append(hcerrors[i])


plt.figure(1)
plt.plot(xpoints,yfitted,label='RS')
plt.plot(xpoints, ypoints, label='Data')
plt.plot(xpoints,hcyfitted, label='RMHC')
plt.legend()
plt.ylim(-10,25)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Analytical Solution vs Data")
plt.show()

plt.figure(2)
plt.plot(rsxiter,rserrors,label="RS Error")
plt.errorbar(xval,RS_yval,yerr=RS_error,linestyle='')
plt.plot(hcxiter,hcerrors,label="RMHC Error")
plt.errorbar(xval,HC_yval,yerr=HC_error,linestyle='')
plt.legend()
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.title("Fitness Curve")
plt.show()

plt.figure(3)
plt.plot(convx,convperc)
plt.xlabel("Iterations")
plt.ylabel("Convergence")
plt.title("Random Search Convergence")
plt.show()

plt.figure(4)
plt.scatter(complengths,poperrs)
plt.xlabel("Binary Tree Length")
plt.ylabel("Errors")
plt.ylim(0,100)
plt.title("RMHC Population Complexity")
plt.show()

plt.figure(5)
plt.plot(xpoints,hcyfitted, label = 'RMHC 1')
plt.plot(xpoints, ypoints, label='Data')
plt.plot(xpoints,hcyfitted2, label = 'RMHC 2')
plt.ylim(-10,25)
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Diversity Plot of 2 Individuals")
plt.show()

#RS_dot = px.scatter(x=xpoints,y=yfitted)   # random search dot plot
#RS_dot.show()

#HC_dot = px.scatter(x=xpoints,y=hcyfitted)   # hill climber dot plot
#HC_dot.show()