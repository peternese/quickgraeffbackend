import os
import requests

# Get Supabase API Key from Environment Variables
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

# Save shortened URL
def save_url(short: str, original: str):
    data = {"short": short, "original": original}
    response = requests.post(f"{SUPABASE_URL}/urls", json=data, headers=HEADERS)
    return response.json()

# Retrieve original URL
def get_original_url(short: str):
    response = requests.get(f"{SUPABASE_URL}/urls?short=eq.{short}", headers=HEADERS)
    data = response.json()
    return data[0]["original"] if data else None

# Erster Versuch über PostgreSQL Supabase, alelrdings nicht erfolgreich, da supabase die Verbindung über Vercel blockiert. Nun über API Zugriff # 
# import os
# import psycopg2

# # PostgreSQL-Verbindungsdetails aus Umgebungsvariable
# DATABASE_URL = os.environ.get("DATABASE_URL")

# # Verbindung zur PostgreSQL-Datenbank herstellen
# conn = psycopg2.connect(DATABASE_URL, sslmode="require")
# c = conn.cursor()

# # Tabelle erstellen, falls sie nicht existiert
# c.execute("""
#     CREATE TABLE IF NOT EXISTS urls (
#         short TEXT PRIMARY KEY, 
#         original TEXT
#     )
# """)
# conn.commit()

# # Funktion zum Speichern einer URL
# def save_url(short: str, original: str):
#     c.execute("INSERT INTO urls (short, original) VALUES (%s, %s)", (short, original))
#     conn.commit()

# # Funktion zum Abrufen einer originalen URL
# def get_original_url(short: str):
#     c.execute("SELECT original FROM urls WHERE short=%s", (short,))
#     return c.fetchone()
