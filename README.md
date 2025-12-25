# 🚀 Flask 快速部署範例

這是一個最簡單的 Python Flask 網站範例，可以輕鬆從 GitHub 部署到雲端。

---

## 📁 專案結構

```
├── app.py              # Flask 主程式
├── requirements.txt    # Python 依賴套件
├── render.yaml         # Render 部署配置
└── README.md           # 說明文件
```

---

## 🖥️ 本地執行

### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

### 2. 啟動伺服器

```bash
python app.py
```

### 3. 開啟瀏覽器

前往 http://localhost:5000 即可看到網站！

---

## 🌐 網站路由

| 路由 | 說明 | 回應類型 |
|------|------|----------|
| `/` | 首頁 | HTML 網頁 |
| `/api/hello` | API 範例 | JSON 資料 |

---

## ☁️ 部署到網路（免費）

### 方法：使用 Render 平台

**Render** 提供免費的網站託管服務，可以直接從 GitHub 自動部署。

#### 步驟一：將程式碼推送到 GitHub

**新建倉庫時執行：**

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/zhanyanjie6796/cursor-python-flask-base.git
git push -u origin main
```

**如果已有本地倉庫：**

```bash
git remote add origin https://github.com/zhanyanjie6796/cursor-python-flask-base.git
git branch -M main
git push -u origin main
```

#### 步驟二：在 Render 部署

1. 前往 [render.com](https://render.com) 並註冊帳號（可用 GitHub 登入）
2. 點擊右上角 **New** → **Web Service**
3. 選擇 **Build and deploy from a Git repository**
4. 連接你的 GitHub 帳號並選擇此倉庫
5. Render 會自動偵測 `render.yaml` 設定檔
6. 點擊 **Create Web Service**
7. 等待約 2-3 分鐘完成部署
8. 部署完成後，網站網址為：**https://cursor-python-flask-base.onrender.com**

---

## ⚠️ 注意事項

### 關於 GitHub Pages

GitHub Pages **只能託管靜態網頁**（HTML、CSS、JavaScript），**無法執行 Python 程式**。

如果需要執行 Flask 這類後端程式，必須使用支援 Python 的平台：

| 平台 | 免費方案 | 特色 |
|------|----------|------|
| [Render](https://render.com) | ✅ 有 | 自動從 GitHub 部署 |
| [Vercel](https://vercel.com) | ✅ 有 | 需額外設定 |
| [Railway](https://railway.app) | ✅ 有限制 | 簡單好用 |
| [PythonAnywhere](https://pythonanywhere.com) | ✅ 有 | 專為 Python 設計 |

---

## 🛠️ 常見問題

### Q: 為什麼不能用 GitHub Pages？
A: GitHub Pages 是靜態網站託管服務，無法執行伺服器端程式（如 Python、Node.js）。Flask 需要 Python 執行環境，必須使用支援動態網站的平台。

### Q: Render 免費版有什麼限制？
A: 免費版的服務會在閒置時自動休眠，下次訪問時需要約 50 秒或更久的喚醒時間。

### Q: 如何新增更多頁面？
A: 在 `app.py` 中新增路由即可，例如：

```python
@app.route("/about")
def about():
    return "<h1>關於我們</h1>"
```

---

## 📝 授權

本專案為範例程式碼，可自由使用與修改。

