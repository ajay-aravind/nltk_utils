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
    categoriesCount = [0, 0, 0, 0, 0,0,0,0];
    for i in categorized_text:
        if i[1] == "NN" or i[1] == "NNS":
            categoriesCount[0] += 1;
        if i[1] == "NNP" or i[1] == "NNPS":
            categoriesCount[1] += 1;
        if i[1] == "JJ" or i[1] == "JJR" or i[1] == "JJS":
            categoriesCount[2] += 1;
        if i[1] == "RB" or i[1] == "RBS" or i[1] == "RBS":
            categoriesCount[3] += 1;
        if i[1].startswith("VB"):
            categoriesCount[4] += 1;
        if i[1] == "NN" or i[1] == "NNS" or i[1]=="NNP" or i[1]=="NNPS":
            categoriesCount[5] += 1;
        if i[1]=="DT":
            categoriesCount[6]+=1;
        if i[1] == "IN":
            categoriesCount[7] += 1;

    if(printRes):
        print(categoriesCount);
    return categoriesCount;

def plotPartsOfSpeechCount(text):
    labels=["Nouns","ProperNouns","adjectives","adverbs","verbs"];
    categoriesCount=getPartOfSpeech(simple_text=text);
    plotPieChart(categoriesCount,labels,"Grammar");

def plotPieChart(slicesData,labels,legend=""):
    plotter.pie(slicesData, labels=labels, startangle=90, autopct='%.1f%%');
    plotter.title(legend);
    plotter.show();
def intializeOrIncriment(hashMap,key):
    if key in hashMap:
        hashMap[key]+=1;
    else:
        hashMap[key]=1;

def getNMostFrequentNouns(simple_text,n):

    return getNMostElements(simple_text,n,"Nouns");

def getNMostFrequentVerbs(simple_text,n):

    return getNMostElements(simple_text,n,"Verbs");

def getNMostPrepositions(simple_text,n):

    return  getNMostElements(simple_text,n,"Prepos");

def getNMostElements(simple_text,n,category):
    categories_fq = getFrequenciesOfPOS(simple_text);
    categories_fq[category] = categories_fq[category][:n];
    return categories_fq[category];


def getFrequenciesOfPOS(simple_text,printRes=False):
    categories_fq = {"Nouns": {}, "Verbs": {}, "Prepos": {},"Delimeters":{}};

    for i in simple_text:
        if i[1] == "NN" or i[1] == "NNS" or i[1]=="NNP" or i[1]=="NNPS":
            intializeOrIncriment(categories_fq["Nouns"], i[0]);
        elif i[1] == "IN":
            intializeOrIncriment(categories_fq['Prepos'], i[0]);
        elif i[1].startswith("VB"):
            intializeOrIncriment(categories_fq["Verbs"], i[0]);
        elif i[1]=="DT":
            intializeOrIncriment(categories_fq["Delimeters"], i[0]);

    categories_fq["Nouns"] = list(categories_fq["Nouns"].items());
    categories_fq["Verbs"] = list(categories_fq["Verbs"].items());
    categories_fq["Prepos"] = list(categories_fq["Prepos"].items());
    categories_fq["Delimeters"] = list(categories_fq["Delimeters"].items());

    categories_fq["Nouns"] = sorted(categories_fq["Nouns"], key=lambda item: item[1], reverse=True);
    categories_fq["Verbs"] = sorted(categories_fq["Verbs"], key=lambda item: item[1], reverse=True);
    categories_fq["Prepos"] = sorted(categories_fq["Prepos"], key=lambda item: item[1], reverse=True);
    categories_fq["Delimeters"] = sorted(categories_fq["Delimeters"], key=lambda item: item[1], reverse=True);

    if(printRes):
        print(categories_fq);
    return categories_fq;