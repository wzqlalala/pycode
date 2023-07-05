from helium import *
start_chrome("https://www.zhihu.com/signin?next=%2F")
click(Text("密码登录"))
write("17384783755",into=S("@username"))
write("19981128wzq",into="密码")
click(Button("",below="登录"))