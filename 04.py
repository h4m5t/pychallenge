#and the next nothing is 44827
import urllib.request

response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82304')
str1=str(response.read().decode('utf-8'))

new_str=str1[-5:]

#print(str2)

for i in range(400):
    the_next_url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+new_str
    response=urllib.request.urlopen(the_next_url)
    new_str_temp=str(response.read().decode('utf-8'))
    print(new_str_temp)

    #如果倒数第5位是空格，说明是4位数
    if ord(new_str_temp[-5])==32:
        new_str=new_str_temp[-4:]
    #如果倒数第5位是s，说明是3位数
    elif ord(new_str_temp[-5])==115:
        new_str=new_str_temp[-3:]
    else:
        new_str=new_str_temp[-5:]
    print(new_str)















