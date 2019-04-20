u=input()
w=list(u)
l=int(len(w))
print(l)
for i in l:
    Min=min(u)
    u.append(Min)
    u.remove(Min)
print(u)
