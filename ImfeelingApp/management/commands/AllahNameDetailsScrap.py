from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from django.utils.text import slugify
from ImfeelingApp.models import NameOfAllah

class Command(BaseCommand):
    help = 'Scrape names of Allah and save to database'

    def handle(self, *args, **kwargs):
        # Fetch all names from the database
        names = NameOfAllah.objects.all()

        for name_entry in names:
            name = name_entry.name
            slug = name_entry.slug
            url = f"https://www.islamestic.com/{slug}/"  # Construct the URL using the slug
            print(name, slug, url)
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an error for bad responses
                soup = BeautifulSoup(response.content, 'html.parser')

                # Scraping the required details
                arabic_name = soup.find('h6', class_='has-text-align-center has-large-font-size wp-block-heading').get_text(strip=True)
                english_name = soup.find('pre', class_='wp-block-verse has-text-align-center').get_text(strip=True)
                meaning = soup.find_all('pre', class_='wp-block-verse has-text-align-center')[1].get_text(strip=True).replace("Meaning :", "").strip()
                explanation = soup.find('p').get_text(strip=True)

                # Update the existing entry in the database
                name_entry.description = f"<div style='background-color: #f0f0f0; font-size: 16px; color: #333; padding: 10px;'><strong>{arabic_name}</strong><br><strong>Meaning:</strong> {meaning}<br><strong>Explanation:</strong> {explanation}</div>"
                name_entry.save()

                self.stdout.write(self.style.SUCCESS(f'Updated: {name}'))

            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f'Error fetching {url}: {e}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing {name}: {e}'))