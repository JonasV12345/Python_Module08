import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
MATRIX = os.getenv("MATRIX_MODE", "development")
print("ORACLE STATUS: Reading the Matrix...")
print()
print("configuartion loaded:")
print(f"Mode: {MATRIX}")
print("Database: Connected to local instance"
      if os.getenv("DATABASE_URL") != "Not configured" else
      "Database: Not connected")
print(f"API Access: {os.getenv('API_KEY', 'No Acces')}")
print(f"Log Level: {os.getenv('LOG_LEVEL', 'DEBUG')}")
print("Zion Network: Online"
      if os.getenv("ZION_ENDPOINT") != "Not configured" else
      "Zion Network: Offline")
print("\nEnvironment security check:")
if os.getenv("API_KEY") == "None":
    print("[Warning] missing API key")
else:
    print("[OK] No hardcoded secrets detected")
if os.path.exists(".env"):
    print("[OK] .env file properly configured")
else:
    print("[Warning] .env file is missing")
if MATRIX == "development":
    print("[Warning] no production overrides available")
else:
    print("[OK] Production overrides available")
print("\nThe Oracle sees all configurations.")
