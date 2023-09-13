a = 4,5,66,44,23,6,'one','two','three'

a =list(a)
a[1]=55
a.append(12)
a.append(22)
a.append(55)
print(a)
a.remove(4)
a.remove(55)

a=tuple(a)
print(a)

print(set(a))