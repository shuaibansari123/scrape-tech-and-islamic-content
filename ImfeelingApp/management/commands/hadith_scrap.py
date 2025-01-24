import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from django.core.management.base import BaseCommand
from ImfeelingApp.models import Hadith  # Import the new model

class Command(BaseCommand):
    help = 'Scrape hadiths from the collection'

    def handle(self, *args, **kwargs):
        # Set up the Selenium WebDriver (make sure to specify the correct path to your driver)
        driver = webdriver.Chrome()  # or webdriver.Firefox() if using Firefox
        driver.get("https://www.islamestic.com/hadiths-collection/")

        # Find the dropdown for hadith selection
        dropdown = Select(driver.find_element(By.CLASS_NAME, "chaptershadith"))

        # Iterate through each option in the dropdown
        for option in dropdown.options:
            hadith_title = option.text.strip()
            option.click()  # Select the hadith

            time.sleep(4)  # Wait for the content to load

            # Extract the content from the hadith
            content_div = driver.find_element(By.CLASS_NAME, "hadith_content")
            content = content_div.get_attribute('outerHTML')  # Get the HTML content
            styled_content = f"""
                    <div style="padding: 20px; border-radius: 8px; font-family: 'Noto Nastaliq Urdu', serif; font-size: 20px; color: #333;">
                        {content}
                    </div>
                    """
            # Create or update the Hadith entry
            hadith, created = Hadith.objects.update_or_create(
                title=hadith_title,
                defaults={'content': styled_content}  # Save the HTML content
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created new entry: {hadith_title}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Updated entry: {hadith_title}"))
            

        driver.quit()  # Close the browser