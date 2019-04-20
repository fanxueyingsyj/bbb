def Join(List, sep=None):
    return (sep or ',').join(List)
print(Join(['a', 'b', 'c']))
print(Join(['a', 'b', 'c'],':'))

