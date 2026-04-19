from flask import Flask, request, jsonify
import subprocess
import hashlib
import psycopg2
import redis
import os

app = Flask(__name__)

cache = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379)

def get_db():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'appdb'),
        user=os.getenv('DB_USER', 'appuser'),
        password=os.getenv('DB_PASSWORD', 'secret')
    )

# Уязвимость 1 — Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True)
    return result.stdout.decode()

# Уязвимость 2 — SQL Injection
@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return jsonify(cur.fetchall())

# Уязвимость 3 — слабый хэш
@app.route('/hash')
def hash_password():
    password = request.args.get('password')
    return hashlib.md5(password.encode()).hexdigest()

# Уязвимость 4 — hardcoded secret
SECRET_KEY = "super_secret_key_12345"
AWS_KEY = "AKIAIOSFODNN7ABCDEFG"

@app.route('/')
def index():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
