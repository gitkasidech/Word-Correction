 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["โดน", "ล็อกรหัส", "OTP.", " ", "ต้อง", "ทำไง", "ค้ะ"]
    syntax = {"ค่ะ":["ค้ะ"]}
    eng2tha = {"โอทีพี": ["otp"]}
    bay = {}
    bank = {}
    general = {}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
#word()