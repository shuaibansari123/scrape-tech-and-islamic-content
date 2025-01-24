from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from urllib.request import urlretrieve
from .models import Playlist, VideoPlaylist
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect
from yt_dlp import YoutubeDL
from django.conf import settings
import os
from .models import Surah, SurahTranslation
from .models import Prayer
from .models import ProphetStory
from .models import DuaDhikr
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect
from .models import ImFeeling, NameOfAllah, RamadanDua, Seerah, FamilyMember, MuhammadChildren, Battle, Wife, Hadith, VideoPlaylist, Playlist
from django.db.models.functions import Substr
from django.core.paginator import Paginator
import random
from django.core.management import call_command
from django.contrib import messages
from .forms import PlaylistURLForm


def index(request):
    # context = {
    #     'featured_videos': VideoPlaylist.objects.filter(image__isnull=False).order_by('-views')[:6],
    #     'latest_videos': VideoPlaylist.objects.filter(image__isnull=False).order_by('created_at')[:6],
    #     'playlists': Playlist.objects.all()[:6],
    # }

    context = {
        'featured_videos': VideoPlaylist.objects.none(),
        'latest_videos': VideoPlaylist.objects.none(),
        'playlists': Playlist.objects.none(),
    }
    return render(request, 'index.html', context)


def playlist_detail(request, playlist_id):
    """View for displaying playlist details"""
    playlist = get_object_or_404(Playlist, id=playlist_id)
    videos = VideoPlaylist.objects.filter(playlist=playlist).order_by('-id')

    # If there are videos, use the first video as current_video
    current_video = videos.first() if videos.exists() else None

    context = {
        'playlist': playlist,
        'playlist_videos': videos,
        'current_video': current_video,
    }
    return render(request, 'videos/playlist_detail.html', context)


def playlist_detail_without_video(request, playlist_id):
    """View for displaying playlist without specific video"""
    playlist = get_object_or_404(Playlist, id=playlist_id)
    videos = VideoPlaylist.objects.filter(playlist=playlist).order_by('-id')

    # If there are videos, use the first video as current_video
    current_video = videos.first() if videos.exists() else None

    context = {
        'playlist': playlist,
        'playlist_videos': videos,
        'current_video': current_video,
    }
    return render(request, 'videos/playlist_detail.html', context)


def imfeeling(request):
    objs = ImFeeling.objects.all()

    # List of colors to choose from
    colors = [
        "#ffdddd", "#ddffdd", "#ddddff", "#ffffdd",
        "#ffe5e5", "#e5ffe5", "#e5e5ff", "#ffffe5",
        "#ffcccb", "#d1e7dd", "#cfe2ff", "#fff3cd"
    ]

    # Assign a random color to each object
    for obj in objs:
        obj.color = random.choice(colors)

    context = {
        'objs': objs,
    }
    return render(request, 'imfeeling.html', context)


def single_feeling(request, feeling):
    if feeling:
        obj = ImFeeling.objects.get(title=feeling)
        return render(request, 'single_feeling.html', {'obj': obj})


# views.py


def dua_dhikr_list(request):
    dua_dhikr = DuaDhikr.objects.all()
    return render(request, 'dua_dhikr/dua_dhikr_list.html', {'dua_dhikr': dua_dhikr})


def dua_dhikr_detail(request, pk):
    dua_dhikr = get_object_or_404(DuaDhikr, pk=pk)
    return render(request, 'dua_dhikr/dua_dhikr_detail.html', {'dua_dhikr': dua_dhikr})


# views.py


def prophet_story_list(request):
    stories = ProphetStory.objects.all()
    return render(request, 'story/prophet_story_list.html', {'stories': stories})


def prophet_story_detail(request, pk):
    story = get_object_or_404(ProphetStory, pk=pk)
    return render(request, 'story/prophet_story_detail.html', {'story': story})


def prayer_list(request):
    prayers = Prayer.objects.all()
    return render(request, 'prayer/prayer_list.html', {'prayers': prayers})


def prayer_detail(request, pk):
    prayer = get_object_or_404(Prayer, pk=pk)
    return render(request, 'prayer/prayer_detail.html', {'prayer': prayer})


