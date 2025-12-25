from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# Tasarım ve HTML yapısı (Komple Yenilendi)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music Discovery</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #121212;
            --card-color: #181818;
            --accent-color: #1DB954;
            --text-color: #ffffff;
            --secondary-text: #b3b3b3;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
        }

        .header {
            text-align: center;
            padding: 30px 0;
        }

        .search-box {
            margin-bottom: 40px;
            display: flex;
            justify-content: center;
            gap: 10px;
        }

        input[type="text"] {
            padding: 12px 20px;
            width: 300px;
            border-radius: 25px;
            border: none;
            outline: none;
            font-size: 16px;
            background: #282828;
            color: white;
        }

        button {
            padding: 12px 25px;
            border-radius: 25px;
            border: none;
            background-color: var(--accent-color);
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
        }

        button:hover {
            transform: scale(1.05);
            background-color: #1ed760;
        }

        .container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 25px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .card {
            background-color: var(--card-color);
            padding: 15px;
            border-radius: 12px;
            transition: transform 0.3s, background 0.3s;
            text-align: center;
        }

        .card:hover {
            background-color: #282828;
            transform: translateY(-5px);
        }

        .card img {
            width: 100%;
            aspect-ratio: 1/1;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            margin-bottom: 15px;
            object-fit: cover;
        }

        .card h3 {
            margin: 10px 0 5px 0;
            font-size: 16px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .card p {
            color: var(--secondary-text);
            font-size: 13px;
            margin-bottom: 15px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        audio {
            width: 100%;
            height: 30px;
            filter: invert(0.8);
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎵 iTunes Explorer</h1>
        <div class="search-box">
            <form method="GET" action="/" style="display: flex; gap: 10px;">
                <input type="text" name="search" placeholder="Sanatçı veya şarkı..." value="{{ term }}">
                <button type="submit">KEŞFET</button>
            </form>
        </div>
    </div>

    <div class="container">
        {% for track in tracks %}
        <div class="card">
            <img src="{{ track.artworkUrl100.replace('100x100', '400x400') }}" alt="Kapak">
            <h3>{{ track.trackName }}</h3>
            <p>{{ track.artistName }}</p>
            <audio controls src="{{ track.previewUrl }}"></audio>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    # Arama terimini al, yoksa 'Tarkan' varsayılan yap
    term = request.args.get("search", "Tarkan")
    url = f"https://itunes.apple.com/search?term={term}&entity=song&limit=20"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        tracks = data.get("results", [])
    except Exception as e:
        print(f"Hata: {e}")
        tracks = []

    return render_template_string(HTML_TEMPLATE, tracks=tracks, term=term)

if __name__ == "__main__":
    # Docker ve dış erişim için 0.0.0.0 şart
    app.run(host='0.0.0.0', port=5000)
