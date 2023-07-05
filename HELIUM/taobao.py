from helium import *
import time
import re
start_chrome("https://www.taobao.com/")
click(Link("亲，请登录"))
click(Text("密码登录"))
time.sleep(2)
write("17384783755",into="会员名/邮箱/手机号")
time.sleep(2)
write("19981128wzq",into="请输入登录密码")
click(Button("",below="登录"))