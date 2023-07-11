import pdfplumber


def convert_pdf_to_txt(pdf_path, txt_path):
    with pdfplumber.open(pdf_path) as pdf:
        with open(txt_path, "w", encoding="utf-8") as txt_file:
            for page in pdf.pages:
                text = page.extract_text()
                txt_file.write(text)
                txt_file.write("\n")  # Add a new line after each page

    print(f"PDF successfully converted to TXT. Output saved to {txt_path}")


def process_large_text(text, chunk_size, directory_path, cnt=0):
    # Split the large text into smaller chunks
    chunks = [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

    # Save each chunk as a separate file in the specified directory
    cntix=(cnt if cnt else len(chunks))
    for i, chunk in enumerate(chunks):
        if i > cntix:
            break
        file_path = f"{directory_path}/chunk_{i}.txt"
        with open(file_path, "w") as file:
            file.write(chunk)

import sys
if __name__ == "__main__":
    # Provide the paths to your input PDF file and output TXT file
    pdf_file_path = "MOS-AST.pdf"
    txt_file_path = "MOS-AST.pdf.txt"
    try:
        CHUNK_COUNT = 0 if not len(sys.argv) else int(sys.argv[1])
    except ValueError:
        raise ValueError("'int or nothing for arg1'")
    # Step 1
    try:
        with open(txt_file_path) as s:
            pass
    except:
        convert_pdf_to_txt(pdf_file_path, txt_file_path)

    # Step 2
    large_text = ""
    with open(txt_file_path) as f:
        large_text = f.read()
    chunk_size = 15000
    DIRECTORY_PATH = "chunx"
    process_large_text(large_text, chunk_size, DIRECTORY_PATH, cnt=CHUNK_COUNT)
