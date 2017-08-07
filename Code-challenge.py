# coding=utf8
def main():
    # 3 Test syntax,bay,bank,general corpus with downcase.
    # deep_cut = ["คือ", "ผม", "จะ", "โอน", "เงิน", "ผ่าน", "พร้อม", "เพย์", "ไป", "อีก", "บัญชี่", "หนึ่ง", "ต่าง", "ธนาคาร", " ", "พอกรอก", "รายละเอียด", "เสร็จ", "แล้ว", "ก็", "กด", "ตกลง", " ", "ก็", "จะ", "ขึ้น", "ให้", "ใส่", "หมาย", "เลย", "อ้างอิง", " ", "OTP", " ", "ครับ"]
    # syntax = {"หมายเลข":["หมาย,เลย"]}
    # eng2tha = {}
    # bay = {"พร้อมเพย์":["พร้อมเพ","prompay","พร้อมย์เพย์","พ้อม,เพ","พร้อม,เพย์"],"โอทีพี":["otp"]}
    # bank = {"บัญชี": ["บันชี","บัญชี่", "บัญชี"]}
    # general = {"พอ,กรอก": ["พอก,รอก","พอกอก","พอกรอก"]}

    # 4 Test bay and general corpus.
    # deep_cut = ["02", "-", "777", "-", "1000", "ใช่", "เบอร์", "กรุงศรีรึป่าว", "คะ", " ", "เพราะ", "โทร", "มา", "แต่", "ไม่", "ได้", "รับ", "น่ะ", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี":["กรุงศรี"]}
    # bank = {}
    # general = {"เปล่า":["ป่าว"]}

    # 5 Test eng2thai corpus 1.
    # deep_cut = ["1", ".", " ", "Krungsri", " ", "Mobile", " ", "App"]
    # syntax = {}
    # eng2tha = {"กรุงศรี":["krungsri"],"โมบาย":["mobile"],"แอพ": ["app"]}
    # bay = {}
    # bank = {}
    # general = {}

    # 6 Test eng2thai corpus 2.
    # deep_cut = ["01034047731", "โทร", "กลับ", "นะ", "ค่ะ", " ", "ติดต่อ", "mobile", " ", "application", "ถูก", "ล็อค", "ค่ะ"]
    # syntax = {}
    # eng2tha = {"โมบาย":["mobile"],"แอพ": ["application"]}
    # bay = {}
    # bank = {}
    # general = {}

    # 7 Test eng2thai corpus 2. 
    # deep_cut = ["กรุงศรีเยล", "โล่พ้อย", " ", "จะ", "หมด", "อายุ", "แล้ว", "ทั้งหมด", "เลย", "ใช่", "ไหม", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี":["กรุงศรี"]}
    # bank = {}
    # general = {"เยลโล่พ้อยท์":["เยล,โล่พ้อย"]}

    # 8 Test 1 sentence 2 corpus 
    # deep_cut = ["ต้อง", "ปลด", "บล๊อคแอพกรุงศรีโมบาย"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี":["กรุงศรี"]}
    # bank = {'แอพพลิเคชั่น':["แอพ"]}
    # general = {'แอพพลิเคชั่น':["แอพ"], "มือถือ": ["โมบาย"], "ปลด":["ปลด"], "บล็อก": ["บล๊อค"]}

    # 9 Test split and edit sentence
    # deep_cut = ["กรุงศรีออโต้สมัค", "ไม่", "ได้"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี":["กรุงศรี"],"ออโต้":["ออโต้"]}
    # bank = {}
    # general = {"สมัคร":["สมัค"]}

    # 10 Test split and edit sentence
    # deep_cut = ["กี่", "วัน", "อนุมัตคับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"อนุมัติ":["อนุมัต"]}
    # bank = {}
    # general = {}

    # 11 Test split and edit sentence 
    # deep_cut = ["ข้อความ", "แจ้ง", "ยอด", "เงิน", "เข้ายอด", "เงิน", "ออก", "ไม่", "เข้า", "มือถือ", "เลย", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ยอด":["ยอด"],"เงิน":["เงิน"]}

    # 12 Test eng2thai corpus
    # deep_cut = ["ขอรับ", " ", "username", " ", "password", " ", "ของ", "ทาง", "ธนาคาร", "ได้", "ไหม", "ครับ"]
    # syntax = {}
    # eng2tha = {"รหัสผู้ใช้งาน":["username"],"รหัสผ่าน":["password"]}
    # bay = {}
    # bank = {}
    # general = {}

    # 13 Test merge sentence and eng2thai
    # deep_cut = ["first", " ", "choice", " ", "บัตร", "เครดิต"]
    # syntax = {}
    # eng2tha = {"เฟิร์สช้อยส์":["first,choice"]}
    # bay = {}
    # bank = {}
    # general = {}

    # 14 Test eng2thai,split and edit sentence
    # deep_cut = ["Login", " ", "เข้า", "กรุงศรีโม", "บายแอป", " ", "แล้ว", " ", "ไม่", "แสดง", "ยอด", "เงิน", "คงเหลือ", " ", "ขึ้น", " ", "not", " ", "availabe", " ", "ค่ะ"]
    # syntax = {}
    # eng2tha = {"ล็อคอิน":["login"],"ไม่":["not"],"พร้อม":["available","availabe"]} 
    # bay = {"กรุงศรี":["กรุงศรี"]}
    # bank = {"แอพพลิเคชั่น":["แอป"]}
    # general = {"มือถือ":["โม,บาย"]} 

    # 15 Test eng2thai and split sentence 
    # deep_cut = ["Otp โดน", "ล๊อค"]
    # syntax = {}
    # eng2tha = {"โอทีพี":["otp"]}
    # bay = {}
    # bank = {}
    # general = {"โดน":["โดน"],"ล็อค":["ล๊อค"]}

    # 16 Test eng2thai and merge sentence
    # deep_cut = ["Krungsri", " ", "prime", " ", "สิทธิ์", " ", "dining", " ", "มี", "กา", "แฟ", "ทรู", "อย่าง", "เดียว", "หรอ", " ", "ปกติ", "เห็น", "มี", "หลาย", "อย่าง", " ", "อิอิ"]
    # syntax = {}
    # eng2tha = {"กรุงศรี":["krungsri"],"ไพร์ม":["prime"]}
    # bay = {}
    # bank = {}
    # general = {"กาแฟ":["กา,แฟ"]}

    # 17 Test split sentence
    # deep_cut = ["paypal", "โอน", "เงิน", "เข้า", "ธนาคาร", "แล้ว", "ต้อง", "รอ", "ทาง", "ธนาคารโอน", "เงิน", "เข้า", "บัญชี", "กี่", "วัน", "คะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"ธนาคาร":["ธนาคาร"],"โอน":["โอน"]}
    # general = {}


    # 18 Test eng2thai and merge sentence 
    # deep_cut = ["กด", "เงิน", "สด", "จาก", "บัตร", "A", "TMคะ"]
    # syntax = {}
    # eng2tha = {"เอทีเอ็ม":["a,tm"]}
    # bay = {}
    # bank = {}
    # general = {}

    # 19 Test 1 sentence 2 corpus 
    # deep_cut = ["กดรหัส", "ผิด", "ค่ะ", " ", "แต่", "ครั้ง", "สุดท้าย", "กด", "ถูก", " ", "แต่", "บัตร", "โดน", "อายัด", " ", "ตอน", "นี้", "อยู่", "เชียงราย", " ", "แต่", "สมุด", "ฝาก", "อยู่", " ", "กทม", " ", "ต้อง", "ทำ", "ยัง", "ไง", "บ้าง", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"อายัด":["อายัด"]}
    # general = {"อายัด":["อายัด"]}

    # 20 Test 1 sentence 2 corpus 
    # deep_cut = ["กรณี", "ไม่", "มี", "บัตร", " ", "มี", "แต่", "สมุด", "บัญชี"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {}

    # 21 No output
    # deep_cut = ["กรณี", "ลืม", "รหัส", "ประจำ", "ตัว", "ละ", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {}

    # 22 No output
    # deep_cut = ["กรอก", "รหัส", "ประจำ", "ตัว", "ผิด", " ", "ต้อง", "ทำ", "ยัง", "ไง", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {}

    # 23 Test 1 sentence 2 corpus 
    # deep_cut = ["กรุงศรี", " ซุปเปอร์", " ", "พร้อม", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"ซุปเปอร์":["ซุปเปอร์"]}
    # bank = {"ซุปเปอร์":["ซุปเปอร์"]}
    # general = {}

    # 24 Test split sentence
    # deep_cut = ["กรุงศรีออนไลน์", "ปลอด", "ภัย", "หรือ", "ไม่"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี":["กรุงศรี"]}
    # bank = {}
    # general = {"ออนไลน์":["ออนไลน์"]}

    # 25 No output
    # deep_cut = ["การ", "เปิด", "บัญชี", "สำหรับ", "ชาว", "ต่าง", "ชาติ", "มี", "กี่", "ขั้นตอน"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {}

    # 26 Test genneral corpus
    # deep_cut = ["การ", "โอน", "เงิน", "ใน", "โทรศัพท์", "โดน", "ล็อค", "ทำ", "งัย", "ดี", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ไง":["งัย"]}

    # 27 Test split and edit sentence
    # deep_cut = ["กรุงศรีออโต้สมัค", "ไม่", "ได้"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี":["กรุงศรี"],"ออโต้":["ออโต้"]}
    # bank = {}
    # general = {"สมัคร":["สมัค"]}

    # 28 Test split sentence
    # deep_cut = ["กรุงศรีโมบาย", ".", " ", "จำรหัส", "ผ่าน", ".", " ", "กับ", "ไอดี", "ไม่", "ได้", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี":["กรุงศรี"]}
    # bank = {}
    # general = {"มือถือ":["โมบาย"]}

    # 29 Test genneral corpus
    # deep_cut = ["กี่", "วัน", "รู้", "ผล", "อนุมัติ", "ครับ", "สินเชื่อ", "ส้วน", "บุคคล"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ส่วน":["ส้วน"]}

    # 30 Test 1 sentence 2 corpus 
    # deep_cut = ["กี่", "วัน", "อนุมัตคับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"อนุมัติ":["อนุมัต"]}
    # general = {"อนุมัติ":["อนุมัต"]}

    # 31 Test eng2thai,split and edit sentence
    # deep_cut = ["ขอ", "เบออายัด", "บัตร", " ", "atm", " ", "หน่อย", "คะ"]
    # syntax = {}
    # eng2tha = {"เอทีเอ็ม":["atm"]}
    # bay = {}
    # bank = {"อายัด":["อายัด"]}
    # general = {"เบอร์":["เบอ"]}

    # 32 Test split sentence
    # deep_cut = ["ขอรหัส", "ชั่วคราว", "หน่อย", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ขอ":["ขอ"],"รหัส":["รหัส"]}

    # 33 Test bank corpus overdata
    # deep_cut = ["ขอสเตทเม้นท์", " ", "ต่าง", "สาขา", "ได้", "ไหม", "คะ", " ", "หรือ", "ต้อง", "ไป", "สาขา", "ที่", "เปิด", "บัญชี"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"สเตทเม้น":["เสตรทเมัน","สเตสเม้น","เสตรเมท","สเตสเมน","สเตทเม้นท์","สเตจเม้นท์","สเตจเม้นท์","สเตตเม้นท์","สเตดเม้นท์","สเตดเม้นท์","สเตดเม้นท์","สเตดเม้นท์","สเตทเม้น","สเตสเมน","สเต็สเม้น", "เสตรทเมัน"]}
    # general = {}

    # 34 Test genneral corpus
    # deep_cut = ["ขอโทษ", "นะ", "คะ", "ลืมรหัส", "ทำ", "งัย", "ดี", "คะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ไง":["งัย"]}

    # 35 Test split and edit sentence
    # deep_cut = ["ขอโทดสอบถาม", "เกี่ยว", "กับ", "กรุงศรีโมบาย", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ขอโทษ":["ขอโทด"],"สอบ":["สอบ"],"ถาม":["ถาม"]}

    # 36 Test split sentence
    # deep_cut = ["ขอ", "ทราบ", "เบอร์โทร", "ของ", "กรุงศรีหน่อย", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี":["กรุงศรี"]}
    # bank = {}
    # general = {"หน่อย":["หน่อย"]}

    # 37 Test split sentence
    # deep_cut = ["ขอ", "ถาม", "อีก", "อย่าง", "คะแล้ว", "ถ้า", "ไอดี", "กับ", "รหัส", "ผ่าน", "เข้า", "แอพกรุงศรีถูก", "ล๊อก", "ล้ะ", "ค้ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี":["กรุงศรี"]}
    # bank = {"แอพพลิเคชั่น":["แอพ"]}
    # general = {"ล็อค":["ล๊อก"],"คะ":["ค้ะ"]} 

    # 38 Test 1 sentence 2 corpus over data
    # deep_cut = ["เกี่ยว", "กับ", "การ", "ปลดรหัส", "แอพ", "กรุงศรี", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = { "แอพพลิเคชั่น":["แอพพิเคชั่น","แอฟ","แอป","แอบพลิเคชัน","แอบพลิเคชั่น","แอบพิเคชัน","แอบพิเคชั่น", "แอปพลิเคชัน","แอปพลิเคชั่น","แอปพิเคชัน","แอปพิเคชั่น","แอพ","แอพพลิเคชัน","แอพพิเคชัน","แอพพิเคชั่น","แอฟ","แอฟพลิเคชัน","แอฟพลิเคชั่น","แอฟพิเคชัน","แอฟพิเคชั่น","แอ๊ป","แอ๊พ","แอ๊บ","แอฟพริเอชั่น","แอบป","เเอบป", "แอฟฟิเคชั่น","ออป", "แอปฯ", "แอพฯ","แอฟฯ","แอ็ป","แอบ","แอพลิเคชั่น"]}
    # general = {"แอพพลิเคชั่น":["แอพพิเคชั่น","แอฟ","แอป","แอบพลิเคชัน","แอบพลิเคชั่น","แอบพิเคชัน","แอบพิเคชั่น", "แอปพลิเคชัน","แอปพลิเคชั่น","แอปพิเคชัน","แอปพิเคชั่น","แอพ","แอพพลิเคชัน","แอพพิเคชัน","แอพพิเคชั่น","แอฟ","แอฟพลิเคชัน","แอฟพลิเคชั่น","แอฟพิเคชัน","แอฟพิเคชั่น","แอ๊ป","แอ๊พ","แอ๊บ","แอฟพริเอชั่น","แอบป","เเอบป", "แอฟฟิเคชั่น","ออป", "แอปฯ", "แอพฯ","แอฟฯ","แอ็ป","แอบ","แอพลิเคชั่น"]}

    # 39 No output
    # deep_cut = ["เกี่ยว", "กับ", "กรุงศรีออโต้", "นะ", "คะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {}

    # 40 No output
    # deep_cut = ["เข้า", "ใช้", "งาน", "แล้ว", "ลืม", "รหัส", "ผ่าน"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {}

    # 41 Test eng2thai corpus
    # deep_cut = ["ค่า", "ทำ", "บัตร", " ", "atm", " ", "เท่า", "ไหร่", "อ่ะ", "คะ"]
    # syntax = {}
    # eng2tha = {"เอทีเอ็ม":["atm"]}
    # bay = {}
    # bank = {}
    # general = {}

    # 42 Test split sentence
    # deep_cut = ["ค่า", "ธรรมเนียมบัตร", "เดบิตราย", "ปี"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"เดบิต":["เดบิต"],"รายปี":["ราย,ปี"]}
    # general = {} 

    # 43 No output
    # deep_cut = ["คือ", " ", "ใส่", "รหัส", "ผ่าน", " ", "เกิน", "3", "ครั้ง"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 44 Test eng2thai and split sentence
    # deep_cut = ["คือ", "ทาง", "กรุงศรีไม่", "ส่ง", "รหัส", "otp", "มา", "ให้", "ค่ะ"]
    # syntax = {}
    # eng2tha = {"โอทีพี":["otp"]}
    # bay = {"กรุงศรี":["กรุงศรี"]}
    # bank = {}
    # general = {"ไม่":["ไม่"]} 

    # 45 No output
    # deep_cut = ["คือ", "แบบ", "ว่า", "ผม", "ลืม", "รหัส", "ประจำ", "ตัว", "และ", "รหัส", "เข้า", "ต้อง", "ทำ", "ยัง", "ไง", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 46 Test split sentence
    # deep_cut = ["คือ", "ผม", "อาญัติบัตร"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"อายัด":["อาญัติ"],"บัตร":["บัตร"]}
    # general = {} 

    # 47 Test eng2thai corpus 
    # deep_cut = ["จะ", "ปลด", "ล็อค", "OTP", "ครับ"]
    # syntax = {}
    # eng2tha = {"โอทีพี":["otp"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 48 Test genneral corpus
    # deep_cut = ["จะ", "สมคัร", "กรุงศรีออนไลน์"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"สมัคร":["สมคัร"]} 

    # 49 Test genneral corpus
    # deep_cut = ["จะ", "สมัคร", "รับ", "ข้อความ", "เงิน", "เข้า", "เงิน", "ออก", "อะคับ", "ทำ", "งัย"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ไง":["งัย"]} 

    # 50 No output
    # deep_cut = ["จะ", "สอบถาม", "เรื่อง", "บัตร", "เครดิต", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 51 Test eng2thai and edit sentence   
    # deep_cut = ["จะ", "อายัติบัตร", " ", "ATM"]
    # syntax = {}
    # eng2tha = {"เอทีเอ็ม":["atm"]}
    # bay = {}
    # bank = {"อายัด":["อายัติ" ]}
    # general = {} 

    # 52 No output
    # deep_cut = ["จะ", "โอน", "เงิน", "ผ่าน", "ทาง", "โทรศัพท์", "มือถือ", "จะ", "ต้อง", "ทำ", "ยัง", "ไร", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 53 Test split sentence
    # deep_cut = ["จำรหัส", "เข้า", "กรุงศรีโมบาย", "ไม่", "ได้", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี":["กรุงศรี"]}
    # bank = {}
    # general = {"มือถือ":["โมบาย"]} 

    # 54 No output
    # deep_cut = ["แจ้ง", "เปลี่ยน", "ที่", "อยู่", "ใน", "การ", "จัด", "ส่ง", "เอกสาร", "ยัง", "ไง", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 55 Test 1 sentence 2 corpus 
    # deep_cut = ["ดอกเบี้ย", "เงิน", "ฝาก"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 56 Test sentence 2 corpus 
    # deep_cut = ["ดอก", "เบี๋ย", "เท่า", "ไร", "คะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"ดอกเบี้ย":["ดอก,เปี้ย","ดอก,เยี้ย","ดอก,เบี๋ย","ดอก,เบี้ย"]}
    # general = {"ดอกเบี้ย":["ดอก,เปี้ย","ดอก,เยี้ย", "ดอก,เบี๋ย","ดอก,เบี้ย"]}

    # 57 Test  sentence 2 corpus
    # deep_cut = ["ดอกเบี้ย", "เท่า", "ไหร่"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"ดอกเบี้ย":[ "ดอกเบี้ย"]}
    # general = {"ดอกเบี้ย":[ "ดอกเบี้ย"]}

    # 58 Test  1 Corpus
    # deep_cut = ["ขอสเตทเม้นท์", " ", "ต่าง", "สาขา", "ได้", "ไหม", "คะ", " ", "หรือ", "ต้อง", "ไป", "สาขา", "ที่", "เปิด", "บัญชี"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"สเตทเม้น":["เสตรทเมัน","สเตสเม้น","เสตรเมท","สเตสเมน","สเตทเม้นท์","สเตจเม้นท์","สเตจเม้นท์","สเตตเม้นท์","สเตดเม้นท์" , "สเตดเม้นท์", "สเตดเม้นท์", "สเตดเม้นท์", "สเตทเม้น","สเตสเมน","สเต็สเม้น", "เสตรทเมัน" , "สเตทเม้น"]}
    # general = {} 

    # 59 Match Corpus
    # deep_cut = ["ขอสมัคร", "สินเชื่อ", "ส่วน", "บุคคล", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 60 Test eng2thai   
    # deep_cut = ["ขอ", "สอบถาม", "กน่อย", "ครับ", "..", "บัตร", "เครดิต", "..", "ถ้า", "ส่ง", " ", "sms", " ", "ไป", "เปิด", "บัตร", "แล้ว", "ต้อง", "ทำ", "ยัง", "ไง", "ต่อ", "ครับ"]
    # syntax = {}
    # eng2tha = {"เอสเอ็มเอส":["sms"]}
    # bay = {}
    # bank = {}
    # general = {}  

    # 61 Test sentence 2 corpus 
    # deep_cut = ["ขอ", "สอบถาม", "หน่อย", "ค่ะ", "หนู", "ลืม", "รหัส", "ผ่าน", "กับ", "รหัส", "ประจำ", "ตัว", "ทำ", "ไง", "ให้", "เข้า", "สู่", "ระบบ", "ได้", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {}

    # 62 Test  1 Corpus
    # deep_cut = ["ขอ", "เสตสเม้น", "ย้อนหลัง", "ได้", "ไหม", "คับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"สเตทเม้น":["เสตสเม้น","เสตรทเมัน","สเตสเม้น","เสตรเมท","สเตสเมน","สเตทเม้นท์","สเตจเม้นท์","สเตจเม้นท์","สเตตเม้นท์","สเตดเม้นท์" , "สเตดเม้นท์", "สเตดเม้นท์", "สเตดเม้นท์", "สเตทเม้น","สเตสเมน","สเต็สเม้น", "เสตรทเมัน", "สเตทเม้น"]}
    # general = {} 

    # 63 Test sentence 2 corpus
    # deep_cut = ["เข้า", "กรุงศรีโมบาย", "แอปไม่", "ได้", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"แอพพลิเคชั่น":["แอพพิเคชั่น", "แอฟ", "แอป", "แอบพลิเคชัน", "แอบพลิเคชั่น", "แอบพิเคชัน", "แอบพิเคชั่น", "แอป", "แอปพลิเคชัน", "แอปพลิเคชั่น", "แอปพิเคชัน", "แอปพิเคชั่น", "แอพ", "แอพพลิเคชัน", "แอพพิเคชัน", "แอพพิเคชั่น", "แอฟ", "แอฟพลิเคชัน", "แอฟพลิเคชั่น", "แอฟพิเคชัน", "แอฟพิเคชั่น", "แอ๊ป","แอ๊พ", "แอ๊บ","แอฟพริเอชั่น","แอบป", "เเอบป", "แอฟฟิเคชั่น","ออป", "แอปฯ", "แอพฯ", "แอฟฯ","แอ็ป", "แอบ" , "แอพพลิเคชั่น"] }
    # general = {"แอพพลิเคชั่น":["แอพพิเคชั่น", "แอฟ", "แอป", "แอบพลิเคชัน", "แอบพลิเคชั่น", "แอบพิเคชัน", "แอบพิเคชั่น", "แอป", "แอปพลิเคชัน", "แอปพลิเคชั่น", "แอปพิเคชัน", "แอปพิเคชั่น", "แอพ", "แอพพลิเคชัน", "แอพพิเคชัน", "แอพพิเคชั่น", "แอฟ", "แอฟพลิเคชัน", "แอฟพลิเคชั่น", "แอฟพิเคชัน", "แอฟพิเคชั่น", "แอ๊ป","แอ๊พ", "แอ๊บ","แอฟพริเอชั่น","แอบป", "เเอบป", "แอฟฟิเคชั่น","ออป", "แอปฯ", "แอพฯ", "แอฟฯ","แอ็ป", "แอบ" , "แอพพลิเคชั่น"]} 

    # 64 Test eng2thai   
    # deep_cut = ["ค่า", "ทำ", "บัตร", " ", "atm", " ", "เท่า", "ไหร่", "อ่ะ", "คะ"]
    # syntax = {}
    # eng2tha = {"เอทีเอ็ม":["atm"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 65 Test eng2thai   
    # deep_cut = ["เคย", "สมัคร", "กรุงศรีbanking", " ", "mobile", " ", "แล้ว", " ", "จำuser", " ", " ", "และ", " ", "รหัส", " ", "ไม่", "ได้", "แล้ว", " ", "ทำ", "งัย", "ดี", "คะ"]
    # syntax = {}
    # eng2tha = {"แบงค์กิ้ง": ["banking"] , "มือถือ" : ["mobile"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 66 Match Corpus
    # deep_cut = ["เครื่อง", "รูด",""  ," edc","" ," คิด", "ค่าธรรมเนียม", "ยังไง", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 67 Match Corpus
    # deep_cut = ["จะ", "สมัคร", "โอน", "เงิน", "บน", "มือถือ", "จะ", "ทำ", "อย่าง", "ไร", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 68 Test sentence 2 corpus
    # deep_cut = ["จะ", "สอบถาม", "เกี่ยว", "กับ", "บัตร", "เครดิต", "กรุงศรี"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 69 Test eng2thai   
    # deep_cut = ["จะ", "อายัติบัตร", " ", "ATM"]
    # syntax = {}
    # eng2tha = {"เอทีเอ็ม": ["atm"]}
    # bay = {}
    # bank = {"อายัด":["อายัติ","อายัต"]}
    # general = {"อายัด":["อายัติ","อายัต"]}

    # 70 Test sentence 2 corpus
    # deep_cut = ["ดี", "จ้า", "เมื่อ", "ไหร่", "จะ", "ทราบ", "ผล", "การ", "สมัคร", "บัตร", "เครดิต"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 71 Test eng2thai
    # deep_cut = ["โดน", "ล็อกรหัส", "OTP.", " ", "ต้อง", "ทำไง", "ค้ะ"]
    # syntax = {"ค่ะ":["ค้ะ"]}
    # eng2tha = {"โอทีพี": ["otp"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 72 Match Corpus
    # deep_cut = ["ต้องการ", "กู้", "เงิน"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 73 Test  1 Corpus 
    # deep_cut = ["ต้องการ", "ขอรหัส", "ผ่าน", "ชั่วคราม", "ใหม่", "คัฟ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ชั่วคราว":["ชั่วคราม"]} 

    # 74 Match Corpus
    # deep_cut = ["ต้องการ", "จะ", "เปลี่ยนแปลง", "ที่", "อยู่", "ใบ", "แจ้ง", "หนี้", "ใน", "อีเมล", " ", "สามารถ", "ทำ", "ได้", "ทาง", "ไหน", "บ้าง", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 75 Test 1 Corpus
    # deep_cut = ["ต้องการ", "รี", "ไฟแนน", "บ้าน", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"รีไฟแนนซ์":["ลีไฟแน้","ไฟแนนซ์", "รีไฟแนนซ์", "รัไฟแนนท์", "รีฟายแนนซ์", "รี,ไฟแนน", "รีไฟแนนท์","ไฟแนนท์","ไฟแนนซ์" , "รีไฟแนน"]}
    # bank = {}
    # general = {} 

    # 76 Test general corpus.
    # deep_cut = ["ต้อง", "แจ้ง", "สมุด", "บัญชี", "หาย", "ไหใคะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ไหน" : [" ใหน", "ไหน" , "ไหใ"]} 

    # 77 Test 1 Corpus
    # deep_cut = ["ตอน", "นี้", "ร้อน", "เงิน", " ", "อยาก", "ได้สินเชื่อ", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"สินเชื่อ": ["สินเชื่อ"]}
    # general = {} 

    # 78 Test sentence 2 corpus
    # deep_cut = ["ถ้า", "มา", "จำนอง", "กับ", "กรุงศรีคิด", "ดอกเบี้ย", "ยัง", "ไง", "คะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 79 Test eng2thai
    # deep_cut = ["บัตร", " ", "atm", " ", "หาย"]
    # syntax = {}
    # eng2tha = {"เอทีเอ็ม": ["atm"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 80 Match Corpus
    # deep_cut = ["บัตร", " ", "เดบิต"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 81 Test eng2thai
    # deep_cut = ["บัตร", "atm", "ตู้", "ยึด", "ครับ"]
    # syntax = {}
    # eng2tha = {"เอทีเอ็ม": ["atm"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 82 Test eng2thai
    # deep_cut = ["บัตร", "debit"]
    # syntax = {}
    # eng2tha = {"เดบิต": ["debit"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 83 Test sentence 2 corpus
    # deep_cut = ["บัตร", "เครดิตหาย"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"เครดิต": ["เครดิต"]}
    # general = {"เครดิต": ["เครดิต"]} 

    # 84 บัตรเอทีเอ็มหายทำไงดี
    # deep_cut = ["บัตร", "เอทีเอ็มหาย", "ทำ", "ไง", "ดี"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 85 Test eng2thai
    # deep_cut = ["ปลด", "ล็อก", "", "otp", "ยัง", "ไง"]
    # syntax = {}
    # eng2tha = {"โอทีพี": ["otp"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 86 Match Corpus
    # deep_cut = ["เปิด", "บัญชี"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 87 Test eng2thai
    # deep_cut = ["ผม", "จะ", "สมัคร", "ใช", "งาน", "กรุงศรีโมบาย"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ใช้":["ช่","ไช้" ,"ใช"]}

    # 88 Test eng2thai
    # deep_cut = ["ผม", "ไม่", "ไดรับรหัส", "otp"]
    # syntax = {}
    # eng2tha = {"โอทีพี": ["otp"]}
    # bay = {}
    # bank = {}
    # general = {"ได้":["ใด้","ได่", "ได้ำ","ได"]} 

    # 89 Match Corpus
    # deep_cut = ["ผม", "ลืม", "รหัส", " ", "ประจำ", "ตัว"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 90 Test 1 Corpus 
    # deep_cut = ["พร้อม", "เพค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"พร้อมเพย์":["พร้อม,เพ","prompay","พร้อมย์เพย์","พ้อม,เพ", "พร้อมเพย์"]}
    # bank = {}
    # general = {} 

    # 91 Match Corpus
    # deep_cut = ["พอดี", "รหัส", "โดน", "ล็อค", "ค่ะ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 92 Test eng2thai
    # deep_cut = ["พอดี", "สมุด", "บัญชี", "ผม", "หายatm", "ก็", "หาย", "อยาก", "รู้", "ว่า", "ต้อง", "ทำไง", "ถึง", "จะ", "เบิก", "เงิน", "ได้"]
    # syntax = {}
    # eng2tha = {"เอทีเอ็ม": ["atm"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 93 Test eng2thai
    # deep_cut = ["พี่ลืม", "username"]
    # syntax = {}
    # eng2tha = {"รหัสผู้ใช้งาน": ["username"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 94 Match Corpus
    # deep_cut = ["ผม", "ว่า", "จะ", "สมัคเช็ก", "ยอด", "เงิน"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = { "เช็ค" : ["เช็ก"] }
    # general = {"สมัคร":["สมัค"]} 

    # 95 Math Corpus
    # deep_cut = ["ผม", "อยาก", "เช็ค", "เงิน", "ให้", "มือถือ", "ได้", "อะครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 96 Test sentence 2 corpus
    # deep_cut = ["ผม", "อยาก", "ทราบ", "ว่า", "ผม", "ล็อค", "อินแอพกรุงศรี", "ไม่", "ได้", "ต้อง", "ทำ", "ไง", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {"กรุงศรี": ["กรุงศรี"]}
    # bank = {"แอพพลิเคชั่น":["แอพพิเคชั่น", "แอฟ", "แอป", "แอบพลิเคชัน", "แอบพลิเคชั่น", "แอบพิเคชัน", "แอบพิเคชั่น", "แอป", "แอปพลิเคชัน", "แอปพลิเคชั่น", "แอปพิเคชัน", "แอปพิเคชั่น", "แอพ", "แอพพลิเคชัน", "แอพพิเคชัน", "แอพพิเคชั่น", "แอฟ", "แอฟพลิเคชัน", "แอฟพลิเคชั่น", "แอฟพิเคชัน", "แอฟพิเคชั่น", "แอ๊ป","แอ๊พ", "แอ๊บ","แอฟพริเอชั่น","แอบป", "เเอบป", "แอฟฟิเคชั่น","ออป", "แอปฯ", "แอพฯ", "แอฟฯ","แอ็ป", "แอบ" , "แอพพลิเคชั่น"] }
    # general = {"แอพพลิเคชั่น":["แอพพิเคชั่น", "แอฟ", "แอป", "แอบพลิเคชัน", "แอบพลิเคชั่น", "แอบพิเคชัน", "แอบพิเคชั่น", "แอป", "แอปพลิเคชัน", "แอปพลิเคชั่น", "แอปพิเคชัน", "แอปพิเคชั่น", "แอพ", "แอพพลิเคชัน", "แอพพิเคชัน", "แอพพิเคชั่น", "แอฟ", "แอฟพลิเคชัน", "แอฟพลิเคชั่น", "แอฟพิเคชัน", "แอฟพิเคชั่น", "แอ๊ป","แอ๊พ", "แอ๊บ","แอฟพริเอชั่น","แอบป", "เเอบป", "แอฟฟิเคชั่น","ออป", "แอปฯ", "แอพฯ", "แอฟฯ","แอ็ป", "แอบ" , "แอพพลิเคชั่น"] }

    # 97
    # deep_cut = ["ฝาก", "เงิน", "ผ่าน", "ตู้", "แล้ว", "เงิน", "ไม่", "เข้า", "ทำไง", "ครับ"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {} 

    # 98
    # deep_cut = ["เมื่อ", "ไร", "จะ", "ทราบ", "ผล", "การ", "สมัคร", "บัตร", "เครติด"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"เครดิต":["เครติด"]}
    # general = {"เครดิต":["เครติด"]}

    # 99
    # deep_cut = ["รหัส", " ", "otp", " ", "คือ", "อะไร", "ค่ะ"]
    # syntax = {}
    # eng2tha = {"โอทีพี": ["otp"]}
    # bay = {}
    # bank = {}
    # general = {} 

    # 100
    # deep_cut = ["รหัสโดนล๊อก"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {}
    # general = {"ล็อค":["ล็อด","ล๊อค","ล็อก","ล้อค","ล๊อก","ล็อก","ล็ก","ลอค","ล็อก","ล้อค","ล้อก","ลอก็","ล็อค"]}

    # 101
    # deep_cut = ["รหัส", "โดนอายัด"]
    # syntax = {}
    # eng2tha = {}
    # bay = {}
    # bank = {"อายัด": ["อายัด"]}
    # general = {"อายัด": ["อายัด"]}

    outputs = {}
    corpus = [syntax,eng2tha,bay,bank,general]
    nameCorpus = ["|syntax","|eng2tha","|bay","|bank","|general"]
    count = 0

    oldKey = []
    newDeep = []
    outputs = algor(deep_cut,outputs,corpus,nameCorpus)
    print(outputs)

