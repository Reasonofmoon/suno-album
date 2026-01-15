# src/download_assets.py
import requests
import os

TRACKS = [
    {
        "filename": "rhizome_v1.mp3",
        "url": "https://musicfile.api.box/YThmMTA3M2ItM2E2NC00M2RlLWE3ZTktOTMyY2E3NTAxNzJh.mp3"
    },
    {
        "filename": "rhizome_v2.mp3",
        "url": "https://musicfile.api.box/OTQ0MzFiNTEtNjNhYi00ZmQzLTljZTQtNGNlMDg1MTVkZmIw.mp3"
    }
]

OUTPUT_DIR = r"c:\Users\sound\Documents\MyZettelkasten\05 Projects\Reason_Moon_Album\assets"

def main():
    if not os.path.exists(OUTPUT_DIR):
        print(f"Creating directory: {OUTPUT_DIR}")
        os.makedirs(OUTPUT_DIR)

    for track in TRACKS:
        print(f"⬇️ Downloading {track['filename']}...")
        try:
            r = requests.get(track['url'], stream=True)
            if r.status_code == 200:
                filepath = os.path.join(OUTPUT_DIR, track['filename'])
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"✅ Saved to {filepath}")
            else:
                print(f"❌ Failed to download {track['filename']}: Status {r.status_code}")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
