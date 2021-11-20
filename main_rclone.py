import os
import sys
import ftplib
import subprocess

from datetime import datetime
from twitchdl import twitch

from videos import videos
from download import _download_video, _video_target_filename

print(f"Script Started {datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}")

limit_size = 751618891971 #MAX UPLOAD Limit #7GB
limit_size_representation = 1073741824 
format='mkv'
max_workers=20
quality='source'
start=None
end=None
overwrite=False

# FTP CONNECTION
FTP_HOST = "ftp.stackcp.com"
FTP_USER = "fiverr@noc.baxtmann.me"
FTP_PASS = "fiverr1274"


# Write File Location PAth In TXT FIle
def write_video_path(video_path_dir):
    file = open('downloaded_videos.txt', 'a')
    file.write(f'{video_path_dir}\n')
    file.close()


# Check File Downloaded OR Not
def video_already_downloaded(video_id):
    video = twitch.get_video(video_id)
    video_path = _video_target_filename(video, format)
    file = open('downloaded_videos.txt', 'r')
    videos_list = file.read().split('\n')
    file.close()
    if video_path in videos_list:
        print('Already DOwnloaded')
        return True
    return False


# Create DIR In FTP
def create_ftp_dir(dir_name):
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = "utf-8"
    try:
        ftp.mkd(dir_name)
        ftp.close()
        return
    except:
        return

# Empty parts file after script in order to save space
def empty_all_parts_file():
    for i in range(10):
        with open(f"parts/_part_{i}.mkv", 'wb') as new_file:
            new_file.write(b'')

# Check File Uploaded or not in FTP
def already_uploaded_to_ftp(video_path):
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = "utf-8"
    dir_path = '/'.join([str(item) for item in video_path.split('/')[:-1]])
    # dir_path_locations = video_path.split('/')
    # for i in dir_path_locations:
    #     dir_path += i + "/"
    list_vod = ftp.nlst(dir_path)
    ftp.close()
    if video_path in list_vod:
        print('Already Uploaded To FTP')
        return True
    return False


# FTP Upload
def ftp_upload(video_path):
    print('UPloading to FTP')
    # Determining single part size by splitting it by filesize
    chunksize = 1000000000
    # chunksize = 3221225472
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
                    print('COPIED')
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


#Reading Channels.txt
file = open("channels.txt", "r")
content = file.read()
file.close()
# list of channels
channels = content.split('\n')


# Make DIrectory
for channel in channels:
    if not os.path.exists(f'VOD/{channel}'):
        os.makedirs(os.path.join('VOD/', channel.lower()))
    # Rclone DIR
    subprocess.run(['rclone', 'mkdir', 'gdrive:twitch:new:'+str(channel)])
    #FTP DIRECTORY
    create_ftp_dir(f'VOD/{channel.lower()}')


# Retreiving Info And Downloading

try:
    for channel in channels:
        data = videos(channel, 100)
        for i in data:
            if not video_already_downloaded(i['id']):
                if limit_size > 0:
                    video_path = _download_video(i['id'], format, max_workers, quality, start, end, overwrite)
                    video_size = os.stat(video_path).st_size
                    limit_size -= video_size
                    print('Uploading to Drive')
                    subprocess.run(['rclone', 'copy', video_path, 'gdrive:twitch:new:' + video_path.split('/')[1]])
                    print("Uploaded to Drive")
                    print(f'Drive Limit Left: {limit_size / limit_size_representation} GB')
                    write_video_path(video_path)
                    if not already_uploaded_to_ftp(video_path):
                        upload_video = ftp_upload(video_path)
                    subprocess.run(['rm', video_path])
                else:
                    print('MAximum Upload Limit Reached')
                    sys.exit()
    print('All Videos Downloaded.')
    empty_all_parts_file()
except Exception as e:
    print('==========================================+')
    print('Error!!!!!!')
    print('-------------------------------------------')
    print(e)
    print('-------------------------------------------')
    print('===========================================')
    print("If you don't understand the error Contact the Developer")
    print('-------------------------------------------')
    print("|| https://www.fiverr.com/farzanulhaq935 ||")
    print('-------------------------------------------')
    print('===========================================')



# TESTING PURPOSE
#for i in range(1):
    # data = videos(channel, 10)
 #   for i in range(2):
  #      if not video_already_downloaded("1008950743"):
   #         video_path = _download_video("1008950743", format, max_workers, quality, start, end, overwrite)
    #        write_video_path(video_path)
     #       if not already_uploaded_to_ftp(video_path):
      #          upload_video = ftp_upload(video_path)
# limit_size = 1000000000000000000000000
# for i in range(1):
#     # data = videos(channel, 100)
#     for i in range(2):
#         if limit_size > 0:
#             # video_path = _download_video("1008950743", format, max_workers, quality, start, end, overwrite)
#             video_path = 'VOD/valorant/20210502_008950743_valorant_team_liquid_vs_fnatic_challengers_emea_stage_2_main_event_finals_map_1.mkv'

#             video_size = os.stat(video_path).st_size
#             if limit_size - video_size > 0:
#                 print('Uploading to Drive')
#                 # subprocess.run(['rclone', 'copy', video_path, 'gdrive:twitch:new:' + video_path.split('/')[1]])
#                 print("Uploaded to Drive")
#                 # write_video_path(video_path)
#                 # if not already_uploaded_to_ftp(video_path):
#                     # upload_video = ftp_upload(video_path)
#                 subprocess.run(['rm', video_path])
#             else:
#                 print('Maximum Upload Limit Reached!')
#                 sys.exit()
#         else:
#             print('Maximum Upload Limit Reached!')
#             sys.exit()
# print('All Videos Downloaded.')
# empty_all_parts_file()
