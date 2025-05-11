from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379) 

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f"Hello! You have visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) #내로컬호스트이 5000포트에서 실행해라는뜻인듯