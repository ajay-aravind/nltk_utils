from docx import Document;

def getTextFromDocx(filePath,printRes=False):
    file=Document(filePath);
    text="";
    for para in file.paragraphs:
        text=text+para.text;
    logResult(printRes,text);
    return text;

def getTextFromFile(filePath,printRes=False):
    file=open(filePath);
    text=[];
    for line in file:
        text.append(line);

    result="".join(text);
    logResult(printRes,result);
    return result

def getLinesCount(filePath,printRes=False):
    file=open(filePath);
    count=0;
    for line in file:
        if(line.strip()!=""):
            count+=1;
    logResult(printRes,count);
    return count;

def logResult(printRes,res):
    if(printRes):
        print(res);

def writeListToCSV(fileHandler,data,delim='\\'):
    for i in data:
        fileHandler.write(str(i)+",");
    fileHandler.write(str(i)+"\n");