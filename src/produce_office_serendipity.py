import sys
import time
import json
import subprocess
import os
from suno_client import SunoClient

# Load Track Data
DATA_FILE = os.path.join(os.path.dirname(__file__), "album2_data.json")

def load_data():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_command(cmd):
    print(f"👉 Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        return False
    return True

def main():
    tracks = load_data()
    client = SunoClient()
    
    print(f"🚀 Starting Production for Album 2: Office Serendipity ({len(tracks)} tracks)")
    
    for i, track in enumerate(tracks):
        print(f"\n==========================================")
        print(f"💿 Producing Track {i+1}/{len(tracks)}: {track['title']}")
        print(f"==========================================")
        
        # 1. Generate Music
        # We need to decide if we use 'custom' mode or not. Lyrics implies custom mode.
        prompt = track['lyrics']
        style = track['style']
        title = track['title']
        
        print("🎵 Calling Suno API...")
        # Since this script runs locally, we assume the user has credits.
        response = client.generate_music(
            prompt=prompt,
            style=style,
            title=title,
            model="V5", # Updated to V5 as per latest docs
            custom_mode=True
        )
        
        if not response:
            print("❌ Generation request failed. Skipping...")
            continue
            
        # The response structure from wrapper usually contains the task/clip IDs
        # Let's inspect it carefully. wrapper returns response.json()
        # Typically: {'id': '...'} or {'clips': [...]}
        # Our publish.py expects a Task ID (or Clip ID) to fetch status.
        # Let's find a valid ID.
        try:
             # Often returns a list of clips or a task ID
            if 'clips' in response:
                task_id = response['clips'][0]['id'] 
            elif 'id' in response:
                task_id = response['id']
            elif 'data' in response and isinstance(response['data'], dict) and 'taskId' in response['data']:
                task_id = response['data']['taskId'] # Handle {'code': 200, 'data': {'taskId': '...'}}
            elif isinstance(response, list) and len(response) > 0:
                task_id = response[0]['id']
            else:
                print(f"⚠️ Unknown response format: {response}")
                continue
        except Exception as e:
             print(f"❌ Error parsing response ID: {e}")
             continue

        print(f"✅ Generation Started! Task ID: {task_id}")
        
        # 2. Wait
        print("⏳ Waiting 150 seconds for audio generation...")
        time.sleep(150) # 2.5 minutes
        
        # 3. Publish
        print("📥 Downloading and Publishing...")
        if not run_command(f'python src/publish.py {task_id} album_2'):
            print("❌ Publishing failed.")
        else:
            print("💾 Committing to Git...")
            run_command(f'git add . && git commit -m "Feat: Add Album 2 Track {title}" && git push origin main')
            
        print("💤 Cooling down for 30s...")
        time.sleep(30)

    print("\n🎉 Album Production Batch Complete!")

if __name__ == "__main__":
    main()
