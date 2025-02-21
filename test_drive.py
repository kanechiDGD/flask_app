from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Configurar credenciales
SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "flaskapp-451604.json"  # Asegúrate de que este archivo esté en tu proyecto
DRIVE_FILE_ID = "1vgucV7LtzOO0laXz-_PZIwqHAp7CQM0N"  # ID de tu archivo en Google Drive

try:
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build("drive", "v3", credentials=creds)
    
    # Intentar obtener el archivo
    file = service.files().get(fileId=DRIVE_FILE_ID).execute()
    print(f"✅ Conexión exitosa. Nombre del archivo: {file['name']}")
except Exception as e:
    print(f"❌ Error conectando con Google Drive: {e}")
