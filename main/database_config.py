import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to connect to MySQL Database using .env variables
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),          # Load from .env file
            user=os.getenv("DB_USER"),          # Load from .env file
            password=os.getenv("DB_PASSWORD"),  # Load from .env file
            database=os.getenv("DB_NAME")       # Load from .env file
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
