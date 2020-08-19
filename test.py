def start():
    lst = [1,2,3,4]
    
    print(lst)
    
    change(lst)
    
    print(lst)
    
    return 1

def change(lst):
    
    lst.append(9)
    lst[:] = lst[1:]
    
    print(lst)
    
    
    return 1

start()