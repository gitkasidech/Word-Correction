 # -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["ขอ", "เสตสเม้น", "ย้อนหลัง", "ได้", "ไหม", "คับ"]
    syntax = {}
    eng2tha = {}
    bay = {}
    bank = {"สเตทเม้น":["เสตสเม้น","เสตรทเมัน","สเตสเม้น","เสตรเมท","สเตสเมน","สเตทเม้นท์","สเตจเม้นท์","สเตจเม้นท์","สเตตเม้นท์","สเตดเม้นท์" , "สเตดเม้นท์", "สเตดเม้นท์", "สเตดเม้นท์", "สเตทเม้น","สเตสเมน","สเต็สเม้น", "เสตรทเมัน", "สเตทเม้น"]}
    general = {}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
#word()