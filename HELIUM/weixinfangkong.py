from helium import *
start_chrome("https://fangkong.hnu.edu.cn/app/#/login?redirect=%2Fhome")
# click(Text("密码登录"))
write("S200200262",into="学工号")
write("19981128wzq",into="个人门户登录密码")
# click(Image(alt="imagevcode"))
# write("",into="验证码")
click(Button("",below="登录"))