def algor(deep_cut,outputs,corpus,nameCorpus):

    iCorpus = 0
    lenDeep = len(deep_cut)
    oldKey = []
    newDeep = []

    loopNewdeepLow(deep_cut,lenDeep,newDeep)
    outputs = loopCorpus(corpus,newDeep,deep_cut,lenDeep,nameCorpus,iCorpus,outputs,oldKey)
    
    return outputs 

def loopNewdeepLow(deep_cut,lenDeep,newDeep):
    for i in range(lenDeep):
        lowDeep = deep_cut[i].lower()
        newDeep.append(lowDeep)
def loopCorpus(corpus,newDeep,deep_cut,lenDeep,nameCorpus,iCorpus,outputs,oldKey):
    for c in corpus:
        outputs = loopKey(newDeep,deep_cut,lenDeep,nameCorpus,iCorpus,outputs,oldKey,c)
        iCorpus = iCorpus + 1
    return outputs
def loopKey(newDeep,deep_cut,lenDeep,nameCorpus,iCorpus,outputs,oldKey,c):
    for key, value in c.items():
        if key in oldKey:
            continue
        oldKey.append(key)
        outputs = loopValue(newDeep,value,deep_cut,lenDeep,key,nameCorpus,iCorpus,outputs)
    return outputs
