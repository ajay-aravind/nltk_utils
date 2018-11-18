import simplejson as json

config={
    "tokenizers":{"first":"one",
                        "second":"two"}
}

def getConfig(key):
    res=config;
    for i in key.split("."):
        res=res[i];
    return res;