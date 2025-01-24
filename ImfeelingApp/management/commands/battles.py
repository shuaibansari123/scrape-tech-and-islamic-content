import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import Battle  # Import the new model

class Command(BaseCommand):
    help = 'Scrape battles fought by Prophet Muhammad (PBUH)'

    def handle(self, *args, **kwargs):
        # URL of the main page containing battles
        main_url = "https://www.islamestic.com/battles-fought-by-prophet/"
        
        # Fetch the main page
        response = requests.get(main_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the titles in the specified class
        sections = soup.find_all('h2', class_='wp-block-heading has-text-align-center')

        for section in sections:
            title = section.text.strip()  # Get the title text
            detail_url = section.find_next('a')['href']  # Get the link to the detail page

            # Fetch the detail page
            detail_response = requests.get(detail_url)
            detail_soup = BeautifulSoup(detail_response.content, 'html.parser')

            # Extract content from the detail page
            content_div = detail_soup.find('div', class_='rishi-post-wrapper')
            if content_div:
                content = content_div.decode_contents()  # Get the HTML content

                # Create or update the Battle entry
                battle, created = Battle.objects.update_or_create(
                    title=title,
                    defaults={'content':  f"""
                    <div style="padding: 20px; border-radius: 8px; font-family: 'Noto Nastaliq Urdu', serif; font-size: 20px; color: #333;">
                        {content}
                    </div>
                    """}  # Save the HTML content
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created new entry: {title}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated entry: {title}"))
            else:
                self.stdout.write(self.style.WARNING(f"No content found for: {title}"))