import tkinter as tk
from tkinter import messagebox
import random

perguntas = {
    'Qual a capital do Brasil?': 'Brasilia',
    'Quem escreveu Sitio do Pica Pau Amarelo?': 'Monteiro Lobato',
    'Quem escreveu "Dom Casmurro"?': 'Machado De Assis',
    'Qual é o maior rio do Brasil?': 'Amazonas',
    'Que filme é conhecido por ter um leão e três crianças?': 'Narnia',
    'Qual a melhor amiga do Harry Potter?': 'Hermione',
    'Quem canta Como Nossos Pais?': 'Elis Regina',
    'Nome da raça de cachorros favorita da Cruella': 'Dalmata',
    'Quem escreveu Turma da Monica?': 'Mauricio de Souza',
    'Destino turistico brasileiro mais frequentado? ': 'Rio de Janeiro'
}

acertos = 0
erros = 0
perguntaAtual = ''

def aleatorizarPergunta():
    global perguntaAtual
    perguntaAleatoria = random.choice(list(perguntas.keys()))
    perguntaAtual = perguntaAleatoria
    label.config(text=perguntaAtual)



def verificarResposta():

    global resposta_entry
    resposta_usuario = resposta_entry.get().strip()
    global perguntaAtual
    global acertos
    global erros

    for pergunta, resposta in perguntas.items():
        if pergunta == perguntaAtual:
            if resposta_usuario.capitalize() == resposta.capitalize():
                acertos += 1
                messagebox.showinfo("Parabéns!", "Você acertou!")
            else:
                erros += 1
                messagebox.showinfo("Poxa :(", "Você errou!")

    acerto.config(text=f"Acertos: {acertos}")
    erro.config(text=f"Erros: {erros}")

    aleatorizarPergunta()
    resposta_entry.delete(0, tk.END)
def confirmar():
    verificarResposta()

janelaTrivia = tk.Tk()
janelaTrivia.title("Jogo de Trivia")

janelaTrivia.grid_columnconfigure(0, weight=1)
janelaTrivia.grid_rowconfigure(1, weight=1)

label = tk.Label(janelaTrivia, text=perguntaAtual, font=('Arial', 12))
label.grid(row=0, column=1, padx=10, pady=10)

acerto = tk.Label(janelaTrivia, text='Acertos: ')
acerto.grid(row=3,column=0, padx=10,pady=10)

erro = tk.Label(janelaTrivia,text='Erros')
erro.grid(row=3, column=2,padx=10,pady=10)

resposta_entry = tk.Entry(janelaTrivia, font=('Arial', 14))
resposta_entry.grid(row=2, column=1, padx=10, pady=10)

botao = tk.Button(janelaTrivia, text="Confirmar", command=confirmar)
botao.grid(row=3, column=1, padx=10, pady=10)
aleatorizarPergunta()


janelaTrivia.mainloop()





