# -*- coding = utf-8 -*-
# @Time : 2022/8/18 20:39
# @Author : Iscolito
# @File : String_find.py
# @Software : PyCharm
class KMP:
    def find(self, str_aim, str_temp):
        str_aim, str_temp = list(str_aim), list(str_temp)
        def next(temp):
            next=[-1]
            j = 0
            k = -1
            while j < len(temp):
                # 对比原字符串和最大重复串的尾值
                if temp[j] == temp[k] or k == -1:
                    j += 1
                    k += 1
                    next.append(k)
                else:
                    # 如果最大重复尾值不同，则寻找最大重复串的最大重复串的尾值
                    k = next[k]
            return next
        next_pos = next(str_temp)
        i, j = 0, 0
        while i < len(str_aim) and j < len(str_temp):
            if str_aim[i] == str_temp[j]:
                i += 1
                j += 1
            else:
                if j != -1:
                    j = next_pos[j]
                else:
                    i += 1
                    j = 0
        if j == len(str_temp):
            pos = i-j
        else:
            pos = -1
        return pos

a = KMP()
m, n = map(str, input().split())
b = a.find(m, n)
print(b)