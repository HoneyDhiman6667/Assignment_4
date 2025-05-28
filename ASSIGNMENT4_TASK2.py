'''
with open ('output.txt','r') as file1:
    reading_file = file1.read()
    print(reading_file)

with open ('output.txt','a') as file1:
    appending_file = file1.write('\nHello, Pyhton!')
    print(appending_file)
'''
with open ('output.txt','r') as file1:
    reading_file = file1.read()
    print(reading_file)