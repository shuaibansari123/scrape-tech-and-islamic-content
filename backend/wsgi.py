# """
# WSGI config for backend project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# application = get_wsgi_application()






import os
import sys

# Add your project directory to the sys.path
path = '/home/InnerPeace/InnerPeace'
if path not in sys.path:
    sys.path.append(path)

# Add your project's parent directory to the sys.path
parent_path = '/home/InnerPeace'
if parent_path not in sys.path:
    sys.path.append(parent_path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'  # Adjust if your settings path is different

# Import Django WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()