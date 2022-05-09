from pytube import 	YouTube

link = "https://youtu.be/YciheqisAtg"

video = YouTube(link)

# print(f"The video title is:\n{video.title}\n--------------")
# print(f"The vide description is:\n{video.description}\n--------------")
# print(f"The video views is:\n{video.views}\n--------------")
# print(f"The video length is:\n{(video.length)/60}\n--------------")

for stream in video.streams.filter(progressive=True,res="720p"):
	print(stream)

video.streams.get_highest_resolution().download(output_path=r"C:\Users\amustafa\Desktop\py\YouTubeDownloader")
