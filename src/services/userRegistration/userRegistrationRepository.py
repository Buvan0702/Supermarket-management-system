import mysql.connector
from db_config import get_db_connection

# Register user in the database
def register_user(first_name, last_name, email, password_hash):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO users (first_name, last_name, email, password_hash)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (first_name, last_name, email, password_hash))
        connection.commit()

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        raise Exception(f"Database error occurred: {err}")
    except Exception as e:
        raise Exception(f"Unexpected error during user registration: {str(e)}")

# Validate user credentials during login
def validate_user(email):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user
    except mysql.connector.Error as err:
        raise Exception(f"Database error occurred: {err}")
    except Exception as e:
        raise Exception(f"Unexpected error during user validation: {str(e)}")

# Delete user with cascading delete
def delete_user(user_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        connection.commit()

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        raise Exception(f"Database error occurred: {err}")
    except Exception as e:
        raise Exception(f"Unexpected error during user deletion: {str(e)}")
