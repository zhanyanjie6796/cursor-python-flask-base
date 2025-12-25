from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


def log_visitor():
    """記錄訪問者資訊到控制台"""
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr
    path = request.path
    user_agent = request.user_agent.string
    print(f"[訪問] {log_time} | IP: {ip} | 頁面: {path} | 裝置: {user_agent}")


@app.route("/")
def home():
    log_visitor()
    return render_template("index.html")


@app.route("/api/hello")
def api_hello():
    log_visitor()
    return {"message": "Hello from Flask API!", "status": "success"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
