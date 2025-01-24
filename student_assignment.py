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

    # Join all text from all pages
    full_text = "".join([doc.page_content for doc in documents])

    # Use regex pattern for separators
    import re

    separators = [
        r"第\s*[一二三四五六七八九十百零]+\s*章\s*\n?",
        r"第\s*\d+\s*條\s*\n?",
        r"第\s*\d+-\d+\s*條\s*\n?",
    ]

    # Initialize RecursiveCharacterTextSplitter with adjusted parameters
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_overlap=0, chunk_size=10, separators=separators, is_separator_regex=True
    )

    # Split the full text
    split_chunks = recursive_splitter.split_text(full_text)

    # Debugging
    # print(separators)
    # for i, chunk in enumerate(split_chunks):
    #     print(f"=> Chunk # {i + 1}\n=> Length: {len(chunk)}\n\n {chunk}\n")

    return len(split_chunks)


# Testing
# print(hw02_1(q1_pdf))
# print(hw02_2(q2_pdf))
