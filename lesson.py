import sqlite3
from pathlib import Path

db_file = Path("E:/CodexOutput/python_practice/data/lesson.db")
db_file.parent.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(db_file)
print(type(connection))

connection.execute(
    "CREATE TABLE IF NOT EXISTS demo (id INTEGER PRIMARY KEY, name TEXT)"
)
connection.commit()
connection.close()

print("数据库文件存在：", db_file.exists())