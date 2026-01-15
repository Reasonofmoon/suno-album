# src/publish.py
import sys
import json
import os
import re
import requests
from suno_client import SunoClient

# Configuration
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_FILE = os.path.join(PROJECT_ROOT, "content.js")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
BASE_URL = "assets/" # URL used in content.js for the player

def clean_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title).replace(" ", "_").lower()

def update_content_js(new_track_data):
    """
    Updates content.js with the new track data.
    """
    with open(CONTENT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the injection point (end of tracks array)
    # Looking for the last closing bracket of the tracks array
    # We assume 'tracks': [ ... ] structure
    
    # Strategy: Load the JS object as JSON (skipping the assignment)
    # Then dump back to JS format.
    
    # 1. Extract JSON part
    start_idx = content.find('{')
    json_str = content[start_idx:content.rfind(';')]
    
    # JavaScript object keys often aren't quoted, and it uses backticks for lyrics.
    # Python's json parser won't like that.
    # So we will do a text insertion instead.
    
    # Construct the JS string for the new track
    new_track_js = json.dumps(new_track_data, indent=8)
    # Fix lyrics quotes to backticks for multiline support
    # (JSON dump escapes newlines as \n, we want literal newlines with backticks)
    lyrics_json_str = json.dumps(new_track_data['lyrics'])
    lyrics_literal = "`" + new_track_data['lyrics'].replace("`", "\`") + "`"
    
    # Replace the lyrics line in the JSON string
    # We look for "lyrics": "..." and replace with "lyrics": `...`
    # Note: json.dumps escapes control characters.
    
    # Simpler approach: Just construct the string manually
    versions_str = ",\n                ".join([
        f'{{ "name": "{v["name"]}", "file": "{v["file"]}" }}' for v in new_track_data['versions']
    ])
    
    track_entry = f"""
        {{
            "id": "{new_track_data['id']}",
            "title": "{new_track_data['title']}",
            "lyrics": `{new_track_data['lyrics']}`,
            "art": "{new_track_data['art']}",
            "versions": [
                {versions_str}
            ]
        }}"""

    # Insert before the last closing bracket/brace sequence of the tracks array
    # We look for the closing of the tracks array `    ]`
    insert_pos = content.rfind('    ]')
    
    if insert_pos == -1:
        # Fallback for empty or minified
        insert_pos = content.rfind(']')
    
    if insert_pos == -1:
        print("❌ Could not find tracks array end in content.js")
        return

    # specific check to add a comma if it's not the first item
    prefix = "," if "tracks: [" not in content[insert_pos-20:insert_pos] else ""
    
    new_content = content[:insert_pos] + prefix + track_entry + "\n" + content[insert_pos:]
    
    with open(CONTENT_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ content.js updated successfully.")

def download_file(url, filename):
    filepath = os.path.join(ASSETS_DIR, filename)
    print(f"⬇️ Downloading {filename}...")
    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"   Saved to {filepath}")
            return f"assets/{filename}"
        else:
            print(f"❌ Failed download: {r.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error downloading: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/publish.py <TASK_ID>")
        return

    task_id = sys.argv[1]
    client = SunoClient()
    
    print(f"🔎 Fetching Task: {task_id}")
    status = client.get_generation_status(task_id)
    
    if not status:
        print("❌ Failed to get status.")
        return

    # Parse Data
    import pprint
    pprint.pprint(status)
    try:
        clips = status['data']['response']['sunoData']
    except KeyError:
        print("❌ Unexpected JSON structure.")
        return

    if not clips:
        print("❌ No clips found.")
        return

    # Assume all clips belong to same "Track Concept"
    base_clip = clips[0]
    title = base_clip.get('title', 'Unknown Track')
    lyrics = base_clip.get('prompt', '')
    safe_title = clean_filename(title)
    
    # Download Art (from first clip)
    art_filename = f"cover_{safe_title}.jpeg"
    art_path = download_file(base_clip['imageUrl'], art_filename)

    versions = []
    for i, clip in enumerate(clips):
        # Audio
        fname = f"{safe_title}_v{i+1}_{clip['id'][:4]}.mp3"
        audio_path = download_file(clip['audioUrl'], fname)
        
        if audio_path:
            versions.append({
                "name": f"Ver {i+1} ({clip.get('modelName', 'V5')})",
                "file": audio_path
            })

    if not versions:
        print("❌ No audio files downloaded.")
        return

    # Construct Data Object
    new_track = {
        "id": task_id,
        "title": title,
        "lyrics": lyrics,
        "art": art_path,
        "versions": versions
    }
    
    # Update JS
    update_content_js(new_track)
    print("\n🎉 Publishing Complete! Open index.html to view.")

if __name__ == "__main__":
    main()
