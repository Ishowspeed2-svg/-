import jieba
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import os

# 让用户输入文件名
file_path = input("请输入你要分析的 .txt 文件名（如 comments.txt）：\n")

# 检查文件是否存在
if not os.path.exists(file_path):
    print(f"❌ 文件 '{file_path}' 不存在，请确认文件名或路径是否正确。")
else:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 分词
    words = jieba.lcut(text)

    # 停用词集合
    stopwords = {'的', '了', '和', '是', '您', '我', '也', '就', '都', '而', '及', '与',
        '着', '或', '一个', '没有', '我们', '你们', '他们', '她们', '把'
        '是否', '自己', '这个', '那个', '这些', '那些', '什么',
        '因为', '所以', '如果', '但是', '不是', '就是', '还有',
        '以及', '而且', '那么', '然后', '对', '啊', '哦', '嗯',
        '呀', '啦', '得', '去', '在', '有', '被', '由', '把', '会',
        '要', '能', '到', '做', '说', '看', '听', '让', '用', '等',
        '多', '少', '很', '挺', '真', '太', '嘛', '吧', '呢', '着', '过'}

    # 过滤无用词
    filtered = [w for w in words if w.strip() and w not in stopwords and len(w) > 1]

    # 统计词频
    freq = Counter(filtered)
    top_10_words = freq.most_common(10)

    print(f"\nTop 10 的关键词：")
    for i, (word, count) in enumerate(top_10_words, 1):
        print(f"{i}. {word} {count}次")

    # 生成词云
    if freq:
        wc = WordCloud(
            font_path="msyh.ttc",
            background_color='white',
            width=600,
            height=600
        ).generate_from_frequencies(freq)

        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        plt.title("词云图")
        plt.show()
    else:
        print("词云无法生成，内容为空。")

print("2420220024,胡铭涛")
