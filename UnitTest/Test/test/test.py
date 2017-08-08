#-*- coding: utf-8 -*-
import unittest

from .context import row3



class TestStringMethods(unittest.TestCase):

    def test_case3(self):
         deep_cut3 = ["คือ", "ผม", "จะ", "โอน", "เงิน", "ผ่าน", "พร้อม", "เพย์", "ไป", "อีก", "บัญชี่", "หนึ่ง", "ต่าง", "ธนาคาร", " ", "พอกรอก", "รายละเอียด", "เสร็จ", "แล้ว", "ก็", "กด", "ตกลง", " ", "ก็", "จะ", "ขึ้น", "ให้", "ใส่", "หมาย", "เลย", "อ้างอิง", " ", "OTP", " ", "ครับ"]
         self.assertEqual(row3.word(deep_cut3), {'หมายเลข|syntax': 'หมาย,เลย', 'พร้อมเพย์|bay': 'พร้อม,เพย์', 'โอทีพี|bay': 'OTP', 'บัญชี|bank': 'บัญชี่', 'พอ,กรอก|general': 'พอกรอก'})

if __name__ == '__main__':
    unittest.main()