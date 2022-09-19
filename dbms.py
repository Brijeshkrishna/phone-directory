import sqlite3
from typing import Any, List

class database:
    def __init__(self) -> None:
        self.connect = sqlite3.connect("phones.db", check_same_thread=False)
        self.cur = self.connect.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS phone_dir(
                id INTEGER PRIMARY KEY AUTOINCREMENT ,
                name TEXT,
                phone TEXT,
                email TEXT
            )
            """
        )
        self.connect.commit()

    def check_phone(self, phone: str) -> bool:
        self.cur.execute("SELECT * FROM phone_dir  WHERE phone = ? ", (phone,))
        self.connect.commit()
        temp = self.cur.fetchone()
        if temp == () or temp == None:
            return True
        return False

    def insert_user(self, name: str, phone: str, email: str) -> None:
        if self.check_phone(phone):
            self.cur.execute(
                """INSERT INTO phone_dir 
                        (name,phone,email) 
                        VALUES (?,?,?) """,
                (name, phone, email),
            )
            self.connect.commit()

    def update_user(
        self, name: str, phone: str, email: str, previse_phone_number: str
    ) -> None:
        self.cur.execute(
            "UPDATE phone_dir set name = ? , phone = ?, email = ? where phone = ? ",
            (name, phone, email, previse_phone_number),
        )
        self.connect.commit()

    def delete(self, phone_number: str) -> None:
        self.cur.execute("delete from phone_dir where phone = ? ", (phone_number,))
        self.connect.commit()

    def get_user(self, phone: str) -> List[Any]:
        self.cur.execute("""SELECT * FROM phone_dir where phone= ?""", (phone,))
        self.connect.commit()
        return self.cur.fetchone()

    def get_all_users(self) -> List[Any]:
        self.cur.execute("""SELECT * FROM phone_dir  order by id """)
        self.connect.commit()
        return self.cur.fetchall()
