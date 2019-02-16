def Main():
    line=input().split(" ")
    rows=int(line[0])
    column=int(line[1])
    words=[]
    matrix=[]
    for i in range(0,rows):
        row=input()
        matrix.append(row)
        words+=row.split("#")
        i+=1
    for i in range(0,column):
        tmp=""
        for j in range(0,rows):
            tmp+=matrix[j][i]
            j+=1
        i+=1
        words+=tmp.split("#")
    words=sorted(words)
    for word in words:
        if len(word) >= 2:
            return word


print(Main())