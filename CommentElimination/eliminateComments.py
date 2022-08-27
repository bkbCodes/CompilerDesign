filename = "CommentElimination/progWithComment.c" #input("Enter filename: ")
prog = open(filename)
processedProg = []

# for multi-line comment:
flag = 0
newline = 0

for line in prog:
    # adding newline character to previous line when comment is found:
    if newline == 1:
        processedProg[-1] += "\n"
        newline = 0

    # create new line only if there is no multi-line comment open:
    if flag == 0:
        processedProg.append(line[0])

    # scan the line character by character for comments:
    for i in range(1,len(line)):
        ch = line[i]

        # looking for // and /* in line to skip the next character until
        # 1) line in case of single line comment //
        # 2) */ is found in case of multiline comment
        # after comment is closed the resume appending the characters
        if flag == 0:
            if ch == "/" and line[i-1] == "/":
                processedProg[-1] = processedProg[-1][:-1]
                newline = 1
                break
            elif ch == "*" and line[i-1]=="/":
                processedProg[-1] = processedProg[-1][:-1]
                flag = 1
                newline = 1
            else:
                processedProg[-1] += ch
        else:
            if ch == "/" and line[i-1]== "*":
                flag = 0
            else:
                continue

newProg = open("Processed.".join(filename.split(".")),"w")
newProg.write("".join(processedProg))
