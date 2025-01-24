import requests
from bs4 import BeautifulSoup

def scrape_surah_content(surah_number, language_code):
    # Construct the URL based on Surah number and language
    url = f"https://www.example.com/quran?surah={surah_number}&lang={language_code}"  # Replace with the actual URL structure

    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}")

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the section with ID 'quran_main'
    quran_section = soup.find(id='quran_main')
    if not quran_section:
        raise Exception("Could not find the section with ID 'quran_main'")

    # Extract the text or HTML content
    content = quran_section.get_text(strip=True)  # or use quran_section.prettify() for HTML

    return content