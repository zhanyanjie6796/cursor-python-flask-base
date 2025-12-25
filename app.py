from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask 網站</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .container {
                text-align: center;
                padding: 3rem;
                background: rgba(255, 255, 255, 0.05);
                border-radius: 20px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
            }
            h1 {
                color: #e94560;
                font-size: 3rem;
                margin-bottom: 1rem;
                text-shadow: 0 0 30px rgba(233, 69, 96, 0.5);
            }
            p {
                color: #ffffff;
                font-size: 1.2rem;
                opacity: 0.9;
            }
            .emoji { font-size: 4rem; margin-bottom: 1rem; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🚀</div>
            <h1>Hello Flask!</h1>
            <p>歡迎來到你的第一個 Flask 網站</p>
        </div>
    </body>
    </html>
    """


@app.route("/api/hello")
def api_hello():
    return {"message": "Hello from Flask API!", "status": "success"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

