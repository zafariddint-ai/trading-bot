from flask import Flask, request
import requests
import requests
app = Flask(name)
BOT_TOKEN = "9206124491:AAFxu_3Nd4QIIfr6ku3ZkyZThmOvi8bc1YU" CHAT_ID = "5779661411"
@app.route('/webhook', methods=['POST']) def webhook(): data = request.data.decode('utf-8')
if data:
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🚨 **TradingView Alert:**\n\n{data}",
        "parse_mode": "Markdown"
    }
    requests.post(telegram_url, json=payload)
    return "OK", 200

return "No Data", 400if name == 'main': app.run(host='0.0.0.0', port=5000)
