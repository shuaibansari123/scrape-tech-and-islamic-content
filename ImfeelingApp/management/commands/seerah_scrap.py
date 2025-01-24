import os
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import RamadanDua  

from ImfeelingApp.models import Seerah

class Command(BaseCommand):
    help = 'Scrape Seerah'

    def handle(self, *args, **kwargs):
        url = "https://www.islamestic.com/seerah/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        
        sections = soup.find_all('h2')
        for section in sections:
            section_title = section.get_text(strip=True)
            subsections = section.find_next('ul') 

            if subsections:
                for li in subsections.find_all('li'):
                    subsection_title = li.get_text(strip=True)
                    content = f"<p>{subsection_title}</p>"  # You can customize this as needed

                    # Create a new Seerah object
                    seerah_entry = Seerah(
                        title=subsection_title,
                        content=content,
                        section=section_title,
                        subsection=subsection_title,
                    
                    )
                    seerah_entry.save()  # Save the object to the database

                    self.stdout.write(self.style.SUCCESS(f'Successfully save Seerah: {subsection_title}'))
            else:
                # If there are no subsections, create a Seerah entry for the section itself
                content = f"<p>{section_title}</p>"
                seerah_entry = Seerah(
                    title=section_title,
                    content=content,
                    section=section_title
                )
                seerah_entry.save()  # Save the object to the database
                self.stdout.write(self.style.SUCCESS(f'Successfully save Seerah: {section_title}'))

        self.stdout.write(self.style.SUCCESS('Successfully scraped and saved/updated Seerah data.'))