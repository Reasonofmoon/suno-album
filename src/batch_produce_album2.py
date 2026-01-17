import sys
import time
import subprocess
import os

# 8 Tracks for Album 2: "Office Serendipity"
TOPICS = [
    "Morning Coffee Ritual (모닝 커피 리추얼) - Lo-Fi Hip Hop",
    "Empty Elevator (빈 엘리베이터의 행운) - Smooth Jazz / Bossa",
    "Sunny Window Seat (창가 자리의 햇살) - Acoustic Guitar/Piano",
    "Lunchtime Stroll (점심시간의 산책) - City Pop (Chill)",
    "Focus Flow (몰입의 즐거움) - Deep House / Downtempo",
    "Unexpected Praise (뜻밖의 칭찬) - Upbeat Jazz Piano",
    "Rainy Office View (비 오는 창밖 풍경) - Ambient / Rain Sounds",
    "Leaving Work on Time (칼퇴근의 발걸음) - Synthwave / Funky"
]

INSTRUCTION = "IMPORTANT: Lyrics MUST be strictly in Korean (Hangul). The vibe is 'Office Serendipity' - BGM for working professionals. Focus on small, happy moments. Musical style should be instrumental-heavy, lo-fi, jazz, or ambient, suitable for background functioning."

def run_command(cmd):
    print(f"👉 Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        return False
    return True

def main():
    print("🚀 Starting Album 2: 'Office Serendipity'")
    
    for i, topic in enumerate(TOPICS):
        print(f"\n==========================================")
        print(f"💿 Album 2 - Track {i+1}/8: {topic}")
        print(f"==========================================")
        
        # 1. Compose (Calls Agents -> Updates next_track.json)
        # Pass the extra instruction as the second argument
        if not run_command(f'python src/compose.py "{topic}" "{INSTRUCTION}"'):
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
            
            # 4. Publish (Targeting album_2)
            if not run_command(f'python src/publish.py {task_id} album_2'):
                print("❌ Publishing failed/timed out.")
            else:
                # 5. Auto-Commit
                print("💾 Committing to Git...")
                # We commit index.html too in case structure changed in previous steps
                run_command(f'git add . && git commit -m "Feat: Add Album 2 Track {topic}" && git push origin main')

        except Exception as e:
            print(f"❌ Error during publishing setup: {e}")
            
        # 6. Safety Sleep
        print("💤 Cooling down for 30s...")
        time.sleep(30)

if __name__ == "__main__":
    main()
