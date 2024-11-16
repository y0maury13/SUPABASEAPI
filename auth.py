from dotenv import load_dotenv
import os
from supabase import create_client, Client

# Cargar las variables de entorno
load_dotenv()

# Obtener URL y clave desde las variables de entorno
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Crear el cliente de Supabase
supabase: Client = create_client(url, key)

# Datos del usuario
user = supabase.auth.sign_up({ "juansanchez@python.com": Email })
print(user)