import os

from dotenv import load_dotenv
from types.excel_utils import readExcel
from types.pdf_utils import readPDF

# load api key
load_dotenv()

# criar um arquivo .env e adicionar a chave do open ai
api_key = os.getenv("OPENAI_API_KEY")

# readPDF(api_key)

readExcel(api_key)

