 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["เมื่อ", "ไร", "จะ", "ทราบ", "ผล", "การ", "สมัคร", "บัตร", "เครติด"]
    syntax = {}
    eng2tha = {}
    bay = {}
    bank = { "เครดิต":["เครติด"]}
    general = { "เครดิต":["เครติด"]}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
#word()