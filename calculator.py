import customtkinter

# mode apperance 'dark'
customtkinter.set_appearance_mode('dark')

# configuration  window
window = customtkinter.CTk()
window.geometry('361x450+423+159')

def calculate():
    calculo = output.get('0.0', 'end')
    resultado = eval(calculo)
    output.delete('0.0', 'end')
    output.insert('0.0', resultado)

# text box for showing
output = customtkinter.CTkTextbox(window, width=300, height=50,corner_radius=15, border_width=5, border_color='#042940', font=(('Arial', 50)))
output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

#buttons
btn10 = customtkinter.CTkButton(window,text='(', command= lambda:output.insert('end', '('), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn10.grid(row=1, column=0, padx=5, pady=5)

btn11 = customtkinter.CTkButton(window,text=')', command= lambda:output.insert('end', ')'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn11.grid(row=1, column=1, padx=5, pady=5)

btn12 = customtkinter.CTkButton(window,text='%', command= lambda:output.insert('end', '/100'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn12.grid(row=1, column=2, padx=5, pady=5)

btn13 = customtkinter.CTkButton(window,text='AC', command=lambda:output.delete('0.0', 'end'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn13.grid(row=1, column=3, padx=5, pady=5)

btn1 = customtkinter.CTkButton(window,text='7', command= lambda:output.insert('end', 7), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn1.grid(row=2, column=0, padx=5, pady=5)

btn2 = customtkinter.CTkButton(window,text='8', command= lambda:output.insert('end', 8), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn2.grid(row=2, column=1, padx=5, pady=5)

btn3 = customtkinter.CTkButton(window,text='9', command=lambda:output.insert('end', 9), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn3.grid(row=2, column=2, padx=5, pady=5)

btn_dividir = customtkinter.CTkButton(window,text='÷', command=lambda:output.insert('end', '/'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_dividir.grid(row=2, column=3, padx=5, pady=5)

btn4 = customtkinter.CTkButton(window,text='4', command=lambda:output.insert('end', 4), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn4.grid(row=3, column=0, padx=5, pady=5)

btn5 = customtkinter.CTkButton(window,text='5', command=lambda:output.insert('end', 5), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn5.grid(row=3, column=1, padx=5, pady=5)

btn6 = customtkinter.CTkButton(window,text='6', command=lambda:output.insert('end', 6), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn6.grid(row=3, column=2, padx=5, pady=5)

btn_multiplicar = customtkinter.CTkButton(window,text='x', command=lambda:output.insert('end', '*'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_multiplicar.grid(row=3, column=3, padx=5, pady=5)

btn41 = customtkinter.CTkButton(window,text='1', command=lambda:output.insert('end', 1), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn41.grid(row=4, column=0, padx=5, pady=5)

btn51 = customtkinter.CTkButton(window,text='2', command=lambda:output.insert('end', 2), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn51.grid(row=4, column=1, padx=5, pady=5)

btn61 = customtkinter.CTkButton(window,text='3', command=lambda:output.insert('end', 3), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn61.grid(row=4, column=2, padx=5, pady=5)

btn_multiplicar = customtkinter.CTkButton(window,text='-', command=lambda:output.insert('end', '-'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_multiplicar.grid(row=4, column=3, padx=5, pady=5)


btn0 = customtkinter.CTkButton(window, text='0', command= lambda:output.insert('end', 0), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn0.grid(row=5, column=0, padx=5, pady=5)

btn01 = customtkinter.CTkButton(window, text='.', command= lambda:output.insert('end', '.'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn01.grid(row=5, column=1, padx=5, pady=5)

btn_calculate = customtkinter.CTkButton(window,text='=', command=calculate, corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_calculate.grid(row=5, column=2, padx=5, pady=5)

btn_somar = customtkinter.CTkButton(window,text='+', command=lambda:output.insert('end', '+'), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_somar.grid(row=5, column=3, padx=5, pady=5)







window.mainloop()