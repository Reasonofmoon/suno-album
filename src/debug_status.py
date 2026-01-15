# src/debug_status.py
from suno_client import SunoClient
import json

TASK_ID = "53a547a5103da653750d0e99ebad093c"

def main():
    client = SunoClient()
    print(f"🔎 Inspecting Status for Task: {TASK_ID}")
    
    status = client.get_generation_status(TASK_ID)
    
    print("\n[FULL JSON OUTPUT]")
    print(json.dumps(status, indent=2))
    
    # Save to file
    with open("status_dump.json", "w") as f:
        json.dump(status, f, indent=2)

if __name__ == "__main__":
    main()
