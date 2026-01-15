import sys
import time
from suno_client import SunoClient

def main():
    task_id = "55b3d150a4544b971c0c8551cb4ba749"
    client = SunoClient()
    print(f"Waiting for audio for Task: {task_id}")
    
    for i in range(30): # Wait 5 minutes max
        status = client.get_generation_status(task_id)
        if status:
            clips = status.get('data', {}).get('response', {}).get('sunoData', [])
            if clips and clips[0].get('audioUrl'):
                print("✅ Audio is ready!")
                return
        print(f"[{i+1}/30] Still processing...")
        time.sleep(10)
    print("❌ Timed out.")

if __name__ == "__main__":
    main()