def name_list(request):
    names = NameOfAllah.objects.all()
    colors = [
        '#FFDDC1',  # Light peach
        '#FFABAB',  # Light red
        '#FFC3A0',  # Light pink
        '#FF677D',  # Light rose
        '#D4A5A5',  # Light brown
        '#FFE156',  # Light yellow
        '#A0E7E5',  # Light teal
        '#B9FBC0',  # Light green
        '#F6F6F6',  # Very light gray
        '#FFEDDB',  # Light apricot
        '#D9BF77',  # Light gold
        '#F0E68C',  # Light lemon
        '#E2C2E2',
    ]
    name_color_pairs = list(
        zip(names, colors * (len(names) // len(colors) + 1)))[:len(names)]

    return render(request, 'allah_name/name_list.html', {'name_color_pairs': name_color_pairs})


def name_detail(request, slug):
    name = get_object_or_404(NameOfAllah, slug=slug)
    return render(request, 'allah_name/name_detail.html', {'name': name})


def ramadan_duas(request):
    duas = RamadanDua.objects.all()  # Fetch all dua entries
    return render(request, 'ramadan_duas.html', {'duas': duas})


def subsection_list(request):
    subsections = Seerah.objects.all()  # Fetch all subsections
    return render(request, 'muhammad/seerah_list.html', {'subsections': subsections})


def subsection_detail(request, pk):
    # Fetch the specific subsection by primary key
    seerah = get_object_or_404(Seerah, pk=pk)
    return render(request, 'muhammad/seerah_detail.html', {'seerah': seerah})


def muhammad_family(request):
    members = FamilyMember.objects.all().annotate(
        content_preview=Substr('content', 1, 100))
    return render(request, 'muhammad/family_list.html', {'members': members})


def muhammad_family_detail(request, pk):
    member = get_object_or_404(FamilyMember, pk=pk)
    members = FamilyMember.objects.all().annotate(
        content_preview=Substr('content', 1, 100))
    return render(request, 'muhammad/family_detail.html', {'member': member, 'members': members})


def muhammad_children(request):
    childrens = MuhammadChildren.objects.all().annotate(
        content_preview=Substr('content', 1, 100))
    return render(request, 'muhammad/muhammad_children.html', {'childrens': childrens})


def muhammad_children_detail(request, pk):
    children = get_object_or_404(MuhammadChildren, pk=pk)
    childrens = MuhammadChildren.objects.all().annotate(
        content_preview=Substr('content', 1, 100))
    return render(request, 'muhammad/muhammad_children_detail.html', {'children': children, 'childrens': childrens})


def battles_list(request):
    battles = Battle.objects.all().annotate(
        content_preview=Substr('content', 1, 100))
    return render(request, 'muhammad/battles_list.html', {'battles': battles})


def battles_detail(request, pk):
    battle = get_object_or_404(Battle, pk=pk)
    battles = Battle.objects.all().annotate(
        content_preview=Substr('content', 1, 100))
    return render(request, 'muhammad/battles_detail.html', {'battle': battle, 'battles': battles})


def hadith_list(request):
    hadiths = Hadith.objects.all().annotate(
        content_preview=Substr('content', 1, 100))
    return render(request, 'muhammad/hadith_list.html', {'hadiths': hadiths})


def hadith_detail(request, pk):
    hadith = get_object_or_404(Hadith, pk=pk)
    hadiths = Hadith.objects.all().annotate(
        content_preview=Substr('content', 1, 100))
    return render(request, 'muhammad/hadith_detail.html', {'hadith': hadith, 'hadiths': hadiths})


def muhammad_wife(request):
    wifes = Wife.objects.all().annotate(content_preview=Substr('content', 1, 100))
    return render(request, 'muhammad/muhammad_wife.html', {'wifes': wifes})


def muhammad_wife_detail(request, pk):
    wife = get_object_or_404(Wife, pk=pk)
    wifes = Wife.objects.all().annotate(content_preview=Substr('content', 1, 100))
    return render(request, 'muhammad/muhammad_wife_detail.html', {'wife': wife, 'wifes': wifes})


def select_surah(request):
    surahs = Surah.objects.all()
    languages = SurahTranslation.objects.values_list(
        'language', flat=True).distinct()

    if request.method == 'POST':
        selected_surah_id = request.POST.get('surah')
        selected_language = request.POST.get('language')
        translation = SurahTranslation.objects.filter(
            surah_id=selected_surah_id, language=selected_language).first()

        return render(request, 'quran/display_content.html', {
            'translation': translation,
            'surahs': surahs,
            'languages': languages,
        })

    return render(request, 'quran/select_surah.html', {
        'surahs': surahs,
        'languages': languages,
    })


# def upload_playlist(request):
#     if request.method == 'POST':
#         form = PlaylistURLForm(request.POST)
#         if form.is_valid():
#             playlist_url = form.cleaned_data['playlist_url']
#             uploader_name = form.cleaned_data.get('uploader_name', '')
#             uploader_email = form.cleaned_data.get('uploader_email', '')

#             try:
#                 # Create directory if it doesn't exist
#                 folder_name = os.path.join(settings.MEDIA_ROOT, 'videos_israr_ahmad')
#                 if not os.path.exists(folder_name):
#                     os.makedirs(folder_name)

#                 ydl_opts = {
#                     'outtmpl': os.path.join(folder_name, '%(id)s.%(ext)s'),
#                     'restrictfilenames': True,
#                     'format': 'best',
#                 }

#                 results = {
#                     'success': False,
#                     'playlist_title': '',
#                     'total_videos': 0,
#                     'downloaded_videos': 0,
#                     'video_titles': [],
#                     'error': None
#                 }

#                 with YoutubeDL(ydl_opts) as ydl:
#                     # Extract playlist information
#                     playlist_info = ydl.extract_info(playlist_url, download=False)
#                     playlist_title = playlist_info.get('title', 'Untitled Playlist')
#                     results['playlist_title'] = playlist_title
#                     results['total_videos'] = len(playlist_info['entries'])

#                     # Create or get the Playlist object
#                     playlist = Playlist.objects.create(
#                         title=playlist_title,
#                         uploaded_by={'name': uploader_name, 'email': uploader_email}
#                     )

#                     # Download videos and update the database
#                     for video in playlist_info['entries']:
#                         try:
#                             video_id = video.get('id')
#                             video_title = video.get('title', 'Untitled Video')[:100]  # Limit title length
#                             video_description = video.get('description', '')
#                             video_views = video.get('view_count', 0)
#                             video_image_url = video.get('thumbnail', '')

#                             video_file_path = os.path.join(folder_name, f"{video_id}.mp4")
#                             relative_file_path = f'videos_israr_ahmad/{video_id}.mp4'

#                             # Create or update video entry
#                             video_playlist = VideoPlaylist.objects.create(
#                                 playlist=playlist,
#                                 title=video_title,
#                                 file=relative_file_path,
#                                 views=video_views,
#                                 description=video_description,
#                                 image_url=video_image_url,
#                                 uploaded_by={'name': uploader_name, 'email': uploader_email}
#                             )

#                             if not os.path.exists(video_file_path):
#                                 # Download the video
#                                 ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

#                             if os.path.exists(video_file_path):
#                                 video_playlist.file = relative_file_path
#                                 video_playlist.save()
#                                 results['downloaded_videos'] += 1
#                                 results['video_titles'].append(video_title)

#                         except Exception as e:
#                             print(f"Error processing video {video_title}: {e}")

#                     results['success'] = True

#                 # Store results in session
#                 request.session['upload_results'] = {
#                     'playlist_title': results['playlist_title'],
#                     'total_videos': results['total_videos'],
#                     'downloaded_videos': results['downloaded_videos'],
#                     'video_titles': results['video_titles'],
#                     'playlist_url': playlist_url
#                 }

#                 messages.success(
#                     request,
#                     f"Successfully processed playlist '{results['playlist_title']}'"
#                 )
#                 return redirect('upload_success')

#             except Exception as e:
#                 messages.error(request, f'Error processing playlist: {str(e)}')
#                 print(f"Error: {str(e)}")
#     else:
#         form = PlaylistURLForm()

#     return render(request, 'videos/upload_playlist.html', {'form': form})


# from django.http import JsonResponse
# from django.template.loader import render_to_string
# from django.http import JsonResponse
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import PlaylistURLForm
# from .models import Playlist, VideoPlaylist
# import os
# from django.conf import settings
# from yt_dlp import YoutubeDL
# import json
# from django.views.decorators.csrf import csrf_exempt

# def upload_playlist(request):
#     if request.method == 'POST':
#         form = PlaylistURLForm(request.POST)
#         if form.is_valid():
#             playlist_url = form.cleaned_data['playlist_url']
#             uploader_name = form.cleaned_data.get('uploader_name', '')
#             uploader_email = form.cleaned_data.get('uploader_email', '')

#             try:
#                 # Initialize YoutubeDL to get playlist info
#                 with YoutubeDL() as ydl:
#                     playlist_info = ydl.extract_info(playlist_url, download=False)

#                     # Store initial info in session
#                     request.session['download_info'] = {
#                         'playlist_title': playlist_info.get('title', 'Untitled Playlist'),
#                         'playlist_url': playlist_url,
#                         'total_videos': len(playlist_info['entries']),
#                         'downloaded_count': 0,
#                         'current_video': '',
#                         'videos': [],
#                         'uploader_name': uploader_name,
#                         'uploader_email': uploader_email,
#                         'status': 'initialized'
#                     }

#                     # Store video information
#                     video_info_list = []
#                     for video in playlist_info['entries']:
#                         video_info_list.append({
#                             'id': video.get('id'),
#                             'title': video.get('title', 'Untitled Video'),
#                             'duration': video.get('duration', 0),
#                             'status': 'pending'
#                         })
#                     request.session['video_info'] = video_info_list

#                     return redirect('download_progress')

#             except Exception as e:
#                 messages.error(request, f'Error processing playlist: {str(e)}')
#     else:
#         form = PlaylistURLForm()

#     return render(request, 'videos/upload_playlist.html', {'form': form})

# def download_progress(request):
#     download_info = request.session.get('download_info')
#     if not download_info:
#         messages.error(request, 'No download in progress')
#         return redirect('upload_playlist')

#     return render(request, 'videos/download_progress.html', {
#         'download_info': download_info
#     })

# @csrf_exempt
# def start_download(request):
#     if request.method == 'POST':
#         download_info = request.session.get('download_info')
#         video_info = request.session.get('video_info')

#         if not download_info or not video_info:
#             return JsonResponse({'status': 'error', 'message': 'No download information found'})

#         try:
#             folder_name = os.path.join(settings.MEDIA_ROOT, 'videos_israr_ahmad')
#             if not os.path.exists(folder_name):
#                 os.makedirs(folder_name)

#             ydl_opts = {
#                 'outtmpl': os.path.join(folder_name, '%(id)s.%(ext)s'),
#                 'restrictfilenames': True,
#                 'format': 'best',
#             }

#             # Create or get playlist
#             playlist, created = Playlist.objects.get_or_create(
#                 title=download_info['playlist_title'],
#                 defaults={
#                     'uploader_name': download_info['uploader_name'],
#                     'uploader_email': download_info['uploader_email']
#                 }
#             )

#             download_info['status'] = 'downloading'
#             request.session['download_info'] = download_info

#             with YoutubeDL(ydl_opts) as ydl:
#                 for index, video in enumerate(video_info):
#                     try:
#                         # Update current video status
#                         download_info['current_video'] = video['title']
#                         video['status'] = 'downloading'
#                         request.session['video_info'] = video_info
#                         request.session.modified = True

#                         # Download video
#                         video_url = f"https://www.youtube.com/watch?v={video['id']}"
#                         ydl.download([video_url])

#                         # Create video entry in database
#                         video_file_path = f"videos_israr_ahmad/{video['id']}.mp4"
#                         VideoPlaylist.objects.create(
#                             playlist=playlist,
#                             title=video['title'],
#                             file=video_file_path,
#                             # uploaded_by={'name': uploader_name, 'email': uploader_email}
#                         )

#                         # Update status
#                         download_info['downloaded_count'] += 1
#                         video['status'] = 'complete'
#                         download_info['videos'].append({
#                             'title': video['title'],
#                             'status': 'complete'
#                         })

#                         request.session['download_info'] = download_info
#                         request.session['video_info'] = video_info
#                         request.session.modified = True

#                     except Exception as e:
#                         video['status'] = 'error'
#                         print(f"Error downloading video {video['title']}: {str(e)}")

#             download_info['status'] = 'complete'
#             request.session['download_info'] = download_info

#             return JsonResponse({'status': 'success'})

#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)})

#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# def download_status(request):
#     """
#     AJAX endpoint to get current download status
#     """
#     download_info = request.session.get('download_info', {})
#     video_info = request.session.get('video_info', [])

#     if not download_info:
#         return JsonResponse({'status': 'error', 'message': 'No download information found'})

#     response_data = {
#         'status': download_info['status'],
#         'playlist_title': download_info['playlist_title'],
#         'total_videos': download_info['total_videos'],
#         'downloaded_count': download_info['downloaded_count'],
#         'current_video': download_info['current_video'],
#         'videos': download_info['videos'],
#         'progress_percentage': int((download_info['downloaded_count'] / download_info['total_videos']) * 100),
#         'video_statuses': [
#             {
#                 'title': video['title'],
#                 'status': video['status']
#             } for video in video_info
#         ]
#     }

#     return JsonResponse(response_data)

# def upload_success(request):
#     download_info = request.session.get('download_info')
#     if not download_info or download_info['status'] != 'complete':
#         return redirect('upload_playlist')

#     try:
#         playlist = Playlist.objects.get(title=download_info['playlist_title'])
#         videos = VideoPlaylist.objects.filter(playlist=playlist).order_by('-id')

#         context = {
#             'download_info': download_info,
#             'playlist': playlist,
#             'videos': videos,
#         }

#         # Clear session data
#         request.session.pop('download_info', None)
#         request.session.pop('video_info', None)

#         return render(request, 'videos/upload_success.html', context)

#     except Playlist.DoesNotExist:
#         messages.error(request, "Couldn't find the uploaded playlist.")
#         return redirect('upload_playlist')


def upload_playlist(request):
    """Handle the initial playlist URL submission and information extraction."""
    if request.method == 'POST':
        form = PlaylistURLForm(request.POST)
        if form.is_valid():
            playlist_url = form.cleaned_data['playlist_url']
            uploader_name = form.cleaned_data.get('uploader_name', '')
            uploader_email = form.cleaned_data.get('uploader_email', '')

            try:
                with YoutubeDL() as ydl:
                    playlist_info = ydl.extract_info(
                        playlist_url, download=False)

                    # Initialize download info in session
                    request.session['download_info'] = {
                        'playlist_title': playlist_info.get('title', 'Untitled Playlist'),
                        'playlist_url': playlist_url,
                        'total_videos': len(playlist_info['entries']),
                        'downloaded_count': 0,
                        'current_video': '',
                        'videos': [],
                        'uploader_name': uploader_name,
                        'uploader_email': uploader_email,
                        'status': 'initialized'
                    }

                    # Store individual video information
                    video_info_list = [
                        {
                            'id': video.get('id'),
                            'title': video.get('title', 'Untitled Video'),
                            'duration': video.get('duration', 0),
                            'status': 'pending'
                        }
                        for video in playlist_info['entries']
                    ]
                    request.session['video_info'] = video_info_list

                    return redirect('download_progress')

            except Exception as e:
                messages.error(request, f'Error processing playlist: {str(e)}')
    else:
        form = PlaylistURLForm()

    return render(request, 'videos/upload_playlist.html', {'form': form})


def download_progress(request):
    """Display the download progress page."""
    download_info = request.session.get('download_info')
    if not download_info:
        messages.error(request, 'No download in progress')
        return redirect('upload_playlist')

    return render(request, 'videos/download_progress.html', {
        'download_info': download_info
    })


# @csrf_exempt
# def start_download(request):
#     """Handle the actual download process."""
#     if request.method != 'POST':
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

#     download_info = request.session.get('download_info')
#     video_info = request.session.get('video_info')

#     if not download_info or not video_info:
#         return JsonResponse({'status': 'error', 'message': 'No download information found'})

#     try:
#         # Ensure download directory exists
#         folder_name = os.path.join(settings.MEDIA_ROOT, 'videos_israr_ahmad')
#         os.makedirs(folder_name, exist_ok=True)

#         # Configure youtube-dl options
#         ydl_opts = {
#             'outtmpl': os.path.join(folder_name, '%(id)s.%(ext)s'),
#             'format': 'best',  # or 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
#             'quiet': False,
#             'no_warnings': False,
#             'extract_flat': False,
#             'writethumbnail': True,
#             'verbose': True  # Add this for debugging
#         }

#         # Create playlist record
#         playlist = Playlist.objects.create(
#             title=download_info['playlist_title']
#         )

#         # Start downloading process
#         with YoutubeDL(ydl_opts) as ydl:
#             for video in video_info:
#                 try:
#                     # Update current video status
#                     print(f"Starting download for video: {video['title']}")  # Debug print
#                     download_info['current_video'] = video['title']
#                     video['status'] = 'downloading'
#                     request.session.modified = True

#                     # Download video
#                     video_url = f"https://www.youtube.com/watch?v={video['id']}"
#                     print(f"Downloading from URL: {video_url}")  # Debug print
#                     result = ydl.download([video_url])
#                     print(f"Download result: {result}")  # Debug print

#                     # Verify file exists
#                     expected_file = os.path.join(folder_name, f"{video['id']}.mp4")
#                     if not os.path.exists(expected_file):
#                         print(f"Warning: File not found at {expected_file}")
#                         # Try to find the actual file
#                         possible_files = [f for f in os.listdir(folder_name) if f.startswith(video['id'])]
#                         if possible_files:
#                             expected_file = os.path.join(folder_name, possible_files[0])
#                             print(f"Found alternative file: {expected_file}")

#                     # Create video entry in database
#                     relative_path = os.path.relpath(expected_file, settings.MEDIA_ROOT)
#                     video_obj = VideoPlaylist.objects.create(
#                         playlist=playlist,
#                         title=video['title'],
#                         file=relative_path
#                     )
#                     print(f"Created video object: {video_obj.id}")  # Debug print

#                     # Update progress
#                     download_info['downloaded_count'] += 1
#                     video['status'] = 'complete'
#                     download_info['videos'].append({
#                         'title': video['title'],
#                         'status': 'complete'
#                     })

#                     request.session['download_info'] = download_info
#                     request.session['video_info'] = video_info
#                     request.session.modified = True

#                 except Exception as e:
#                     print(f"Error downloading video {video['title']}: {str(e)}")  # Debug print
#                     video['status'] = 'error'
#                     continue

#         download_info['status'] = 'complete'
#         request.session['download_info'] = download_info

#         return JsonResponse({
#             'status': 'success',
#             'message': f'Successfully downloaded {download_info["downloaded_count"]} videos'
#         })

#     except Exception as e:
#         print(f"Error in start_download: {str(e)}")  # Debug print
#         return JsonResponse({
#             'status': 'error',
#             'message': str(e)
#         })


@csrf_exempt
def start_download(request):
    """Handle the actual download process."""
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

    download_info = request.session.get('download_info')
    video_info = request.session.get('video_info')

    if not download_info or not video_info:
        return JsonResponse({'status': 'error', 'message': 'No download information found'})

    try:
        # Ensure download directory exists
        folder_name = os.path.join(settings.MEDIA_ROOT, 'videos_israr_ahmad')
        thumbnail_folder = os.path.join(settings.MEDIA_ROOT, 'thumbnails')
        os.makedirs(folder_name, exist_ok=True)
        os.makedirs(thumbnail_folder, exist_ok=True)

        # Configure youtube-dl options
        ydl_opts = {
            'outtmpl': os.path.join(folder_name, '%(id)s.%(ext)s'),
            'format': 'best',
            'writethumbnail': True,
            'writeinfojson': True,
            'quiet': False,
            'no_warnings': False,
            'extract_flat': False,
            'verbose': True
        }

        # First, get playlist info for thumbnail
        with YoutubeDL() as ydl:
            playlist_info = ydl.extract_info(
                download_info['playlist_url'], download=False)

            # Create playlist record with thumbnail
            playlist = Playlist.objects.create(
                title=download_info['playlist_title']
            )

            # Try to save playlist thumbnail if available
            if playlist_info.get('thumbnail'):
                try:
                    import requests
                    from django.core.files import File
                    from django.core.files.temp import NamedTemporaryFile

                    # Download thumbnail
                    response = requests.get(playlist_info['thumbnail'])
                    if response.status_code == 200:
                        img_temp = NamedTemporaryFile(delete=True)
                        img_temp.write(response.content)
                        img_temp.flush()

                        # Save thumbnail to playlist
                        playlist.image.save(
                            f"playlist_{playlist.id}_thumb.jpg", File(img_temp), save=True)
                except Exception as e:
                    print(f"Error saving playlist thumbnail: {e}")

        # Start downloading videos
        with YoutubeDL(ydl_opts) as ydl:
            for video in video_info:
                try:
                    # Update current video status
                    print(f"Starting download for video: {video['title']}")
                    download_info['current_video'] = video['title']
                    video['status'] = 'downloading'
                    request.session.modified = True

                    # Get video info first
                    video_url = f"https://www.youtube.com/watch?v={video['id']}"
                    video_info_dict = ydl.extract_info(
                        video_url, download=False)

                    # Download video
                    result = ydl.download([video_url])

                    # Find the downloaded video file
                    expected_file = os.path.join(
                        folder_name, f"{video['id']}.mp4")
                    if not os.path.exists(expected_file):
                        possible_files = [f for f in os.listdir(
                            folder_name) if f.startswith(video['id'])]
                        if possible_files:
                            expected_file = os.path.join(
                                folder_name, possible_files[0])

                    # Create video entry in database
                    relative_path = os.path.relpath(
                        expected_file, settings.MEDIA_ROOT)
                    video_obj = VideoPlaylist.objects.create(
                        playlist=playlist,
                        title=video['title'],
                        file=relative_path,
                        description=video_info_dict.get('description', ''),
                        views=video_info_dict.get('view_count', 0)
                    )

                    # Save video thumbnail
                    if video_info_dict.get('thumbnail'):
                        try:
                            import requests
                            from django.core.files import File
                            from django.core.files.temp import NamedTemporaryFile

                            # Download thumbnail
                            response = requests.get(
                                video_info_dict['thumbnail'])
                            if response.status_code == 200:
                                img_temp = NamedTemporaryFile(delete=True)
                                img_temp.write(response.content)
                                img_temp.flush()

                                # Save thumbnail
                                video_obj.image.save(
                                    f"video_{video_obj.id}_thumb.jpg", File(img_temp), save=True)
                        except Exception as e:
                            print(f"Error saving video thumbnail: {e}")

                    # Update progress
                    download_info['downloaded_count'] += 1
                    video['status'] = 'complete'
                    download_info['videos'].append({
                        'title': video['title'],
                        'status': 'complete',
                        'thumbnail': video_info_dict.get('thumbnail', ''),
                        'description': video_info_dict.get('description', ''),
                        'views': video_info_dict.get('view_count', 0)
                    })

                    request.session['download_info'] = download_info
                    request.session['video_info'] = video_info
                    request.session.modified = True

                except Exception as e:
                    print(f"Error downloading video {
                          video['title']}: {str(e)}")
                    video['status'] = 'error'
                    continue

        download_info['status'] = 'complete'
        request.session['download_info'] = download_info

        return JsonResponse({
            'status': 'success',
            'message': f'Successfully downloaded {download_info["downloaded_count"]} videos'
        })

    except Exception as e:
        print(f"Error in start_download: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })


def download_status(request):
    """AJAX endpoint to get current download status."""
    download_info = request.session.get('download_info', {})
    video_info = request.session.get('video_info', [])

    if not download_info:
        return JsonResponse({'status': 'error', 'message': 'No download information found'})

    total_videos = download_info.get('total_videos', 0)
    downloaded_count = download_info.get('downloaded_count', 0)

    response_data = {
        'status': download_info.get('status', ''),
        'playlist_title': download_info.get('playlist_title', ''),
        'total_videos': total_videos,
        'downloaded_count': downloaded_count,
        'current_video': download_info.get('current_video', ''),
        'videos': download_info.get('videos', []),
        'progress_percentage': int((downloaded_count / total_videos * 100) if total_videos > 0 else 0)
    }

    return JsonResponse(response_data)


def upload_success(request):
    download_info = request.session.get('download_info')
    if not download_info or download_info['status'] != 'complete':
        return redirect('upload_playlist')

    try:
        playlist = Playlist.objects.get(title=download_info['playlist_title'])
        videos = VideoPlaylist.objects.filter(
            playlist=playlist).order_by('-id')

        results = {
            'playlist': playlist,
            'total_videos': download_info['total_videos'],
            'downloaded_videos': download_info['downloaded_count'],
            'playlist_title': download_info['playlist_title'],
            'videos': videos,
        }

        # Clear session data
        request.session.pop('download_info', None)
        request.session.pop('video_info', None)

        return render(request, 'videos/upload_success.html', {'results': results})

    except Playlist.DoesNotExist:
        messages.error(request, "Couldn't find the uploaded playlist.")
        return redirect('upload_playlist')


def check_download_status(request):
    """Debug view to check download status"""
    download_info = request.session.get('download_info', {})
    video_info = request.session.get('video_info', [])
    playlists = Playlist.objects.all()
    videos = VideoPlaylist.objects.all()

    context = {
        'download_info': download_info,
        'video_info': video_info,
        'playlists': playlists,
        'videos': videos,
    }
    return render(request, 'videos/debug_status.html', context)


def video_detail(request, video_id):
    video = get_object_or_404(VideoPlaylist, id=video_id)
    suggested_videos = VideoPlaylist.objects.exclude(id=video_id)[:5]
    return render(request, 'videos/video_detail.html', {'video': video, 'suggested_videos': suggested_videos})


def playlist_detail(request, playlist_id, video_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    playlist_videos = playlist.playlists.all()
    current_video = get_object_or_404(VideoPlaylist, id=video_id)
    return render(request, 'videos/playlist_detail.html', {'playlist': playlist, 'playlist_videos': playlist_videos, 'current_video': current_video})

# def playlist_detail(request, playlist_id):
#     """View for displaying playlist details"""
#     try:
#         playlist = Playlist.objects.get(id=playlist_id)
#         videos = VideoPlaylist.objects.filter(playlist=playlist)

#         context = {
#             'playlist': playlist,
#             'videos': videos,
#         }
#         return render(request, 'videos/playlist_detail.html', context)
#     except Playlist.DoesNotExist:
#         messages.error(request, "Playlist not found.")
#         return redirect('playlist_list')


def video_list(request):
    videos = VideoPlaylist.objects.all()
    return render(request, 'videos/video_list.html', {'videos': videos})


def playlist_list(request):
    playlists = Playlist.objects.all().order_by('-id')
    return render(request, 'videos/playlist_list.html', {'playlists': playlists})

# def playlist_detail(request, playlist_id):
#     playlist = Playlist.objects.get(id=playlist_id)
#     videos = VideoPlaylist.objects.filter(playlist=playlist).order_by('-id')
#     return render(request, 'videos/playlist_detail.html', {
#         'playlist': playlist,
#         'videos': videos
#     })


# from django.http import HttpResponse
# from django.conf import settings
# import os

# def serve_video(request, path):
#     video_path = os.path.join(settings.MEDIA_ROOT, path)
#     start = 0
#     end = None
#     file_size = os.path.getsize(video_path)

#     # Check if the Range header is present
#     range_header = request.headers.get('Range', None)
#     if range_header:
#         # Parse the range header
#         byte_range = range_header.split('=')[1]
#         start, end = byte_range.split('-')
#         start = int(start)
#         if end:
#             end = int(end)
#         else:
#             end = file_size - 1

#     # Read the file in the range requested
#     with open(video_path, 'rb') as f:
#         f.seek(start)
#         data = f.read(end - start + 1)

#     # Set the proper headers for partial content
#     response = HttpResponse(data, content_type='video/mp4')
#     response['Content-Range'] = f'bytes {start}-{end}/{file_size}'
#     response['Content-Length'] = str(len(data))
#     response['Accept-Ranges'] = 'bytes'

#     print('...........................................tttttttttttttttt')
#     return response


# TODO: add images, slugs in url,pagination,etc.
# design homepage with slider, cards, etc.
# add ISRAR AHMAD VIDEOS
# modify content of https://www.islamestic.com/sample-page/ for about us page
# add donation button
# add drug , recovery related, etc.
# scrape islamic content and modify before saving ( for copy right )
#  link videos and playlist page to home PAGE, because its my important feature (with best ui )
#  pagination/search bar, default thumbnails
# add islamic podcasts, upload bucket/s3 media and static files
# setup backup for media and db content
# add islamic books
# add islamic movies
# add shorts
# library
# add search bar
