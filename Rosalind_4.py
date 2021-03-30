s = 'We tried list and we tried dicts also we tried Zen'

for word in s.split(' '):
    a = s.count(word)
    d = {}
    d[word] = a
#    print(d)

for key, value in d.items():
    print(key, value)
    
    
