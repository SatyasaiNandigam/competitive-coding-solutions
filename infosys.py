arr1 = input().split(',')
row = int(input())
column = int(input())
arr2 = input().split(',')
key = input()
Matrix = []
for i in range(row):
    Matrix.append(arr1[i*3:(i+1)*3])
for i in range(len(arr2)):
    r,c=int(arr2[i][0])-1,int(arr2[i][1])-1
    Matrix[r][c] = arr1[i]
for char in key:
    flag = 0
    count = 0
    for i in range(row):
        for j in range(column):
            count +=1
            if char in Matrix[i][j]:
                flag = 1
                print(str(count),end='')
                for l in range(len(Matrix[i][j])):
                    if char==Matrix[i][j][l]:
                        print(str(l+1),end='')
            if flag ==1:
                break
            if count ==9 and flag==0:
                print('**',end='')