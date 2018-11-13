from docx import Document;

def getTextFromDocx(filePath,printRes=False):
    file=Document(filePath);
    text="";
    for para in file.paragraphs:
        text=text+para.text;
    if(printRes):
        print(text);
    return text;