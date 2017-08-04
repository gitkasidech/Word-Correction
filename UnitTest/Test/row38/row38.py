 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["เกี่ยว", "กับ", "การ", "ปลดรหัส", "แอพ", "กรุงศรี", "ค่ะ"]
    syntax = {}
    eng2tha = {}
    bay = {}
    bank = { "แอพพลิเคชั่น":["แอพพิเคชั่น","แอฟ","แอป","แอบพลิเคชัน","แอบพลิเคชั่น","แอบพิเคชัน","แอบพิเคชั่น", "แอปพลิเคชัน","แอปพลิเคชั่น","แอปพิเคชัน","แอปพิเคชั่น","แอพ","แอพพลิเคชัน","แอพพิเคชัน","แอพพิเคชั่น","แอฟ","แอฟพลิเคชัน","แอฟพลิเคชั่น","แอฟพิเคชัน","แอฟพิเคชั่น","แอ๊ป","แอ๊พ","แอ๊บ","แอฟพริเอชั่น","แอบป","เเอบป", "แอฟฟิเคชั่น","ออป", "แอปฯ", "แอพฯ","แอฟฯ","แอ็ป","แอบ","แอพลิเคชั่น"]}
    general = {"แอพพลิเคชั่น":["แอพพิเคชั่น","แอฟ","แอป","แอบพลิเคชัน","แอบพลิเคชั่น","แอบพิเคชัน","แอบพิเคชั่น", "แอปพลิเคชัน","แอปพลิเคชั่น","แอปพิเคชัน","แอปพิเคชั่น","แอพ","แอพพลิเคชัน","แอพพิเคชัน","แอพพิเคชั่น","แอฟ","แอฟพลิเคชัน","แอฟพลิเคชั่น","แอฟพิเคชัน","แอฟพิเคชั่น","แอ๊ป","แอ๊พ","แอ๊บ","แอฟพริเอชั่น","แอบป","เเอบป", "แอฟฟิเคชั่น","ออป", "แอปฯ", "แอพฯ","แอฟฯ","แอ็ป","แอบ","แอพลิเคชั่น"]}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
#     count = 0
#     lenDeep = len(deep_cut)
#     oldKey = []
#
#     for c in corpus:
#         for key, value in c.items():
#             if key in oldKey:
#                 continue
#             oldKey.append(key)
#             for v in value:
#                 j = []
#                 newDeep = []
#                 comma = 0
#                 space = 0
#                 elsej = 0
#                 if "," in v:
#                     spl = v.split(",")
#                     comma = comma + 1
#                 elif " " in v:
#                     spl = v.split(" ")
#                     space = space + 1
#                 else:
#                     spl = v
#                 for i in range(lenDeep):
#                     lowDeep = deep_cut[i].lower()
#                     newDeep.append(lowDeep)
#                     if newDeep[i] in spl:
#                         j.append(deep_cut[i])
#                         elsej = elsej + 1
#                     elif v in newDeep[i]:
#                         j.append(v)
#                         elsej = elsej + 1
#                         deep_cut[i] = newDeep[i].replace(v, "")
#                 if space == 1 and elsej > 0:
#                     j = " ".join(j)
#                     k1 = key
#                     k2 = nameCorpus[count]
#                     ks = k1 + k2
#                     outputs[ks] = j
#                 elif comma == 1 and elsej > 0:
#                     j = ",".join(j)
#                     k1 = key
#                     k2 = nameCorpus[count]
#                     ks = k1 + k2
#                     outputs[ks] = j
#                 elif elsej > 0:
#                     j = "".join(j)
#                     k1 = key
#                     k2 = nameCorpus[count]
#                     ks = k1 + k2
#                     outputs[ks] = j
#         count = count + 1
#
#     print(outputs)
#     return outputs
# #word()