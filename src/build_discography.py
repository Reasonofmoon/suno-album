# build_discography.py
# Add Werther's Mirror album to discography.json
import json
import os
import re

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISCO_PATH = os.path.join(PROJECT_ROOT, "assets", "discography.json")
ALBUM_MD = os.path.join(PROJECT_ROOT, "music-system", "albums", "werthers_mirror.md")
TRACKS_JSON = os.path.join(PROJECT_ROOT, "music-system", "albums", "werthers_mirror_tracks.json")

# Read existing discography
with open(DISCO_PATH, "r", encoding="utf-8") as f:
    discography = json.load(f)

# Read track metadata from API results
with open(TRACKS_JSON, "r", encoding="utf-8") as f:
    api_tracks = json.load(f)

# Read album markdown for lyrics
with open(ALBUM_MD, "r", encoding="utf-8") as f:
    md_content = f.read()

# Parse lyrics blocks from markdown
def extract_lyrics(md, track_num):
    """Extract lyrics between ### Suno Lyrics ``` blocks for a given track"""
    # Find the track section
    pattern = rf"## Track {track_num:02d}.*?### Suno Lyrics\s*```\s*\n(.*?)```"
    match = re.search(pattern, md, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "[Lyrics not found]"

# Track definitions
track_defs = [
    {"num": 1, "title": "윤곽 없는 사람"},
    {"num": 2, "title": "당신이라는 빛"},
    {"num": 3, "title": "네가 보는 나"},
    {"num": 4, "title": "부드러운 연습"},
    {"num": 5, "title": "고백 연습장"},
    {"num": 6, "title": "거울의 정원"},
    {"num": 7, "title": "사라질까 봐"},
    {"num": 8, "title": "내 이름으로 서는 법"},
    {"num": 9, "title": "베르테르의 고백"},
    {"num": 10, "title": "나라는 계절"},
]

# Build tracks
tracks = []
for tdef in track_defs:
    num = tdef["num"]
    title = tdef["title"]
    num_str = f"{num:02d}"
    
    # Extract lyrics
    lyrics = extract_lyrics(md_content, num)
    
    # Get Suno image URL from API data (first variant)
    api_matches = [t for t in api_tracks if t["number"] == num_str and t["variant"] == 1]
    suno_img = api_matches[0]["image_url"] if api_matches else ""
    
    track_entry = {
        "id": f"werthers_{num_str}_{title.replace(' ', '_')}",
        "title": title,
        "lyrics": lyrics,
        "art": f"assets/cover_werthers_mirror.png",  # Use album cover for all
        "versions": [
            {
                "name": "Ver 1",
                "file": f"assets/werthers_{num_str}_{title.replace(' ', '_')}_v1.mp3"
            },
            {
                "name": "Ver 2",
                "file": f"assets/werthers_{num_str}_{title.replace(' ', '_')}_v2.mp3"
            }
        ]
    }
    tracks.append(track_entry)
    print(f"  Track {num_str}: {title} | lyrics={len(lyrics)} chars")

# Build album entry
album_entry = {
    "id": "album_5",
    "title": "베르테르의 거울 (Werther's Mirror)",
    "artist": "Reason Moon",
    "cover_art": "assets/cover_werthers_mirror.png",
    "tracks": tracks
}

# Check if album_5 already exists
existing_ids = [a["id"] for a in discography]
if "album_5" in existing_ids:
    # Replace
    discography = [a for a in discography if a["id"] != "album_5"]
    print("\n  Replacing existing album_5")

discography.append(album_entry)

# Save
with open(DISCO_PATH, "w", encoding="utf-8") as f:
    json.dump(discography, f, ensure_ascii=False, indent=4)

print(f"\nDiscography updated: {len(discography)} albums, album_5 has {len(tracks)} tracks")
print(f"Saved to: {DISCO_PATH}")
