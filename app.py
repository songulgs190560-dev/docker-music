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
            --accent-color: #1DB954; /* Spotify Yeşili */
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
            padding: 40px 0;
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
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .card {
            background-color: var(--card-color);
            padding: 20px;
            border-radius: 12px;
            transition: background 0.3s;
            text-align: center;
        }

        .card:hover {
            background-color: #282828;
        }

        .card img {
            width: 100%;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            margin-bottom: 15px;
        }

        .card h3 {
            margin: 10px 0 5px 0;
            font-size: 18px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .card p {
            color: var(--secondary-text);
            font-size: 14px;
            margin-bottom: 15px;
        }

        audio {
            width: 100%;
            height: 35px;
            filter: invert(1); /* Player'ı karanlık modla uyumlu yapar */
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎵 iTunes Explorer</h1>
        <div class="search-box">
            <form method="GET" action="/" style="display: contents;">
                <input type="text" name="search" placeholder="Şarkı veya sanatçı ara..." value="{{ term }}">
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
