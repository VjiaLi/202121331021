<div align = "center">

# [作业链接（代码已开源）](https://github.com/VjiaLi/202121331021.git)

# Information

| 这个作业属于哪个课程 | [计算21级](https://edu.cnblogs.com/campus/jmu/ComputerScience21)|
| ----------------- |--------------- |
| 这个作业要求在哪里| <center>[作业要求](https://edu.cnblogs.com/campus/jmu/ComputerScience21/homework/13034)</center>|
| 这个作业的目标 | 开发项目入门级练习 |

</div>
<div align = "center">

##Requirements

</div>

题目：**论文查重**

​	设计一个论文查重算法，给出一个原文文件和一个在这份原文上经过了增删改的抄袭版论文的文件，在答案文件中输出其重复率。

- 原文示例：今天是星期天，天气晴，今天晚上我要去看电影。
- 抄袭版示例：今天是周天，天气晴朗，我晚上要去看电影。

要求输入输出采用文件输入输出，规范如下：

- 从**命令行参数**给出：论文原文的文件的**绝对路径**。
- 从**命令行参数**给出：抄袭版论文的文件的**绝对路径**。
- 从**命令行参数**给出：输出的答案文件的**绝对路径**。

注意：答案文件中输出的答案为浮点型，精确到小数点后两位

<div align = "center">

## Introduction

</div>
本次作业对文本相似度计算中主流的几种算法进行复现，并集成在我的个人项目中，同时，对不同算法的时间开销、准确度、内存占比等方面进行综合考量与对比，可将项目保存到本地进行个人算法的优化。

<div align="center">

|  Checker | Time↓ | Accuracy↑ | MEM_COST↓ |
| -------- | ----- | ----- | ----- |
| [Cosine]()    | 0.47±0.05s | 54.77% | 249.83MB |
| [Jaccard]() | 0.46±0.02s | 37.50% | 247.69MB |
| [Levenshtein]()     | 0.48±0.2s | 69.77% | 247.80MB |
| [Minhash]() | 0.46±0.1s  | 33.59% | 247.84MB |
| [Simhash]()  | 0.47±0.3s | 34.38% | 248.04MB |
| [Custom]() |      | | |
|<img width=200/>                                   | <img width=100/> | <img width=100/> | <img width=100/> |
</div>
<sub> NOTES: 该结果是作业中所提供的数据上进行测量的，并不能反映绝大部分情况，仅供参考。时间开销由py中的time库测得,内存占用由py中的memory_profiler库测得。</sub>

<div align="center">

## Installation

</div>
如果你想要在这个项目上进行代码的开发与优化:

建议使用anaconda创建[**Python>=3.9**](https://www.python.org/) 的虚拟环境.

```
git clone https://github.com/VjiaLi/202121331021.git
cd 202121331021
pip install -r requirements.txt .
```

但是如果仅仅只是想要完成作业:

```
git clone https://github.com/VjiaLi/202121331021.git
cd 202121331021/methods
Ctrl+C
Ctrl+V
```

<div align = "center">

## My Idea

</div>
如果想实现一个简单高效、内存占用率低的算法，那就要减少第三方库的调用，但是，这必然会导致算法精度的下降。

通常来讲，由于欧式距离具有平方与开方的复杂操作，计算开销必然比余弦距离大，但是余弦距离不考虑向量的绝对大小，只关注方向，因此对于某些应用场景可能不够精确，我们需要在这之间有所取舍，所以，我设置了一个超参数去权衡二者之间的关系。

1. **数据预处理**

> 使用 jieba 去除停用词。
> 自定义函数提取文本关键字。

2. **计算公式**

$$		
Similarity =（1 - \alpha）\cdot \text{Cosine} + \alpha \cdot （1 \div{(\text{Euclidean} + 1)})
$$

<sub> NOTES: 该优化更注重的是精确度，可能会在计算开销上有所损失</sub>

<div align = "center">

#How To Use

</div>
关于如何使用该项目进行优化开发

<details>
<summary>Deafalt</summary>
使用默认的算法完成

```bash
$ python main.py --orig-path your_path --orig-add-path your_path --output your_path
```
</details>

<details>
<summary>Cosine</summary>
使用余弦距离算法完成

```bash
$ python main.py --orig-path your_path --orig-add-path your_path --output your_path --check-method cosine
```
</details>

<details>
<summary>Jaccard</summary>
使用Jaccard算法完成

```bash
$ python main.py --orig-path your_path --orig-add-path your_path --output your_path --check-method jaccard
```
</details>

<details>
<summary>Levenshtein</summary>
使用Levenshtein算法完成

```bash
$ python main.py --orig-path your_path --orig-add-path your_path --output your_path --check-method levenshtein
```
</details>

<details>
<summary>Minhash</summary>
使用Minhash算法完成

```bash
$ python main.py --orig-path your_path --orig-add-path your_path --output your_path --check-method minhash
```
</details>

<details>
<summary>Simhash</summary>
使用Minhash算法完成

```bash
$ python main.py --orig-path your_path --orig-add-path your_path --output your_path --check-method simhash
```
</details>

<details>
<summary>Custom</summary>
使用自定义算法完成

```bash
$ python main.py --orig-path your_path --orig-add-path your_path --output your_path --check-method custom
```
</details>


<div align="center">

#程序流程

<img src="https://img2023.cnblogs.com/blog/3273612/202309/3273612-20230923200522054-1838019642.png" width="30%">

</div>


<div align="center">

#异常处理

</div>

<details>
<summary>文件地址输入异常</summary>

```python
try:
  ...
except FileNotFoundError as e:
  print(f"文件未找到:{e.filename}")
except IOError as e:
  print(f"文件读写错误:{e}")
except Exception as e:
  print(f"发生未知错误:{e}") 
```

</details>

<details>
<summary>除零异常</summary>

```python
try:
  sim = cosine_similarity(sample)
  return sim[1][0]
except Exception as e:
  print(e)
  return 0.0
```

</details>

<div align="center">

#性能分析

</div>

<div align="center">

<img src="https://img2023.cnblogs.com/blog/3273612/202309/3273612-20230923194325855-1821398884.png" width="60%">
<sub> NOTES: 主要时间开销在于numpy向量计算，可从该方面入手优化</sub>


# PSP 表格记录

</div>

|                PSP2.1                 | Personal Software Process Stages | 预估耗时（min） | 实际耗时（min） |
| :-----------------------------------: | :------------------------------: | :-------------: | :-------------: |
|               Planning                |               计划               |       10        |        5        |
|               Estimate                |     估计这个任务需要多少时间     |        5        |        5        |
|              Development              |               开发               |       10        |       10        |
|               Analysis                |    需求分析 (包括学习新技术)     |        5        |        5        |
|              Design Spec              |           生成设计文档           |        5        |        3        |
|             Design Review             |             设计复审             |       10        |        2        |
|            Coding Standard            |             代码规范             |        5        |        5        |
|                Design                 |             具体设计             |        5        |        5        |
|                Coding                 |             具体编码             |       10        |        8        |
|              Code Review              |             代码复审             |        5        |        5        |
|                 Test                  |               测试               |        5        |        5        |
|               Reporting               |               报告               |       10        |       10        |
|              Test Repor               |             测试报告             |        5        |        5        |
|           Size Measurement            |            计算工作量            |        5        |        5        |
| Postmortem & Process Improvement Plan |   事后总结, 并提出过程改进计划   |        5        |        5        |
|                                       |               合计               |       95        |       80        |
