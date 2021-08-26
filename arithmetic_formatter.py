def arithmetic_arranger(problems, showResult=False):
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    answer = 0

    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
            if '*' in problem or '/' in problem:
                return "Error: Operator must be either '+' or '-'."
            if '-' in problem or '+' in problem:
                if '-' in problem:
                    operands = problem.split('-')
                    operand1 = operands[0].strip()
                    operand2 = operands[1].strip()
                    if len(operand1) > 4 or len(operand2) > 4:
                        return "Error: Numbers cannot be more than 4 digits."
                    elif operand1.isdecimal() == False or operand2.isdecimal() == False:
                        return "Error: Numbers must only contain digits."
                    else:
                        if operand1.isdecimal() == True and operand2.isdecimal() == True:
                            if len(operand1) > len(operand2):
                                row1 = row1 + operand1.rjust(len(operand1) + 2) + '    '
                                row2 = row2 + '- ' + operand2.rjust(len(operand1)) + '    '
                                row3 = row3 + (('-')*(len(operand1))+('--')) + '    '
                                if showResult == True:
                                    num1 = int(operand1)
                                    num2 = int(operand2)
                                    answer = num1 - num2
                                    answer2 = str(answer)
                                    row4 = row4 + answer2.rjust(len(operand1) + 2) + '    '
                            else:
                                row1 = row1 + operand1.rjust(len(operand2) + 2) + '    '
                                row2 = row2 + '- ' + operand2 + '    '
                                row3 = row3 + (('-')*(len(operand2))+('--')) + '    '
                                if showResult == True:
                                    num1 = int(operand1)
                                    num2 = int(operand2)
                                    answer = num1 - num2
                                    answer2 = str(answer)
                                    row4 = row4 + answer2.rjust(len(operand2) + 2) + '    '
                else:
                    operands = problem.split('+')
                    operand1 = operands[0]
                    operand1 = operand1.strip()
                    operand2 = operands[1]
                    operand2 = operand2.strip()
                    if len(operand1) > 4 or len(operand2) > 4:
                        return "Error: Numbers cannot be more than 4 digits."
                    if operand1.isdecimal() == False or operand2.isdecimal() == False:
                        return "Error: Numbers must only contain digits."
                    else:
                        if len(operand1) > len(operand2):
                            row1 = row1 + operand1.rjust(len(operand1) + 2) + '    '
                            row2 = row2 + '+ ' + operand2.rjust(len(operand1)) + '    '
                            row3 = row3 + (('-')*(len(operand1))+('--')) + '    '
                            if showResult == True:
                                num1 = int(operand1)
                                num2 = int(operand2)
                                answer = num1 + num2
                                answer2 = str(answer)
                                row4 = row4 + answer2.rjust(len(operand1) + 2) + '    '
                        else:
                            row1 = row1 + operand1.rjust(len(operand2) + 2) + '    '
                            row2 = row2 + '+ ' + operand2 + '    '
                            row3 = row3 + (('-')*(len(operand2))+('--')) + '    '
                            if showResult == True:
                                num1 = int(operand1)
                                num2 = int(operand2)
                                answer = num1 + num2
                                answer2 = str(answer)
                                row4 = row4 + answer2.rjust(len(operand2) + 2) + '    '
    if showResult == False:
        return row1 + "\n" + row2 + "\n" + row3
    else:
        return row1 + "\n" + row2 + "\n" + row3  + "\n" + row4
