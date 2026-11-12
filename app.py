
import sqlite3


def conectar():
    return sqlite3.connect("laboratorio.db")


def criar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    cursor.execute("""
        INSERT INTO usuarios (usuario, senha)
        SELECT 'admin', '123456'
        WHERE NOT EXISTS (
            SELECT 1 FROM usuarios WHERE usuario = 'admin'
        )
    """)

    conexao.commit()
    conexao.close()


def login(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    consulta = """
        SELECT * FROM usuarios
        WHERE usuario = ? AND senha = ?
    """

    cursor.execute(consulta, (usuario, senha))

    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        print("\nLogin realizado com sucesso!")
    else:
        print("\nUsuário ou senha incorretos.")


if __name__ == "__main__":
    criar_banco()

    print("===== SISTEMA DE LOGIN =====")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    login(usuario, senha)
