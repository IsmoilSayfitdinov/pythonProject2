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
        photo = """
            CREATE TABLE IF NOT EXISTS photo(
                id SERIAL PRIMARY KEY,
                chat_id BIGINT,
                photo_id VARCHAR(300),
                status BOOLEAN default False
            )
        """
        likes = """
            CREATE TABLE IF NOT EXISTS likes(
                id SERIAL PRIMARY KEY,
                users_id INT REFERENCES users(id),
                photo_id INT REFERENCES photo(id),
                is_like BOOLEAN default False
            )
        """

        self.cursor.execute(photo)
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
    
    def get_chat_id_photo_users(self, chat_id):
        query = f"SELECT * FROM photo WHERE chat_id = {chat_id} AND status = true"
        self.cursor.execute(query)
        res = self.cursor.fetchone()
        return res
    
    def add_photo(self, data: dict):
        chat_id = data['chat_id']
        photo_id = data['photo_id']
        status = True
        query = f"INSERT INTO photo (chat_id, photo_id, status) VALUES ({chat_id}, '{photo_id}', {status})"
        self.cursor.execute(query)
        self.conn.commit()
        return True
    
    def get_random_photo(self):
        import random
        query = f"SELECT * FROM photo WHERE status = true"
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        return random.choice(res)
        