from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    # Load PDF using PyPDFLoader
    loader = PyPDFLoader(q1_pdf)
    documents = loader.load()

    # Initialize CharacterTextSplitter with chunk_overlap=0
    text_splitter = CharacterTextSplitter(chunk_overlap=0)

    # Split PDF by page
    split_documents = text_splitter.split_documents(documents)

    return split_documents[-1]


def hw02_2(q2_pdf):
    pass


# Testing
print(hw02_1(q1_pdf))
# print(hw02_2(q2_pdf))
