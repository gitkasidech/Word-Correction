# coding=utf8
def main():
    deep_cut = ["paypal", "โอน", "เงิน", "เข้า", "ธนาคาร", "แล้ว", "ต้อง", "รอ", "ทาง", "ธนาคารโอน", "เงิน", "เข้า", "บัญชี", "กี่", "วัน", "คะ"]
    syntax = {}
    eng2tha = {}
    bay = {}
    bank = {"ธนาคาร":["ธนาคาร"],"โอน":["โอน"]}
    general = {}

    outputs = {}
    corpus = [syntax,eng2tha,bay,bank,general]
    nameCorpus = ["|syntax","|eng2tha","|bay","|bank","|general"]

    outputs = algor(deep_cut,outputs,corpus,nameCorpus)
    print(outputs)

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
        vOut = []
        comma = 0
        checkJ = 0
        iRe = 0

        if "," in v:
            comma = 1

        spl = v.split(",")

        vOut,checkJ,iRe = loopPushVout(newDeep,iRe,v,deep_cut,vOut,checkJ,lenDeep,spl,comma)
        outputs = checkJforPush(key,nameCorpus,iCorpus,vOut,outputs,comma,checkJ,spl,v,deep_cut,newDeep,iRe)
    return outputs
def loopPushVout(newDeep,iRe,v,deep_cut,vOut,checkJ,lenDeep,spl,comma):
    for i in range(lenDeep):
        if newDeep[i] in spl and newDeep[i] != "":
            vOut.append(deep_cut[i])
            checkJ = checkJ + 1
            iRe = i
            continue
        elif v in newDeep[i] and newDeep[i] != "" :
            vOut,checkJ,iRe = caseVinNewdeep(newDeep,i,iRe,v,deep_cut,vOut,checkJ)
            continue
        elif comma == 1:
            vOut,checkJ,iRe = caseCommaIs1(spl,vOut,checkJ,i,deep_cut,newDeep,iRe)
    return vOut,checkJ,iRe
def pushOutput(key,nameCorpus,iCorpus,vOut,outputs):
    k1 = key
    k2 = nameCorpus[iCorpus]
    ks = k1 + k2
    outputs[ks] = vOut
    return outputs
def checkJforPush(key,nameCorpus,iCorpus,vOut,outputs,comma,checkJ,spl,v,deep_cut,newDeep,iRe):
    if comma == 1 and checkJ == len(spl):
        vOut = ",".join(vOut)
        vjLow = vOut.lower()
        if (vjLow == v):
            outputs = pushOutput(key,nameCorpus,iCorpus,vOut,outputs)

    elif len(vOut) != 0 and len(vOut[0]) == len(v):
        vOut = " ".join(vOut)
        vjLow = vOut.lower()
        if (vjLow == v):
            outputs = pushOutput(key,nameCorpus,iCorpus,vOut,outputs)
            deep_cut[iRe] = newDeep[iRe].replace(v, "")
            newDeep[iRe] = newDeep[iRe].replace(v, "")
        elif checkJ>0 and " " in vOut:
            vOut = vOut.split(" ")
            vOut = vOut[0]
            outputs = pushOutput(key,nameCorpus,iCorpus,vOut,outputs)
    return outputs
def caseVinNewdeep(newDeep,i,iRe,v,deep_cut,vOut,checkJ):
    if " " in newDeep[i]:
        splNew = newDeep[i].split(" ")
        iRe = i
        if splNew[0] in v and splNew[0] != "": 
            splDeep = deep_cut[i].split(" ")
            vOut.append(splDeep[0])
        if splNew[1] in v and splNew[1] != "":
            splDeep = deep_cut[i].split(" ")
            vOut.append(splDeep[1])
    else:
        vOut.append(v)
        checkJ = checkJ+1
        iRe = i
    return vOut,checkJ,iRe
def caseCommaIs1(spl,vOut,checkJ,i,deep_cut,newDeep,iRe):
    for j in range(len(spl)):
        if spl[j] in newDeep[i]:
            rem = newDeep[i].replace(spl[j],"")
            org = deep_cut[i].replace(rem,"")
            vOut.append(org)
            checkJ = checkJ+1
            iRe = i
    return vOut,checkJ,iRe

main()

# deep_cut = ["ข้อความ", "แจ้ง", "ยอด", "เงิน", "เข้ายอด", "เงิน", "ออก", "ไม่", "เข้า", "มือถือ", "เลย", "ค่ะ"]
# general = {"ยอด":["ยอด"],"เงิน":["เงิน"]}
# ["ยอด","ยอด"] --> ["ยอด ยอด"] --> ["ยอด"]

# deep_cut = ["Otp โดน", "ล๊อค"]
# eng2tha = {"โอทีพี":["otp"]}

# deep_cut = ["กด", "เงิน", "สด", "จาก", "บัตร", "A", "TM"]
# eng2tha = {"เอทีเอ็ม":["a,tm"]}

# deep_cut = ["ดอก", "เบี๋ย", "เท่า", "ไร", "คะ"]
# bank = {"ดอกเบี้ย":["ดอก,เปี้ย","ดอก,เยี้ย","ดอก,เบี๋ย","ดอก,เบี้ย"]}

# deep_cut = ["กี่", "วัน", "อนุมัตคับ"]
# bay = {"อนุมัติ":["อนุมัต"]}
