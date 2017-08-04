 # -*- coding: utf-8 -*-
# from Test.logic import *
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import logic
def word(deep_cut):
    #deep_cut = ["คือ", "ผม", "จะ", "โอน", "เงิน", "ผ่าน", "พร้อม", "เพย์", "ไป", "อีก", "บัญชี่", "หนึ่ง", "ต่าง", "ธนาคาร", " ", "พอกรอก", "รายละเอียด", "เสร็จ", "แล้ว", "ก็", "กด", "ตกลง", " ", "ก็", "จะ", "ขึ้น", "ให้", "ใส่", "หมาย", "เลย", "อ้างอิง", " ", "OTP", " ", "ครับ"]
    syntax = {"หมายเลข": ["หมาย,เลย"]}
    eng2tha = {}
    bay = {"พร้อมเพย์":["พร้อมเพ","prompay","พร้อมย์เพย์","พ้อม,เพ","พร้อม,เพย์"],"โอทีพี":["otp"]}
    bank = {"บัญชี": ["บันชี","บัญชี่", "บัญชี"]}
    general = {"พอ,กรอก": ["พอก,รอก","พอกอก","พอกรอก"]}
    outputs = {}
    corpus = [syntax, eng2tha, bay, bank, general]
    nameCorpus = ["|syntax", "|eng2tha", "|bay", "|bank", "|general"]

    func = logic.algor(deep_cut,outputs,corpus,nameCorpus)

    print(func)
    return func
#word()



