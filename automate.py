import os
import shutil
path = "D:/MyFiles"  
folders = ["Images", "Documents", "Videos", "Others"]

for folder in folders:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
files = os.listdir(path)
for file in files:
    file_path = os.path.join(path, file)

    
    if os.path.isdir(file_path):
        continue

    
    if file.endswith((".jpg", ".png", ".jpeg")):
        shutil.move(file_path, os.path.join(path, "Images", file))

    
    elif file.endswith((".pdf", ".docx", ".txt")):
        shutil.move(file_path, os.path.join(path, "Documents", file))

    
    elif file.endswith((".mp4", ".mkv")):
        shutil.move(file_path, os.path.join(path, "Videos", file))

    
    else:
        shutil.move(file_path, os.path.join(path, "Others", file))

print("✅ Files organized successfully!")