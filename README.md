# Python编程从入门到提高
参考清华大学出版社《Python编程从入门到提高》源代码及课件: https://github.com/hitlic/python_book

# Python数据分析
参考:Python for Data Analysis, 3rd Edition  代码课件:https://github.com/wesm/pydata-book
第二版中文:https://seancheney.gitbook.io/python-for-data-analysis-2nd

# transformer
参考 https://huggingface.co/docs/transformers/v4.38.2/zh/pipeline_tutorial
https://github.com/zyds/transformers-code/
https://www.bilibili.com/video/BV1ta4y1g7bq/?spm_id_from=333.788&vd_source=3d47766182d08faadaa31d1333050507
https://transformers.run/intro/2021-12-08-transformers-note-1/#%E8%BF%99%E4%BA%9B-pipeline-%E8%83%8C%E5%90%8E%E5%81%9A%E4%BA%86%E4%BB%80%E4%B9%88

## 内容

- 源代码
  - `codes`
- 课件：Jupyter notebook格式的幻灯片
  - `notebook_slides`

## 课件使用

详细说明参见`notebook_slides/课件使用说明.md`。

### 仅使用Notebook显示

- 安装Jupyter和autopep8
  - 使用pip：`pip install jupyter==6.4.8`
  - 使用conda：`conda install jupyter==6.4.8 autopep8`
- 为了配置方便，建议安装Jupyter Nbextensions Configurator
  - 使用pip
    - `pip install jupyter_nbextensions_configurator==0.4.1`
    - `jupyter nbextensions_configurator enable --user`
  - __使用conda__
    - `conda install -c conda-forge jupyter_nbextensions_configurator==0.4.1`
- 运行jupyter notebook
  - 在终端进入课件所在目录
  - 运行命令`jupyter notebook .`即可
- 使用jupyter lab也可以
  参考: https://cloud.tencent.com/developer/article/1918314 安装 ,有些插件也可以使用https://cloud.tencent.com/developer/article/1971947
  https://www.zhihu.com/tardis/zm/art/101070029?source_id=1003
### 使用幻灯片显示

- 安装Jupyter和autopep8
  - 使用pip：`pip install jupyter==6.4.8`
  - 使用conda：`conda install jupyter==6.4.8`

- 安装RISE插件
  - 使用pip：`pip install RISE`

  - 使用conda：`conda install -c conda-forge rise`
  
- 为了配置方便，建议安装Jupyter Nbextensions Configurator
  - 使用pip
    - `pip install jupyter_nbextensions_configurator==0.4.1`
    - `jupyter nbextensions_configurator enable --user`
  - __使用conda__
    - `conda install -c conda-forge jupyter_nbextensions_configurator==0.4.1`

- 运行jupyter notebook

  - 在终端进入课件所在目录
  - 运行命令`jupyter notebook .`

- 在弹出的浏览器中选择一个课件打开，点击下图所示的图标即可以幻灯片形式显示

### git 大文件管理

https://help.aliyun.com/document_detail/206889.html
以及管理 目录

