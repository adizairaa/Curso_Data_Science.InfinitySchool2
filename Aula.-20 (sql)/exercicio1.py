import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")
conn.commit()


def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")

    cursor.execute("""
    INSERT INTO alunos (nome, email)
    VALUES (?, ?)
    """, (nome, email))

    conn.commit()
    print("Aluno adicionado com sucesso!")

def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    print("\n Lista de alunos:")
    for aluno in alunos:
        print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Email: {aluno[2]}")
    print()

def atualizar_email():
    id_aluno = input("Digite o ID do aluno: ")
    novo_email = input("Digite o novo email: ")

    cursor.execute("""
    UPDATE alunos
    SET email = ?
    WHERE id = ?
    """, (novo_email, id_aluno))

    conn.commit()
    print(" Email atualizado com sucesso!")

def remover_aluno():
    id_aluno = input("Digite o ID do aluno que deseja remover: ")

    cursor.execute("""
    DELETE FROM alunos
    WHERE id = ?
    """, (id_aluno,))

    conn.commit()
    print(" Aluno removido com sucesso!")


def menu():
    while True:
        print("""
=== SISTEMA DE ALUNOS ===
1 - Adicionar aluno
2 - Listar alunos
3 - Atualizar email
4 - Remover aluno
0 - Sair
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            atualizar_email()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print(" Opção inválida!")



menu()


conn.close()