 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["paypal", "โอน", "เงิน", "เข้า", "ธนาคาร", "แล้ว", "ต้อง", "รอ", "ทาง", "ธนาคารโอน", "เงิน", "เข้า", "บัญชี", "กี่", "วัน", "คะ"]
    syntax = {}
    eng2tha = {}
    bay = {}
    bank = {"ธนาคาร":["ธนาคาร"],"โอน":["โอน"]}
    general = {}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]
    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
#word()


