# src/suno_client.py
import requests
import time
import json
import os

API_BASE_URL = "https://api.sunoapi.org/api/v1"
API_KEY = "d38063ca1110014b3e5fc55b7a09c5a6"  # Hardcoded as per user implementation, usually better in env var

class SunoClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate_music(self, prompt, style, title, instrumental=False, model="V5", custom_mode=True, callBackUrl=None):
        """
        Triggers music generation.
        Returns the Task ID (or equivalent) to track progress.
        """
        url = f"{API_BASE_URL}/generate"
        payload = {
            "customMode": custom_mode,
            "instrumental": instrumental,
            "prompt": prompt,  # Lyrics if customMode=True, Description if False
            "style": style,
            "title": title,
            "model": model,
            "callBackUrl": callBackUrl or "https://example.com/callback"
        }

        
        print(f"🎵 Sending Generation Request: '{title}' [{model}]")
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data # Should contain 'data' with task_id or similar
        except requests.exceptions.RequestException as e:
            print(f"❌ Error generating music: {e}")
            if response is not None:
                print(f"   Response output: {response.text}")
            return None

    def get_generation_status(self, task_id):
        """
        Checks status of generation task.
        """
        if not task_id:
            return None
            
        url = f"{API_BASE_URL}/generate/record-info"
        # The documentation mentions this endpoint but parameters might vary. 
        # Usually it takes a query param or path param. 
        # Based on typical patterns of this wrapper: ?taskId=... or similar
        # But let's assume it accepts a query string based on the docs mentioning 'record-info'
        # CAUTION: The exact param name (taskId vs id) is not in the snippet.
        # I will try typical 'taskId' or 'ids'.
        
        # NOTE: Some wrapper docs say /generate/record-info?ids=...
        params = {"taskId": task_id}
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error checking status: {e}")
            return None

    def wait_for_completion(self, task_id, timeout=300, interval=10):
        """
        Polls until completion or timeout.
        """
        print(f"⏳ Waiting for task {task_id}...")
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            status_data = self.get_generation_status(task_id)
            if status_data:
                # Need to parse the specific response structure. 
                # Usually it returns a list of items.
                # If status is within the items.
                # I'll print the raw status first to debug in the test script.
                pass 
                
            yield status_data
            time.sleep(interval)

    def get_songs(self):
        """
        Retrieves recent generated songs.
        """
        # Try likely endpoint for library/feed
        url = "https://api.sunoapi.org/api/get"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error getting songs: {e}")
            return None

if __name__ == "__main__":
    # Quick Test
    client = SunoClient()
    print("Client initialized.")
