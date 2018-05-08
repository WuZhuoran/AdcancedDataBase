# AdvancedDataBase
Project for COSC 580 Advanced Databases Spring 2018. Build R-tree and KNN search on Restaurant Data.

## Get Start

```bash
git clone git@github.com:WuZhuoran/AdvancedDataBase.git
cd AdvancedDataBase
```

### Install Requirement
```bash
pip install -r requirement.txt
```

### Run Experiment
```bash
cd src
python performance_naive.py
cd python_rtree
python rtree_nn_test.py

```

### Run Website
```bash
cd src/flask
python app.py
```
Then Please check [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Report

The [final report](https://github.com/WuZhuoran/AdvancedDataBase/blob/master/report/Zhuoran%20Wu%20-%20Advanced%20Database%20Report.pdf) is in the report folder. 

## Author

[Zhuoran Wu](@WuZhuoran)    
Master Student    
Department of Computer Science    
Georgetown University    
<[zw118@georgetown.edu](mailto:zw118@georgetown.edu)>

## Acknowledge

Thanks [Wenchao Zhou]() as instructor for COSC 580 Advanced Databased Spring 2018.

Thanks [Yuankai Zhang]() as TA for courses.

## Reference

[1] Jens Even Berg Blomsøy, Evaluating Algorithms for Nearest Neighbor Searches in Spatial Databases Using R-Trees, Norwegian University of Science and Technology, June 2017.

[2] A. Guttman, “R-trees: a dynamic index structure for spatial searching,” in SIGMOD, 1984.

[3] Nasrin Mazaheri Soudani et al., The spatial nearest neighbor skyline queries, International Journal of Database Management Systems ( IJDMS ) Vol.3, No.4, November 2011.

[4] Jun Zhang, N. Mamoulis, D. Papadias and Yufei Tao, "All-nearest-neighbors queries in spatial databases," Proceedings. 16th International Conference on Scientific and Statistical Database Management, 2004., 2004, pp. 297-306.

[5] Yufei Tao, Aggregate Nearest Neighbor Queries in Spatial Databases, ACM Transactions on Database Systems, Vol. 30, No. 2, June 2005, Pages 529–576.

[6] Jiaheng Lu et al., Reverse Spatial and Textual k Nearest Neighbor Search, Proceeding SIGMOD '11 Proceedings of the 2011 ACM SIGMOD International Conference on Management of data Pages 349-360.

[7] Hideki Satoa, Ryoichi Narita, Efficient Maximum Range Search on Remote Spatial Databases Using k-Nearest Neighbor Queries, Procedia Computer Science, Volume 22, 2013, Pages 836-845.

[8] M. L. Yiu, X. Dai, N. Mamoulis, and M. Vaitis, "Top-k Spatial Preference Queries," Proceedings of the 23rd International Conference on Data Engineering (ICDE), Instanbul, Turkey, April 2007.

[9] Mehdi Sharifzadeh and Cyrus Shahabi. 2010. VoR-tree: R-trees with Voronoi diagrams for efficient processing of spatial nearest neighbor queries. Proc. VLDB Endow. 3, 1-2 (September 2010), 1231-1242.

[10] A. Corral, Y. Manolopoulos, Y. Theodoridis, and M. Vassilakopoulos. 2004. Algorithms for processing K-closest-pair queries in spatial databases. Data Knowl. Eng. 49, 1 (April 2004), 67-104.