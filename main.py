#This code should be able to solve the problem in "Instructions.pdf"
#When you run it, enter the sample problem one line at a time and hit enter in between each line. You should get the right output.
# Read the number of lines
lines = int(input())

# setup output variable
output = ""

# loop through the lines
for i in range(0, lines):
    # Read in a line
    currentLine = input()

    # initialize variables for the current line
    currentChar = ''
    currentCount = 0
    previousChar = ''

    # loop through the characters in the line
    for j in range(0, len(currentLine)):
        # If it's the first character of the line
        if j == 0:
            currentChar = currentLine[j]
            currentCount = 1
        else:
            #set previous to the old current char
            previousChar = currentChar
            # get the new current char from position j
            currentChar = currentLine[j]

            # if current and previous are the same, increase the count
            if currentChar == previousChar:
                currentCount += 1
            # if they aren't the same, save the old run and reset count
            else:
                output += str(currentCount) + " " + str(previousChar) + " "
                currentCount = 1

        # if we're on the last character of the line, commit the final run
        if j == len(currentLine) - 1:
            output += str(currentCount) + " " + str(currentChar) + " "

    # add a newline to the output after processing each line
    output += "\n"

# Print the final result
print(output)

#"4, +++===!!!, 777777......TTTTTTTTTTTT, (AABBC), 3.1415555
