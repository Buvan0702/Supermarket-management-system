import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_connection():
    """Establish connection to the MySQL database"""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),  # Default to localhost
            user=os.getenv("DB_USER", "root"),      # Default to root user
            password=os.getenv("DB_PASSWORD", ""),  # Default to empty password
            database=os.getenv("DB_NAME", "supermarket_db")  # Default database name
        )

        if connection.is_connected():
            print("✅ Successfully connected to MySQL database")
        return connection
    except mysql.connector.Error as err:
        print(f"❌ Error while connecting to MySQL: {err}")
        return None

