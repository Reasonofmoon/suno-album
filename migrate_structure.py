import shutil
import os

def move_player_to_root():
    # Paths
    root = os.getcwd()
    player_dir = os.path.join(root, "player")
    assets_src = os.path.join(player_dir, "assets")
    assets_dst = os.path.join(root, "assets")
    
    # 1. Move Files
    if os.path.exists(os.path.join(player_dir, "index.html")):
        shutil.move(os.path.join(player_dir, "index.html"), os.path.join(root, "index.html"))
        print("Moved index.html")
        
    if os.path.exists(os.path.join(player_dir, "content.js")):
        shutil.move(os.path.join(player_dir, "content.js"), os.path.join(root, "content.js"))
        print("Moved content.js")

    # 2. Merge Assets
    if not os.path.exists(assets_dst):
        os.makedirs(assets_dst)
    
    if os.path.exists(assets_src):
        for item in os.listdir(assets_src):
            s = os.path.join(assets_src, item)
            d = os.path.join(assets_dst, item)
            if os.path.isfile(s):
                shutil.copy2(s, d) # Copy to overwrite or merge
                os.remove(s)
                print(f"Moved asset: {item}")
        
        # Remove empty assets dir
        try:
            os.rmdir(assets_src)
        except:
            pass

    # 3. Cleanup
    try:
        os.rmdir(player_dir)
        print("Removed player directory")
    except Exception as e:
        print(f"Could not remove player dir (not empty?): {e}")

if __name__ == "__main__":
    move_player_to_root()
