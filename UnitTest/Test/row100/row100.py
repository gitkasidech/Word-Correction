 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["รหัสโดนล๊อก"]
    syntax = {}
    eng2tha = {}
    bay = {}
    bank = {}
    general = {"ล็อค":["ล็อด","ล๊อค","ล็อก","ล้อค","ล๊อก","ล็อก","ล็ก","ลอค","ล็อก","ล้อค","ล้อก","ลอก็","ล็อค"] }
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
#word()