 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["ต้องการ", "รี", "ไฟแนน", "บ้าน", "ค่ะ"]
    syntax = {}
    eng2tha = {}
    bay = {"รีไฟแนนซ์":["ลีไฟแน้","ไฟแนนซ์", "รีไฟแนนซ์", "รัไฟแนนท์", "รีฟายแนนซ์", "รี,ไฟแนน", "รีไฟแนนท์","ไฟแนนท์","ไฟแนนซ์" , "รีไฟแนน"]}
    bank = {}
    general = {}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
#word()