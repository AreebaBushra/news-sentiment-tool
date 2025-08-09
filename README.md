

```markdown
# 📰 News Sentiment Analysis Tool

A web-based application that fetches the latest news headlines and performs sentiment analysis to classify them as **Positive**, **Negative**, or **Neutral**.  
This tool helps users quickly gauge the general mood of the news in real time.

## 🚀 Features
- Fetches live news headlines using **NewsAPI** (or sample news if no API key is provided).
- Performs sentiment analysis using Python's `TextBlob`.
- Displays results in a simple and interactive dashboard.
- Easy to deploy on **Render**, **Railway**, or **PythonAnywhere**.

## 📂 Project Structure
```

.
├── app.py              # Main Flask application
├── templates/
│   ├── index.html      # Dashboard UI
├── static/
│   ├── style.css       # Styling for the dashboard
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation

````

## 🛠️ Installation & Usage
### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App Locally

```bash
python app.py
```

The app will be available at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**.

---

## 🌐 Deployment

### **Deploy to Render**

1. Create a new **Web Service** on [Render](https://render.com/).
2. Connect your GitHub repo.
3. Set the **Start Command** to:

```bash
gunicorn app:app
```

4. Add a **Build Command**:

```bash
pip install -r requirements.txt
```

5. Click **Deploy**.

---

## 🔑 API Key (Optional)

* Get your free API key from [NewsAPI](https://newsapi.org/).
* Create a `.env` file in the project root and add:

```env
NEWS_API_KEY=your_api_key_here
```

* If no key is provided, the app will use sample news.

---

## 📸 Screenshots

![Dashboard Screenshot](screenshot.png)

---

## 📜 License

This project is licensed under the MIT License.

```

Do you want me to make that one too?
```
