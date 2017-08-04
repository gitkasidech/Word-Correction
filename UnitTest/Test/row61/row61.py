 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["ขอ", "สอบถาม", "หน่อย", "ค่ะ", "หนู", "ลืม", "รหัส", "ผ่าน", "กับ", "รหัส", "ประจำ", "ตัว", "ทำ", "ไง", "ให้", "เข้า", "สู่", "ระบบ", "ได้", "ค่ะ"]
    syntax = {}
    eng2tha = {}
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