# src/fetch_tracks.py - v3: correct field path = data.response.sunoData (camelCase)
import requests
import json
import os

API_KEY = "d38063ca1110014b3e5fc55b7a09c5a6"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

task_ids = [
    ("01", "윤곽 없는 사람", "20ada1335a90bc98451095707dd0265e"),
    ("02", "당신이라는 빛", "0fc158963adc17ddb1b004016548df20"),
    ("03", "네가 보는 나", "412e0f28b0bbf43dc40a76f5e7801447"),
    ("04", "부드러운 연습", "77d430330a7fb1fe422dda8cc894ad9c"),
    ("05", "고백 연습장", "a1561ea2214fc94d38984e6004263e85"),
    ("06", "거울의 정원", "b2d357ed03d0d0e43ead45397e76942f"),
    ("07", "사라질까 봐", "6879dbe8a40424f5978f5e7fe4aba228"),
    ("08", "내 이름으로 서는 법", "815eea08a734bcfbbc1a39fb02c5e687"),
    ("09", "베르테르의 고백", "e3c1ea97d04030482e937e4cb99da0fd"),
    ("10", "나라는 계절", "86b04354f4b617b87e9ab8cd45260881"),
]

all_tracks = []

for num, name, tid in task_ids:
    try:
        r = requests.get(
            "https://api.sunoapi.org/api/v1/generate/record-info",
            params={"taskId": tid},
            headers=headers,
            timeout=15
        )
        d = r.json()
        task_data = d.get("data", {})
        
        # Correct path: data.response is a dict with "sunoData" (camelCase)
        resp = task_data.get("response", {})
        if isinstance(resp, str):
            try:
                resp = json.loads(resp)
            except:
                resp = {}
        
        suno_data = resp.get("sunoData", [])
        
        if suno_data:
            for i, item in enumerate(suno_data):
                track = {
                    "number": num,
                    "title": name,
                    "variant": i + 1,
                    "audio_url": item.get("audioUrl", ""),
                    "source_audio_url": item.get("sourceAudioUrl", ""),
                    "stream_audio_url": item.get("streamAudioUrl", ""),
                    "image_url": item.get("imageUrl", ""),
                    "image_large_url": item.get("imageLargeUrl", ""),
                    "duration": item.get("duration", 0),
                    "id": item.get("id", ""),
                    "suno_title": item.get("title", ""),
                }
                all_tracks.append(track)
                dur = track["duration"]
                has_audio = "YES" if track["audio_url"] else "NO"
                print(f"  {num} {name} v{i+1}: {dur:.1f}s | audio={has_audio} | id={track['id'][:20]}")
        else:
            print(f"  {num} {name}: No sunoData found. Status: {task_data.get('status', '?')}")
            
    except Exception as e:
        print(f"  {num} {name}: ERROR - {e}")

# Save results
output_dir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "music-system", "albums"
)
output_path = os.path.join(output_dir, "werthers_mirror_tracks.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_tracks, f, ensure_ascii=False, indent=2)

print(f"\nTotal tracks: {len(all_tracks)}")
print(f"Saved to: {output_path}")

# Download audio files
audio_dir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "assets", "audio", "werthers-mirror"
)
os.makedirs(audio_dir, exist_ok=True)

print(f"\nDownloading audio to: {audio_dir}")
for track in all_tracks:
    url = track["audio_url"] or track["source_audio_url"]
    if not url:
        print(f"  SKIP {track['number']}-v{track['variant']}: no audio URL")
        continue
    
    filename = f"{track['number']}_{track['variant']}_{track['title'].replace(' ','_')}.mp3"
    filepath = os.path.join(audio_dir, filename)
    
    try:
        print(f"  Downloading {filename}...", end=" ", flush=True)
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(resp.content)
        size_mb = len(resp.content) / (1024 * 1024)
        print(f"OK ({size_mb:.1f} MB)")
    except Exception as e:
        print(f"FAIL: {e}")

print("\nDone!")
