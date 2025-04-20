import os
import sys
from dotenv import load_dotenv
from groq import Groq
from src.utils.utils import load_file
from src.exception import CustomException


def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()


def initialize_groq_client():
    """Initialize the Groq API client."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")
    return Groq(api_key=api_key)


def build_corpus(file_path: str) -> list:
    """Extract relevant fields from the course data."""
    try:
        data = load_file(file_path)
        return [
            {
                "title": course.get("title", ""),
                "description": course.get("description", "")
            }
            for course in data
        ]
    except Exception as e:
        raise CustomException(e, sys)
