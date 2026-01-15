# src/test_generation.py
from suno_client import SunoClient
import time
import json

def test_run():
    client = SunoClient()
    
    # 1. Define Test Data
    print("🧪 Starting Test Run: 'Rhizome Test'")
    lyrics = """
    [Intro]
    Testing the connection...
    Is the Rhizome growing?
    
    [Verse]
    Pixels and waves, 
    Digital caves.
    """
    style = "glitch hop, lo-fi"
    title = "Rhizome Test 01"
    
    # 2. Trigger Generation
    response_data = client.generate_music(
        prompt=lyrics,
        style=style,
        title=title,
        model="V5"
    )
    
    print("📨 Response from Generate:")
    print(json.dumps(response_data, indent=2))
    
    if not response_data:
        print("❌ Generation failed.")
        return

    # Extract Task ID (Guessing key name 'data' -> 'taskId' based on common patterns)
    # The actual response usually has 'data': 'taskId' or similar.
    # Let's inspect the output safely.
    
    task_id = None
    if isinstance(response_data, dict):
        # Look for typical keys
        if 'data' in response_data:
            # Sometimes data is the ID string itself, or a dict
            if isinstance(response_data['data'], str):
                 task_id = response_data['data']
            elif isinstance(response_data['data'], dict) and 'taskId' in response_data['data']:
                 task_id = response_data['data']['taskId']
    
    if not task_id:
        print(f"⚠️ Could not extract Task ID from response. Keys: {response_data.keys()}")
        return

    print(f"🆔 Task ID extracted: {task_id}")

    # 3. Poll for Status (Just once to check format)
    print("🔎 Checking Status (One-off)...")
    time.sleep(5) # Wait a bit
    status = client.get_generation_status(task_id)
    print("📨 Status Response:")
    print(json.dumps(status, indent=2))

if __name__ == "__main__":
    test_run()
