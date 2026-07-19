todos = []

while True:
    # add options shortcuts a,d,c,s and catch non options passed and return to enter proper options
    user_input = input('please choose one option[add,del,clear,show]: ')

    match user_input:
        case 'add':
            # add feature to remove spaces in input passed using strip method.
            todo = input('please enter task name: ')
            todos.append(todo)
            print(f'{todo} added.')
        case 'delete':
            # add delete feature of deleting using values
            todos.pop()
            print('removed last task.')
        case 'clear':
            todos.clear()
            print('cleared all todos.')
        case 'show':
            # add numbers to left of tasks
            for i in todos:
                print(i)
        case 'exit':
            break

