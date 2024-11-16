from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

# Conexión a Supabase
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

try:
    # Obtener datos
    data = supabase.table("CRUD").select("Nombre Completo,Carrera,Universidad").execute()
    
    print("\nLista de Estudiantes:")
    print("-" * 60)
    print(f"{'No.':<4} {'Nombre Completo':<25} {'Carrera':<20} {'Universidad':<20}")
    print("-" * 60)
    
    for i, registro in enumerate(data.data, 1):
        print(f"{i:<4} {registro['Nombre Completo']:<25} {registro['Carrera']:<20} {registro['Universidad']:<20}")
    
    print("-" * 60)
    print(f"Total de registros: {len(data.data)}")
    
except Exception as e:
    print(f"Error: {str(e)}")