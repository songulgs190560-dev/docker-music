import requests
import sys

def search_music(term):
    print(f"\n--- '{term}' için sonuçlar getiriliyor ---\n")
    url = "https://itunes.apple.com/search"
    params = {"term": term, "entity": "song", "limit": 5}
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["resultCount"] == 0:
            print("Sonuç bulunamadı.")
            return

        for track in data["results"]:
            print(f"🎵 Şarkı: {track['trackName']}")
            print(f"👤 Sanatçı: {track['artistName']}")
            print(f"💿 Albüm: {track['collectionName']}")
            print(f"🔗 Dinle: {track['previewUrl']}")
            print("-" * 30)
            
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    # Eğer CMD'den isim girilmezse varsayılan olarak 'Tarkan' ara
    search_term = sys.argv[1] if len(sys.argv) > 1 else "Tarkan"
    search_music(search_term)