def loopValue(newDeep,value,deep_cut,lenDeep,key,nameCorpus,iCorpus,outputs):
    for v in value:
        vj = []
        comma = 0
        checkJ = 0
        iRe = 0

        if "," in v:
            comma = 1
        spl = v.split(",")

        vj,checkJ,iRe = loopPushVJ(newDeep,iRe,v,deep_cut,vj,checkJ,lenDeep,spl,comma)
        outputs = checkJforPush(key,nameCorpus,iCorpus,vj,outputs,comma,checkJ,spl,v,deep_cut,newDeep,iRe)
    return outputs
def loopPushVJ(newDeep,iRe,v,deep_cut,vj,checkJ,lenDeep,spl,comma):
    for i in range(lenDeep):
        if newDeep[i] in spl and newDeep[i] != "":
            vj.append(deep_cut[i])
            checkJ = checkJ + 1
            iRe = i
            continue
        elif v in newDeep[i] and newDeep[i] != "" :
            vj,checkJ,iRe = caseVinNewdeep(newDeep,i,iRe,v,deep_cut,vj,checkJ)
            continue
        elif comma == 1:
            vj,checkJ,iRe = caseCommaIs1(spl,vj,checkJ,i,deep_cut,newDeep,iRe)
    return vj,checkJ,iRe
