import os,shutil,logging
logging.basicConfig(
    level="info",
    filemode='a',
    filename='logs.txt',
    format="%(asctime)s - %(logtype)s - %(message)"
)
folder_main = input("Enter the main folder path : ")
currentdir = r"{}".format(folder_main)
map_ = {
    "Documents":[".docx",".xlsx",".pdf",".txt"],
    "Images" : [".jpg",".jpeg",".png",".gif",".bmp"],
    "Audio" : [".mp3",".wav",".aiff"],
    "Programs":[".exe",".py",".cpp"]
}
os.chdir(currentdir)
allfiles = os.listdir(currentdir)

for file in allfiles:
    file_path = os.path.join(currentdir,file)
    if os.path.isfile(file_path):
        moved = False
        for folder,extensions in map_.items():
            if file.lower().endswith(tuple(extensions)):
                try:
                    os.makedirs(os.path.join(currentdir,folder),exist_ok=True)
                    shutil.move(file_path,os.path.join(currentdir,folder,file))

                except:
                    print("Warning: could not move file {} to folder {}".format(file,folder))
                moved = True
                break
        if not moved:
            try:
                os.makedirs(os.path.join(currentdir, 'Others'), exist_ok=True)
                shutil.move(file_path,os.path.join(currentdir,"Others",file))
            except:
                print("Warning: could not move file {} to folder {}".format(file,folder))