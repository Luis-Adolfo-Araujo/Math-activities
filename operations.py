from random import randrange

weekDays = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

class Activity:

    def buildOperations():
        
        #for to take the exact file day
        for index in range(7):
            results = open('resultados.txt', 'a')
            day = weekDays[index]

            #Since the operation is generated randomly, getOperand() do its thing and 
            # return a number that corresponds to the operation
            operation = Activity.getOperation()

            if operation == 0:
                operation = '+'
            elif operation == 1:
                operation = '-'
            else:
                operation = 'x'

            #define a number to be the right operand of the operations. One per file
            operand = Activity.getOperand(10)
            results.write("\t\t  {}\n".format(day))
            results.write("--------------------------------------------------".format(day))

            for quantityOfLines in range(23):
                file = open('{}.txt'.format(day), 'a')

                if operation == 'x':
                    operand1 = Activity.getOperand(10)
                    operand1 += 1
                    operand2 = Activity.getOperand(10)
                    operand2 += 1

                else:
                    operand1 = Activity.getOperand(100)
                    operand2 = Activity.getOperand(100)
                
                resultados = Activity.getResults(operand1, operand, operation)

                results.write("\n{}) = {}\t\t\t\t".format(quantityOfLines+1, resultados))
                results.write("{}) = {}\n".format(quantityOfLines+1, resultados))

                file.write(" \n {}) {} {} {} = \t\t\t\t".format(quantityOfLines+1, operand1, operation, operand))
                file.write(" {}) {} {} {} = \n".format(quantityOfLines +1, operand2, operation, operand))

    def getOperand(num):
        operand = randrange(num)
        if operand == 0 or operand == 1:
            operand = 2
        return operand
    
    def getOperation():
        operand = randrange(3)
        return operand

    def getResults(operand, operand1, operation):

        if operation == '+':
             operand += operand1
             return operand
        elif operation == '-':
            operand -= operand1
            return operand
        else:
            operand *= operand1
            return operand