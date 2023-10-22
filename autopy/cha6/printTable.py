def longest(table):
    longest = []
    for i in range(len(table)):
        max = 0
        for j in range(len(table[0])):
           if max < len(table[i][j]):
               max = len(table[i][j])
        longest.append(max)
    return longest

def printTable(table):
    lenth = longest(table)
    print(lenth)
    for i in range(len(table[0])):
        for j in range(len(table)):
            if j==0:
                print(table[j][i].rjust(lenth[j]),end=' ')
            else:
                print(table[j][i].ljust(lenth[j]),end=' ')
        print()

table_data = [['apples','orange','cherries','banana'],
              ['Alice','Bob','Carol','David'],
              ['dogs','cats','moose','goose']]
printTable(table_data)
# 'make'.rjust()