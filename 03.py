f=open("pychallenge\\temp.txt",mode='r')

#for line in f:
#print(line)

#大写字母65~90
#小写字母97~122
result=[]
str1=f.read()

#判断是否是大写
def cap(a):
    if 122>=ord(a)>=97:
        return False
    elif 90>=ord(a)>=65:
        return True


for i in range(4,len(str1)-4):
    #如果为小写，判断前后3个字母
    if not cap(str1[i]):
        #print(str1[i])
        if cap(str1[i-1]) and cap(str1[i-2]) and cap(str1[i-3]) and cap(str1[i+1]) and cap(str1[i+2]) and cap(str1[i+3]):
            if (not cap(str1[i-4])) and (not cap(str1[i+4])):
                result.append(str1[i])

print(result)














