import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import Surah, SurahTranslation  # Adjust the import based on your app structure

class Command(BaseCommand):
    help = 'Scrape Surah content for all languages and save to the database'

    def handle(self, *args, **kwargs):
        # Fetch all Surahs from the database
        surahs = Surah.objects.all()
        languages = ['hindi', 'urdu', 'english']  # Add more languages as needed

        for surah in surahs:
            for language in languages:
                self.scrape_and_save(surah, language)

    def scrape_and_save(self, surah, language):
        # Construct the URL based on Surah name and language
        url = f"https://www.islamestic.com/al-quran-with-translation/?sourate={surah.title.lower().replace(' ', '-')}-{surah.number}&lang={language}"
        self.stdout.write(self.style.SUCCESS(f'URL: {url}'))

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            self.save_surah_content(soup, surah, language)
        else:
            self.stdout.write(self.style.ERROR(f'Failed to retrieve data from {url}'))

    def save_surah_content(self, soup, surah, language):
        # Find the content section in the soup object
        content_divs = soup.find_all('div', class_='aya')  # Adjust this class name based on your HTML structure
        content = []

        for aya in content_divs:
            # Extract the aya number and content
            aya_num = aya.find('span', class_='quranbadge')
            aya_text = aya.get_text(strip=True)  # Get the text of the aya

            if aya_num and aya_text:  # Check if both aya_num and aya_text are found
                aya_num = aya_num.text.strip()
                content.append(f"Aya {aya_num}: {aya_text}")

        # Join all content into a single string
        full_content = "\n".join(content)
        if full_content:
        # Save to the database
            SurahTranslation.objects.update_or_create(
                surah=surah,
                language=language,
                defaults={'content': full_content}  # Update the content field
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully updated content for Surah {surah.title} in {language}.'))
        else:
            self.stdout.write(self.style.ERROR(f'Content not found for Surah {surah.title} in {language}.'))