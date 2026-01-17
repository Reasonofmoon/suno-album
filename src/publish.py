# src/publish.py
import sys
import json
import os
import re
import requests
from suno_client import SunoClient
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, USLT, error

# Configuration
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(PROJECT_ROOT, "assets", "discography.json")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
BASE_URL = "assets/"

def clean_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title).replace(" ", "_").lower()

def update_discography_json(new_track_data, album_id="album_1"):
    """
    Updates discography.json with the new track data for the specified album.
    """
    if not os.path.exists(DATA_FILE):
        print(f"❌ Error: {DATA_FILE} not found.")
        return

    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            discography = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Error decoding JSON: {e}")
        return

    # Find the album
    album_found = False
    for album in discography:
        if album['id'] == album_id:
            album['tracks'].append(new_track_data)
            album_found = True
            break
    
    if not album_found:
        print(f"❌ Album '{album_id}' not found in discography.")
        return

    # Write back
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(discography, f, indent=4, ensure_ascii=False)
    
    print(f"✅ discography.json updated successfully for {album_id}.")

def tag_mp3(audio_path, title, artist, album, art_path, lyrics=""):
    """
    Embeds ID3 tags into the MP3 file.
    """
    try:
        audio = MP3(audio_path, ID3=ID3)
        # Add ID3 tag if it doesn't exist
        try:
            audio.add_tags()
        except error:
            pass

        # Title
        audio.tags.add(TIT2(encoding=3, text=title))
        # Artist
        audio.tags.add(TPE1(encoding=3, text=artist))
        # Album
        audio.tags.add(TALB(encoding=3, text=album))
        
        # Lyrics (USLT)
        if lyrics:
             audio.tags.add(USLT(encoding=3, lang='eng', desc='Lyrics', text=lyrics))

        # Cover Art
        if art_path and os.path.exists(art_path):
            with open(art_path, 'rb') as albumart:
                audio.tags.add(
                    APIC(
                        encoding=3, 
                        mime='image/jpeg', 
                        type=3, 
                        desc=u'Cover',
                        data=albumart.read()
                    )
                )
        
        audio.save()
        print(f"   🏷️  Tagged: {title}")
    except Exception as e:
        print(f"❌ Error tagging MP3: {e}")

def download_file(url, filename):
    filepath = os.path.join(ASSETS_DIR, filename)
    # Check if file exists to avoid redownload? 
    # But usually we overwrite for updates.
    print(f"⬇️ Downloading {filename}...")
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.get(url, headers=headers, stream=True)
        if r.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"   Saved to {filepath}")
            return filepath
        else:
            print(f"❌ Failed download: {r.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error downloading: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/publish.py <TASK_ID> [ALBUM_ID]")
        return

    task_id = sys.argv[1]
    album_id = sys.argv[2] if len(sys.argv) > 2 else "album_1"
    
    # Map IDs to Album Names for tagging
    album_names = {
        "album_1": "A Thousand Plateaus",
        "album_2": "Office Serendipity"
    }
    album_title = album_names.get(album_id, "Reason Moon Album")

    client = SunoClient()
    
    print(f"🔎 Fetching Task: {task_id} for {album_id}")
    status = client.get_generation_status(task_id)
    
    if not status:
        print("❌ Failed to get status.")
        return

    # Parse Data logic (same as before)
    try:
        if 'sunoData' in status['data']['response']:
             clips = status['data']['response']['sunoData']
        elif isinstance(status['data'], list):
             clips = status['data']
        else:
             clips = [status['data']] 
    except KeyError as e:
        if isinstance(status, list):
            clips = status
        else:
            print(f"❌ Unexpected JSON structure: {e}")
            return

    if not clips:
        print("❌ No clips found.")
        return

    # Assume all clips belong to same "Track Concept"
    base_clip = clips[0]
    title = base_clip.get('title', 'Unknown Track')
    lyrics = base_clip.get('prompt', '') or base_clip.get('metadata', {}).get('prompt', '')
    safe_title = clean_filename(title)
    
    # Download Art
    art_filename = f"cover_{safe_title}.jpeg"
    # Fallback art if missing
    image_url = base_clip.get('imageUrl')
    if image_url:
        art_path = download_file(image_url, art_filename)
        art_web_path = f"{BASE_URL}{art_filename}"
    else:
        print("⚠️ No image URL found. Using default.")
        art_path = None
        art_web_path = "assets/cover_sketch.png"

    versions = []
    for i, clip in enumerate(clips):
        fname = f"{safe_title}_v{i+1}_{clip['id'][:4]}.mp3"
        url = clip.get('audioUrl') or clip.get('streamAudioUrl')
        if not url: continue
        
        audio_path = download_file(url, fname)
        if audio_path:
            tag_mp3(audio_path, title, "Reason Moon", album_title, art_path, lyrics)
            versions.append({
                "name": f"Ver {i+1} ({clip.get('modelName', 'V5')})",
                "file": f"{BASE_URL}{fname}"
            })

    if not versions:
        print("❌ No audio files downloaded.")
        return

    new_track = {
        "id": task_id,
        "title": title,
        "lyrics": lyrics,
        "art": art_web_path,
        "versions": versions
    }
    
    update_discography_json(new_track, album_id)
    print("\n🎉 Publishing Complete! (JSON Updated)")

if __name__ == "__main__":
    main()
