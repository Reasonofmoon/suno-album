import sys
import time
import subprocess
import os

TOPICS = [
    "Sleepless Night - Insomnia",
    "Sleepless Night - Neon Rain",
    "Sleepless Night - 3AM Coffee",
    "Sleepless Night - Empty Subway",
    "Sleepless Night - Digital Ghosts",
    "Sleepless Night - White Noise",
    "Sleepless Night - Lonely Satellite",
    "Sleepless Night - Lucid Dream",
    "Sleepless Night - Night Drive",
    "Sleepless Night - Dawn Breaking"
]

def run_command(cmd):
    print(f"👉 Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        return False
    return True

def main():
    print("🚀 Starting Batch Production: 10 Tracks (Sleepless Night)")
    
    for i, topic in enumerate(TOPICS):
        if i < 6: continue # Skip first 6 tracks (already done)
        print(f"\n==========================================")
        print(f"💿 Track {i+1}/10: {topic}")
        print(f"==========================================")
        
        # 1. Compose (Calls Agents -> Updates next_track.json)
        # We pass the topic to compose.py
        if not run_command(f'python src/compose.py "{topic}"'):
            continue
            
        # 2. Generate (Calls Suno -> Updates metadata)
        # Assuming generate_track.py reads next_track.json
        if not run_command('python src/generate_track.py'):
            continue
            
        # 3. Publish (Downloads Assets -> Updates content.js)
        # We need the task ID. `generate_track.py` usually saves it to `latest_task_id.txt`
        # But `generate_track.py` in its current state might not run publishing.
        # Let's check `generate_track.py` workflow.
        # It currently runs generation and that's it.
        # We need to grab the task ID from `latest_task_id.txt`
        
        try:
            with open("latest_task_id.txt", "r") as f:
                task_id = f.read().strip()
            
            # 4. Wait for Audio (Suno takes ~2 mins)
            # We can run `publish.py` which will fail if audio isn't ready, OR
            # Use our polling script logic.
            # Best way: Use `publish.py` but loop it? No, `publish.py` just fetches once.
            
            print(f"⏳ Waiting 2 minutes for audio generation (Task: {task_id})...")
            time.sleep(120) 
            
            # 5. Publish
            if not run_command(f'python src/publish.py {task_id}'):
                print("❌ Publishing failed/timed out.")
            else:
                # 6. Auto-Commit
                print("💾 Committing to Git...")
                run_command(f'git add . && git commit -m "Feat: Add Track {topic}" && git push origin main')

        except Exception as e:
            print(f"❌ Error during publishing setup: {e}")
            
        # 7. Safety Sleep
        print("💤 Cooling down for 30s...")
        time.sleep(30)

if __name__ == "__main__":
    main()
