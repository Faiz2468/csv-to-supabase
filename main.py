import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Load CSV
csv_file = "data.csv"

try:
    df = pd.read_csv(csv_file)
    print(f"✅ CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
except FileNotFoundError:
    print("❌ CSV file not found. Make sure 'data.csv' is in the same folder.")
    exit()

# Upload to Supabase table
for index, row in df.iterrows():
    data = row.to_dict()
    try:
        response = supabase.table("students").insert(data).execute()
        print(f"✅ Row {index + 1} uploaded:", response)
    except Exception as e:
        print(f"❌ Error uploading row {index + 1}:", e)
