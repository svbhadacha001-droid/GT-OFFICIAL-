from flask import Flask
import os

app = Flask(__name__)

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
        .btn-insta { background: linear-gradient(45deg, #833ab4, #fd1d1d, #fcaf45); color: white; padding: 15px; border: none; cursor: pointer; border-radius: 50px; font-weight: bold; width: 100%; margin-top: 10px; transition: 0.3s; }
        .btn:hover, .btn-insta:hover { transform: scale(1.05); }
        input { width: 100%; padding: 14px; margin: 10px 0; border-radius: 12px; border: 1px solid #ffd700; background: rgba(0,0,0,0.5); color: white; box-sizing: border-box; }
        .rule-list { list-style-type: none; padding-left: 0; }
        .rule-list li { margin: 10px 0; padding-left: 25px; position: relative; color: #ffcc00; }
        .rule-list li::before { content: '♛'; position: absolute; left: 0; }
        .hidden { display: none; }
        h1 { color: #ffd700; text-shadow: 2px 2px 10px #000; }
        .footer { font-size: 8px; color: #888; margin-top: 20px; letter-spacing: 1px; }
        /* લીડરબોર્ડ ટેબલ સ્ટાઈલ */
        .glory-table { width: 100%; color: white; border-collapse: collapse; margin-top: 10px; }
        .glory-table td, .glory-table th { padding: 8px; border-bottom: 1px solid #444; }
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
                <h3 style="color: #ffd700; text-align: center;">🏆 TOP GLORY PLAYERS</h3>
                <table class="glory-table">
                    <tr><th>Player</th><th>Glory</th></tr>
                    <tr><td>GT DADDY</td><td style="color:#ffd700">9500</td></tr>
                    <tr><td>Player 2</td><td style="color:#ffd700">8200</td></tr>
                    <tr><td>Player 3</td><td style="color:#ffd700">7500</td></tr>
                </table>
            </div>

            <div class="box">
                <h2 style="text-align: center; color: #ffd700;">📝 Join Form</h2>
                <label>🎮 FREE FIRE U_ID:</label>
                <input type="text" id="ff_uid" placeholder="UID લખો">
                <label>💬 તમારું નામ/નંબર:</label>
                <input type="text" id="contact_info" placeholder="નામ અથવા નંબર લખો">
                <button class="btn" onclick="submitRequest()">SUBMIT REQUEST</button>
                
                <a href="https://www.instagram.com/gt_daddy_01" target="_blank" style="text-decoration: none;">
                    <button class="btn-insta">FOLLOW ON INSTAGRAM 📸</button>
                </a>
            </div>
            
            <div class="footer">CREATED BY SATISH</div>
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
            if(uid == "" || contact == "") { alert("બધી વિગતો ભરો!"); return; }
            var message = "🔥 *GT OFFICIAL ♛ JOIN REQUEST* 🔥\\n\\n🎮 *UID:* " + uid + "\\n💬 *Contact:* " + contact;
            window.location.href = "https://wa.me/917990843839?text=" + encodeURIComponent(message);
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
