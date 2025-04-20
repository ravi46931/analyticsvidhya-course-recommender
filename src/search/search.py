import sys
from src.constants import MODEL_NAME, TEMPERATURE, MAX_TOKENS, DELIMITER, N_COURSES
from src.search.helper import load_environment, initialize_groq_client, build_corpus
from src.exception import CustomException


class CourseSuggester:
    def __init__(self, corpus_file: str = "courses_info.json"):
        load_environment()
        self.client = initialize_groq_client()
        self.corpus = build_corpus(corpus_file)
        self.system_message = self._construct_system_message()

    def _construct_system_message(self) -> str:
        """Construct the system message for the LLM."""
        return (
            f"You are a course assistant. Your role is to suggest courses "
            f"based on the query delimited by {DELIMITER}.\n"
            f"Select the data from the following list of courses, which contain title and description:\n{self.corpus}\n\n"
            f"Please suggest at most the top {N_COURSES} relevant courses. Only give the course titles."
        )

    def _get_completion(self, messages: list) -> str:
        """Send message payload to Groq and get the LLM response."""
        try:
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=MODEL_NAME,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            raise CustomException(e, sys)

    def get_response(self, query: str) -> str:
        """Public method to get suggested course titles for a given query."""
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": f"{DELIMITER}{query}{DELIMITER}"},
        ]
        return self._get_completion(messages)


if __name__ == "__main__":
    suggester = CourseSuggester()
    query = "Suggest me the courses for writing data science articles"
    response = suggester.get_response(query)
    print("Suggested Courses:\n", response)
