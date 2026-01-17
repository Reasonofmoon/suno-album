import json
import os
import glob
import re

ASSETS_DIR = "assets"
JSON_PATH = os.path.join(ASSETS_DIR, "discography.json")

ALBUM_2_TRACKS = [
    "morning_coffee_(아침_커피)",
    "meeting_finished_(회의_끝)",
    "lunch_walk_(점심_산책)",
    "focus_mode_(집중_모드)",
    "sunset_window_(창가_노을)",
    "late_night_office_(야근의_미학)",
    "way_home_(퇴근길)",
    "sunday_night_prep_(일요일_밤의_다짐)",
    "brainstorming_(브레인스토밍)",
    "keyboard_rhythm_(키보드_리듬)"
]

def get_title_from_filename(filename_base):
    # 'morning_coffee_(아침_커피)' -> 'Morning Coffee (아침 커피)'
    title = filename_base.replace("_", " ")
    # Capitalize words
    return title.title()

def main():
    with open(JSON_PATH, 'r', encoding='utf-8-sig') as f:
        discography = json.load(f)

    # Find Album 2
    album2 = next((a for a in discography if a['id'] == 'album_2'), None)
    if not album2:
        print("Album 2 not found!")
        return

    # Clear existing tracks to avoid duplicates if partial
    album2['tracks'] = []

    for track_key in ALBUM_2_TRACKS:
        # Find files
        # pattern: track_key + "_v*.mp3"
        pattern = os.path.join(ASSETS_DIR, f"{track_key}_v*.mp3")
        files = glob.glob(pattern)
        
        if not files:
            print(f"No files found for {track_key}")
            continue
            
        # Sort files to get v1, v2
        files.sort()
        
        # Cover art
        # pattern: cover_track_key.jpeg or .png
        cover_pattern = os.path.join(ASSETS_DIR, f"cover_{track_key}.*")
        covers = glob.glob(cover_pattern)
        cover_art = covers[0].replace("\\", "/") if covers else "assets/cover_sketch.png"
        
        versions = []
        for i, file_path in enumerate(files):
            # Extract version name and file path relative to root
            filename = os.path.basename(file_path)
            # file path should be assets/filename
            relative_path = f"assets/{filename}"
            
            # Helper to get task id from filename if needed, but not critical
            # format: name_v1_taskid.mp3
            match = re.search(r'_v(\d)_([a-f0-9]+)\.mp3', filename)
            ver_num = match.group(1) if match else str(i+1)
            
            versions.append({
                "name": f"Ver {ver_num}",
                "file": relative_path
            })

        track_entry = {
            "id": f"track_{track_key}", # Simple ID
            "title": get_title_from_filename(track_key),
            "lyrics": "[Instrumental / Lyrics Unavailable]", 
            "art": cover_art,
            "versions": versions
        }
        
        album2['tracks'].append(track_entry)
        print(f"Added {track_key} with {len(versions)} versions.")

    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(discography, f, indent=4, ensure_ascii=False)
    
    print("Discography updated successfully.")

if __name__ == "__main__":
    main()
