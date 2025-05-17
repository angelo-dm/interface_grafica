# 🎓 Sistema de Controle de Visitantes - Escola Técnica

Este é um sistema simples de controle de entrada de visitantes, desenvolvido com **Python**, **Tkinter** e **MySQL**. Ele permite o registro de visitantes com os seguintes dados:

* Nome
* Documento (RG ou CPF)
* Motivo da visita
* Data da visita (preenchida automaticamente)

---

## 📌 Funcionalidades

* Interface gráfica amigável
* Registro de visitantes com campos obrigatórios
* Armazenamento em banco de dados MySQL
* Feedback visual sobre sucesso ou erro ao salvar

---

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* Tkinter (GUI)
* MySQL
* mysql-connector-python

---

## 🧱 Estrutura do Banco de Dados

```sql
CREATE DATABASE IF NOT EXISTS cadastro;

USE cadastro;

CREATE TABLE IF NOT EXISTS visitantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    documento VARCHAR(20),
    motivo VARCHAR(255),
    data_visita DATE
);
```

---

## 🚀 Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/controle-visitantes.git
   cd controle-visitantes
   ```

2. Instale o conector MySQL:

   ```bash
   pip install mysql-connector-python
   ```

3. Configure o banco de dados MySQL (usuário, senha, host, etc) no script `main.py`.

4. Execute o aplicativo:

   ```bash
   python main.py
   ```

---

## 📸 Screenshots

### 🖼️ Tela de Cadastro

![Tela de Cadastro](screenshots/screen1.png)

### ✅ Confirmação de Registro

![Confirmação](screenshots/screen2.png) 
![Confirmação](screenshots/screen3.png)

### 📊 Dados no Banco de Dados

![Banco de Dados](screenshots/screen4.png)


---

## 📁 Estrutura do Projeto

```
interface_grafica/
├── app.py
├── dump.sql
├── README.md
└── screenshots/
    ├── screen1.png
    ├── screen2.png
    ├── screen3.png
    └── screen4.png
```

---

## 👨‍💻 Autor

Desenvolvido por [Angelo](https://github.com/angelo-dm)

---


