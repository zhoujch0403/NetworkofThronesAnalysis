# 权利的游戏人物关系的复杂网络分析

## 数据来源

* [NETWORK OF THRONES | A Song of Math and Westeros](https://networkofthrones.wordpress.com/)

* [Network Data for the Books](https://github.com/mathbeveridge/asoiaf)

* [Network Data for the Series](https://github.com/mathbeveridge/gameofthrones)

## 说明
### NoteBook
* `demo3.ipynb`：分析权游第三季人物关系
* `demo.ipynb`：全季人物复杂网络分析

### Script
* `preprocessing.py`：处理**Network Data for the Series**数据集中`edge.csv`文件，删除季的字段，合并八个数据文件为一个（即整个电视剧的人物同时登场次数）
* `demo3.py`：对应`demo3.ipynb`的脚本，但是保存分析结果图

### Data
* `gameofthrones/data_processed`：`preprocessing.py`处理结果