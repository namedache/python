import jieba
import re
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


#对数据进行展示
def word():
    text = ''
    removes =['最佳', '表现', '集锦', '狂胜', '回顾', '获胜', '使用','能力','盖帽','得分','进攻']
    with open('./weibocontent2.txt', 'r') as f:
        text = f.read()
        f.close()
    print(text[:100])
    words = jieba.lcut(text)
    # pattern = re.compile(r'^[a-zA-Z0-1]+$')
    words = [w for w in words if w not in removes]
    cuted = ' '.join(words)
    print(cuted[:500])

    fontpath = 'SourceHanSansCN-Regular.otf'

    aimask = np.array(Image.open("Ai.png"))

    genclr = ImageColorGenerator(aimask)

    wc = WordCloud(font_path=fontpath,  # 设置字体
                   background_color="white",  # 背景颜色
                   max_words=1000,  # 词云显示的最大词数
                   max_font_size=100,  # 字体最大值
                   min_font_size=5,  # 字体最小值
                   random_state=42,  # 随机数
                   collocations=False,  # 避免重复单词
                   mask=aimask,  # 造型遮盖
                   color_func=genclr,
                   width=1600, height=1200, margin=2,  # 图像宽高，字间距，需要配合下面的plt.figure(dpi=xx)放缩才有效
                   )
    wc.generate(cuted)

    plt.figure(dpi=150)  # 通过这里可以放大或缩小
    plt.imshow(wc, interpolation='catrom', vmax=1000)
    plt.axis("off")


    #展示图片
    wc.to_file("show2.png")
