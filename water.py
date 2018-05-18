#!/usr/bin/python
# -*- coding:utf8 -*-
# 家里水卡数据算法
# 数据保存在第12块,数据算法如下:
# 1.a=金额×100+10000 类型为dword
# 2.b=a取反 类型为dword
# 3.结果等于a.取字节集+b.取字节集+a.取字节集+'00FF00FF'

import struct;
import sys;


py_ver = sys.version_info[0];
money = float(input("Please input the money(0-255):"));
if money > 255.0 or money < 0.0:       #限定输入范围，超出读卡器不识别
    print("Out of range!");
    exit();
money = money * 100 + 100000;
if str(py_ver) == '2':
    str_money = struct.pack("i", int(money)).encode("hex");
    str_verif = struct.pack("i", ~int(money)).encode("hex");
else:
    str_money = struct.pack("i", int(money)).hex();
    str_verif = struct.pack("i", ~int(money)).hex();
str_out = str_money + str_verif + str_money + '00FF00FF';


print("Please modiy the 12th block as follows:");
print(str_out.upper());
