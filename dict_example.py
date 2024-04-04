# dict: key:value pair, collection of keys and values,  {k:v,k:v,k:v}
#print(dir(dict)) will show methods of dict, key must be imuatable (int.float,bool,string,complex,tuple)
# key should be unique, dict is mutable data structure

d1 = {'id':101, "name":"anant", 'age':64, 'city':'ahmedabd'}
#print(d1)
#print(d1['name'])
#print(d1.keys())
#print(d1.values())
#print(d1.get('salary',25000))
#print(d1.get(""))

#d1 ['age'] = 65
# del d1['name]

# setdefault parameter if key dont exsist than it will add
#d1.setdefault('salary') # none will be added ad deafult value of salary
#d1.setdefault('salary',50000)

#print(list(d1.items()))

#for x in d1.items():
#for x in d1.keys():
#for x in d1.values():
#    print(x)
 #   print(x , end=" ")

#print(d1.pop('age'))
#print(d1.popitem())

#d2 = {"name": "anant", 'age': 45, 'salary': 45000}

#d1.update(d2)

# d3={'101':{'id':101, 'name':'deepak'}}
# print (d3.keys())
# print (d3.values())
# print (d3.items())
# print (d3.get('101'))

print(d1)



#print(d1.get(""))