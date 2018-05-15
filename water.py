#!/usr/bin/python
# -*- coding:utf8 -*-
# 家里水卡数据算法
# 数据保存在第8块,数据算法如下:
# 1.a=金额×100+10000 类型为dword
# 2.b=a取反 类型为dword
# 3.结果等于a.取字节集+b.取字节集+a.取字节集+'00FF00FF'

import struct

money = float(input("Please input the money(0-255):"));
if money > 255.0:
    print("Out of range!");
    exit();
money = money * 100;
money = money + 100000;
str_money = struct.pack("i", int(money)).encode("hex");
str_verif = struct.pack("i", ~int(money)).encode("hex");
str_out = str_money + str_verif + str_money + '00FF00FF';


print("Please modiy the 8th block as follows:");
print(str_out.upper());