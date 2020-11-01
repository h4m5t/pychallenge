str1="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

intab  = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = str1.maketrans(intab, outtab)   # 制作翻译表
 
print(str1.translate(trantab))

#或者直接用ASCII码表对应的方式，利用ord(),chr()函数
#result:i hope you didnt translate it by hand. 
#thats what computers are for. doing it in by hand is 
#inefficient and that's why this text is so long. 
#using string.maketrans() is recommended. now apply on the url.