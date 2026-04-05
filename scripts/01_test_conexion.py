import pyodbc

# Configuración de conexión según tus capturas previas
# Cambia 'TU_CONTRASEÑA' por la que asignaste al usuario CPFSQL2025
config = {
    'driver': '{ODBC Driver 17 for SQL Server}', # Usando el driver de tu captura
    'server': 'JOEL-LT',                         # Tu servidor
    'database': 'NDFPCYFCH',                     # Tu BD de Fiscalía
    'user': 'CPFSQL2025',                        # Tu usuario creado
    'password': 'A1JOEL*@#'                  
}

def probar_conexion():
    try:
        conn_str = (
            f"DRIVER={config['driver']};"
            f"SERVER={config['server']};"
            f"DATABASE={config['database']};"
            f"UID={config['user']};"
            f"PWD={config['password']};"
            "Encrypt=no;" # Recomendado para conexiones locales de prueba
        )
        
        conn = pyodbc.connect(conn_str)
        print("✅ ¡Éxito! Python se conectó a la BD de la Fiscalía de Familia.")
        
        # Una pequeña consulta para validar acceso a tablas
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 1 name FROM sys.tables")
        row = cursor.fetchone()
        if row:
            print(f"🔎 Conexión verificada. Primera tabla encontrada: {row[0]}")
            
        conn.close()
    except Exception as e:
        print(f"❌ Error al conectar: {e}")

if __name__ == "__main__":
    probar_conexion()