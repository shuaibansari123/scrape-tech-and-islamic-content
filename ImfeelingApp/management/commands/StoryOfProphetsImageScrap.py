import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import ProphetStory 

class Command(BaseCommand):
    help = 'Scrape stories of prophets from the specified webpage'

    def handle(self, *args, **kwargs):
        url = "https://www.islamestic.com/the-stories-of-prophets/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the main content area
        main_content = soup.find('div', class_='entry-content')
        articles = main_content.find_all('div', class_='ultp-block-item')

        for article in articles:
            # Safely extract the title and image URL
            try:
                title = article.find('img')['alt']  # Use 'alt' from the image tag
                image_url = article.find('img')['data-src']  # Use 'data-src' for the image URL
                story_link = article.find('a')['href']  # Get the link to the story

                # Fetch the content from the story link
                story_response = requests.get(story_link)
                story_soup = BeautifulSoup(story_response.content, 'html.parser')
                description = story_soup.find('div', class_='entry-content').decode_contents()

                # Save to the database
                ProphetStory.objects.update_or_create(
                    title=title,
                    defaults={'description': description, 'image_url': image_url}
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully scraped and saved: {title}'))

            except KeyError as e:
                self.stdout.write(self.style.ERROR(f'KeyError: {e} for article: {article}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error: {e} for article: {article}'))