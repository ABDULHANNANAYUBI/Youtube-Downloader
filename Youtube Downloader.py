from pytube import YouTube
folder_d = input("Enter download folder path: (C://Downloads: )");

Download_Folder = folder_d
range_download = int(input("How many videos would you like to download : "));

for i in range(0, range_download):
    video_url = input(f"Enter {i + 1} video link : ");
    video_obj = YouTube(video_url)
    stream = video_obj.streams.get_highest_resolution();
    stream.download(Download_Folder);


