import sqlite3
conn=sqlite3.connect('Usuários.db')

cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        login TEXT PRIMARY KEY,
        senha TEXT NOT NULL
)
''')
conn.commit()

print("BEM- VINDO")
login1=""
senha1=""
while True:
    print("1. CRIAR CONTA \n2. ENTRAR")
    entrada=int(input("Escolha o número desejado: "))
    if entrada == 1:
        print("---CRIAR CONTA---")
        login1=input("Criar Login: ").lower()
        senha1=input("Criar Senha: ").lower()
        cursor.execute("SELECT * FROM usuarios WHERE login = ?", (login1,))
        if cursor.fetchall():
            print("Login Existente!")
        else:
            cursor.execute("INSERT INTO usuarios (login, senha) VALUES(?,?)", (login1, senha1))
            conn.commit()
            print("CONTA CRIADA COM SUCESSO!")
        print("-"*10)

    elif entrada == 2:
        while True:
            login=input("Login: ").lower()
            senha=input("Senha: ").lower()
            cursor.execute("SELECT * FROM usuarios WHERE login = ? AND senha = ?", (login, senha))
            if cursor.fetchall():
                print("Login efetuado com SUCESSO!")
                break
            else:
                print("Login ou senha errados!")
        break
    else:
        print("Escolha 1 ou 2!")
conn.close()