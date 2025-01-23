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
    ]
    separators = [f"第 {i} 章" for i in numbers_in_chinese]
    for i in range(1, 90):
        separators.append(f"第 {i} 條")
        if i in [10, 17, 22, 30, 32, 63, 79, 80, 84]:
            separators.append(f"第 {i}-1 條")
            if i == 84:
                separators.append(f"第 {i}-2 條")

    # Initialize RecursiveCharacterTextSplitter with adjusted parameters
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_overlap=0, chunk_size=5, separators=separators
    )

    # Split the full text
    split_chunks = recursive_splitter.split_text(full_text)

    return len(split_chunks)


# Testing
# print(hw02_1(q1_pdf))
# print(hw02_2(q2_pdf))
