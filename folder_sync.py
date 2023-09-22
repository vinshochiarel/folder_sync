import os
import shutil
import argparse
import time

def copy_folder_files(source_folder, replica_folder):
    for item in os.listdir(source_folder):
        source_item = os.path.join(source_folder, item)
        replica_item = os.path.join(replica_folder, item)

        if os.path.isdir(source_item):
            if not os.path.exists(replica_item):
                os.makedirs(replica_item)
            copy_folder_files(source_item, replica_item) #copy subfolders and their files
        else:
            shutil.copy2(source_item, replica_item) #copy individual files
            
def sync_folders(source_folder, replica_folder, interval):
    try:
        while True:
            for item in os.listdir(replica_folder):
                item_path = os.path.join(replica_folder, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path) #delete files from replica folder

            copy_folder_contents(source_dir, replica_dir) #copy files in replica folder
            print("folders are synchronized.")
            time.sleep(interval)
    except Exception as e:
        print(f"error synchronizing folders: {e}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sync two folders.")
    parser.add_argument("source_folder")
    parser.add_argument("replica_folder")
    parser.add_argument("interval", type=int) #time interval in seconds
    args = parser.parse_args()

    sync_folders(args.source_dir, args.replica_dir, args.interval)

#in-line command to provide folder paths, sync interval
#example interval: 3600 seconds = 1 hour
#paths and time interval are modified below
    python folder_sync.py /path_to_source_folder /path_to_replica_folder time_interval       


