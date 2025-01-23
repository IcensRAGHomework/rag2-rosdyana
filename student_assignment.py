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

    # Initialize CharacterTextSplitter with chunk_overlap=0
    text_splitter = CharacterTextSplitter(chunk_overlap=0)

    # Split PDF by page
    split_documents = text_splitter.split_documents(documents)

    # Generate separators list
    numbers_in_chinese = [
        "一",
        "二",
        "三",
        "四",
        "五",
        "六",
        "七",
        "八",
        "九",
        "十",
        "十一",
        "十二",
        "十三",
        "十四",
        "十五",
        "十六",
        "十七",
        "十八",
        "十九",
    ]
    separators = [f"第 {i} 章" for i in numbers_in_chinese]
    separators.extend([f"第 {i} 條" for i in range(1, 90)])

    # Initialize RecursiveCharacterTextSplitter with adjusted parameters
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_overlap=0, chunk_size=5, separators=separators
    )

    # Iterate over all pages and count the number of chunks
    total_split_chunks = 0
    for doc in split_documents:
        text = doc.page_content
        split_chunks = recursive_splitter.split_text(text)
        total_split_chunks += len(split_chunks)

    return total_split_chunks


# Testing
# print(hw02_1(q1_pdf))
print(hw02_2(q2_pdf))
