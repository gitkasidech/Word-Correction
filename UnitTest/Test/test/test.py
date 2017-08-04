#-*- coding: utf-8 -*-
import unittest

from .context import row3
from .context import row4
from .context import row5
from .context import row6
from .context import row7
from .context import row8
from .context import row9
from .context import row10
from .context import row11
from .context import row12
from .context import row13
from .context import row14
from .context import row15
from .context import row16
from .context import row17
from .context import row18
from .context import row19
from .context import row20
from .context import row21
from .context import row22
from .context import row23
from .context import row24
from .context import row25
from .context import row26
from .context import row27
from .context import row28
from .context import row29
from .context import row30
from .context import row31
from .context import row32
from .context import row33
from .context import row34
from .context import row35
from .context import row36
from .context import row37
from .context import row38
from .context import row39
from .context import row40
from .context import row41
from .context import row42
from .context import row43
from .context import row44
from .context import row45
from .context import row46
from .context import row47
from .context import row48
from .context import row49
from .context import row50
from .context import row51
from .context import row52
from .context import row53
from .context import row54
from .context import row55
from .context import row56
from .context import row57
from .context import row58
from .context import row59
from .context import row60
from .context import row61
from .context import row62
from .context import row63
from .context import row64
from .context import row65
from .context import row66
from .context import row67
from .context import row68
from .context import row69
from .context import row70
from .context import row71
from .context import row72
from .context import row73
from .context import row74
from .context import row75
from .context import row76
from .context import row77
from .context import row78
from .context import row79
from .context import row80
from .context import row81
from .context import row82
from .context import row83
from .context import row84
from .context import row85
from .context import row86
from .context import row87
from .context import row88
from .context import row89
from .context import row90
from .context import row91
from .context import row92
from .context import row93
from .context import row94
from .context import row95
from .context import row96
from .context import row97
from .context import row98
from .context import row99
from .context import row100
from .context import row101



