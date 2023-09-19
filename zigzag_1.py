def zigzag(s,numrows):
    if numrows==1 or numrows>=len(s):
        return s
    
    ROWS=[[] for row in range(numrows)] #list comprehension crete a empty list for the number of rows specified
    index=0                             # can use res = [""]*numRows but in same line     # We will fill in each line in the zigzag
    step=0
    for char in s:
        ROWS[index].append(char)
        if index==0:
            step=1
        elif index==numrows-1:
            step=-1
        
        index+=step
    for i in range(numrows):
        ROWS[i]="".join(ROWS[i])
    return "".join(ROWS)

word=input("Enter a string : ")
numrows=int(input("Enter the number of rows : "))
print(zigzag(word,numrows))