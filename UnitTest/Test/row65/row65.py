 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["เคย", "สมัคร", "กรุงศรีbanking", " ", "mobile", " ", "แล้ว", " ", "จำuser", " ", " ", "และ", " ", "รหัส", " ", "ไม่", "ได้", "แล้ว", " ", "ทำ", "งัย", "ดี", "คะ"]
    syntax = {}
    eng2tha = {"แบงค์กิ้ง": ["banking"] , "มือถือ" : ["mobile"]}
    bay = {}
    bank = {}
    general = {}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
