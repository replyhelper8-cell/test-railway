import os
from flask import Flask

app = Flask(__name__)

counter = 0

@app.get("/")
def hello():
    global counter
    counter += 1
    return "hello railway"

@app.get("/stats")
def stats():
    global counter
    return "count =" + str(counter)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
