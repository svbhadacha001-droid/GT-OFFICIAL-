from flask import Flask
import os

app = Flask(__name__)

# ફાઈનલ કોડ
html_design = """
<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GT OFFICIAL ♛</title>
    <style>
        body { 
            background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), url('https://i.imgur.com/vH9Jj8v.jpeg'); 
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white; 
            font-family: 'Segoe UI', sans-serif; 
            text-align: center; 
            padding: 20px; 
            min-height: 100vh; 
        }
        .container { max-width: 500px; margin: auto; }
        .box { background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(10px); border: 2px solid #ffd700; padding: 25px; border-radius: 20px; margin-bottom: 20px; text-align: left; }
        .btn { background: linear-gradient(45deg, #ffd700, #ff8c00); color: black; padding: 15px; border: none; cursor: pointer; border-radius: 50px; font-weight: bold; width: 100%; margin-top: 20px; transition: 0.3s; }
        .btn:hover { transform: scale(1.05); }
        input, select { width: 100%; padding: 14px; margin: 10px 0; border-radius: 12px; border: 1px solid #ffd700; background: rgba(0,0,0,0.5); color: white; box-sizing: border-box; }
        .rule-list { list-style-type: none; padding-left: 0; }
        .rule-list li { margin: 10px 0; padding-left: 25px; position: relative; color: #ffcc00; }
        .rule-list li::before { content: '♛'; position: absolute; left: 0; }
        .hidden { display: none; }
        h1 { color: #ffd700; text-shadow: 2px 2px 10px #000; }
        .footer { font-size: 10px; color: gray; margin-top: 30px; opacity: 0.7; }
    </style>
</head>
<body>
    <div class="container">
        <div id="welcome_screen">
            <h1 style="margin-top: 50px;">WELCOME<br>GT OFFICIAL ♛</h1>
            <button class="btn" onclick="showRules()">ENTER NOW</button>
        </div>

        <div id="main_content" class="hidden">
            <div class="box">
                <h3 style="color: #ffd700; text-align: center;">🎯 ગિલ્ડના નિયમો</h3>
                <ul class="rule-list">
                    <li>Player daily online</li>
                    <li>Gujrati player only</li>
                    <li>Weekly glori push 7/8 k</li>
                    <li>Without guild test entry</li>
                    <li>Koi pan problem hoi guild leder sate vat karo</li>
                    <li>No hat other guild</li>
                </ul>
            </div>

            <div class="box">
                <h2 style="text-align: center; color: #ffd700;">📝 Join Form</h2>
                <label>🎮 FREE FIRE U_ID:</label>
                <input type="text" id="ff_uid" placeholder="UID લખો">
                <label>💬 INSTAGRAM/WHATSAPP:</label>
                <input type="text" id="contact_info" placeholder="તમારું નામ/નંબર">
                <label>📩 કોનો સંપર્ક કરવો છે:</label>
                <select id="admin_select">
                    <option value="917990843839">Leader (7990843839)</option>
                    <option value="919023506977">Acting Leader (9023506977)</option>
                </select>
                <button class="btn" onclick="submitRequest()">SUBMIT REQUEST</button>
            </div>
            
            <div class="footer">Created by SATISH</div>
        </div>
    </div>

    <script>
        function showRules() {
            document.getElementById('welcome_screen').style.display = 'none';
            document.getElementById('main_content').classList.remove('hidden');
        }
        function submitRequest() {
            var uid = document.getElementById("ff_uid").value;
            var contact = document.getElementById("contact_info").value;
            var adminNumber = document.getElementById("admin_select").value;
            if(uid == "" || contact == "") { alert("બધી વિગતો ભરો!"); return; }
            var message = "🔥 *GT OFFICIAL ♛ GUILD JOIN REQUEST* 🔥\\n\\n🎮 *UID:* " + uid + "\\n💬 *Name/Contact:* " + contact;
            window.location.href = "https://wa.me/" + adminNumber + "?text=" + encodeURIComponent(message);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return html_design

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

