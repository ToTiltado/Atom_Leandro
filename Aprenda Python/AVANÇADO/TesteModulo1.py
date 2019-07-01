from collections import Counter
from collections import defaultdict
l = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
print(Counter(l))
print(Counter('skmsfdfjnfdnjfnfjnjfdnjfd'))
s = 'Hello python hello'
s1 = s.split()
print(Counter(s1))
d = defaultdict(object)
d['one']
for item in d:
    print(item)
