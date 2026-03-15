import xbmc
import xbmcgui
import os
import urllib2
import json
import sqlite3
import shutil

# URLs and paths galore!
GITHUB_URL = "https://api.github.com/repos/faithvoid/XboxSaveDB/contents/"
DB_URL = "https://mobcat.zip/XboxIDs/titleIDs.db"
UDATA_PATH = "E:\\UDATA\\"
ICON = os.path.join(os.getcwd(), "icon.png")

# Saves MobCat's "titlesID.db" to Z:/ (temp storage) and fetches game information from there, deleting it as soon as the title IDs are mapped to real names. Attempts with the "tempfile" library were less than successful, and basically do the same thing anyway.
def get_in_memory_map():
    title_map = {}
    try:
        req = urllib2.Request(DB_URL)
        req.add_header('User-Agent', 'XBMC4Xbox')
        db_data = urllib2.urlopen(req).read()

        temp_path = "Z:\\titleIDs.db"
        with open(temp_path, 'wb') as f:
            f.write(db_data)
            
        conn = sqlite3.connect(temp_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT Title_ID, Title_Name FROM TitleIDs")
        for row in cursor.fetchall():
            tid = str(row[0]).lower()
            title_map[tid] = "%s (%s)" % (row[1], row[0])
            
        conn.close()
        if os.path.exists(temp_path):
            os.remove(temp_path)
    except:
        pass
    return title_map

# Handle downloading save files via urllib2
def download_save_file(url, dest):
    try:
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        with open(dest, 'wb') as f:
            f.write(res.read())
        return True
    except:
        return False

# Create a backup folder if requested, appending "-backup" to the end of the title ID.
def backup_folder(title_id):
    src = os.path.join(UDATA_PATH, title_id)
    dst = os.path.join(UDATA_PATH, title_id + "-backup")
    try:
        if os.path.exists(dst):
            if os.path.isdir(dst): shutil.rmtree(dst)
            else: os.remove(dst)
        shutil.copytree(src, dst)
        return True
    except:
        return False

# Access the GitHub save game repository, map titleIDs to human-readable names using MobCat's API, as well as asking the user if they'd like to backup/overwrite any files, if saves are already found with the same title ID. 
def run_installer(repo_path, title_id, name_map):
    display_name = name_map.get(title_id.lower(), title_id)
    api_url = GITHUB_URL + repo_path
    
    try:
        req = urllib2.Request(api_url)
        items = json.loads(urllib2.urlopen(req).read())
    except:
        return

    for item in items:
        local_path = os.path.join(UDATA_PATH, item['path'].replace('/', os.sep))
        
        if item['type'] == 'dir':
            if os.path.exists(local_path):
                if xbmcgui.Dialog().yesno("Overwrite?", "Folder exists: %s\nOverwrite for %s?" % (item['name'], display_name)):
                    run_installer(item['path'], title_id, name_map)
            else:
                os.makedirs(local_path)
                run_installer(item['path'], title_id, name_map)
        else:
            if os.path.exists(local_path):
                if xbmcgui.Dialog().yesno("Overwrite?", "Replace file: %s?" % item['name']):
                    download_save_file(item['download_url'], local_path)
            else:
                download_file = download_save_file(item['download_url'], local_path)

# Main function
def main():
    name_map = get_in_memory_map()
    
    try:
        req = urllib2.Request(GITHUB_URL)
        repo_data = json.loads(urllib2.urlopen(req).read())
    except:
        return

    options = []
    id_lookup = {}
    for entry in repo_data:
        if entry['type'] == 'dir':
            tid = entry['name']
            label = name_map.get(tid.lower(), tid)
            options.append(label)
            id_lookup[label] = tid
    
    options.sort()

    choice = xbmcgui.Dialog().select("sakuraUnlocker", options)
    if choice != -1:
        sel_label = options[choice]
        sel_id = id_lookup[sel_label]

        target_dir = os.path.join(UDATA_PATH, sel_id)
        if os.path.exists(target_dir):
            if xbmcgui.Dialog().yesno("sakuraUnlocker", "Existing save data found for %s.\nBackup folder before installing?" % sel_label):
                xbmc.executebuiltin("Notification(sakuraUnlocker, Backing up original save folder..., 2000, ICON)")
                backup_folder(sel_id)
        
        run_installer(sel_id, sel_id, name_map)
        xbmc.executebuiltin("Notification(sakuraUnlocker, Installation finished!, 2000, ICON)")

if __name__ == '__main__':
    main()
