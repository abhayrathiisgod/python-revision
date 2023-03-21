#try except

try: 
    x= int(input('input a integer value'))
    print(x)
except ValueError:
    print('value is not an integer')
else:
    print('ntohing went wrong')
finally:
    print('taskecomplleted')
    
