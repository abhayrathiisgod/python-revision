#read write on a file
reading = open('abc.txt','r+')
#returns boolean 
print(reading.readable())
reading.write('I am a godd')
for text in reading.readlines():
    print(text)
reading.close()