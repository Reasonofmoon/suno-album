# src/find_tracks.py
from suno_client import SunoClient
import json

def main():
    client = SunoClient()
    print("🔎 Fetching recent generations...")
    try:
        data = client.get_songs()
        # The API usually returns a list of songs/clips.
        # Structure varies, assume it's a list.
        if not data:
            print("No data returned.")
            return

        # Debug: print keys of first item if possible
        # print(json.dumps(data[0], indent=2))
        
        # We need to group by title or ID
        print(f"Found {len(data)} items.")
        
        # Display last 5
        seen_ids = set()
        count = 0
        for song in data:
            if count >= 10: break
            
            # Extract info
            sid = song.get('id')
            title = song.get('title', 'Untitled')
            status = song.get('status', 'Unknown')
            
            # Since generating creates 2 clips per task, the task ID is often hidden or same as clip ID?
            # Actually, `get_songs` usually returns individual clips.
            # We want the "Task ID" usually associated with the generation.
            # BUT `publish.py` expects a Task ID to fetch the *pair*.
            # Wait, `publish.py` calls `get_generation_status(task_id)`.
            # If `get_songs` returns clips, how do we get the original generation Task ID?
            # Inspecting `suno_client.py` might be needed.
            # The 'get_songs' endpoint might output `metadata` containing `audio_prompt_id` or similar.
            
            print(f"- [{status}] {title} (ID: {sid})")
            count += 1

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
