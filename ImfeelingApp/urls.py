from django.urls import path
from . import views
# from django_serve_media import serve


urlpatterns = [
    path('', views.index, name='home'),
    path('feeling', views.imfeeling, name='i-m-feeling'),
    path('feeling/<str:feeling>', views.single_feeling, name='single-feeling'),

    path('dua-dhikr/', views.dua_dhikr_list, name='dua_dhikr_list'),
    path('dua-dhikr/<int:pk>/', views.dua_dhikr_detail, name='dua_dhikr_detail'),

    path('prophet-stories/', views.prophet_story_list, name='prophet_story_list'),
    path('prophet-stories/<int:pk>/', views.prophet_story_detail, name='prophet_story_detail'),


    path('prayers/', views.prayer_list, name='prayer_list'),
    path('prayers/<int:pk>/', views.prayer_detail, name='prayer_detail'),

    path('names/', views.name_list, name='name_list'),  # List of names
    path('names/<slug:slug>/', views.name_detail, name='name_detail'),  # Detail view for each name

    path('ramadan-duas/', views.ramadan_duas, name='ramadan_duas'),

    path('seerah/subsections/', views.subsection_list, name='subsection_list'),
    path('seerah/subsections/<int:pk>/', views.subsection_detail, name='subsection_detail'),

    path('muhammad/family/', views.muhammad_family, name='muhammad_family'),
    path('muhammad/family/<int:pk>/', views.muhammad_family_detail, name='muhammad_family_detail'),

    path('muhammad/children/', views.muhammad_children, name='muhammad_children'),
    path('muhammad/children/<int:pk>/', views.muhammad_children_detail, name='muhammad_children_detail'),


    path('hadith/', views.hadith_list, name='hadith_list'),
    path('hadith/<int:pk>/', views.hadith_detail, name='hadith_detail'),

    path('battles/', views.battles_list, name='battles_list'),
    path('battles/<int:pk>/', views.battles_detail, name='battles_detail'),

    path('muhammad/wife/', views.muhammad_wife, name='muhammad_wife'),
    path('muhammad/wife/<int:pk>/', views.muhammad_wife_detail, name='muhammad_wife_detail'),

    path('select-surah/', views.select_surah, name='select_surah'),




    path('videos/', views.video_list, name='video_list'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('playlists/', views.playlist_list, name='playlist_list'),
    path('playlist/<int:playlist_id>/<int:video_id>', views.playlist_detail, name='playlist_detail'),
    path('playlist/<int:playlist_id>/', views.playlist_detail_without_video, name='playlist_detail_without_video'),
    
    # upload playlist
    path('upload-playlist/', views.upload_playlist, name='upload_playlist'),
    path('download-progress/', views.download_progress, name='download_progress'),
    path('start-download/', views.start_download, name='start_download'),
    path('download-status/', views.download_status, name='download_status'),
    path('upload-success/', views.upload_success, name='upload_success'),
    path('debug-status/', views.check_download_status, name='debug_status'),

    # path('media/videos/<path:path>/', views.serve_video, name='serve_video'),
    # path('media/<path:path>/', serve, name='serve_media'),


]

# before migrate backup db
# sqlite3 your_database.db .dump > dump.sql
# set PYTHONIOENCODING=utf-8 && python manage.py dumpdata --natural-primary --natural-foreign --exclude=contenttypes --exclude=auth.Permission > db.json
# python -m json.tool db.json

# cursor.execute("PRAGMA cache_size = 100000;")  # Larger cache size
# cursor.execute("PRAGMA temp_store = MEMORY;") # Use in-memory temp tables
# print("Memory limits increased for SQLite.")

# import sqlite3
# conn = sqlite3.connect('db.sqlite3')
# with open('dump.sql', 'w', encoding='utf-8') as f:
#     for line in conn.iterdump():
#         f.write(f'{line}\n')
# conn.close()



# export sqlite db data (migrate to cloud db)
# python manage.py dumpdata --natural-primary --natural-foreign --exclude=contenttypes --exclude=auth.Permission > db.json
# python manage.py loaddata db.json
#  for gcp
    # DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    # GS_BUCKET_NAME = 'your_bucket_name'
    # GS_CREDENTIALS = 'path/to/your/service-account-file.json'
    # gsutil rsync -r /path/to/media/ gs://your_bucket_name/

# for aws
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # AWS_ACCESS_KEY_ID = 'your_aws_access_key_id'
    # AWS_SECRET_ACCESS_KEY = 'your_aws_secret_access_key'
    # AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
    # AWS_S3_REGION_NAME = 'your_region'  # e.g., 'us-west-1'
    # AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    # aws s3 sync /path/to/media/ s3://your_bucket_name

# python manage.py s3_sync media/ s3://your-bucket-name/media/
# UPDATE your_table SET file_field = REPLACE(file_field, '/media/', 'https://your_bucket_name.s3.amazonaws.com/');




# django-ckeditor==6.7.1

# super user credencial
# Email address: test1@gmail.com / 
# Username (leave blank to use 'shuai'): test1 / islam
# Password: 1234 / password

# server superu user 
# name: islam
# password: password

# selenium version==
# when download video, save in db with playlist and video,  title description, etc. video file name should not be greather then 90 words
# why m not able to play video from random timelines

# domain name suggestions :
    # keywords: inner, existance, supreme, secrets, peace

# use in ckeditor for content
#  <div style="padding: 20px; border-radius: 8px; font-family: 'Noto Nastaliq Urdu', serif; font-size: 20px; color: #333;">

# create comments, like sections,
# create uploader library functionality (youtube playlist uploader)

# nginx conf for serving files 
# location /media/ {
#     root /path/to/your/project;
#     add_header Cache-Control "public, max-age=31536000";
#     sendfile on;
#     tcp_nopush on;
#     tcp_nodelay on;
#     keepalive_timeout 65;
#     aio on;
#     directio 4m;
# }

# #  location /media/ {
#         root /path/to/your/project;  # Adjust this to the path where your media files are stored
#         add_header Cache-Control "public, max-age=31536000";
#         sendfile on;
#         tcp_nopush on;
#         tcp_nodelay on;
#         keepalive_timeout 65;
#         aio on;
#         directio 4m;
# }


# location /media/ {
#     root /path/to/your/project;
#     add_header Cache-Control "public, max-age=31536000";
#     sendfile on;
#     tcp_nopush on;
#     tcp_nodelay on;
#     keepalive_timeout 65;
#     aio on;
#     directio 4m;
#     # Optional: Set a maximum size for range requests
#     client_max_body_size 2G;
#     # Enable proper support for range requests
#     chunked_transfer_encoding on;
# }