import os
import shutil

#フォルダ名指定
dir_name1 = "画像フォルダ"
dir_name2 = "音声フォルダ"
dir_name3 = "映像フォルダ"
dir_name4 = "テキストフォルダ"

#整頓するデータの最低数指定
data_number = 3

if(len(os.listdir()) >= data_number):
    try:
        data_files = os.listdir()

        os.mkdir(dir_name1)
        os.mkdir(dir_name2)
        os.mkdir(dir_name3)
        os.mkdir(dir_name4)
    except FileExistsError:
        print("FileExistsError:すでに同じ名前のフォルダが存在しています")

    dir_name1_path = dir_name1 + "/"
    dir_name2_path = dir_name2 + "/"
    dir_name3_path = dir_name3 + "/"
    dir_name4_path = dir_name4 + "/"

    for files in data_files:
        if(files.endswith(".png") or files.endswith(".jpg") or files.endswith(".bmp")):
            shutil.move(files, dir_name1_path + files)
        elif(files.endswith(".mp3") or files.endswith(".wav")):
            shutil.move(files, dir_name2_path + files)
        elif(files.endswith(".mp4") or files.endswith(".mov")):
            shutil.move(files, dir_name3_path + files)
        elif(files.endswith(".txt") or files.endswith(".csv")):
            shutil.move(files, dir_name4_path + files)
        else:
            pass

else:
    print("整頓するほどのデータが存在しません")