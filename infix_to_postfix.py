'''
In order to convert an infix equation to prefix we do the following:
Step1 :- Create a stack to keep the operators(+,-,*,/,(,))
Step2 :- Create an output stack to directly push the operands into it 
Step3 :- If we encounter any opening bracket we push it on the operator stack
Step4 :- If we encounter any closing bracket we pop all the items from 
         the operator stack till the opening bracket and push it to the output
         stack. We then pop the opening bracket and discard it
Step5 :- Whenever we get an operator see if an higher precedence operator is
         already in the stack, if yes then pop it , add to the output stack
         and push the new operator to the operator stack.
Step6 :- After all the pieces of the equation have been worked upon and there
         still operators left in the operator stack ,then pop them all and add
         them directly to the output stack.
'''
def main(eq):
    close_brackets=')}]'
    open_brackets='({['
    operators={'+':1,'-':1,'*':2,'/':2,'%':2,'^':3}
    #Step1
    operator_stack=[]
    #Step2
    res=[]
    for literal in eq:
        if literal in operators.keys() or \
            literal in close_brackets or literal in open_brackets:
            if operator_stack:
                #Step3
                if literal in open_brackets:
                    operator_stack.append(literal)
                #Step4
                elif literal in close_brackets:
                    while operator_stack[-1] not in open_brackets:
                        res.append(operator_stack.pop())
                    operator_stack.pop()
                #Step5
                elif operators.get(literal,0) > \
                    operators.get(operator_stack[-1],0):
                    operator_stack.append(literal)
                else:
                #Step5
                    while operators[operator_stack[-1]] > operators[literal]:
                        res.append(operator_stack.pop())
                        if not operator_stack:
                            break
                    operator_stack.append(literal)
            else:
                operator_stack.append(literal)
        else:
            #Step2
            res.append(literal)
    #Step6
    for operand in operator_stack[::-1]:
        res.append(operand)
    return res


if __name__=='__main__':
    eq='(a+b)*(c+d)/(e+f)'
    res=''.join(main(eq))
    print('The prefix of {} is {}'.format(eq,res))