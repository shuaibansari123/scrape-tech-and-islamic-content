import requests
from bs4 import BeautifulSoup
from .models import DuaDhikr

def scrape_morning_dhikr():
    url = "https://www.islamestic.com/morning-adhkar/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the content you want to scrape
    content_div = soup.find('div', class_='entry-content')
    headings = content_div.find_all(['h2', 'h6'])
    
    for heading in headings:
        title = heading.get_text(strip=True)
        description = heading.find_next_sibling('pre').get_text(strip=True) if heading.find_next_sibling('pre') else ""
        
        DuaDhikr.objects.create(title=title, description=description)