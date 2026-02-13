import sys
import time
import json
import subprocess
import os
from suno_client import SunoClient

# Load Track Data
DATA_FILE = os.path.join(os.path.dirname(__file__), "album4_data.json")

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
    # Optional: start from a specific track index
    start_from = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    
    tracks = load_data()
    client = SunoClient()
    
    print(f"🚀 Starting Production for Album 4: Curiosity ({len(tracks)} tracks)")
    if start_from > 0:
        print(f"   ⏩ Resuming from track {start_from + 1}")
    
    for i, track in enumerate(tracks):
        if i < start_from:
            continue
            
        print(f"\n==========================================")
        print(f"💿 Producing Track {i+1}/{len(tracks)}: {track['title']}")
        print(f"   🎨 Style: {track['style']}")
        print(f"==========================================")
        
        # 1. Generate Music
        prompt = track['lyrics']
        style = track['style']
        title = track['title']
        
        print("🎵 Calling Suno API...")
        response = client.generate_music(
            prompt=prompt,
            style=style,
            title=title,
            model="V5",
            custom_mode=True
        )
        
        if not response:
            print("❌ Generation request failed. Skipping...")
            continue
            
        # Extract Task ID (handle multiple response formats)
        task_id = None
        try:
            if isinstance(response, dict):
                if 'data' in response:
                    data = response['data']
                    if isinstance(data, str):
                        task_id = data
                    elif isinstance(data, dict):
                        task_id = data.get('taskId') or data.get('task_id') or data.get('id')
                elif 'clips' in response:
                    task_id = response['clips'][0]['id']
                elif 'id' in response:
                    task_id = response['id']
            elif isinstance(response, list) and len(response) > 0:
                task_id = response[0]['id']
        except Exception as e:
            print(f"❌ Error parsing response ID: {e}")
            
        if not task_id:
            print(f"⚠️ Unknown response format. Dumping response:")
            print(json.dumps(response, indent=2, ensure_ascii=False)[:500])
            continue

        print(f"✅ Generation Started! Task ID: {task_id}")
        
        # Save task ID for recovery
        with open("latest_task_id.txt", "w") as f:
            f.write(f"{task_id}\n{title}\n{i}")
        
        # 2. Wait for audio generation (Suno typically takes 2-3 minutes)
        print("⏳ Waiting 150 seconds for audio generation...")
        time.sleep(150)
        
        # 3. Publish (downloads MP3, cover art, updates discography.json)
        print("📥 Downloading and Publishing...")
        if not run_command(f'python src/publish.py {task_id} album_4'):
            print("❌ Publishing failed.")
        else:
            print("💾 Committing to Git...")
            safe_title = title.replace('"', '\\"')
            run_command(f'git add . && git commit --no-gpg-sign -m "Feat: Add Curiosity Track {i+1} - {safe_title}" && git push origin main')
            
        print("💤 Cooling down for 30s...")
        time.sleep(30)

    print("\n🎉 Album 4 'Curiosity' Production Complete!")

if __name__ == "__main__":
    main()
