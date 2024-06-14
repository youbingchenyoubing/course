# 课程说明

## Python 编程从入门到提高

参考:

[清华大学出版社《Python 编程从入门到提高》源代码及课件](https://github.com/hitlic/python_book)

## Python 数据分析

参考:

[Python for Data Analysis, 3rd Edition 代码课件](https://github.com/wesm/pydata-book)

[第二版中文](https://seancheney.gitbook.io/python-for-data-analysis-2nd)

## 机器学习

## 深度学习

## transformer(智能化学习)

> Transformers 是由 Hugging Face 开发的一个 NLP 包，支持加载目前绝大部分的预训练模型。随着 BERT、GPT 等大规模语言模型的兴起，越来越多的公司和研究者采用 Transformers 库来构建 NLP 应用。当然不止 NLP，Transformers 也支持其他领域的预训练模型，如图像、音频、文本生成等。

参考:

[huggingface](https://huggingface.co/docs/transformers/v4.38.2/zh/pipeline_tutorial)

[对应的 B 站视频的源码](https://github.com/zyds/transformers-code/)

[对应的 B 站视频](https://www.bilibili.com/video/BV1ta4y1g7bq/?spm_id_from=333.788&vd_source=3d47766182d08faadaa31d1333050507)

[transfomer 快速入门](https://transformers.run/)

## 练习
+ 基础编程题: http://ybt.ssoier.cn:8088/, https://www.luogu.com.cn/, https://leetcode.com/
+ 数据分析numpy刷题: https://developer.aliyun.com/article/1107871, https://www.heywhale.com/mw/project/59f29f67c5f3f5119527a2cc
+ 数据分析实战: https://github.com/jackfrued/Python-100-Days/blob/master/Day66-80/66.%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%A6%82%E8%BF%B0.md

# 公众号

![程序猿阿三](imgs/getqrcode.png)

## 内容

- 源代码
  - `codes`
- 课件：Jupyter notebook 格式的幻灯片
  - `notebook_slides`

## 课件使用

详细说明参见`notebook_slides/课件使用说明.md`。

### 仅使用 Notebook 显示

- 安装 Jupyter 和 autopep8
  - 使用 pip：`pip install jupyter==6.4.8`
  - 使用 conda：`conda install jupyter==6.4.8 autopep8`
- 为了配置方便，建议安装 Jupyter Nbextensions Configurator
  - 使用 pip
    - `pip install jupyter_nbextensions_configurator==0.4.1`
    - `jupyter nbextensions_configurator enable --user`
  - **使用 conda**
    - `conda install -c conda-forge jupyter_nbextensions_configurator==0.4.1`
- 运行 jupyter notebook
  - 在终端进入课件所在目录
  - 运行命令`jupyter notebook .`即可
- 使用 jupyter lab 也可以
  参考: https://cloud.tencent.com/developer/article/1918314 安装 ,有些插件也可以使用https://cloud.tencent.com/developer/article/1971947
  https://www.zhihu.com/tardis/zm/art/101070029?source_id=1003

### 使用幻灯片显示

- 安装 Jupyter 和 autopep8

  - 使用 pip：`pip install jupyter==6.4.8`
  - 使用 conda：`conda install jupyter==6.4.8`

- 安装 RISE 插件

  - 使用 pip：`pip install RISE`

  - 使用 conda：`conda install -c conda-forge rise`

- 为了配置方便，建议安装 Jupyter Nbextensions Configurator

  - 使用 pip
    - `pip install jupyter_nbextensions_configurator==0.4.1`
    - `jupyter nbextensions_configurator enable --user`
  - **使用 conda**
    - `conda install -c conda-forge jupyter_nbextensions_configurator==0.4.1`

- 运行 jupyter notebook

  - 在终端进入课件所在目录
  - 运行命令`jupyter notebook .`

- 在弹出的浏览器中选择一个课件打开，点击下图所示的图标即可以幻灯片形式显示

### git 大文件管理

https://help.aliyun.com/document_detail/206889.html
以及管理 目录

### 课后练习题
编程网站
+ 入门: https://ti.luogu.com.cn/problemset/
+ 入门: 