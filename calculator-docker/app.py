from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)

# Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():
    return "Calculator + Redis Running"

@app.route("/add")
def add():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    result = a + b

    # Store last result in Redis
    r.set("last_result", result)

    return jsonify({"result": result})

@app.route("/last")
def last():
    result = r.get("last_result")
    return jsonify({"last_result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

