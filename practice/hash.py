d = {}

while True:
    choice = input('choose a option [add,clear,del,show,update]: ')
    match choice:
        case "add":
            k = input('enter key dictionary: ')
            v = input('enter val dictionary: ')

            d[k] = v
            print('added the item',d)
        case "update":
            k = input('enter key for update: ')
            v = input('enter val for update: ')
            if k in d:
                d[k] = v
            else:
                print("key doesn't exist")
        case "clear":
            d.clear()
            print('cleared the dictionary.')
        case "show":
            if len(d) == 0:
                print("Empty.")
            else:
                print(d)
        case "del":
            k = input('enter the key to del: ')
            del d[k]
            print(k,"deleted")



