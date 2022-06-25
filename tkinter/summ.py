import tkinter as tk
window = tk.Tk()
window.title('The  Dark world')
window.geometry("400x150")

l1 = tk.Label(window, text='enter the first number ')
l1.grid(row=0, column=0)
l2 = tk.Label(window, text='enter the second number')
l2.grid(row=1, column=0)

num1 = tk.Entry(window,text='first number')
num1.grid(row=0, column=5)
num2 = tk.Entry(window)
num2.grid(row=1, column=5)

def sum():
    result = float(num1.get()) + float(num2.get())
    print('the sum is {} '.format(result))
    tk.Label(window,text='the sum is {} '.format(result)).grid(row=6)
    
button1 = tk.Button(window, text='Exit', width=6, padx=6, pady=6,
                    bg='black', fg='white', command=window.destroy).grid(row=2, column=0)
button2 = tk.Button(window, text='SUM', width=7, padx=7, pady=7,
                    bg='black', fg='white', command=sum).grid(row=2, column=1)

# e1 =(window, width=20).grid(row=0)
window.mainloop()
