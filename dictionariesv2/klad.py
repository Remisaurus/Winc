dic={'is':'is','not':'not','even':'even'}
dic2={'ok':'ok','ok2':'ok2'}

print(dic)


if not 'oh' in dic:
    dic['oh']='Oh'


print(dic)
print(type(dic))
print(dic['is'])

dic['dic2']=dic2

print(bool(dic['dic2']))