class TestStringMethods(unittest.TestCase):

    def test_case3(self):
         deep_cut3 = ["คือ", "ผม", "จะ", "โอน", "เงิน", "ผ่าน", "พร้อม", "เพย์", "ไป", "อีก", "บัญชี่", "หนึ่ง", "ต่าง", "ธนาคาร", " ", "พอกรอก", "รายละเอียด", "เสร็จ", "แล้ว", "ก็", "กด", "ตกลง", " ", "ก็", "จะ", "ขึ้น", "ให้", "ใส่", "หมาย", "เลย", "อ้างอิง", " ", "OTP", " ", "ครับ"]
         self.assertEqual(row3.word(deep_cut3), {'หมายเลข|syntax': 'หมาย,เลย', 'พร้อมเพย์|bay': 'พร้อม,เพย์', 'โอทีพี|bay': 'OTP', 'บัญชี|bank': 'บัญชี่', 'พอ,กรอก|general': 'พอกรอก'})

    def test_case4(self):
         deep_cut4 = ["02", "-", "777", "-", "1000", "ใช่", "เบอร์", "กรุงศรีรึป่าว", "คะ", " ", "เพราะ", "โทร", "มา", "แต่", "ไม่", "ได้", "รับ", "น่ะ", "ค่ะ"]
         self.assertEqual(row4.word(deep_cut4), {'กรุงศรี|bay': 'กรุงศรี', 'เปล่า|general': 'ป่าว'})

    def test_case5(self):
         deep_cut5 = ["1", ".", " ", "Krungsri", " ", "Mobile", " ", "App"]
         self.assertEqual(row5.word(deep_cut5), {'กรุงศรี|eng2tha': 'Krungsri', 'โมบาย|eng2tha': 'Mobile', 'แอพ|eng2tha': 'App'})

    def test_case6(self):
         deep_cut6 = ["01034047731", "โทร", "กลับ", "นะ", "ค่ะ", " ", "ติดต่อ", "mobile", " ", "application", "ถูก", "ล็อค", "ค่ะ"]
         self.assertEqual(row6.word(deep_cut6), {'โมบาย|eng2tha': 'mobile', 'แอพ|eng2tha': 'application'})

    def test_case7(self):
         deep_cut7 = ["กรุงศรีเยล", "โล่พ้อย", " ", "จะ", "หมด", "อายุ", "แล้ว", "ทั้งหมด", "เลย", "ใช่", "ไหม", "ค่ะ"]
         self.assertEqual(row7.word(deep_cut7),{'กรุงศรี|bay': 'กรุงศรี', 'เยลโล่พ้อยท์|general': 'เยล,โล่พ้อย'})

    def test_case8(self):
         deep_cut8 = ["ต้อง", "ปลด", "บล๊อคแอพกรุงศรีโมบาย"]
         self.assertEqual(row8.word(deep_cut8),{'กรุงศรี|bay': 'กรุงศรี', 'แอพพลิเคชั่น|bank': 'แอพ', 'มือถือ|general': 'โมบาย', 'ปลด|general': 'ปลด', 'บล็อก|general': 'บล๊อค'})

    def test_case9(self):
         deep_cut9 = ["กรุงศรีออโต้สมัค", "ไม่", "ได้"]
         self.assertEqual(row9.word(deep_cut9), {'กรุงศรี|bay': 'กรุงศรี', 'ออโต้|bay': 'ออโต้', 'สมัคร|general': 'สมัค'})

    def test_case10(self):
         deep_cut10 = ["กี่", "วัน", "อนุมัตคับ"]
         self.assertEqual(row10.word(deep_cut10), {'อนุมัติ|bank': 'อนุมัต'})

    def test_case11(self):
         deep_cut11 = ["ข้อความ", "แจ้ง", "ยอด", "เงิน", "เข้ายอด", "เงิน", "ออก", "ไม่", "เข้า", "มือถือ", "เลย", "ค่ะ"]
         self.assertEqual(row11.word(deep_cut11), {'ยอด|general': 'ยอด ยอด', 'เงิน|general': 'เงิน เงิน'})

    def test_case12(self):
         deep_cut12 = ["ขอรับ", " ", "username", " ", "password", " ", "ของ", "ทาง", "ธนาคาร", "ได้", "ไหม", "ครับ"]
         self.assertEqual(row12.word(deep_cut12), {'รหัสผู้ใช้งาน|eng2tha': 'username', 'รหัสผ่าน|eng2tha': 'password'})

    def test_case13(self):
         deep_cut13 = ["first", " ", "choice", " ", "บัตร", "เครดิต"]
         self.assertEqual(row13.word(deep_cut13), {'เฟิร์สช้อยส์|eng2tha': 'first,choice'})

    def test_case14(self):
         deep_cut14 = ["Login", " ", "เข้า", "กรุงศรีโม", "บายแอป", " ", "แล้ว", " ", "ไม่", "แสดง", "ยอด", "เงิน", "คงเหลือ", " ", "ขึ้น", " ", "not", " ", "availabe", " ", "ค่ะ"]
         self.assertEqual(row14.word(deep_cut14), {'ล็อคอิน|eng2tha': 'Login', 'ไม่|eng2tha': 'not', 'พร้อม|eng2tha': 'availabe', 'กรุงศรี|bay': 'กรุงศรี', 'แอพพลิเคชั่น|bank': 'แอป', 'มือถือ|general': 'โม,บาย'})

    def test_case15(self):
         deep_cut15 = ["Otp โดน", "ล๊อค"]
         self.assertEqual(row15.word(deep_cut15), {'โอทีพี|eng2tha': 'Otp', 'โดน|general': 'โดน', 'ล็อค|general': 'ล๊อค'})

    def test_case16(self):
         deep_cut16 = ["Krungsri", " ", "prime", " ", "สิทธิ์", " ", "dining", " ", "มี", "กา", "แฟ", "ทรู", "อย่าง", "เดียว", "หรอ", " ", "ปกติ", "เห็น", "มี", "หลาย", "อย่าง", " ", "อิอิ"]
         self.assertEqual(row16.word(deep_cut16), {'กรุงศรี|eng2tha': 'Krungsri', 'ไพร์ม|eng2tha': 'prime', 'กาแฟ|general': 'กา,แฟ'})

    def test_case17(self):
         deep_cut17 = ["paypal", "โอน", "เงิน", "เข้า", "ธนาคาร", "แล้ว", "ต้อง", "รอ", "ทาง", "ธนาคารโอน", "เงิน", "เข้า", "บัญชี", "กี่", "วัน", "คะ"]
         self.assertEqual(row17.word(deep_cut17), {'ธนาคาร|bank': 'ธนาคาร ธนาคาร', 'โอน|bank': 'โอน โอน'})


    def test_case18(self):
         deep_cut18 = ["กด", "เงิน", "สด", "จาก", "บัตร", "A", "TMคะ"]
         self.assertEqual(row18.word(deep_cut18), {'เอทีเอ็ม|eng2tha': 'A,TM'})

    def test_case19(self):
         deep_cut19 = ["กดรหัส", "ผิด", "ค่ะ", " ", "แต่", "ครั้ง", "สุดท้าย", "กด", "ถูก", " ", "แต่", "บัตร", "โดน", "อายัด", " ", "ตอน", "นี้", "อยู่", "เชียงราย", " ", "แต่", "สมุด", "ฝาก", "อยู่", " ", "กทม", " ", "ต้อง", "ทำ", "ยัง", "ไง", "บ้าง", "ครับ"]
         self.assertEqual(row19.word(deep_cut19), {"อายัด|bank":"อายัด"})

    def test_case20(self):
         deep_cut20 = ["กรณี", "ไม่", "มี", "บัตร", " ", "มี", "แต่", "สมุด", "บัญชี"]
         self.assertEqual(row20.word(deep_cut20),{})

    def test_case21(self):
         deep_cut21 = ["กรณี", "ลืม", "รหัส", "ประจำ", "ตัว", "ละ", "ครับ"]
         self.assertEqual(row21.word(deep_cut21), {})

    def test_case22(self):
         deep_cut22 = ["กรอก", "รหัส", "ประจำ", "ตัว", "ผิด", " ", "ต้อง", "ทำ", "ยัง", "ไง", "ครับ"]
         self.assertEqual(row22.word(deep_cut22), {})

    def test_case23(self):
         deep_cut23 = ["กรุงศรี", " ซุปเปอร์", " ", "พร้อม", "ค่ะ"]
         self.assertEqual(row23.word(deep_cut23), {'ซุปเปอร์|bay': 'ซุปเปอร์'})

    def test_case24(self):
         deep_cut24 = ["กรุงศรีออนไลน์", "ปลอด", "ภัย", "หรือ", "ไม่"]
         self.assertEqual(row24.word(deep_cut24), {'กรุงศรี|bay': 'กรุงศรี', 'ออนไลน์|general': 'ออนไลน์'})

    def test_case25(self):
         deep_cut25 = ["การ", "เปิด", "บัญชี", "สำหรับ", "ชาว", "ต่าง", "ชาติ", "มี", "กี่", "ขั้นตอน"]
         self.assertEqual(row25.word(deep_cut25), {})

    def test_case26(self):
         deep_cut26 = ["การ", "โอน", "เงิน", "ใน", "โทรศัพท์", "โดน", "ล็อค", "ทำ", "งัย", "ดี", "ค่ะ"]
         self.assertEqual(row26.word(deep_cut26), {'ไง|general': 'งัย'})

    def test_case27(self):
         deep_cut27 = ["กรุงศรีออโต้สมัค", "ไม่", "ได้"]
         self.assertEqual(row27.word(deep_cut27), {'กรุงศรี|bay': 'กรุงศรี', 'ออโต้|bay': 'ออโต้', 'สมัคร|general': 'สมัค'})

    def test_case28(self):
         deep_cut28= ["กรุงศรีโมบาย", ".", " ", "จำรหัส", "ผ่าน", ".", " ", "กับ", "ไอดี", "ไม่", "ได้", "ครับ"]
         self.assertEqual(row28.word(deep_cut28), {'กรุงศรี|bay': 'กรุงศรี', 'มือถือ|general': 'โมบาย'})

    def test_case29(self):
         deep_cut29 = ["กี่", "วัน", "รู้", "ผล", "อนุมัติ", "ครับ", "สินเชื่อ", "ส้วน", "บุคคล"]
         self.assertEqual(row29.word(deep_cut29), {'ส่วน|general': 'ส้วน'})

    def test_case30(self):
         deep_cut30 = ["กี่", "วัน", "อนุมัตคับ"]
         self.assertEqual(row30.word(deep_cut30), {'อนุมัติ|bank': 'อนุมัต'})

    def test_case31(self):
         deep_cut31 = ["ขอ", "เบออายัด", "บัตร", " ", "atm", " ", "หน่อย", "คะ"]
         self.assertEqual(row31.word(deep_cut31), {'เอทีเอ็ม|eng2tha': 'atm', 'อายัด|bank': 'อายัด', 'เบอร์|general': 'เบอ'})

    def test_case32(self):
         deep_cut32 = ["ขอรหัส", "ชั่วคราว", "หน่อย", "ค่ะ"]
         self.assertEqual(row32.word(deep_cut32), {'ขอ|general': 'ขอ', 'รหัส|general': 'รหัส'})

    def test_case33(self):
         deep_cut33 = ["ขอสเตทเม้นท์", " ", "ต่าง", "สาขา", "ได้", "ไหม", "คะ", " ", "หรือ", "ต้อง", "ไป", "สาขา", "ที่", "เปิด", "บัญชี"]
         self.assertEqual(row33.word(deep_cut33), {'สเตทเม้น|bank': 'สเตทเม้นท์'})

    def test_case34(self):
         deep_cut34 = ["ขอโทษ", "นะ", "คะ", "ลืมรหัส", "ทำ", "งัย", "ดี", "คะ"]
         self.assertEqual(row34.word(deep_cut34), {'ไง|general': 'งัย'})

    def test_case35(self):
         deep_cut35 = ["ขอโทดสอบถาม", "เกี่ยว", "กับ", "กรุงศรีโมบาย", "ค่ะ"]
         self.assertEqual(row35.word(deep_cut35), {'ขอโทษ|general': 'ขอโทด', 'สอบ|general': 'สอบ', 'ถาม|general': 'ถาม'})

    def test_case36(self):
         deep_cut36 = ["ขอ", "ทราบ", "เบอร์โทร", "ของ", "กรุงศรีหน่อย", "ค่ะ"]
         self.assertEqual(row36.word(deep_cut36), {'กรุงศรี|bay': 'กรุงศรี', 'หน่อย|general': 'หน่อย'})

    def test_case37(self):
         deep_cut37 = ["ขอ", "ถาม", "อีก", "อย่าง", "คะแล้ว", "ถ้า", "ไอดี", "กับ", "รหัส", "ผ่าน", "เข้า", "แอพกรุงศรีถูก", "ล๊อก", "ล้ะ", "ค้ะ"]
         self.assertEqual(row37.word(deep_cut37), {'กรุงศรี|bay': 'กรุงศรี', 'แอพพลิเคชั่น|bank': 'แอพ', 'ล็อค|general': 'ล๊อก', 'คะ|general': 'ค้ะ'})

    def test_case38(self):
         deep_cut38= ["เกี่ยว", "กับ", "การ", "ปลดรหัส", "แอพ", "กรุงศรี", "ค่ะ"]
         self.assertEqual(row38.word(deep_cut38), {'แอพพลิเคชั่น|bank': 'แอพ'})

    def test_case39(self):
         deep_cut39 = ["เกี่ยว", "กับ", "กรุงศรีออโต้", "นะ", "คะ"]
         self.assertEqual(row39.word(deep_cut39), {})

    def test_case40(self):
         deep_cut40 = ["กี่", "วัน", "อนุมัตคับ"]
         self.assertEqual(row40.word(deep_cut40), {})

    def test_case41(self):
         deep_cut41 = ["ค่า", "ทำ", "บัตร", " ", "atm", " ", "เท่า", "ไหร่", "อ่ะ", "คะ"]
         self.assertEqual(row41.word(deep_cut41), {'เอทีเอ็ม|eng2tha': 'atm'})

    def test_case42(self):
         deep_cut42 = ["ค่า", "ธรรมเนียมบัตร", "เดบิตราย", "ปี"]
         self.assertEqual(row42.word(deep_cut42), {'เดบิต|bank': 'เดบิต', 'รายปี|bank': 'ราย,ปี'})

    def test_case43(self):
         deep_cut43 = ["คือ", " ", "ใส่", "รหัส", "ผ่าน", " ", "เกิน", "3", "ครั้ง"]
         self.assertEqual(row43.word(deep_cut43), {})

    def test_case44(self):
         deep_cut44 = ["คือ", "ทาง", "กรุงศรีไม่", "ส่ง", "รหัส", "otp", "มา", "ให้", "ค่ะ"]
         self.assertEqual(row44.word(deep_cut44), {'โอทีพี|eng2tha': 'otp', 'กรุงศรี|bay': 'กรุงศรี', 'ไม่|general': 'ไม่'})

    def test_case45(self):
         deep_cut45 = ["คือ", "แบบ", "ว่า", "ผม", "ลืม", "รหัส", "ประจำ", "ตัว", "และ", "รหัส", "เข้า", "ต้อง", "ทำ", "ยัง", "ไง", "ครับ"]
         self.assertEqual(row45.word(deep_cut45), {})

    def test_case46(self):
         deep_cut46 = ["คือ", "ผม", "อาญัติบัตร"]
         self.assertEqual(row46.word(deep_cut46), {'อายัด|bank': 'อาญัติ', 'บัตร|bank': 'บัตร'})

    def test_case47(self):
         deep_cut47 = ["จะ", "ปลด", "ล็อค", "OTP", "ครับ"]
         self.assertEqual(row47.word(deep_cut47), {'โอทีพี|eng2tha': 'OTP'})

    def test_case48(self):
         deep_cut48 = ["จะ", "สมคัร", "กรุงศรีออนไลน์"]
         self.assertEqual(row48.word(deep_cut48), {'สมัคร|general': 'สมคัร'})

    def test_case49(self):
         deep_cut49 = ["จะ", "สมัคร", "รับ", "ข้อความ", "เงิน", "เข้า", "เงิน", "ออก", "อะคับ", "ทำ", "งัย"]
         self.assertEqual(row49.word(deep_cut49), {'ไง|general': 'งัย'})

    def test_case50(self):
         deep_cut50 = ["กี่", "วัน", "อนุมัตคับ"]
         self.assertEqual(row50.word(deep_cut50), {})

    def test_case51(self):
         deep_cut51 = ["จะ", "อายัติบัตร", " ", "ATM"]
         self.assertEqual(row51.word(deep_cut51), {'เอทีเอ็ม|eng2tha': 'ATM', 'อายัด|bank': 'อายัติ'})

    def test_case52(self):
         deep_cut52 = ["จะ", "โอน", "เงิน", "ผ่าน", "ทาง", "โทรศัพท์", "มือถือ", "จะ", "ต้อง", "ทำ", "ยัง", "ไร", "ครับ"]
         self.assertEqual(row52.word(deep_cut52), {})

    def test_case53(self):
         deep_cut53 = ["จำรหัส", "เข้า", "กรุงศรีโมบาย", "ไม่", "ได้", "ค่ะ"]
         self.assertEqual(row53.word(deep_cut53), {'กรุงศรี|bay': 'กรุงศรี', 'มือถือ|general': 'โมบาย'})

    def test_case54(self):
         deep_cut54 = ["แจ้ง", "เปลี่ยน", "ที่", "อยู่", "ใน", "การ", "จัด", "ส่ง", "เอกสาร", "ยัง", "ไง", "ครับ"]
         self.assertEqual(row54.word(deep_cut54), {})

    def test_case55(self):
         deep_cut55 = ["ดอกเบี้ย", "เงิน", "ฝาก"]
         self.assertEqual(row55.word(deep_cut55), {})
    
    def test_case56(self):
         deep_cut56 = ["ดอก", "เบี๋ย", "เท่า", "ไร", "คะ"]
         self.assertEqual(row56.word(deep_cut56), {'ดอกเบี้ย|bank': 'ดอก,เบี๋ย'})

    def test_case57(self):
         deep_cut57 = ["ดอกเบี้ย", "เท่า", "ไหร่"]
         self.assertEqual(row57.word(deep_cut57), {'ดอกเบี้ย|bank': 'ดอกเบี้ย'})

    def test_case58(self):
         deep_cut58 = ["ขอสเตทเม้นท์", " ", "ต่าง", "สาขา", "ได้", "ไหม", "คะ", " ", "หรือ", "ต้อง", "ไป", "สาขา", "ที่", "เปิด", "บัญชี"]
         self.assertEqual(row58.word(deep_cut58), {'สเตทเม้น|bank': 'สเตทเม้นท์'})

    def test_case59(self):
         deep_cut59 = ["ขอสมัคร", "สินเชื่อ", "ส่วน", "บุคคล", "ครับ"]
         self.assertEqual(row59.word(deep_cut59), {})

    def test_case60(self):
         deep_cut60 = ["ขอ", "สอบถาม", "กน่อย", "ครับ", "..", "บัตร", "เครดิต", "..", "ถ้า", "ส่ง", " ", "sms", " ", "ไป", "เปิด", "บัตร", "แล้ว", "ต้อง", "ทำ", "ยัง", "ไง", "ต่อ", "ครับ"]
         self.assertEqual(row60.word(deep_cut60), {'เอสเอ็มเอส|eng2tha': 'sms'})

    def test_case61(self):
         deep_cut61 = ["ขอ", "สอบถาม", "หน่อย", "ค่ะ", "หนู", "ลืม", "รหัส", "ผ่าน", "กับ", "รหัส", "ประจำ", "ตัว", "ทำ", "ไง", "ให้", "เข้า", "สู่", "ระบบ", "ได้", "ค่ะ"]
         self.assertEqual(row61.word(deep_cut61), {})

    def test_case62(self):
         deep_cut62 = ["ขอ", "เสตสเม้น", "ย้อนหลัง", "ได้", "ไหม", "คับ"]
         self.assertEqual(row62.word(deep_cut62), {'สเตทเม้น|bank': 'เสตสเม้น'})

    def test_case63(self):
         deep_cut63 = ["เข้า", "กรุงศรีโมบาย", "แอปไม่", "ได้", "ค่ะ"]
         self.assertEqual(row63.word(deep_cut63), {'แอพพลิเคชั่น|bank': 'แอป'})

    def test_case64(self):
         deep_cut64 = ["ค่า", "ทำ", "บัตร", " ", "atm", " ", "เท่า", "ไหร่", "อ่ะ", "คะ"]
         self.assertEqual(row64.word(deep_cut64), {'เอทีเอ็ม|eng2tha': 'atm'})

    def test_case65(self):
         deep_cut65 = ["เคย", "สมัคร", "กรุงศรีbanking", " ", "mobile", " ", "แล้ว", " ", "จำuser", " ", " ", "และ", " ", "รหัส", " ", "ไม่", "ได้", "แล้ว", " ", "ทำ", "งัย", "ดี", "คะ"]
         self.assertEqual(row65.word(deep_cut65), {'แบงค์กิ้ง|eng2tha': 'banking', 'มือถือ|eng2tha': 'mobile'})
    
    def test_case66(self):
         deep_cut66 = ["เครื่อง", "รูด",""  ," edc","" ," คิด", "ค่าธรรมเนียม", "ยังไง", "ครับ"]
         self.assertEqual(row66.word(deep_cut66), {})

    def test_case67(self):
         deep_cut67 = ["จะ", "สมัคร", "โอน", "เงิน", "บน", "มือถือ", "จะ", "ทำ", "อย่าง", "ไร", "ครับ"]
         self.assertEqual(row67.word(deep_cut67), {})

    def test_case68(self):
         deep_cut68= ["จะ", "สอบถาม", "เกี่ยว", "กับ", "บัตร", "เครดิต", "กรุงศรี"]
         self.assertEqual(row68.word(deep_cut68), {})

    def test_case69(self):
         deep_cut69 = ["จะ", "อายัติบัตร", " ", "ATM"]
         self.assertEqual(row69.word(deep_cut69), {'เอทีเอ็ม|eng2tha': 'ATM', 'อายัด|bank': 'อายัติ'})

    def test_case70(self):
         deep_cut70 = ["ดี", "จ้า", "เมื่อ", "ไหร่", "จะ", "ทราบ", "ผล", "การ", "สมัคร", "บัตร", "เครดิต"]
         self.assertEqual(row70.word(deep_cut70), {})

    def test_case71(self):
         deep_cut71 = ["โดน", "ล็อกรหัส", "OTP.", " ", "ต้อง", "ทำไง", "ค้ะ"]
         self.assertEqual(row71.word(deep_cut71), {'ค่ะ|syntax': 'ค้ะ', 'โอทีพี|eng2tha': 'otp'})

    def test_case72(self):
         deep_cut72 = ["ต้องการ", "กู้", "เงิน"]
         self.assertEqual(row72.word(deep_cut72), {})

    def test_case73(self):
         deep_cut73 = ["ต้องการ", "ขอรหัส", "ผ่าน", "ชั่วคราม", "ใหม่", "คัฟ"]
         self.assertEqual(row73.word(deep_cut73), {'ชั่วคราว|general': 'ชั่วคราม'})

    def test_case74(self):
         deep_cut74 = ["ต้องการ", "จะ", "เปลี่ยนแปลง", "ที่", "อยู่", "ใบ", "แจ้ง", "หนี้", "ใน", "อีเมล", " ", "สามารถ", "ทำ", "ได้", "ทาง", "ไหน", "บ้าง", "ครับ"]
         self.assertEqual(row74.word(deep_cut74), {})

    def test_case75(self):
         deep_cut75 = ["ต้องการ", "รี", "ไฟแนน", "บ้าน", "ค่ะ"]
         self.assertEqual(row75.word(deep_cut75), {'รีไฟแนนซ์|bay': 'รี,ไฟแนน'})
    
    def test_case76(self):
         deep_cut76 = ["ต้อง", "แจ้ง", "สมุด", "บัญชี", "หาย", "ไหใคะ"]
         self.assertEqual(row76.word(deep_cut76), {'ไหน|general': 'ไหใ'})

    def test_case77(self):
         deep_cut77 = ["ตอน", "นี้", "ร้อน", "เงิน", " ", "อยาก", "ได้สินเชื่อ", "ครับ"]
         self.assertEqual(row77.word(deep_cut77), {'สินเชื่อ|bank': 'สินเชื่อ'})

    def test_case78(self):
         deep_cut78= ["ถ้า", "มา", "จำนอง", "กับ", "กรุงศรีคิด", "ดอกเบี้ย", "ยัง", "ไง", "คะ"]
         self.assertEqual(row78.word(deep_cut78), {})

    def test_case79(self):
         deep_cut79 = ["บัตร", " ", "atm", " ", "หาย"]
         self.assertEqual(row79.word(deep_cut79), {'เอทีเอ็ม|eng2tha': 'atm'})

    def test_case80(self):
         deep_cut80 = ["บัตร", " ", "เดบิต"]
         self.assertEqual(row80.word(deep_cut80), {})

    def test_case81(self):
        deep_cut81 = ["บัตร", "atm", "ตู้", "ยึด", "ครับ"]
        self.assertEqual(row81.word(deep_cut81), {'เอทีเอ็ม|eng2tha': 'atm'})

    def test_case82(self):
         deep_cut82 = ["บัตร", "debit"]
         self.assertEqual(row82.word(deep_cut82), {'เดบิต|eng2tha': 'debit'})

    def test_case83(self):
         deep_cut83 = ["บัตร", "เครดิตหาย"]
         self.assertEqual(row83.word(deep_cut83), {'เครดิต|bank': 'เครดิต'})

    def test_case84(self):
         deep_cut84 = ["บัตร", "เอทีเอ็มหาย", "ทำ", "ไง", "ดี"]
         self.assertEqual(row84.word(deep_cut84), {})

    def test_case85(self):
         deep_cut85 = ["ปลด", "ล็อก", "", "otp", "ยัง", "ไง"]
         self.assertEqual(row85.word(deep_cut85), {'โอทีพี|eng2tha': 'otp'})
    
    def test_case86(self):
         deep_cut86 = ["เปิด", "บัญชี"]
         self.assertEqual(row86.word(deep_cut86), {})

    def test_case87(self):
         deep_cut87 = ["ผม", "จะ", "สมัคร", "ใช", "งาน", "กรุงศรีโมบาย"]
         self.assertEqual(row87.word(deep_cut87), {'ใช้|general': 'ใช'})

    def test_case88(self):
         deep_cut88= ["ผม", "ไม่", "ไดรับรหัส", "otp"]
         self.assertEqual(row88.word(deep_cut88), {'โอทีพี|eng2tha': 'otp', 'ได้|general': 'ได'})

    def test_case89(self):
         deep_cut89 = ["ผม", "ลืม", "รหัส", " ", "ประจำ", "ตัว"]
         self.assertEqual(row89.word(deep_cut89), {})

    def test_case90(self):
         deep_cut90 = ["พร้อม", "เพค่ะ"]
         self.assertEqual(row90.word(deep_cut90), {'พร้อมเพย์|bay': 'พร้อม,เพ'})

    def test_case91(self):
         deep_cut91 = ["พอดี", "รหัส", "โดน", "ล็อค", "ค่ะ"]
         self.assertEqual(row91.word(deep_cut91), {})
    
    def test_case92(self):
         deep_cut92 = ["พอดี", "สมุด", "บัญชี", "ผม", "หายatm", "ก็", "หาย", "อยาก", "รู้", "ว่า", "ต้อง", "ทำไง", "ถึง", "จะ", "เบิก", "เงิน", "ได้"]
         self.assertEqual(row92.word(deep_cut92), {'เอทีเอ็ม|eng2tha': 'atm'})

    def test_case93(self):
         deep_cut93 = ["พี่ลืม", "username"]
         self.assertEqual(row93.word(deep_cut93), {'รหัสผู้ใช้งาน|eng2tha': 'username'})

    def test_case94(self):
         deep_cut94 =   ["ผม", "ว่า", "จะ", "สมัคเช็ก", "ยอด", "เงิน"]
         self.assertEqual(row94.word(deep_cut94), {'เช็ค|bank': 'เช็ก', 'สมัคร|general': 'สมัค'})

    def test_case95(self):
         deep_cut95 = ["ผม", "อยาก", "เช็ค", "เงิน", "ให้", "มือถือ", "ได้", "อะครับ"]
         self.assertEqual(row95.word(deep_cut95), {})
    
    def test_case96(self):
         deep_cut96 = ["ผม", "อยาก", "ทราบ", "ว่า", "ผม", "ล็อค", "อินแอพกรุงศรี", "ไม่", "ได้", "ต้อง", "ทำ", "ไง", "ครับ"]
         self.assertEqual(row96.word(deep_cut96), {'กรุงศรี|bay': 'กรุงศรี', 'แอพพลิเคชั่น|bank': 'แอพ'})

    def test_case97(self):
         deep_cut97 = ["ฝาก", "เงิน", "ผ่าน", "ตู้", "แล้ว", "เงิน", "ไม่", "เข้า", "ทำไง", "ครับ"]
         self.assertEqual(row97.word(deep_cut97), {})

    def test_case98(self):
         deep_cut98= ["เมื่อ", "ไร", "จะ", "ทราบ", "ผล", "การ", "สมัคร", "บัตร", "เครติด"]
         self.assertEqual(row98.word(deep_cut98), {'เครดิต|bank': 'เครติด'})

    def test_case99(self):
         deep_cut99 = ["รหัส", " ", "otp", " ", "คือ", "อะไร", "ค่ะ"]
         self.assertEqual(row99.word(deep_cut99), {'โอทีพี|eng2tha': 'otp'})

    def test_case100(self):
         deep_cut100 = ["รหัสโดนล๊อก"]
         self.assertEqual(row100.word(deep_cut100), {'ล็อค|general': 'ล๊อก'})

    def test_case101(self):
         deep_cut101 = ["รหัส", "โดนอายัด"]
         self.assertEqual(row101.word(deep_cut101), {'อายัด|bank': 'อายัด'})

if __name__ == '__main__':
    unittest.main()