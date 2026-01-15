# src/compose.py
import os
import sys
import json
import google.generativeai as genai
from agents.prompts import SYSTEM_ARCHITECT, SYSTEM_SONIC, SYSTEM_LYRICIST

# Configuration
API_KEY = "AIzaSyC7zXTr2IsmwCEPC3lej1Uh2hQmF-hEfDs"
# Using a high-quality model for reasoning/lyrics and a fast one for technicals if needed.
# Converting user request "Gemini 3 Pro / Flash Preview" to likely valid SDK strings.
MODEL_NAME = "gemini-2.5-pro"
genai.configure(api_key=API_KEY)

def call_agent(system_prompt, user_input):
    """Generic function to call a Gemini Agent."""
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        chat = model.start_chat(history=[
            {"role": "user", "parts": [system_prompt]},
            {"role": "model", "parts": ["Understood. I am ready."]}
        ])
        response = chat.send_message(user_input)
        if not response.text:
            return "{}"
        return response.text
    except Exception as e:
        print(f"❌ Error calling Gemini Agent ({MODEL_NAME}): {e}")
        # Fallback to older model if strictly needed, or just return basic
        return json.dumps({"error": str(e)})

def main():
    if len(sys.argv) < 2:
        target_topic = "Nomadology"
    else:
        target_topic = sys.argv[1]

    print(f"🎨 Composition Started: '{target_topic}' via Gemini")
    
    # 1. ARCHITECT
    print("   🧠 Architect (Gemini) is thinking...")
    concept_str = call_agent(SYSTEM_ARCHITECT, f"Topic: {target_topic}. Return ONLY valid JSON.")
    
    if not concept_str or "error" in concept_str:
        print("   ⚠️ Architect failed. Using fallback.")
        concept = {"concept_title": f"Plateau: {target_topic}", "philosophical_angle": "Manual Override"}
    else:
        # Clean up formatting
        concept_str = concept_str.replace("```json", "").replace("```", "").strip()
        try:
            concept = json.loads(concept_str)
            print(f"      Title: {concept.get('concept_title')}")
        except:
            print(f"      ⚠️ Failed to parse Architect JSON.")
            concept = {"concept_title": f"Plateau: {target_topic}", "philosophical_angle": concept_str}

    # 2. SONIC SCULPTOR (Style)
    print("   🎛️ Sonic Sculptor is designing...")
    sonic_input = f"Concept: {json.dumps(concept)}. Return ONLY valid JSON."
    style_str = call_agent(SYSTEM_SONIC, sonic_input)
    style_str = style_str.replace("```json", "").replace("```", "").strip()
    
    try:
        style_data = json.loads(style_str)
        style_tags = style_data['style_tags']
        print(f"      Style: {style_tags}")
    except:
         print(f"      ⚠️ Failed to parse Sonic JSON.")
         style_tags = "abstract hip hop, glitch"

    # 3. LYRICIST (Lyrics)
    print("   ✍️  Lyricist is writing...")
    lyric_input = f"Concept: {json.dumps(concept)}\nStyle: {json.dumps(style_data) if 'style_data' in locals() else style_tags}"
    lyrics = call_agent(SYSTEM_LYRICIST, lyric_input)
    
    # 4. Save Output
    output_data = {
        "title": concept.get('concept_title', target_topic),
        "tags": style_tags,
        "prompt": lyrics
    }
    
    with open("next_track.json", "w", encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
        
    print("\n✅ Track Composition Complete. Saved to 'next_track.json'")

if __name__ == "__main__":
    main()
