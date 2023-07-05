#wordcloud.py
import wordcloud

f = open("English.txt","r");
txt = f.read();
w = wordcloud.WordCloud(font_path="msyh.ttc",width = 1000,height= 700,background_color= "white")
w.generate(txt)
w.to_file("xxx.png")