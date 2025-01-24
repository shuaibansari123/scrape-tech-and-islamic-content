# # import os
# # from django.core.management.base import BaseCommand
# # from django.conf import settings
# # from yt_dlp import YoutubeDL
# # from ImfeelingApp.models import Playlist, VideoPlaylist

# # class Command(BaseCommand):
# #     help = 'Download videos from a YouTube playlist and save them to the database'

# #     def handle(self, *args, **kwargs):
# #         # Specify the URL of the YouTube playlist
# #         playlist_url_dajjal = 'https://www.youtube.com/playlist?list=PLTd3_myEY8GlHcRaeC5q0uxCN-AGid5YA'  # Replace with the actual playlist URL

# #         folder_name = 'israr_ahmad_islamic_videos'
# #         if not os.path.exists(folder_name):
# #             os.makedirs(folder_name)

# #         ydl_opts = {
# #             'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),  
# #             'format': 'best',  # Download the best quality
# #             'noplaylist': False,  # Download the entire playlist
# #         }

# #         try:
# #             with YoutubeDL(ydl_opts) as ydl:
# #                 # Extract playlist information
# #                 playlist_info = ydl.extract_info(playlist_url_dajjal, download=False)
# #                 playlist_title = playlist_info.get('title', 'Untitled Playlist')

# #                 # Create or get the Playlist object
# #                 playlist, created = Playlist.objects.get_or_create(title=playlist_title)

# #                 # Download videos and save to the database
# #                 for video in playlist_info['entries']:
# #                     video_title = video.get('title', 'Untitled Video')
# #                     video_file = os.path.join(folder_name, f"{video_title}.mp4")  # Assuming mp4 format
# #                     video_description = video.get('description', '')
# #                     video_views = video.get('view_count', 0)
# #                     video_image_url = video.get('thumbnail', '')

# #                     # Validate filename length
# #                     if len(video_title) > 100:
# #                         video_title = video_title[:100]  # Truncate to 100 characters

# #                     # Create the VideoPlaylist object
# #                     video_playlist = VideoPlaylist(
# #                         playlist=playlist,
# #                         title=video_title,
# #                         file=video_file,
# #                         views=video_views,
# #                         description=video_description,
# #                         image_url=video_image_url
# #                     )
# #                     video_playlist.save()  # Save to the database

# #                 print(f'Downloaded all videos from the playlist "{playlist_title}" and saved to the database.')
# #         except Exception as e:
# #             print(f'An error occurred: {e}')





# # import os
# # import yt_dlp

# # # Specify the URL of the YouTube playlist
# # playlist_url = 'https://www.youtube.com/playlist?list=PLTd3_myEY8GlHcRaeC5q0uxCN-AGid5YA'  # Replace with the actual playlist URL

# # # Create a directory to save the videos
# # folder_name = 'israr ahmad islamic videos'
# # if not os.path.exists(folder_name):
# #     os.makedirs(folder_name)

# # # Download the videos from the playlist
# # ydl_opts = {
# #     'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),  # Save with video title
# # }

# # try:
# #     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #         ydl.download([playlist_url])
# #     print(f'Downloaded all videos from the playlist to {folder_name}')
# # except Exception as e:
# #     print(f'An error occurred: {e}')















