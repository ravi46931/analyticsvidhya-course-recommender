import json
from bs4 import BeautifulSoup

from src.utils.utils import save_file, remove_file
from src.exception import CustomException
from src.constants import URL, PAGES
from src.scrap.helper import (
    is_free,
    get_html_soup,
    get_course_soup,
    get_title,
    get_description,
    get_curriculum,
)


class CourseScraper:
    """
    Scraper class to extract course titles, descriptions, and curriculum
    from the Analytics Vidhya website.
    """

    def __init__(self, base_url: str = URL, pages: int = PAGES, filename="courses_info_temp.jsonl"):
        self.base_url = base_url
        self.pages = pages
        self.filename = filename 
        self.data = []

    def scrape(self):
        """Main scraping loop over all pages."""
        try:
            for page in range(1, self.pages + 1):
                print(f"Page: {page} started")
                page_url = self.base_url.format(page=page)
                self._scrape_page(page_url)
                print(f"End: {page}")
                print("--" * 30)
        except Exception as e:
            print(f"An error occurred during scraping: {e}")
        finally:
            self.finalize_json_file(output_file='courses_info.json')
            remove_file(self.filename)
            
    def _scrape_page(self, url: str):
        """Scrape a single page of courses."""
        soup = get_html_soup(url)
        try:
            main_div = soup.find("div", class_="collections__container")
            product_cards = main_div.find("div", class_="collections__product-cards")
            course_list = product_cards.find("ul", class_="products__list")
            courses = course_list.find_all("li", class_="products__list-item")
        except AttributeError:
            print("Error parsing course list for URL:", url)
            return

        for course in courses:
            if not is_free(course):
                continue
            course_data = self._extract_course_data(course)
            # self.data.append(course_data)
            print("Extracted:", course_data["title"])
            self.save_single_record(course_data)

    def _extract_course_data(self, course) -> dict:
        """Extract data for a single course."""
        title = get_title(course)
        course_soup = get_course_soup(course)
        description = get_description(course_soup)
        curriculum = get_curriculum(course_soup)
        return {
            "title": title,
            "description": description if description is not None else title,
            "curriculum": curriculum
        }

    def save_single_record(self, record):
        try:
            with open(self.filename, 'a', encoding='utf-8') as f:
                json.dump(record, f, ensure_ascii=False)
                f.write('\n')  # newline-delimited JSON
        except Exception as e:
            raise CustomException(e, sys)

    def save_to_file(self):
        """Save scraped data to a JSON file."""
        try:
            save_file(self.data, self.filename)
            print()
        except Exception as e:
            raise CustomException(e, sys)

    def finalize_json_file(self, output_file='courses_iolp.json'):
        try:
            with open(self.filename, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
                data = [json.loads(line.strip()) for line in lines]

            with open(output_file, 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)

            print(f"Final JSON written to: {output_file}")
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    scraper = CourseScraper()
    scraper.scrape()
    # scraper.finalize_json_file()
    # scraper.save_to_file()
