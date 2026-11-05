# robot

## 启动
pip install fastapi uvicorn
uvicorn app:app --reload

## 功能
访问 /ask?q=转专业绩点，会返回答案、来源 source、是否拒答 refused。

## 当前指标
- eval 数量：10
- 拒答判断正确：写你的真实分数，比如 8/10
- 已知问题：会误伤简称；还不会像人一样总结

## 不会做什么
不知道就拒答，不编电话、日期、网址。

## 下一步
接大模型，把检索到的原文总结成自然语言，并保留 source。