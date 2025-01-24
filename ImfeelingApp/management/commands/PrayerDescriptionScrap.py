import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import Prayer  

class Command(BaseCommand):
    help = 'Scrape detailed descriptions for all types of prayers from the specified webpages'

    def handle(self, *args, **kwargs):



        prayer_urls = {
            "fajr": "https://www.islamestic.com/how-to-pray-fajr-prayer/",
            "dhuhr": "https://www.islamestic.com/how-to-pray-dhuhr-prayer/",
            "asr": "https://www.islamestic.com/how-to-pray-asr-prayer/",
            "maghrib": "https://www.islamestic.com/how-to-pray-maghrib-prayer/",
            "isha": "https://www.islamestic.com/how-to-pray-isha-prayer/",
            "witr": "https://www.islamestic.com/how-to-pray-witr-salahnamaz-according-to-authentic-hadiths/",
            "tahajjud": "https://www.islamestic.com/how-to-pray-tahajjud-prayer-importance-benefits-timing/",
            "jummah": "https://www.islamestic.com/how-to-pray-jummah-prayer/",
            "istikhara": "https://www.islamestic.com/how-to-pray-salat-al-istikhara-benefits-importance-timing/",
            "janazah": "https://www.islamestic.com/how-to-pray-salat-al-janazah-steps-to-pray-purposevirtues/",
            "eid": "https://www.islamestic.com/how-to-pray-eid-prayer-namaz-step-by-step/",
            "duha": "https://www.islamestic.com/how-to-pray-salat-al-duha-importance-benefits-timing/",
            "taraweeh": "https://www.islamestic.com/how-to-pray-taraweeh-at-home-step-by-step/"
        }

        for prayer in prayer_urls.keys():
            url = prayer_urls[prayer]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the content from the specified HTML structure
            # Use a more general selector to find the content
            content_div = soup.find('div', class_='entry-content')
            if not content_div:
                # If not found, try to find the first <article> element
                content_div = soup.find('article')

            if content_div:
                description = str(content_div)

                # Add custom styling for CKEditor
                styled_description = f"""
                <div style="font-family: Arial, sans-serif; font-size: 20px; color: #333; background-color: #f9f9f9; padding: 20px; border-radius: 8px;">
                    <h2 style="color: #007bff;">{prayer.capitalize()} Prayer</h2>
                    {description}
                </div>
                """

                # Update the Prayer object with the styled description
                self.stdout.write(self.style.SUCCESS(f'Description: {styled_description}'))
                pr = Prayer.objects.filter(name__icontains=prayer).first()
                pr.description=styled_description
                pr.save()
    
                self.stdout.write(self.style.SUCCESS(f'Successfully save PrayerDescription: {prayer.capitalize()}'))


        self.stdout.write(self.style.SUCCESS('Successfully scraped and saved prayer descriptions with styling.'))