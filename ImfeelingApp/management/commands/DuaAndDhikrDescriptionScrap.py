# scrape_dua_dhikr.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import DuaDhikr  # Adjust the import based on your app name

class Command(BaseCommand):
    help = 'Scrape dua and dhikr from the specified webpage'

    def handle(self, *args, **kwargs):
        url = "https://www.islamestic.com/dua-dhikr/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the main content area
        main_content = soup.find('main', id='primary')
        articles = main_content.find_all('h2', class_='ultp-block-title')

        for article in articles:
            title = article.get_text(strip=True)
            link = article.find('a')['href']

            # Fetch the content from the link
            content_response = requests.get(link)
            content_soup = BeautifulSoup(content_response.content, 'html.parser')
            description = content_soup.find('div', class_='entry-content').decode_contents()

            # Save to the database
            DuaDhikr.objects.update_or_create(
                title=title,
                defaults={'description': f"""
                    <div style="padding: 20px; border-radius: 8px; font-family: 'Noto Nastaliq Urdu', serif; font-size: 20px; color: #333;">
                        {description}
                    </div>
                    """}
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully scraped and saved: {title}'))