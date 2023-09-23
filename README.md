<div align="center">
  
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

## How To Use

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

