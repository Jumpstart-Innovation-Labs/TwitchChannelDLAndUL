import os
import ftplib


def create_ftp_dir(dir_name):
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = "utf-8"
    try:
        ftp.mkd(dir_name)
        ftp.close()
        return
    except:
        ftp.close()
        return

FTP_HOST = "ftp.stackcp.com"
FTP_USER = "fiverr@noc.baxtmann.me"
FTP_PASS = "fiverr1274"

def ftp_upload(video_path):
    print('UPloading to FTP')
    chunksize = 1000000000
    retry = 0
    dir_name = video_path[:-4]
    part_location = f"{dir_name}/{dir_name.split('/')[-1]}"
    create_ftp_dir(dir_name)
    part_no = 1
    try:
        with open(video_path, "rb") as file:
            chunk = file.read(chunksize)
            while chunk:
                with open(f"parts/_part_{part_no}.mkv", 'wb') as new_file:
                    new_file.write(chunk)
                    print('copied part')
                with open(f"parts/_part_{part_no}.mkv", 'rb') as new_file:                   
                    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
                    ftp.encoding = "utf-8"
                    ftp.storbinary(f"STOR {part_location}_part_{part_no}.mkv", new_file)
                    ftp.close()
                    print(f"PArt: {part_no} successfully uploaded")
                part_no += 1
                chunk = file.read(chunksize)
            print('UPloaded Successfully')
            return True
    except Exception as e:
        retry +=1	
        if retry > 15:	
            return False	
        print(e)	
        print('Failed To Upload. Retrying...')

openfile = open('downloaded_videos.txt', 'r')
files_path = openfile.read().split('\n')
openfile.close()

for file_path in files_path:
    if file_path != '':
        try:
            local_file_size = os.stat(file_path).st_size
            remote_file_size = 0
            remote_dir_path = file_path[:-4]+'/'


            ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
            part_files = ftp.nlst(remote_dir_path)
            ftp.voidcmd('TYPE I')
            for part_file in part_files:
                remote_file_size += ftp.size(part_file)
            ftp.close()
        
            if local_file_size != remote_file_size:
                success = ftp_upload(file_path)
        except ftplib.error_temp:
            pass
        except Exception as e:
            print(e)

