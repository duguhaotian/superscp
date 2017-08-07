#!/usr/bin/python
# -*- coding: UTF-8 -*-

class test(object):
    def __init__(self, uid, a=0, b=0):
        self.a = a
        self.b = b
        self.uid = uid
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return False
    def __str__(self):
        return "uid:{}, a={}, b={}".format(self.uid, self.a, self.b)

ta = test("abc", 1, 2)
tb = test("bcd", 2, 3)
tc = test("cde", 3, 4)
td = test("efl", 3, 4)

tt = [test("efl", 2, 3),test("efl", 3, 4),test("efl", 1, 4),test("efl", 0, 0),test("efl", 2, 4)]
arr = [ta, tb, tc, td]
for item in arr:
    print(item)

#for tl in tt:
#    arr.index()
arr.remove(td)
print("----------remove------------")
for item in arr:
    print(item)

print("----------------------------")
if tc == td:
    print("success")
else:
    print("failed")

