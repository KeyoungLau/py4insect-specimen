#识别转化特定格式的经纬度地址
import re
import pyperclip
import time

last_string = pyperclip.paste()
print(last_string)
while True:
    time.sleep(3)
    raw_address = pyperclip.paste()
    if raw_address == last_string or raw_address == '':
        pass
    else:
        if re.match(".*:[0-9.].*,[0-9.].*", raw_address):
            slice1 = re.findall("(.*):", raw_address)
            slice2 = re.findall(":([0-9.].*),", raw_address)
            slice3 = re.findall(",([0-9.].*)", raw_address)
            print(slice1[0])
            print(f"北_{slice3[0]}")
            print(f"东_{slice2[0]}")
            print("-" * 20)
            last_string = raw_address
            #print("raw_add",raw_address)
            #print("last_string", last_string)
        else:
            pass