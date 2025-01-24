import os
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ImfeelingApp.models import Seerah  
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Scrape Seerah'

    def handle(self, *args, **kwargs):
        # Function to scrape detailed content for a subsection
        def scrape_detailed_content(subsection_title):
            # Normalize the subsection title to ensure correct URL formatting
            normalized_title = subsection_title.strip().replace(" ", "-").lower()  # Adjust as needed
            slug = slugify(normalized_title)  # Convert the title to a slug
            subsection_url = f"https://www.islamestic.com/seerah/{slug}/"  # Adjust this based on actual URL structure
            self.stdout.write(self.style.SUCCESS(f"Subsection URL: {subsection_url}"))

            try:
                response = requests.get(subsection_url)
                response.raise_for_status()  # Raise an error for bad responses
            except requests.exceptions.ChunkedEncodingError:
                self.stdout.write(self.style.ERROR(f"ChunkedEncodingError for URL: {subsection_url}"))
                return ""  # Return empty content on error
            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f"Request failed for URL: {subsection_url} with error: {e}"))
                return ""  # Return empty content on error

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                content_div = soup.find('div', class_='entry-content')  # Use the correct class name
                if content_div:
                    # Wrap the content in HTML with CSS styles for CKEditor
                    formatted_content = f"""
                    <div style="padding: 20px; border-radius: 8px; font-family: 'Noto Nastaliq Urdu', serif; font-size: 20px; color: #333;">
                        {content_div}
                    </div>
                    """
                    return formatted_content  # Return the formatted HTML content
            return ""

        # Update content for each Seerah entry
        seerah_entries = Seerah.objects.all()
        for seerah in seerah_entries:
            try:
                detailed_content = scrape_detailed_content(seerah.subsection)
                if detailed_content:
                    seerah.content = detailed_content  # Update the content field
                    seerah.save()  # Save the updated object
                    self.stdout.write(self.style.SUCCESS(f"Updated content for: {seerah.subsection}"))
                else:
                    self.stdout.write(self.style.WARNING(f"No content found for: {seerah.subsection}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error processing subsection {seerah.subsection}: {e}"))