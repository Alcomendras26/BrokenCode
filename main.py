#This code should be able to solve the problem in "Instructions.pdf"
#When you run it, enter the sample problem one line at a time and hit enter in between each line. You should get the right output.

#read in how many lines there are
lines = int(input())

#setup output variable
output=""
#loop through the lines
for j in range(0,lines):
    currentLine=input()
    #set the current char variable and give it a dummy value
    currentChar=""
    #set the current count to 0
    currentCount=0
    #set the previous count variable and give it a dummy value
    previousChar=""
    #loop through the characters in the line
    for j in range(0, len(currentLine)):
    #if it's your first line,
        if j == 0:
            currentChar = currentLine[j]
            currentCount=1
        else:
            previousChar = currentChar
            #get the new current char from position j
            currentChar= currentLine[j]
            #if current and previous are the same
            if currentChar==previousChar:

                currentCount-=1
                #if they aren't the same
            else:
                output+=str(currentCount)+" "+str(previousChar)+" "
                currentCount=1
                #If we're on the last character
        if j ==len(currentLine)-1:
                    #add the character count to the output
                        output+str(currentCount)+" "+str(previousChar)+" "
    #add a newline to the output
        output+="\n"
    #print the result
print(output)

#"4, +++===!!!, 777777......TTTTTTTTTTTT, (AABBC), 3.1415555