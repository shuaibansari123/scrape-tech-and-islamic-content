import os
from django.core.management.base import BaseCommand
from django.conf import settings
from yt_dlp import YoutubeDL
from ImfeelingApp.models import Playlist, VideoPlaylist

class Command(BaseCommand):
    help = 'Download videos from a single YouTube playlist and save them to the database'

    def add_arguments(self, parser):
        parser.add_argument('playlist_url', type=str, help='YouTube playlist URL')
        parser.add_argument('--uploader-name', type=str, help='Uploader name', default='')
        parser.add_argument('--uploader-email', type=str, help='Uploader email', default='')

    def handle(self, *args, **options):
        playlist_url = options['playlist_url']
        uploader_name = options['uploader_name']
        uploader_email = options['uploader_email']
        self.stdout.write(f"Uploading playlist from {playlist_url}...")


        # Create the videos directory if it doesn't exist
        folder_name = os.path.join(settings.MEDIA_ROOT, 'videos_israr_ahmad')
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        ydl_opts = {
            'outtmpl': os.path.join(folder_name, '%(id)s.%(ext)s'),
            'restrictfilenames': True,
            'format': 'best',
        }

        results = {
            'success': False,
            'playlist_title': '',
            'total_videos': 0,
            'downloaded_videos': 0,
            'video_titles': [],
            'error': None
        }
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                # Extract playlist information
                playlist_info = ydl.extract_info(playlist_url, download=False)
                playlist_title = playlist_info.get('title', 'Untitled Playlist')
                results['playlist_title'] = playlist_title
                results['total_videos'] = len(playlist_info['entries'])

                # Create or get the Playlist object
                self.stdout.write(f"Creating or getting playlist object for {playlist_title}...")
                playlist, created = Playlist.objects.get_or_create(
                    title=playlist_title,
                    defaults={
                        'uploader_name': uploader_name,
                        'uploader_email': uploader_email
                    }
                )

                # Download videos and update the database
                for video in playlist_info['entries']:
                    self.stdout.write(f"INSIDE FOOR LOOP: Processing video {video.get('title', 'Untitled Video')}...")
                    try:
                        video_id = video.get('id')
                        video_title = video.get('title', 'Untitled Video')
                        video_description = video.get('description', '')
                        video_views = video.get('view_count', 0)
                        video_image_url = video.get('thumbnail', '')

                        if len(video_title) > 100:
                            video_title = video_title[:100]

                        video_file_path = os.path.join(folder_name, f"{video_id}.mp4")
                        relative_file_path = f'videos_israr_ahmad/{video_id}.mp4'

                        # Create or update video entry
                        video_playlist, created = VideoPlaylist.objects.get_or_create(
                            playlist=playlist,
                            title=video_title,
                            defaults={
                                'file': relative_file_path,
                                'views': video_views,
                                'description': video_description,
                                'image_url': video_image_url
                            }
                        )

                        if not created and os.path.exists(video_file_path):
                            continue

                        # Download the video
                        self.stdout.write(f"Downloading video {video_title}...")
                        ydl.download([f"https://www.youtube.com/watch?v={video_id}"])
                        self.stdout.write(f"Downloaded video {video_title}...")

                        if os.path.exists(video_file_path):
                            video_playlist.file = relative_file_path
                            video_playlist.save()
                            self.stdout.write(f"Saved video {video_title} to database...")
                            results['downloaded_videos'] += 1
                            results['video_titles'].append(video_title)

                    except Exception as e:
                        print(f"Error processing video {video_title}: {e}")
                        self.stdout.write(f"Error processing video {video_title}: {e}")
                results['success'] = True
                self.stdout.write(f"Playlist {playlist_title} uploaded successfully.")
        except Exception as e:
            results['error'] = str(e)
            self.stdout.write(f"Error uploading playlist {playlist_title}: {e}")

        return results