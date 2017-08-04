 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["พร้อม", "เพค่ะ"]
    syntax = {}
    eng2tha = {}
    bay = {"พร้อมเพย์":["พร้อม,เพ","prompay","พร้อมย์เพย์","พ้อม,เพ", "พร้อมเพย์"]}
    bank = {}
    general = {}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
#word()