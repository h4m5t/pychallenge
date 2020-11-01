filepath=r'Learn1\1.txt'
#filepath=r'C:\Users\loeoe\Desktop\Python Codes\Learn1\1.txt'
f=open(filepath, mode='r')

#存储key,存在的字符有哪些
list1=[]

for i in f:
    #print(i)
    for j in i:
        #print(j)
        if j not in list1:
            list1.append(j)
print(list1)






