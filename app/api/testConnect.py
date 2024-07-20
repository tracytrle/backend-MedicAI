import psycopg2

try:
    conn = psycopg2.connect(
        dbname='medic_database',
        user='tracytrle',
        password='truc123',
        host='localhost',
        port='5432'
    )
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")