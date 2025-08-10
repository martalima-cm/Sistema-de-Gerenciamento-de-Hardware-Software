import sqlite3

DATABASE_NAME = "inventario.db"

def get_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    return sqlite3.connect(DATABASE_NAME)

def setup_database():
    """Cria as tabelas de Hardware e Software se elas não existirem."""
    conn = get_connection()
    cursor = conn.cursor()

    # Cria a tabela Hardware
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Hardware (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            modelo TEXT,
            numero_serie TEXT UNIQUE,
            status TEXT NOT NULL,
            localizacao TEXT
        )
    """)

    # Cria a tabela Software
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Software (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_software TEXT NOT NULL,
            versao TEXT,
            chave_licenca TEXT UNIQUE,
            id_hardware_associado INTEGER,
            FOREIGN KEY(id_hardware_associado) REFERENCES Hardware(id)
        )
    """)

    conn.commit()
    conn.close()

# --- Funções de Hardware ---
def add_hardware(nome, tipo, modelo, numero_serie, status, localizacao):
    """Adiciona um novo item de hardware."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Hardware (nome, tipo, modelo, numero_serie, status, localizacao)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, tipo, modelo, numero_serie, status, localizacao))
        conn.commit()
        print(f"Hardware '{nome}' adicionado com sucesso.")
        return True
    except sqlite3.IntegrityError:
        print("Erro: Número de série já existe.")
        return False
    finally:
        conn.close()

def get_all_hardware():
    """Retorna todos os itens de hardware."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Hardware")
    hardware_list = cursor.fetchall()
    conn.close()
    return hardware_list

def update_hardware_status(hardware_id, new_status):
    """Atualiza o status de um item de hardware."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Hardware SET status = ? WHERE id = ?", (new_status, hardware_id))
    conn.commit()
    conn.close()

def delete_hardware(hardware_id):
    """Deleta um item de hardware e seus softwares associados."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Software WHERE id_hardware_associado = ?", (hardware_id,))
    cursor.execute("DELETE FROM Hardware WHERE id = ?", (hardware_id,))
    conn.commit()
    conn.close()

def find_hardware_by_id(hardware_id):
    """Busca um item de hardware pelo ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Hardware WHERE id = ?", (hardware_id,))
    item = cursor.fetchone()
    conn.close()
    return item

# --- Funções de Software ---
def add_software(nome_software, versao, chave_licenca, id_hardware_associado):
    """Adiciona um novo software e o associa a um hardware."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Software (nome_software, versao, chave_licenca, id_hardware_associado)
            VALUES (?, ?, ?, ?)
        """, (nome_software, versao, chave_licenca, id_hardware_associado))
        conn.commit()
        print(f"Software '{nome_software}' adicionado com sucesso.")
        return True
    except sqlite3.IntegrityError:
        print("Erro: Chave de licença já existe.")
        return False
    finally:
        conn.close()

def get_software_for_hardware(hardware_id):
    """Retorna a lista de softwares associados a um hardware."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Software WHERE id_hardware_associado = ?", (hardware_id,))
    software_list = cursor.fetchall()
    conn.close()
    return software_list

def delete_software(software_id):
    """Deleta um software pelo ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Software WHERE id = ?", (software_id,))
    conn.commit()
    conn.close()