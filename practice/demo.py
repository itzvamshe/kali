with open('log.txt','r') as file:
   file =  file.readlines()
    
print(file)
old = file
update = input('enter log: ')

with open('log.txt','w') as file:
    file = list(update) + old
