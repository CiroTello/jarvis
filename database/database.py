import sqlite3

def conectarBD(chatID):
    usuarios = r"Api/Database/usuarios.db"
    miConexion = sqlite3.connect(usuarios)
    miCursor = miConexion.cursor()

    miCursor.execute('''
        CREATE TABLE IF NOT EXISTS DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CHATID VARCHAR(15) UNIQUE,
            OPENKEY VARCHAR(60),
            WEATHERKEY VARCHAR(50),
            ORGANIZATIONKEY VARCHAR(60))
            
        ''')

    miCursor.execute("INSERT OR IGNORE INTO DATOSUSUARIOS (CHATID, OPENKEY,  WEATHERKEY) VALUES (?,?,?)", (chatID, "", ""))
    miConexion.commit()

    return miConexion


def consultarDB(chatID):
    miConexion = conectarBD(chatID)
    miCursor = miConexion.cursor()

    chat_id = str(chatID)

    try:
        miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE CHATID =" + chat_id)
        usuarioLectura = miCursor.fetchone()
       
        print(usuarioLectura)
        miConexion.commit()
        return usuarioLectura

    except Exception as e:
        print("Error al consultar la base de datos: ", e )
        miConexion.commit()
        return None


#! OPEN AI ================================================================================================
def actualizarDB_openAI(chatID, openKey):
    miConexion = conectarBD(chatID)
    miCursor = miConexion.cursor()

    chat_id = str(chatID)

    try:
        miCursor.execute("UPDATE DATOSUSUARIOS SET OPENKEY = ? WHERE CHATID = ?", (openKey, chat_id))
        print("Registro actualizado con éxito")

    except Exception as e:
        print("Error al actualizar el registro: ", e)

    miConexion.commit()
    miConexion.close()

def actualizarDB_OrgKey(chatID, orgKey):
    miConexion = conectarBD(chatID)
    miCursor = miConexion.cursor()

    chat_id = str(chatID)

    try:
        miCursor.execute("UPDATE DATOSUSUARIOS SET ORGANIZATIONKEY = ? WHERE CHATID = ?", (orgKey, chat_id))
        print("Registro actualizado con éxito")

    except Exception as e:
        print("Error al actualizar el registro: ", e)

    miConexion.commit()
    miConexion.close()

#! OPEN WEATHER =========================================================================================
def actualizarDB_openW(chatID, weatherKey):
    miConexion = conectarBD(chatID)
    miCursor = miConexion.cursor()

    chat_id = str(chatID)

    try:
        miCursor.execute("UPDATE DATOSUSUARIOS SET WEATHERKEY = ? WHERE CHATID = ?", (weatherKey, chat_id))
        print("Registro actualizado con éxito")

    except Exception as e:
        print("Error al actualizar el registro: ", e)

    miConexion.commit()
    miConexion.close()