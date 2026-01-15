# src/check_library.py
from suno_client import SunoClient
import json

def main():
    client = SunoClient()
    print("🔎 Fetching recent songs...")
    songs = client.get_songs()
    
    if not songs:
        print("❌ No songs returned or error occurred.")
        return

    print(json.dumps(songs, indent=2))
    
    # Check for Rhizome
    print("\n🎵 Recent Tracks:")
    # Handle list or dict return
    items = []
    if isinstance(songs, list):
        items = songs
    elif isinstance(songs, dict) and 'data' in songs:
        items = songs['data'] # Use getter if it's a dict
        
    for item in items[:5]: # Show top 5
        title = item.get('title')
        status = item.get('status')
        audio_url = item.get('audio_url')
        print(f"- [{status}] {title}: {audio_url}")

if __name__ == "__main__":
    main()
