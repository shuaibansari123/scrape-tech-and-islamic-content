# # scrape_all_prophet_stories.py
# import requests
# from bs4 import BeautifulSoup
# from django.core.management.base import BaseCommand
# from yourapp.models import ProphetStory  # Adjust the import based on your app name

# class Command(BaseCommand):
#     help = 'Scrape stories of all prophets from the specified webpage'

#     def handle(self, *args, **kwargs):
#         base_url = "https://www.islamestic.com"
#         main_url = f"{base_url}/the-stories-of-prophets/"
#         response = requests.get(main_url)
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Find the main content area
#         articles = soup.find_all('div', class_='ultp-block-item')

#         for article in articles:
#             # Extract title and story link
#             title = article.find('img')['alt']
#             story_link = article.find('a')['href']

#             # Fetch the content from the story link
#             story_response = requests.get(story_link)
#             story_soup = BeautifulSoup(story_response.content, 'html.parser')

#             # Extract the content
#             story_title = story_soup.find('h1', class_='entry-title').text.strip()
#             content = story_soup.find('div', class_='entry-content').decode_contents()

#             # Prepare the HTML for saving with advanced CSS/design
#             styled_content = f"""
#             <div style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
#                 <h1 style="text-align: center; color: #2c3e50;">{story_title}</h1>
#                 <div style="margin: 20px; padding: 20px; border: 1px solid #ccc; border-radius: 10px; background-color: #f9f9f9;">
#                     {content}
#                 </div>
#             </div>
#             """

#             # Save to the database
#             ProphetStory.objects.update_or_create(
#                 title=story_title,
#                 defaults={'description': styled_content}
#             )
#             self.stdout.write(self.style.SUCCESS(f'Successfully scraped and saved: {story_title}'))



# scrape_all_prophet_stories.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import ProphetStory  # Adjust the import based on your app name

class Command(BaseCommand):
    help = 'Scrape stories of all prophets from the specified webpage'

    def handle(self, *args, **kwargs):
        base_url = "https://www.islamestic.com"
        main_url = f"{base_url}/the-stories-of-prophets/"
        response = requests.get(main_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the main content area
        articles = soup.find_all('div', class_='ultp-block-item')

        for article in articles:
            # Extract title and story link
            title = article.find('img')['alt']
            story_link = article.find('a')['href']

            # Fetch the content from the story link
            story_response = requests.get(story_link)
            story_soup = BeautifulSoup(story_response.content, 'html.parser')

            # Extract the content
            story_title = story_soup.find('h1', class_='entry-title').text.strip()
            content = story_soup.find('div', class_='entry-content').decode_contents()

            # Prepare the HTML for saving with advanced CSS/design
            styled_content = f"""
            <div style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
                <h1 style="text-align: center; color: #2c3e50;">{story_title}</h1>
                <div style="font-size: 20px; margin: 20px; padding: 20px; border: 1px solid #ccc; border-radius: 10px; background-color: #f9f9f9;">
                    {content}
                </div>
            </div>
            """

            # Save to the database
            ProphetStory.objects.update_or_create(
                title=story_title ,
                defaults={'description': styled_content}
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully scraped and saved: {story_title}'))