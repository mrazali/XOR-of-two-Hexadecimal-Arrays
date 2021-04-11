# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:11:28 2021

@author: Raza_Jutt
"""

def hexaToDec(hexval):
    length = len(hexval)
    base = 1
    dec_val = 0
    for i in range(length - 1, -1, -1):
        if hexval[i] >= '0' and hexval[i] <= '9':
            dec_val += (ord(hexval[i]) - 48) * base
            base = base * 16
        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            dec_val += (ord(hexval[i]) - 55) * base
            base = base * 16
    return dec_val

def decToHexa(n):
    hexaDeciNum = ['0'] * 100
    i = 0
    s=""
    while(n != 0):
        temp = 0
        temp = n % 16
        if(temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)
    j = i - 1
    while(j >= 0):
        s = s+(hexaDeciNum[j])
        j = j - 1
    return s

def comp_len_32(ary):
    temp=[]
    for i in range(0,32-len(ary)):
        temp.append(0)
    for i in ary:
        temp.append(i)
    return temp

def ary_To_string(ary):
    a=""
    for i in ary:
        i = str(i)
        a=a+i
    return a

def string_To_ary(string):
    ary= []
    for i in range(0,len(string),2):
        ary.append(string[i]+string[i+1])
    return ary

def xor(ary1,ary2):
    ary = []
    for i in range(0,len(ary1)):
        if ary1[i]==ary2[i]:
            ary.append(0)
        else:
            ary.append(1)
    return ary

def bin2dec(binary):   
    decimal, i = 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def dec2bin(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

def xor_hexas(ary1,ary2):
    binOfHex = ary_To_string(xor(comp_len_32(dec2bin(hexaToDec(ary_To_string(ary1)))),comp_len_32(dec2bin(hexaToDec(ary_To_string(ary2))))))
    ary=[]
    n= 0
    for i in range(8,len(binOfHex),8):
        ary.append(str(decToHexa(bin2dec(int(binOfHex[n:i])))))
        n=i
    ary.append(str(decToHexa(bin2dec(int(binOfHex[n:])))))
    s=""
    for i in range(0,4):
        for j in range(0,2-len(ary[i])):
            s=s+"0"
        ary[i] = s+ary[i]
        s=""
    return ary

#xor_hexas()