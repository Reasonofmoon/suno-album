import sys
import time
import subprocess
import os

# 8 Distinct Styles/Themes for "Different Styles and Lyrics"
TOPICS = [
    "Neon Samurai - Cyberpunk Trap",
    "Solar Storm - High Energy Drum & Bass",
    "Digital Forest - Organic Ambient",
    "Glitch Bazaar - World Fusion Electronic",
    "Quantum Jazz - Acid Jazz Lo-Fi",
    "Velvet Void - Dark R&B",
    "Chrome Heart - Retro Synthwave",
    "Data Cathedral - Orchestral Electronic"
]

def run_command(cmd):
    print(f"👉 Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        return False
    return True

def main():
    print("🚀 Starting Phase 2: 8 New Distinct Tracks")
    
    for i, topic in enumerate(TOPICS):
        if i < 2: continue # Skip Neon Samurai & Solar Storm (Done)
        print(f"\n==========================================")
        print(f"💿 Track {i+1}/8: {topic}")
        print(f"==========================================")
        
        # 1. Compose (Calls Agents -> Updates next_track.json)
        if not run_command(f'python src/compose.py "{topic}"'):
            continue
            
        # 2. Generate (Calls Suno -> Updates metadata)
        if not run_command('python src/generate_track.py'):
            continue
            
        # 3. Wait for Audio
        try:
            with open("latest_task_id.txt", "r") as f:
                task_id = f.read().strip()
            
            print(f"⏳ Waiting 2 minutes for audio generation (Task: {task_id})...")
            # Wait loop or simple sleep
            time.sleep(130) 
            
            # 4. Publish
            if not run_command(f'python src/publish.py {task_id}'):
                print("❌ Publishing failed/timed out.")
            else:
                # 5. Auto-Commit
                print("💾 Committing to Git...")
                run_command(f'git add . && git commit -m "Feat: Add Phase 2 Track {topic}" && git push origin main')

        except Exception as e:
            print(f"❌ Error during publishing setup: {e}")
            
        # 6. Safety Sleep
        print("💤 Cooling down for 30s...")
        time.sleep(30)

if __name__ == "__main__":
    main()
