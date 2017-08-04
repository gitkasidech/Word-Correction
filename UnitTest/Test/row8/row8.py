# -*- coding: utf-8 -*-
# from Test import logic
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic

def word(deep_cut):
    #deep_cut = ["ต้อง", "ปลด", "บล๊อคแอพกรุงศรีโมบาย"]
    syntax = {}
    eng2tha = {}
    bay = {"กรุงศรี":["กรุงศรี"]}
    bank = {'แอพพลิเคชั่น':["แอพ"]}
    general = {'แอพพลิเคชั่น':["แอพ"], "มือถือ": ["โมบาย"], "ปลด":["ปลด"], "บล็อก": ["บล๊อค"]}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut, outputs, corpus, nameCorpus)

    print(func)
    return func
#word()