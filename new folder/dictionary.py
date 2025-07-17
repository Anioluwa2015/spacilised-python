d1 = { 'name': "Mum" , 'age' : "40" , 'job' : "doctor" }
d1 ['age'] = 48
print(d1['age'])
d1['gender' ] = "woman"
print(d1)
print(d1.pop('job'))
print(d1)
print(d1.popitem())
print(d1)

for i in d1:
    print(i)