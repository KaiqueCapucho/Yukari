import os, sqlite3
import subprocess
import webbrowser
import winreg


def create(bd='./bd.db'):
    with sqlite3.connect(bd) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS Sites(_id INTEGER PRIMARY KEY AUTOINCREMENT,
            key STRING NOT NULL, url STRING NOT NULL UNIQUE, private BOOLEAN NOT NULL)""")
        conn.execute("""CREATE TABLE IF NOT EXISTS Apps(_id INTEGER PRIMARY KEY AUTOINCREMENT,
            key STRING NOT NULL, dir STRING NOT NULL UNIQUE, adm BOOLEAN NOT NULL)""")
        conn.execute("""CREATE TABLE IF NOT EXISTS Archives(_id INTEGER PRIMARY KEY AUTOINCREMENT,
            key STRING NOT NULL, dir STRING NOT NULL UNIQUE, notes String)""")

def drop(bd='./bd.db'):
    if os.path.exists(bd):os.remove(bd)
    else: print(f"O arquivo {bd} não foi encontrado.")

#Problema de SQL Injection no {table}
def insertValue(table, key, value, data, bd='./bd.db' ):
    with sqlite3.connect(bd) as conn:
        conn.execute(f"""INSERT INTO {table} VALUES (?, ?,?,?)""", (None, key, value, data))

#Idem ao InsertValue
def getKeys(table, bd='./bd.db'):
    with sqlite3.connect(bd) as conn:
        return conn.execute(f"SELECT key FROM {table} ORDER BY key").fetchall()

#Idem ao getKeys
def getValue(table, key, bd='./bd.db'):
    with sqlite3.connect(bd) as conn:
        values = [row[2:3] for row in conn.execute(f"SELECT * FROM {table} WHERE key LIKE ?", key)]
    return values[0],[1]

def obterNavegador():
    try:
        # Pega o ProgId do navegador padrão
        browserChoicePath = r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\https\UserChoice"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, browserChoicePath) as bcp:
            #A função QueryValueEx retorna um valor (no caso o ProgID) e seu tipo (int, str, etc)
            progID, _ = winreg.QueryValueEx(bcp, "ProgId")

        # Usa o ProgId para pegar o comando real
        command_path = fr"{progID}\shell\open\command"
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, command_path) as bcp:
            command, _ = winreg.QueryValueEx(bcp, "")

        #retorna o caminho do exe
        return command.split('"')[1] if command.startswith('"') else command.split(' ')[0]

    except Exception as e:
        raise FileNotFoundError("Não foi possível encontrar o navegador padrão.") from e

def openDir(values, arg=0):
    for v in values:
        match v.split('.')[1]:
            case 'docx': subprocess.Popen(['C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.exe', v])
            case 'xlsx': subprocess.Popen(['C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.EXE', v])
            case 'txt':  subprocess.Popen(['C:\\Windows\\System32\\notepad.exe', v])
            case 'pdf':  webbrowser.open(v)
            case 'exe':  subprocess.Popen(v)
            case 'db':   subprocess.Popen(["C:/Program Files/SQLiteStudio/SQLiteStudio.exe", v])
            case _:
                if v.startswith('http') and arg:subprocess.Popen([obterNavegador(), "--incognito", v])
                elif v.startswith('http'): subprocess.Popen([obterNavegador(), v])
                else: print('Erro! Extensão de arquivo inválida')



#insertValue('Sites', 'chatgpt', 'https://chatgpt.com/', True)
#insertValue('Sites', 'spotify', 'https://open.spotify.com/', False)



