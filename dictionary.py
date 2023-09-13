dic = {
    'name':'Forhad','roll':55,
    'Address':['east parola','Patia','Ctg'], 
    'set':{55,44,66}
    }
print(dic)
print(type(dic))


print(dic['name'])
print(dic.get('roll'))

# change_the_dictionary_value
print(dic['name'])
dic['name'] = 'Abdullah'
print(dic['name'])

dic.update(
    {'name':'md',
    'roll':658587,
    'address': ['East Parola','Patiya','Chattogram'],
    'set':66
    }
    
)

print(dic)