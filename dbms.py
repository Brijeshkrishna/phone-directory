import sqlite3

class database:
    def __init__(self) -> None:
        self.connect = sqlite3.connect("phones.db", check_same_thread=False)
        self.cur = self.connect.cursor()

    def create_tabel(self):
        self.cur.execute(
            """CREATE TABLE games_list(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                country_code INT,
                phone_number INT
            )
            """
        )
        self.connect.commit()

    def insert(self, name, country_code, phone_number):
        self.cur.execute(
            """INSERT INTO games_list (name, country_code, phone_number) VALUES (?,?,?) """,
            (name, country_code,phone_number),
        )
        self.connect.commit()



    def get_users(self):
        self.cur.execute("""SELECT * FROM games_list ORDER BY id""")
        self.connect.commit()
        return self.cur.fetchall()

