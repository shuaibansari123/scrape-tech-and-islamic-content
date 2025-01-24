import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import ImFeeling

class Command(BaseCommand):
    help = 'Scrape feelings descriptions and save to the database'

    # List of feelings
    feelings = [
        "uneasy", "angry", "anxious", "bored", "confident", "confused",
        "content", "depressed", "doubtful", "grateful", "greedy", "guilty",
        "happy", "hurt", "hypocritical", "indecisive", "jealous", "lazy",
        "lonely", "lost", "nervous", "overwhelmed", "regret", "sad",
        "scared", "suicidal", "tired", "unloved", "weak", "anticipation",
        "aroused", "curious", "defeated", "desire", "desperate", "determined",
        "disbelief", "envious", "hatred", "humiliated", "impatient", "insecure",
        "irritated", "love", "nostalgic", "offended", "peaceful", "rage",
        "satisfied", "uncertain"
    ]

    def handle(self, *args, **kwargs):
        for feeling in self.feelings:
            url = f"https://www.islamestic.com/i-am-feeling-{feeling}/"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Scrape the description
            description_div = soup.find('div', class_='entry-content', itemprop='text')
            if description_div:
                # Get the full HTML content
                full_description = str(description_div)

                # Add custom styles for Arabic text
                styled_description = f"""
                <div style="font-family: 'Arial', sans-serif; color: #333; font-size: 20px;">
                    <style>
                        .arabic-text {{
                            font-family: 'Amiri', serif; /* Use a suitable Arabic font */
                            font-size: 20px; /* Larger font size for Arabic text */
                            color: #000; /* Color for Arabic text */
                        }}
                    </style>
                    {full_description.replace('<h6>', '<h6 class="arabic-text">').replace('<h1>', '<h1 class="arabic-text">')}
                </div>
                """

                # Save to the database
                ImFeeling.objects.update_or_create(
                    feeling_name=feeling.capitalize(),
                    defaults={
                        'title': feeling.capitalize(),
                        'body': styled_description,  # Save the styled HTML content
                        'description': styled_description  # You can also save it here if needed
                    }
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully scraped and saved: {feeling.capitalize()}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to scrape: {feeling.capitalize()}'))