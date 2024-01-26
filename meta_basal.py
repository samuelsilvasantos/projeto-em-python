from tkinter import *

print('Veja aqui sua taxa de metabolismo Basal: ')

def meta_basal(peso, altura, idade):
    metabolismo = 66.5 + (13.75 * peso) + (5 * altura) - (6.8 * idade)  
    return metabolismo

def meta_basalf (peso, altura, idade):
    metabolismof = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
    return metabolismof


def calcular():
    nome = nome_entry.get()
    sexo = sexo_entry.get()
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())
    idade = int(idade_entry.get())

    if sexo.lower() == 'masculino':
        metabolismo = meta_basal(peso, altura, idade)
        resultado['text'] = f"A taxa de metabolismo basal de {nome} é {metabolismo:.2f}"
    else:
        metabolismof = meta_basalf(peso, altura, idade)
        resultado['text'] = f"A taxa de metabolismo basal de {nome} é {metabolismof:.2f}"

janela = Tk()
janela.title('calculo de taxa metabolica basal')

Label(janela, text='Nome completo:').pack()
nome_entry = Entry(janela)
nome_entry.pack()

Label(janela, text='informe seu sexo : masculino/feminino' ).pack()
sexo_entry = Entry(janela)
sexo_entry.pack()

Label(janela, text='informe seu peso:').pack()
peso_entry = Entry(janela)
peso_entry.pack()

Label(janela, text='informe sua altura:').pack()
altura_entry = Entry(janela)
altura_entry.pack()

Label(janela, text= 'informe sua idade: ').pack()
idade_entry = Entry(janela)
idade_entry.pack()

botao = Button(janela, text='calcular', command=calcular).pack()

resultado = Label(janela, text='')
resultado.pack()

janela.mainloop()
