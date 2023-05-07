//using loop
def rev(s):
    str=""
    for i in s:
        str=i+str
    return str
print(rev("sultan"))



//using slicing
s="Avinash"
print(s[::-1])


// using function recursion
def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


// using stack
def rev(s):                            // stack has first in first out principle
    stack=[]                             // stack
    for char in s:
        stack.append(char)              // all char of string push into stack 
    revers_string=""
    while(len(stack)>0):                // check for the condition of underflow means whether stack is empty or not if not then execute the 
        revers_string+=stack.pop()       // these statement pop the top element of the stack and insert it into reverse_string
    return revers_string
print(rev("avinash"))



//using reversed() function
s="reverse string using reverse() function"
print(''.join(reversed(s)))

