from flask import Flask, render_template_string, request

app = Flask(__name__)

# Data storage
submissions = []
ADMIN_PASSWORD = "9023506977" 

html_design = """
<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <title>GT OFFICIAL ♛</title>
    <style>
        body { background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('https://i.imgur.com/vH9Jj8v.jpeg'); background-size: cover; background-position: center; color: white; text-align: center; padding: 20px; font-family: sans-serif; min-height: 100vh; }
        .box { background: rgba(0,0,0,0.7); border: 2px solid #ffd700; padding: 20px; border-radius: 20px; margin: auto; max-width: 400px; }
    </style>
</head>
<body>
    <div class="box">
        <h1>GT OFFICIAL ♛</h1>
        <form action="/submit" method="POST">
            <input type="text" name="uid" placeholder="UID lakho" required style="width:90%; padding:10px; margin:5px; border-radius:10px;"><br>
            <input type="text" name="name" placeholder="Tamaru nam/number" required style="width:90%; padding:10px; margin:5px; border-radius:10px;"><br>
            <button type="submit" style="width:90%; padding:12px; background:#ffd700; border:none; border-radius:20px; cursor:pointer; font-weight:bold;">SUBMIT REQUEST</button>
        </form>
    </div>
</body>
</html>
"""

admin_page = """
<h1>Admin Panel</h1>
<h3>👥 Form bharnar ni vigato:</h3>
{% for sub in submissions %}
    <div style="border:1px solid #ffd700; padding:10px; margin:5px; border-radius:10px;">
        <p>🎮 UID: {{ sub.uid }} <br> 💬 Nam/Number: {{ sub.name }}</p>
    </div>
{% endfor %}
"""

@app.route('/')
def home():
    return render_template_string(html_design)

@app.route('/submit', methods=['POST'])
def submit():
    uid = request.form.get('uid')
    name = request.form.get('name')
    submissions.append({'uid': uid, 'name': name})
    # WhatsApp link (Fakt leader no number che)
    wa_link = f"https://wa.me/917990843839?text=GT+OFFICIAL+♛+Join+Request:%0AUID:+{uid}%0AName:+{name}"
    return f'<script>window.location.href="{wa_link}";</script>'

@app.route('/admin')
def admin():
    pwd = request.args.get('pass')
    if pwd == ADMIN_PASSWORD:
        return render_template_string(admin_page, submissions=submissions)
    else:
        return "Access Denied! Khoṭo password."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


