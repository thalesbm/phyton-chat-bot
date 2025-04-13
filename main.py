import os

from dotenv import load_dotenv
from pdf_utils import readPDF
from excel_utils import readExcel

# load api key
load_dotenv()

# criar um arquivo .env e adicionar a chave do open ai
api_key = os.getenv("OPENAI_API_KEY")

# readPDF(api_key)

readExcel(api_key)

