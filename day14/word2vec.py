from gensim.models import Word2Vec
# 示例数据
with open('全唐诗.txt', 'r') as f:
    tang_poems = f.read()
# 将诗句进行分词
tokenized_poems = [poem.split() for poem in tang_poems]
# print(tokenized_poems)
# 训练Word2Vec模型
model = Word2Vec(tokenized_poems, vector_size=10, window=5, min_count=1, workers=4)
# 获取与给定输入字最相似的其他字
input_word = '明'
similar_words = model.wv.most_similar(input_word)
# 显示结果
print(f"与'{input_word}'最相似的字：")
for word, similarity in similar_words:
    print(f"{word}: {similarity:.3f}")