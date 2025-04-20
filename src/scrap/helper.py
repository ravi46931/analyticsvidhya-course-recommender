import re
import json
import requests
from bs4 import BeautifulSoup

def get_html_soup(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def is_free(course):
    price = course.find('span', class_='course-card__price').get_text(strip=True)
    return price == "Free"

def get_course_soup(course_item):
    course_link = 'https://courses.analyticsvidhya.com'
    href = course_link + course_item.find('a').get('href')
    soup = get_html_soup(href)
    return soup

def get_title(course_item):
    title = course_item.find('h3').get_text(strip=True)
    return title

def get_description(soup):
    # old version
    # main_div = soup.find('section', class_='rich-text')
    # main = main_div.find('div', class_='custom-theme')
    # description = main.find('p').get_text(strip=True)

    # new version
    try:
        desc_meta = soup.find('meta', attrs={'name': 'description'})
        description = desc_meta['content']
        description = re.sub(r'\\u[0-9a-fA-F]{4}', '', description)
        # description = description.encode('ascii', 'ignore').decode()
        return description
    except:
        return None

def get_curriculum(soup):
    course_curriculum = soup.find_all('span', class_='course-curriculum__chapter-lesson')
    curr = []
    for c in course_curriculum:
        c = c.get_text(strip=True)
        if not c.startswith("Quiz"):
            clean_text = re.sub(r'\\u[0-9a-fA-F]{4}', '', c)
            # clean_text = c.encode('ascii', 'ignore').decode()
            curr.append(clean_text)
    if curr == []:
        try:
            items = soup.select('ul.checklist__list li p')
            curr = [item.get_text(strip=True) for item in items]
        except:
            curr = []
    return curr
