import simplejson as json

config={
    "tokenizers":{"first":"one",
                        "second":"two"}
}
print(config);
def getConfig(key):
    res=config;
    for i in key.split("."):
        res=res[i];
    return res;