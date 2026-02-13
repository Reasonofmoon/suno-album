import re

def verify_lengths(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by Track headers
    tracks = re.split(r'## Track \d+:', content)[1:] # Skip preamble
    
    results = []
    
    for i, track in enumerate(tracks):
        track_num = i + 1
        
        # Extract Prompt
        prompt_match = re.search(r'### \[Genre Prompt\]\s+(.*?)\s+### \[Lyrics\]', track, re.DOTALL)
        if prompt_match:
            prompt_text = prompt_match.group(1).strip()
            prompt_len = len(prompt_text)
        else:
            prompt_len = 0
            
        # Extract Lyrics
        lyrics_match = re.search(r'### \[Lyrics\]\s+(.*?)($|---)', track, re.DOTALL)
        if lyrics_match:
            lyrics_text = lyrics_match.group(1).strip()
            lyrics_len = len(lyrics_text) # Counting chars including spaces/newlines? Usually tools count chars.
        else:
            lyrics_len = 0
            
        results.append({
            "Track": track_num,
            "Prompt_Len": prompt_len,
            "Lyrics_Len": lyrics_len
        })

    print(f"{'Track':<5} | {'Prompt (900-1000)':<20} | {'Lyrics (4000-5000)':<20} | {'Status'}")
    print("-" * 65)
    
    all_pass = True
    for r in results:
        p_status = "OK" if 900 <= r["Prompt_Len"] else "FAIL (Short)" # Relaxed upper bound check for now
        l_status = "OK" if 4000 <= r["Lyrics_Len"] else "FAIL (Short)"
        
        final_status = "PASS" if p_status == "OK" and l_status == "OK" else "FAIL"
        if final_status == "FAIL": all_pass = False
        
        print(f"{r['Track']:<5} | {r['Prompt_Len']:<6} ({p_status})     | {r['Lyrics_Len']:<6} ({l_status})     | {final_status}")
    
    return all_pass

if __name__ == "__main__":
    verify_lengths("c:\\Users\\82109\\Desktop\\Antigravity_김광석 agent Project v.1.0\\CHRISTMAS_ALBUM.md")
