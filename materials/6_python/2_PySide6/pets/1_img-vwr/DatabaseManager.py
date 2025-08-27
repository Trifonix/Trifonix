import sqlite3
import hashlib

class DatabaseManager:
    def __init__(self, db_name="materials/6_python/2_PySide6/pets/1_img-vwr/images.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS images (
                md5_hash TEXT PRIMARY KEY,
                path TEXT,
                is_favorite INTEGER
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY,
                tag_name TEXT UNIQUE
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS image_tags (
                md5_hash TEXT,
                tag_id INTEGER,
                FOREIGN KEY(md5_hash) REFERENCES images(md5_hash),
                FOREIGN KEY(tag_id) REFERENCES tags(id)
            )
        ''')
        self.conn.commit()

    def add_image(self, path):
        with open(path, 'rb') as f:
            md5_hash = hashlib.md5(f.read()).hexdigest()
        self.cursor.execute("INSERT OR IGNORE INTO images (md5_hash, path, is_favorite) VALUES (?, ?, 0)", (md5_hash, path))
        self.conn.commit()
        return md5_hash

    # TODO
    # Методы для добавления/удаления тегов

    def update_best_image(self, path, it_was_best):
        md5_hash = self.add_image(path)
        it_was_best = int(not it_was_best)
        self.cursor.execute("UPDATE images SET is_favorite = ? WHERE md5_hash = ?", (it_was_best, md5_hash,))
        self.conn.commit()
        return md5_hash

    def get_image(self, path):
        md5_hash = self.add_image(path)
        self.cursor.execute("SELECT is_favorite FROM images WHERE md5_hash = ?", (md5_hash,))
        is_best = self.cursor.fetchone()
        return is_best[0]
