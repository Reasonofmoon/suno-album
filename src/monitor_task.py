# src/monitor_task.py
from suno_client import SunoClient
import time
import json
import sys

TASK_ID = "53a547a5103da653750d0e99ebad093c" # From latest run

def main():
    client = SunoClient()
    print(f"🕵️ Monitoring Task: {TASK_ID}")
    
    while True:
        status = client.get_generation_status(TASK_ID)
        
        if not status:
            print("⚠️ No status returned. Retrying...")
            time.sleep(10)
            continue
            
        # Parse based on discovered structure
        # data -> response -> sunoData -> [ list of clips ]
        try:
            data = status.get('data', {})
            overall_status = data.get('status')
            
            clips = []
            if 'response' in data and 'sunoData' in data['response']:
                clips = data['response']['sunoData']
            
            print(f"   Status: {overall_status} | Clips found: {len(clips)}")
            
            # Check if complete
            # Criteria: audioUrl is not empty
            complete = False
            if clips and len(clips) > 0:
                # Check if ANY or ALL have audioUrl? Usually we want to see if valid URLs exist.
                # If audioUrl is filled, it's done.
                completed_clips = [c for c in clips if c.get('audioUrl')]
                
                if len(completed_clips) == len(clips):
                   complete = True
                   print("🎉 All clips completed!")
                elif len(completed_clips) > 0:
                   print(f"⚠️ Partial completion: {len(completed_clips)}/{len(clips)} ready.")
                   
            if complete:
                print("\n🎵 Final Results:")
                for clip in clips:
                    print(f"   - Title: {clip.get('title')}")
                    print(f"   - Audio MP3: {clip.get('audioUrl')}")
                    print(f"   - Stream: {clip.get('streamAudioUrl')}")
                    print(f"   - Video: {clip.get('videoUrl', 'N/A')}")
                    print(f"   - Image: {clip.get('imageUrl')}")
                break
                
        except Exception as e:
            print(f"❌ Error parsing status: {e}")
            
        time.sleep(15)

if __name__ == "__main__":
    main()
