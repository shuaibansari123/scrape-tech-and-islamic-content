import os
from django.core.management.base import BaseCommand
from ImfeelingApp.models import Playlist, VideoPlaylist
import random


class Command(BaseCommand):
    help = 'Create VideoPlaylist objects with random images from static folder'

    # def handle(self, *args, **kwargs):
    #     base_path = r'C:\Users\shuai\Desktop\Additionals\p_project\Islam_project\backend\media\playlist_upload'  # Adjust this path if necessary
    #     static_image_path = r'C:\Users\shuai\Desktop\Additionals\p_project\Islam_project\backend\frontend\img\hand-drawn-flat-design-salat-illustration'  # Path to static images

    #     # Check if the base path exists
    #     if not os.path.exists(base_path):
    #         self.stdout.write(self.style.ERROR(f'Base path does not exist: {base_path}'))
    #         return

    #     # Get a list of all images in the static folder
    #     image_files = [f for f in os.listdir(static_image_path) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    #     # Check if there are any images available
    #     if not image_files:
    #         self.stdout.write(self.style.ERROR(f'No images found in static folder: {static_image_path}'))
    #         return

    #     # Iterate through each folder in the base path
    #     for playlist_folder in os.listdir(base_path):
    #         playlist_path = os.path.join(base_path, playlist_folder)

    #         if os.path.isdir(playlist_path):
    #             # Create a Playlist object
    #             playlist, created = Playlist.objects.get_or_create(title=playlist_folder)
    #             if created:
    #                 self.stdout.write(self.style.SUCCESS(f'Created Playlist: {playlist.title}'))
    #             else:
    #                 self.stdout.write(self.style.WARNING(f'Playlist already exists: {playlist.title}'))

    #             # Iterate through each video file in the playlist folder
    #             for video_file in os.listdir(playlist_path):
    #                 video_path = os.path.join(playlist_path, video_file)

    #                 if os.path.isfile(video_path):
    #                     # Select a random image from the static folder
    #                     random_image = random.choice(image_files)
    #                     image_upload_path = f'hand-drawn-flat-design-salat-illustration/{random_image}'  # Adjust the path for storage

    #                     # Get or create the VideoPlaylist object
    #                     video_playlist, created = VideoPlaylist.objects.get_or_create(
    #                         playlist=playlist,
    #                         title=video_file,
    #                         defaults={
    #                             'file': f'playlist_upload/{playlist_folder}/{video_file}',
    #                             'image': image_upload_path  # Assign the random image
    #                         }
    #                     )

    #                     # If the object already exists, update the image field
    #                     if not created:
    #                         video_playlist.image = image_upload_path  # Update the image field
    #                         video_playlist.save()  # Save the changes
    #                         self.stdout.write(self.style.SUCCESS(f'Updated VideoPlaylist image: {video_playlist.title} in {playlist.title}'))
    #                     else:
    #                         self.stdout.write(self.style.SUCCESS(f'Created VideoPlaylist: {video_playlist.title} in {playlist.title}'))






    # UPDATING 'image' FIELD JUST ***************************************************************************
    def handle(self, *args, **kwargs):
        static_image_path = r'C:\Users\shuai\Desktop\Additionals\p_project\Islam_project\backend\frontend\img\hand-drawn-flat-design-salat-illustration'  # Path to static images

        # Get a list of all images in the static folder
        image_files = [f for f in os.listdir(static_image_path) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        # Check if there are any images available
        if not image_files:
            self.stdout.write(self.style.ERROR(f'No images found in static folder: {static_image_path}'))
            return

        # Iterate through all VideoPlaylist objects
        for video_playlist in VideoPlaylist.objects.all():
            # Select a random image from the static folder
            random_image = random.choice(image_files)
            image_upload_path = f'hand-drawn-flat-design-salat-illustration/{random_image}'  # Adjust the path for storage

            # Update the image field
            video_playlist.image = image_upload_path
            video_playlist.save()  # Save the changes
            self.stdout.write(self.style.SUCCESS(f'Updated VideoPlaylist image: {video_playlist.title}'))