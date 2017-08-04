 # -*- coding: utf-8 -*-
def algor(deep_cut,outputs,corpus,nameCorpus):

    iCorpus = 0
    lenDeep = len(deep_cut)
    oldKey = []
    newDeep = []

    loopNewdeepLow(deep_cut,lenDeep,newDeep)
    outputs = loopCorpus(corpus,newDeep,deep_cut,lenDeep,nameCorpus,iCorpus,outputs,oldKey)
    
    return outputs 

def loopNewdeepLow(deep_cut,lenDeep,newDeep):
    for i in range(lenDeep):
        lowDeep = deep_cut[i].lower()
        newDeep.append(lowDeep)
def loopCorpus(corpus,newDeep,deep_cut,lenDeep,nameCorpus,iCorpus,outputs,oldKey):
    for c in corpus:
        outputs = loopKey(newDeep,deep_cut,lenDeep,nameCorpus,iCorpus,outputs,oldKey,c)
        iCorpus = iCorpus + 1
    return outputs
def loopKey(newDeep,deep_cut,lenDeep,nameCorpus,iCorpus,outputs,oldKey,c):
    for key, value in c.items():
        if key in oldKey:
            continue
        oldKey.append(key)
        outputs = loopValue(newDeep,value,deep_cut,lenDeep,key,nameCorpus,iCorpus,outputs)
    return outputs
def loopValue(newDeep,value,deep_cut,lenDeep,key,nameCorpus,iCorpus,outputs):
    for v in value:
        vj = []
        comma = 0
        checkJ = 0
        iRe = 0

        if "," in v:
            comma = 1
        spl = v.split(",")

        vj,checkJ,iRe = loopPushVJ(newDeep,iRe,v,deep_cut,vj,checkJ,lenDeep,spl,comma)
        outputs = checkJforPush(key,nameCorpus,iCorpus,vj,outputs,comma,checkJ,spl,v,deep_cut,newDeep,iRe)
    return outputs
def loopPushVJ(newDeep,iRe,v,deep_cut,vj,checkJ,lenDeep,spl,comma):
    for i in range(lenDeep):
        if newDeep[i] in spl and newDeep[i] != "":
            vj.append(deep_cut[i])
            checkJ = checkJ + 1
            iRe = i
            continue
        elif v in newDeep[i] and newDeep[i] != "" :
            vj,checkJ,iRe = caseVinNewdeep(newDeep,i,iRe,v,deep_cut,vj,checkJ)
            continue
        elif comma == 1:
            vj,checkJ,iRe = caseCommaIs1(spl,vj,checkJ,i,deep_cut,newDeep,iRe)
    return vj,checkJ,iRe
def pushOutput(key,nameCorpus,iCorpus,vj,outputs):
    k1 = key
    k2 = nameCorpus[iCorpus]
    ks = k1 + k2
    outputs[ks] = vj
    return outputs
def checkJforPush(key,nameCorpus,iCorpus,vj,outputs,comma,checkJ,spl,v,deep_cut,newDeep,iRe):
    if comma == 1 and checkJ == len(spl):
        vj = ",".join(vj)
        vjLow = vj.lower()
        if (vjLow == v):
            outputs = pushOutput(key,nameCorpus,iCorpus,vj,outputs)

    elif len(vj) != 0 and len(vj[0]) == len(v):
        vj = " ".join(vj)
        vjLow = vj.lower()
        if (vjLow == v):
            outputs = pushOutput(key,nameCorpus,iCorpus,vj,outputs)
            deep_cut[iRe] = newDeep[iRe].replace(v, "")
            newDeep[iRe] = newDeep[iRe].replace(v, "")
        elif checkJ>0:
            outputs = pushOutput(key,nameCorpus,iCorpus,vj,outputs)
    return outputs
def caseVinNewdeep(newDeep,i,iRe,v,deep_cut,vj,checkJ):
    if " " in newDeep[i]:
        splNew = newDeep[i].split(" ")
        iRe = i
        if splNew[0] in v and splNew[0] != "": 
            splDeep = deep_cut[i].split(" ")
            vj.append(splDeep[0])
        if splNew[1] in v and splNew[1] != "":
            splDeep = deep_cut[i].split(" ")
            vj.append(splDeep[1])
    else:
        vj.append(v)
        checkJ = checkJ+1
        iRe = i
    return vj,checkJ,iRe
def caseCommaIs1(spl,vj,checkJ,i,deep_cut,newDeep,iRe):
    for j in range(len(spl)):
        if spl[j] in newDeep[i]:
            rem = newDeep[i].replace(spl[j],"")
            org = deep_cut[i].replace(rem,"")
            vj.append(org)
            checkJ = checkJ+1
            iRe = i
    return vj,checkJ,iRe
