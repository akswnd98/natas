data = '''
'''
data = data.split('\n')
string = data[0]

notstring = ""
for x in string:
    i =1
    for y in data[i]:
        if x not in y:
            notstring+= x

        i +=1
            
