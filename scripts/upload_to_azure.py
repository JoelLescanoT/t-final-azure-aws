import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# 1. Cargamos la configuración del archivo .env
load_dotenv()
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

def crear_contenedor_y_subir(nombre_contenedor, ruta_local, nombre_nube):
    try:
        # Conectamos con el Data Lake
        service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Creamos el contenedor (si no existe)
        container_client = service_client.get_container_client(nombre_contenedor)
        if not container_client.exists():
            container_client.create_container()
            print(f"✅ Contenedor '{nombre_contenedor}' creado con éxito.")

        # Subimos el archivo
        blob_client = service_client.get_blob_client(container=nombre_contenedor, blob=nombre_nube)
        
        print(f"⏳ Subiendo archivo '{nombre_nube}'...")
        with open(ruta_local, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        
        print(f"🚀 ¡Éxito total! Archivo disponible en Azure.")

    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

# --- PARTE PARA TU PRUEBA ---
# 1. Crea un archivo de texto simple llamado "prueba.txt" en tu carpeta del proyecto
# 2. Descomenta la línea de abajo (quítale el #) y ejecútalo:
crear_contenedor_y_subir("landing-zone", "prueba.txt", "primer_test.txt")