#!/usr/bin/python
# -*- coding:utf8 -*-
# 家里水卡数据算法
# 数据保存在第8块,数据算法如下:
# 1.a=dword长度取字节集(金额×100+10000)
# 2.b=a逐byte取反
# 3.结果等于a+b+a+'00FF00FF'


def conver(numStr):     #十六进制byte长度取反运算
    strVerif = '';
    tmpnum = int(numStr, 16);
    tmpnum = ~tmpnum;
    tmpnum = tmpnum & 0xff;
    strVerif = hex(tmpnum);
    strVerif = strVerif.replace('0x','');
    return strVerif;


money = 0.0;
money = float(input("Please input the money(0-255):"));
if money > 255.0:
    print("Out of range");
    exit();
money = money * 100;
money = money + 100000;
str = hex(int(money));
i = len(str);
meneyOut = '';
verif = '';
while i//2 > 0:
    tmp1 = str[i-2:i];
    if tmp1[0:1] == 'x':
        tmp1 = '0' + tmp1[1:2];
    tmp2 = conver(tmp1);
    meneyOut = meneyOut + tmp1;
    verif = verif + tmp2;
    i = i - 2;

strOut = meneyOut + '00' + verif + 'FF' + meneyOut + '0000FF00FF'

print("Please modiy the 8th block as follows:");
print(strOut.upper());