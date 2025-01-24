# management/commands/fetch_names.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import NameOfAllah  # Replace 'yourapp' with your app name

class Command(BaseCommand):
    help = 'Fetch names of Allah from the specified webpage'

    def handle(self, *args, **kwargs):
        url = "https://www.islamestic.com/99-names-of-allah/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the relevant div containing the names
        names_div = soup.find('div', class_='ultp-block-items-wrap')
        names = names_div.find_all('div', class_='ultp-block-item')

        for name_div in names:
            name = name_div.find('a').img['alt']  # Get the name from the alt attribute
            description = f"This is the description for {name}."  # Placeholder description

            # Save to the database
            NameOfAllah.objects.update_or_create(name=name , defaults={})
            self.stdout.write(self.style.SUCCESS(f'Successfully fetched and saved names of Allah: {name}'))

        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved names of Allah.'))