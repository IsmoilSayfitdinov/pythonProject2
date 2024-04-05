import psycopg2 as db
from main import config
class Database:
    def __init__(self):
        self.conn = db.connect(
            database=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            port=config.DB_PORT
        )
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def create_table(self):
        users = """
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                chat_id BIGINT,
                full_name VARCHAR(88),
                username VARCHAR(20),
                bio VARCHAR(200),
                create_date TIMESTAMP default now()
            )
        """
        flowers = """
            CREATE TABLE IF NOT EXISTS flowers(
                follower_id SERIAL PRIMARY KEY,
                followes_id INT,
                FOREIGN KEY (followes_id) REFERENCES users (id)
            )
        """

        self.cursor.execute(flowers)
        self.conn.commit()
    def chat_id_cheakc(self, chat_id):
        query = f"SELECT * FROM users WHERE chat_id = {chat_id}"
        self.cursor.execute(query)
        res = self.cursor.fetchone()
        self.cursor.fetchall()
        return res

    def add_users(self,data: dict):
        chat_id = data['chat_id']
        fullname = data['fullname']
        usernmae = data['username']
        bio = data['bio']
        query = f"INSERT INTO users (chat_id, full_name, username, bio) VALUES ({chat_id}, '{fullname}', '{usernmae}', '{bio}')"
        self.cursor.execute(query)
        self.conn.commit()
        return True

    def get_users_data(self):
        query = f"SELECT * FROM users"
        self.cursor.execute(query)
        res = self.cursor.fetchone()
        self.cursor.fetchall()
        return res