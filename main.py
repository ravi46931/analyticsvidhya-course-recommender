from src.search.search import CourseSuggester
# from src.scrap.scrap import CourseScraper

suggester = CourseSuggester()
def get_recommend_courses(query):
    response = suggester.get_response(query)
    return response


# def scrapt_data():
