import nltk;
import string;
#  removes all punctuation symbols and returns the string
def removePunctuations(inputString,printResult=False):
    for punctuation in string.punctuation:
        inputString=inputString.replace(punctuation," ");
    if(printResult):
        print(inputString);
    return inputString;

def removeStopWords(simple_text,printRes=False):
    tokenizer=nltk.WordPunctTokenizer();
    tokens=tokenizer.tokenize(simple_text);
    stopwords=nltk.corpus.stopwords.words('english');

    outputString="";
    for word in tokens:
        if not (stopwords.__contains__(word) or stopwords.__contains__(word.lower())):
            outputString=outputString+" "+word;

    if(printRes):
        print(outputString);
    return outputString;

def cleanText(text,printRes=False):
    text = removePunctuations(text);
    text = removeStopWords(text);
    text = text.split();
    if(printRes):
        print(text);
    return text;


def getStemmetizedText(text_tokens,clean_input=False,printRes=False):
    # if this flag is set , it is assumed that passed input text is raw paragraph
    if(clean_input):
        text_tokens=cleanText(text_tokens);

    stemmer = nltk.SnowballStemmer(language="english");
    res=[stemmer.stem(word) for word in text_tokens];
    if(printRes):
        print(res);
    return res;

def getLemmetizedText(text_tokens,clean_input=False):
    # if this flag is set , it is assumed that passed input text is raw paragraph

    if(clean_input):
        text_tokens=cleanText(text_tokens);

    lemmetizer=nltk.WordNetLemmatizer();
    return [lemmetizer.lemmatize(word) for  word in text_tokens]

def getNGrams(text,N):
    list=[];
    lengthOfList=len(text);
    index=0;
    for word in text:
        nGram=[];
        start=index;
        for i in range(0,N):
            if start+i<lengthOfList:
                nGram.append(text[start+i]);
        nGram = tuple(nGram);
        list.append(nGram);
        index+=1;
    print(list);

def getPosTags(text):
            text = nltk.sent_tokenize(text);
            treeBankWordTknzr=nltk.TreebankWordTokenizer();
            tokens=[ nltk.pos_tag(treeBankWordTknzr.tokenize(sentance)) for sentance in text];
            allTokens=[];
            for i in tokens:
                for j in i:
                    allTokens.append(j);
            return allTokens;