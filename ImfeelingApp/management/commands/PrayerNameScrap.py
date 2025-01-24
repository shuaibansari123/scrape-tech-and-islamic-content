import os
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from ImfeelingApp.models import Prayer  


class Command(BaseCommand):
    help = 'Scrape prayer names and image URLs from the specified webpage'

    def handle(self, *args, **kwargs):
        url = "https://www.islamestic.com/how-to-pray-salah/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the prayer items
        prayer_items = soup.select('.ultp-block-item')

        for item in prayer_items:
            # Extract the prayer name and link
            prayer_name = item.find('img')['alt']
            prayer_link = item.find('a')['href']
            image_url = item.find('img')['data-src']  # Get the image URL

            # Construct the absolute image URL
            if image_url.startswith('/'):
                image_url = f'https://www.islamestic.com{image_url}'

            # Update or create the Prayer object
            Prayer.objects.update_or_create(
                name=prayer_name,
                defaults={
                    'image': image_url  # Save the image URL directly
                }
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully save PrayerName: s{prayer_name}'))

        self.stdout.write(self.style.SUCCESS('Successfully scraped and saved/updated prayer data with image URLs.'))