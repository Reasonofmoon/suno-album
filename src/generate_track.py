# src/generate_track.py
from suno_client import SunoClient
from system_prompts import MUSIC_STYLE_TAGS
import time
import json
import os

# Load Track Data
try:
    with open("next_track.json", "r", encoding='utf-8') as f:
        track_data = json.load(f)
        TRACK_TITLE = track_data.get("title", "Unknown Plateau")
        STYLE = track_data.get("tags", "experimental")
        LYRICS = track_data.get("prompt", "[Instrumental]")
        print(f"📂 Loaded Track: {TRACK_TITLE}")
except FileNotFoundError:
    print("❌ 'next_track.json' not found. Please run 'src/compose.py' first.")
    exit(1)

API_KEY = os.getenv("SUNO_COOKIE")
if not API_KEY:
    print("⚠️ Warning: SUNO_COOKIE not found in environment. Client might fail if auth is required.")

def main():
    print(f"🚀 Starting Generation for: {TRACK_TITLE}")
    print(f"🎨 Style: {STYLE}")

    # NOTE: API_KEY needs to be defined or imported if SunoClient requires it.
    # The original code called SunoClient() without arguments.
    client = SunoClient(API_KEY)

    # 1. Generate
    response = client.generate_music(
        prompt=LYRICS,
        style=STYLE,
        title=TRACK_TITLE,
        model="V5",
        custom_mode=True
    )

    if not response:
        print("❌ Generation failed (No response).")
        return

    # Extract Task ID (Robust extraction)
    task_id = None
    if 'data' in response and isinstance(response['data'], str):
         task_id = response['data']
    elif 'data' in response and isinstance(response['data'], dict):
         task_id = response['data'].get('task_id') or response['data'].get('id') or response['data'].get('taskId')

    # Fallback: check if the response itself is the ID (some wrappers do this)
    if not task_id and 'id' in response:
        task_id = response['id']

    if not task_id:
        print(f"❌ Could not extract Task ID. Saving full response to debug_response.json")
        with open("debug_response.json", "w") as f:
            json.dump(response, f, indent=2)
        return

    print(f"✅ Generation Initiated. Task ID: {task_id}")
    
    # Save Task ID for recovery
    with open("latest_task_id.txt", "w") as f:
        f.write(task_id)

    # 2. Poll for Status
    metadata = None
    for status in client.wait_for_completion(task_id, timeout=300):
        if not status:
            continue
        
        # Check if complete (logic depends on specific API response structure)
        # Assuming status returns list of clips or a status object
        print(f"   Status update: {str(status)[:100]}...") # Truncate log
        
        # Heuristic for completion: check for 'status': 'complete' or 'audio_url' presence
        # Based on wrapper, 'data' might be a list of clips.
        clips = []
        if 'data' in status and isinstance(status['data'], list):
            clips = status['data']
        elif isinstance(status, list):
            clips = status
        
        # Check clips status
        all_complete = False
        if clips:
            complete_count = sum(1 for c in clips if c.get('status') in ['complete', 'streaming'])
            if complete_count == len(clips) and len(clips) > 0:
                all_complete = True
                metadata = clips
        
        if all_complete:
            print("🎉 Generation Complete!")
            break
    
    # 3. Save Metadata / URLs
    if metadata:
        save_metadata(metadata)
        print("\n🎵 Generated Clips:")
        for clip in metadata:
            print(f"   - Title: {clip.get('title')}")
            print(f"   - Audio URL: {clip.get('audio_url')}")
            print(f"   - Video URL: {clip.get('video_url')}")
            print(f"   - ID: {clip.get('id')}")
    else:
        print("⚠️ Timed out or no metadata retrieved.")

def save_metadata(data):
    filename = f"output/metadata/{int(time.time())}_rhizome.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"💾 Metadata saved to {filename}")

if __name__ == "__main__":
    main()
