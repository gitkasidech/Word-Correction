 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["ดอก", "เบี๋ย", "เท่า", "ไร", "คะ"]
    syntax = {}
    eng2tha = {}
    bay = {}
    bank = {"ดอกเบี้ย":["ดอก,เปี้ย","ดอก,เยี้ย","ดอก,เบี๋ย","ดอก,เบี้ย"]}
    general = {"ดอกเบี้ย":["ดอก,เปี้ย","ดอก,เยี้ย", "ดอก,เบี๋ย","ดอก,เบี้ย"]}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
#word()