import os
from django.core.management.base import BaseCommand
from django.conf import settings
from yt_dlp import YoutubeDL
from ImfeelingApp.models import Playlist, VideoPlaylist
class Command(BaseCommand):
    help = 'Download videos from multiple YouTube playlists and save them to the database'

    def handle(self, *args, **kwargs):
        # Define the playlist URLs
        playlist_urls = [
            # 'https://www.youtube.com/playlist?list=PLTd3_myEY8GlHcRaeC5q0uxCN-AGid5YA',  # Playlist 1
            # 'https://www.youtube.com/playlist?list=PL017388606FF45A97',  # Playlist 2
            # 'https://www.youtube.com/playlist?list=PLN5NkUdaF03i2YxYkzZxO3HjALil8_0Pi',  # Playlist 3
            # 'https://www.youtube.com/playlist?list=PLiSOh6uCsX4K_abx0ybhf38SEpwm1qdrn',  # Playlist 4


            # "https://www.youtube.com/watch?v=8Jf2eem4PmQ&list=PLKbACZ1M0i2ZvJ5iW8kVJPT6RarIty85i",
            # "https://www.youtube.com/watch?v=uDnO7sduQD8&list=PL67B13CA64A1B05D3",
            # "https://www.youtube.com/watch?v=VYeZKO_JU80&list=PLWtEv5OeI4vGq95qcH932IjcQOZSMhlCX", 

           "https://www.youtube.com/watch?v=ndqNhjSzTHY&list=PLU5cK6R1qWoNiQMchm5Dg9D51fy_uf4ww",

            "https://www.youtube.com/watch?v=lJuQ4KyrYsM&list=PLtGnTd8qELzgWcDu6ZZrKHqnhccFcUTcK",


            "https://www.youtube.com/watch?v=Red15d7cK7I&list=PL8T_qeb8xNhaSfNBGhzATfGCb8BypJ73v",

            "https://www.youtube.com/watch?v=zbsGF8YLoLw&list=PLv58p9sNSU4kJH-otw3DrMoDH141uhu2A",

        ]

        # Directory to save videos
        folder_name = os.path.join(settings.MEDIA_ROOT, 'videos_israr_ahmad')
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        ydl_opts = {
            'outtmpl': os.path.join(folder_name, '%(id)s.%(ext)s'),  # Use video ID for unique filenames
            'restrictfilenames': True,  # Ensure filenames are URL-safe
            'format': 'best',  # Download the best quality
        }

        for playlist_url in playlist_urls:
            try:
                with YoutubeDL(ydl_opts) as ydl:
                    # Extract playlist information
                    playlist_info = ydl.extract_info(playlist_url, download=False)
                    playlist_title = playlist_info.get('title', 'Untitled Playlist')

                    # Create or get the Playlist object
                    playlist, created = Playlist.objects.get_or_create(title=playlist_title)

                    # Download videos and update the database
                    for video in playlist_info['entries']:
                        try:
                            video_id = video.get('id')  # Unique video ID
                            video_title = video.get('title', 'Untitled Video')
                            video_description = video.get('description', '')
                            video_views = video.get('view_count', 0)
                            video_image_url = video.get('thumbnail', '')

                            # Validate filename length
                            if len(video_title) > 100:
                                video_title = video_title[:100]

                            # Construct the file path for the downloaded video
                            video_file_path = os.path.join(folder_name, f"{video_id}.mp4")
                            relative_file_path = f'videos_israr_ahmad/{video_id}.mp4'

                            # Check if the video already exists in the database
                            video_playlist, created = VideoPlaylist.objects.get_or_create(
                                playlist=playlist,
                                title=video_title,
                                defaults={
                                    'file': relative_file_path,  # Save relative path
                                    'views': video_views,
                                    'description': video_description,
                                    'image_url': video_image_url
                                }
                            )

                            # Skip if the video already exists and the file is present
                            if not created and os.path.exists(video_file_path):
                                continue

                            # Download the video
                            ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

                            # Verify the file exists after download
                            if os.path.exists(video_file_path):
                                video_playlist.file = relative_file_path
                                video_playlist.save()
                                print(f"Successfully downloaded and saved: {video_title}")
                            else:
                                print(f"Failed to download video: {video_title}")

                        except Exception as e:
                            print(f"Error processing video {video_title}: {e}")

                    print(f"All videos from the playlist '{playlist_title}' have been processed.")
            except Exception as e:
                print(f"An error occurred with playlist {playlist_url}: {e}")



 # https://www.youtube.com/watch?v=dKV3wYq_W_c&list=PL017388606FF45A97   (dajjal 10 videos)

        #https://www.youtube.com/watch?v=FSX71LBLOVg&list=PLN5NkUdaF03i2YxYkzZxO3HjALil8_0Pi   --> quran taruk (107 videos)

        # https://www.youtube.com/watch?v=qjn_vHayQGM&list=PLiSOh6uCsX4K_abx0ybhf38SEpwm1qdrn     --- > (order of illuminati 18 video)    -----> already saved







        # https://www.youtube.com/watch?v=8Jf2eem4PmQ&list=PLKbACZ1M0i2ZvJ5iW8kVJPT6RarIty85i  https://www.youtube.com/watch?v=uDnO7sduQD8&list=PL67B13CA64A1B05D3  https://www.youtube.com/watch?v=VYeZKO_JU80&list=PLWtEv5OeI4vGq95qcH932IjcQOZSMhlCX  india lectures 43


        # https://www.youtube.com/watch?v=uDnO7sduQD8&list=PL67B13CA64A1B05D3        last crusede --> done


        # https://www.youtube.com/watch?v=VYeZKO_JU80&list=PLWtEv5OeI4vGq95qcH932IjcQOZSMhlCX     lessons from history 8 --- copleted- alreay dumped

        # emotional bayan 108 
        # https://www.youtube.com/watch?v=ndqNhjSzTHY&list=PLU5cK6R1qWoNiQMchm5Dg9D51fy_uf4ww 

        # zia coplete 508 video 
        # https://www.youtube.com/watch?v=lJuQ4KyrYsM&list=PLtGnTd8qELzgWcDu6ZZrKHqnhccFcUTcK


        # iqbal 
        # https://www.youtube.com/watch?v=Red15d7cK7I&list=PL8T_qeb8xNhaSfNBGhzATfGCb8BypJ73v

        # best israr (r) 28
        # https://www.youtube.com/watch?v=zbsGF8YLoLw&list=PLv58p9sNSU4kJH-otw3DrMoDH141uhu2A