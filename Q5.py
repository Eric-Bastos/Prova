import customtkinter as ctk 


def mais():
    a= float(num1.get())
    b= float(num2.get())
    x= a+b
    resultado.configure(text=(f'O resultado foi: {x}'))    
def menos():
    a= float(num1.get())
    b= float(num2.get())
    x= a-b
    resultado.configure(text=(f'O resultado foi: {x}'))


def mult():
    a= float(num1.get())
    b= float(num2.get())
    x= a*b
    resultado.configure(text=(f'O resultado foi: {x}'))


def div():
    a= float(num1.get())
    b= float(num2.get())
    x= a/b
    resultado.configure(text=(f'O resultado foi: {x}'))


ctk.set_appearance_mode('dark')
janela=ctk.CTk()
janela.geometry('500x500')
ctk.CTkLabel(janela, text= 'Calculadora' ,font=('arial',50,'bold'),text_color='white').pack(pady=15)

num1= ctk.CTkEntry(janela, placeholder_text='Digite o primeiro número',width=450,height=50)
num1.pack(pady=10)

num2= ctk.CTkEntry(janela, placeholder_text='Digite o segundo número ',width=450,height=50)
num2.pack(pady=10)

soma=ctk.CTkButton(janela,text="+",font=('arial',30),fg_color='green',command=mais)
soma.pack(pady=5)

sub=ctk.CTkButton(janela,text="-",font=('arial',30),fg_color='green',command=menos)
sub.pack(pady=5)

multiplicação=ctk.CTkButton(janela,text="x",font=('arial',30),fg_color='green',command=mult)
multiplicação.pack(pady=5)

divisão=ctk.CTkButton(janela,text="/",font=('arial',30),fg_color='green',command=div)
divisão.pack(pady=5)

resultado= ctk.CTkLabel(janela, text='', font=('arial',18))
resultado.pack(pady=5)

janela.mainloop()