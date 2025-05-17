import tkinter as tk
import mysql.connector
from tkinter import messagebox
from datetime import date

def salvar_info():
    nome = entry_nome.get()
    documento = entry_documento.get()
    motivo = entry_motivo.get()
    data_visita = date.today()

    if nome and documento and motivo:
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="angelo@12",
                database="cadastro"
            )
            cursor = conexao.cursor()
            
            sql = "INSERT INTO visitantes (nome, documento, motivo, data_visita) VALUES (%s, %s, %s, %s)"
            valores = (nome, documento, motivo, data_visita)
            cursor.execute(sql, valores)
            conexao.commit()
            
            label_status.config(text=f'Nome "{nome}" salvo com sucesso!', fg="green")
            entry_nome.delete(0, tk.END)
            entry_documento.delete(0, tk.END)
            entry_motivo.delete(0, tk.END)
            
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro de conexão", f"Erro ao conectar ao banco:\n{erro}")
    else:
        label_status.config(text="Por favor, preencha todos os campos.", fg="red")

root = tk.Tk()
root.title("Cadastro de Visitantes")

largura_janela = 400
altura_janela = 300
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

tk.Label(root, text="Digite seu nome:").pack(pady=5)
entry_nome = tk.Entry(root, width=50)
entry_nome.pack()

tk.Label(root, text="Documento (RG ou CPF):").pack(pady=5)
entry_documento = tk.Entry(root, width=50)
entry_documento.pack()

tk.Label(root, text="Motivo da visita:").pack(pady=5)
entry_motivo = tk.Entry(root, width=50)
entry_motivo.pack()

botao_salvar = tk.Button(root, text="Salvar", command=salvar_info)
botao_salvar.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)

root.mainloop()
