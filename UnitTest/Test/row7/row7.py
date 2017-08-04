# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic


def word(deep_cut):
    #deep_cut = ["กรุงศรีเยล", "โล่พ้อย", " ", "จะ", "หมด", "อายุ", "แล้ว", "ทั้งหมด", "เลย", "ใช่", "ไหม", "ค่ะ"]
    syntax = {}
    eng2tha = {}
    bay = {"กรุงศรี":["กรุงศรี"]}
    bank = {}
    general = {"เยลโล่พ้อยท์":["เยล,โล่พ้อย"]}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut, outputs, corpus, nameCorpus)

    print(func)
    return func
#word()