def pushOutput(key,nameCorpus,iCorpus,vj,outputs):
    k1 = key
    k2 = nameCorpus[iCorpus]
    ks = k1 + k2
    outputs[ks] = vj
    return outputs
def checkJforPush(key,nameCorpus,iCorpus,vj,outputs,comma,checkJ,spl,v,deep_cut,newDeep,iRe):
    if comma == 1 and checkJ == len(spl):
        vj = ",".join(vj)
        vjLow = vj.lower()
        if (vjLow == v):
            outputs = pushOutput(key,nameCorpus,iCorpus,vj,outputs)

    elif len(vj) != 0 and len(vj[0]) == len(v):
        vj = " ".join(vj)
        vjLow = vj.lower()
        if (vjLow == v):
            outputs = pushOutput(key,nameCorpus,iCorpus,vj,outputs)
            deep_cut[iRe] = newDeep[iRe].replace(v, "")
            newDeep[iRe] = newDeep[iRe].replace(v, "")
        elif checkJ>0:
            if " " in vj:
                vj = vj.split(" ")
                vj = vj[0]
            outputs = pushOutput(key,nameCorpus,iCorpus,vj,outputs)
    return outputs
def caseVinNewdeep(newDeep,i,iRe,v,deep_cut,vj,checkJ):
    if " " in newDeep[i]:
        splNew = newDeep[i].split(" ")
        iRe = i
        if splNew[0] in v and splNew[0] != "": 
            splDeep = deep_cut[i].split(" ")
            vj.append(splDeep[0])
        if splNew[1] in v and splNew[1] != "":
            splDeep = deep_cut[i].split(" ")
            vj.append(splDeep[1])
    else:
        vj.append(v)
        checkJ = checkJ+1
        iRe = i
    return vj,checkJ,iRe
def caseCommaIs1(spl,vj,checkJ,i,deep_cut,newDeep,iRe):
    for j in range(len(spl)):
        if spl[j] in newDeep[i]:
            rem = newDeep[i].replace(spl[j],"")
            org = deep_cut[i].replace(rem,"")
            vj.append(org)
            checkJ = checkJ+1
            iRe = i
    return vj,checkJ,iRe

main()

