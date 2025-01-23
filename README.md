[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MIand_y9)
# Homework 2 - LangChain & Document Parsing

## Preface

* In the previous assignment, you have learned to use prompts to communicate with LLM.
* Next, we will look at how to collect and process external data.
* In RAG (Retrieval-Augmented Generation) applications, how to split external data into appropriately sized chunks is an important step.
* In this assignment, you will understand the differences produced by using different text splitting strategies.

## Assignment Requirements

* Please use **LangChain** and **PyPDF** packages to complete this assignment.
* Please implement the two methods in **`student_assignment.py`**
    * `hw02_1(q1_pdf)`
    * `hw02_2(q2_pdf)`

---

### Question 1: Familiarize yourself with obtaining content from external document sources and parsing it using text splitting tools.

* **Description**: Split the content of the sample document into appropriately sized chunks.
* **Text**: You have a sample PDF document **`OpenSourceLicenses.pdf`**, which is an introduction to open source licenses.
* **Task**:
  1. Please implement the method `hw02_1(q1_pdf)` to complete this task.
  2. Use the **PyPDFLoader** package's load() method to read the text content of **`OpenSourceLicenses.pdf`**.
  3. Use **CharacterTextSplitter** to split the text by `page` into multiple chunks.
* **Hints**:
  1. You can use **split_text** or **split_documents** to get the split chunks.
  2. Pay attention to the parameters of **CharacterTextSplitter**:
      - chunk_overlap=0
      - chunk_size, separator can use default values or be adjusted
* **Expected Output**:
  - Please return the last chunk object, which is expected to contain the file name, page number, and text content.

---

### Question 2: Explore the differences in data slices produced by different text splitting strategies

* **Description**: In Question 1, the text was suitable for splitting by page. What if the text content spans multiple pages? How should it be split?
* **Text**: Please use another sample PDF document **`勞動基準法.pdf`**, which contains relevant laws of the Labor Standards Act.
* **Task**:
  1. Use the **PyPDFLoader** package's load() method to read the text content of **`勞動基準法.pdf`**.
  2. Use **RecursiveCharacterTextSplitter** to split the text into multiple chunks.
  3. Try to split `each chapter, each article` into individual chunks.
* **Hints**:
  1. Please implement the method `hw02_2(q2_pdf)` to complete this task.
  2. You can use **split_text** or **split_documents** to get the split chunks.
  3. Pay attention to the parameters of **RecursiveCharacterTextSplitter**:
      - chunk_overlap=0
      - chunk_size, separator can be adjusted
* **Expected Output**:
  - Please return the `number of chunks` obtained, which is expected to be an integer.
* **Splitting Example**:
  - For the first page, it is expected to be split like this:
  - ![Alt text](./chunks_example.png "Optional title")

---

## References
- [Question 1](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.CharacterTextSplitter.html)
- [Question 2](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html)