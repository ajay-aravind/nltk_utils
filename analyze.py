import matplotlib.pyplot as plotter;
import nltk
def getArticlesCounts(listOfWords,printAsWell=False):
    dict={};
    for i in listOfWords:
        i=i.lower();
        if i=="a" or i=="an" or i=="the":
            if i in dict:
                dict[i]+=1;
            else:
                dict[i]=0;
    if(printAsWell):
        print(dict);
    return dict;

def getIsAplha(char):
    return ord(char) >= 65 and ord(char) <= 90 or ord(char) >= 97 and ord(char) <= 122;


def getAlphaFq(listOfStrings,printRes=False):
    dict={};
    for word in listOfStrings:
        for char in word:
           if getIsAplha(char):
                char=char.lower();
                if char in dict:
                    dict[char]+=1;
                else:
                    dict[char]=0;
    if(printRes):
        print(dict);
    return dict;

def plotDictionary(inputData,xlabel="",ylabel="",title=""):
    plotter.plot(inputData.keys(), inputData.values());
    plotter.xlabel(xlabel);
    plotter.ylabel(ylabel);
    plotter.title(title);
    plotter.show();

def plotStopWordsFq(simple_text,printRes):
    tokenizer = nltk.WordPunctTokenizer();
    tokens = tokenizer.tokenize(simple_text);
    stopwords = nltk.corpus.stopwords.words('english');

    stop_words={};
    for word in tokens:
        word = word.lower();
        if  stopwords.__contains__(word):
            if word in stop_words:
                stop_words[word]+=1;
            else:
                stop_words[word] =1;
    if(printRes):
        print(stop_words);
    return stop_words;

def getPartOfSpeech(simple_text,printRes=False):
    categorized_text = nltk.pos_tag(simple_text);
    # NN, NNS |NNP, NNPS|JJ,JJR,JJS|RB,RBR,RBS|VB
    categoriesCount = [0, 0, 0, 0, 0];
    for i in categorized_text:
        if i[1] == "NN" or i[1] == "NNS":
            categoriesCount[0] += 1;
        elif i[1] == "NNP" or i[1] == "NNPS":
            categoriesCount[1] += 1;
        elif i[1] == "JJ" or i[1] == "JJR" or i[1] == "JJS":
            categoriesCount[2] += 1;
        elif i[1] == "RB" or i[1] == "RBS" or i[1] == "RBS":
            categoriesCount[3] += 1;
        elif i[1].startswith("VB"):
            categoriesCount[4] += 1;

    if(printRes):
        print(categoriesCount);
    return categoriesCount;

def plotPartsOfSpeechCount(text):
    labels=["Nouns","ProperNouns","adjectives","adverbs","verbs"];
    categoriesCount=getPartOfSpeech(simple_text=text);
    plotPieChart(categoriesCount,labels,"Grammar");

def plotPieChart(slicesData,labels,legend=""):
    plotter.pie(slicesData, labels=labels, startangle=90, autopct='%.1f%%');
    plotter.legend(legend);
    plotter.show();