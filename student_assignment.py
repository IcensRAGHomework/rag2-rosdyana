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
    # Load PDF using PyPDFLoader
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()

    # Join all text from all pages with form feed character
    full_text = "\f".join(doc.page_content for doc in documents)

    # Define the separators as regex patterns
    separators = [r"第.+(?:條 *|章 .*)(?:\n|\f)"]

    # Initialize RecursiveCharacterTextSplitter with adjusted parameters
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_overlap=0, chunk_size=10, separators=separators, is_separator_regex=True
    )

    # Split the full text
    split_chunks = recursive_splitter.split_text(full_text)

    return len(split_chunks)


# Testing
# print(hw02_1(q1_pdf))
# print(hw02_2(q2_pdf))
