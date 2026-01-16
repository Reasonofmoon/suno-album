import os

SEARCH_DIR = r"c:\Users\sound\Documents\MyZettelkasten\05 Projects"
NEW_KEY = "PLACEHOLDER_KEY" # Replace this when running locally
# Old key logic: we generally replace GEMINI_API_KEY=... with the new value
# But if there's a hardcoded old key, we should find that too.
# I'll rely on the variable name GEMINI_API_KEY for .env files.

def rotate_in_env_files():
    print(f"🔍 Scanning for .env files in {SEARCH_DIR}...")
    count = 0
    for root, dirs, files in os.walk(SEARCH_DIR):
        # Skip node_modules and .git to speed up
        if 'node_modules' in dirs: dirs.remove('node_modules')
        if '.git' in dirs: dirs.remove('.git')
        if '__pycache__' in dirs: dirs.remove('__pycache__')

        for file in files:
            if file == ".env":
                filepath = os.path.join(root, file)
                update_env_file(filepath)
                count += 1
    print(f"✅ Scanned {count} .env files.")

def update_env_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        changed = False
        for line in lines:
            if line.startswith("GEMINI_API_KEY="):
                # Check if it's already the new key
                current_val = line.strip().split("=", 1)[1]
                if current_val != NEW_KEY:
                    print(f"   🔄 Updating {filepath}...")
                    new_lines.append(f"GEMINI_API_KEY={NEW_KEY}\n")
                    changed = True
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"      ✨ Updated GEMINI_API_KEY")
    except Exception as e:
        print(f"   ❌ Error reading {filepath}: {e}")

if __name__ == "__main__":
    rotate_in_env_files()
