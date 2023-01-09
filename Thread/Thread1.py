import threading as td

def print_cube(num):
    print("Cube :-{}".format(num * num * num))

def print_square(num):
    print("Square :-{}".format(num * num))

if __name__ == "__main__" :
    # t1= td.Thread(target=print_cube(10))
    # t2= td.Thread(target=print_square(2))
    
    t1= td.Thread(target=print_cube,args=(10,))     # tuple
    t2= td.Thread(target=print_square,args=[5])     # list
    t1.start()
    t2.start()
    t1.join()  # mainthread wait for thread complition then execute next line of code
    t2.join()
    print("Done!")