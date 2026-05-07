import os
import socket
import redis
from flask import Flask

app = Flask(__name__)

r = redis.from_url(os.environ.get("REDIS_URL"), decode_responses=True)

@app.get("/")
def hello():
    r.incr("counter")
    return "hello railway"

@app.get("/stats")
def stats():
    return "count =" + r.get("counter")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
