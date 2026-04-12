import subprocess
import sqlite3

# Уязвимость 1 — Command Injection
def get_file(filename):
    result = subprocess.run("cat " + filename, shell=True)
    return result

# Уязвимость 2 — SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return cursor.fetchall()

# Уязвимость 3 — Hardcoded secret
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD="SuperSecret123!"
AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
AWS_ACCESS_KEY_ID="AKIAIOSFODNN7ABCDEFG"
