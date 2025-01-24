import os
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import RamadanDua  



class Command(BaseCommand):
    help = 'Scrape prayer names and image URLs from the specified webpage'

    def handle(self, *args, **kwargs):
        url = "https://www.islamestic.com/the-ultimate-ramadan-duas-list/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for dua_section in soup.select('h2.wp-block-heading'):
            title = dua_section.get_text()
            arabic = dua_section.find_next('h6').get_text()
            translation = dua_section.find_next('p').get_text()
            reference = dua_section.find_next('strong').get_text()

            # Concatenate the content
            content = f"<div style='padding: 20px; border-radius: 8px; font-family: 'Noto Nastaliq Urdu', serif; font-size: 20px; color: #333;'> <h2 style='text-align:center; align:center; '>{arabic}</h2><p>{translation}</p><strong>{reference}</strong></div>"

            # Create a new Dua object
            dua = RamadanDua(
                title=title,
                description=content,
                reference=reference
            )
            dua.save() 

            self.stdout.write(self.style.SUCCESS(f'Successfully save RamadanDua: s{title}'))

        self.stdout.write(self.style.SUCCESS('Successfully scraped and saved/updated RamadanDua data.'))