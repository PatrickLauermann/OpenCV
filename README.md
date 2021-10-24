# Brief Introduce:



###### Before you use this demo, check whether you have done the following things:

1、python

2、opencv

3、add opencv to your environment variable



if you not done,please...

I suggest you create a new virtual space created by conda:

```
conda update --all
conda install --channel https://conda.anaconda.org/menpo opencv
```

this only download the cv2 for your python(but you should do), you will additional download the source code:

```
https://blog.csdn.net/maizousidemao/article/details/81474834?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163479705916780261970635%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=163479705916780261970635&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~hot_rank-2-81474834.first_rank_v2_pc_rank_v29&utm_term=python+opencv%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F&spm=1018.2226.3001.4187
```



## All Right,let's start



1、You can save the origin data in file "origin_data"

2、Put the negative picture in the file "negative"

3、Put the positive picture in the file "positive"

4、Put the Test picture in the file "Test"

5、 file "treinamento" is the model created by opencv, whenever you decide to re-train, clean it



analiseTreinamento.py used to test one picture

analiseTreinametoVideo.py used to use your camera to recognize timly

buildListNegative.py used to creat negative.exe, run it after you put the negative picture to file

info.txt created by command, it will be touched in the later

renameFiles.py used to rename the img you saved in "negative", "positive" and 'Test'

vectire.vec created by command, it will be touched soon



open cmd,then 

cd your path such as C:\Users\xxxxx\Desktop\OpenCV\Road_Block_Recognition

```
C:\Users\86158\Desktop\OpenCV\Road_Block_Recognition
```

enter by order:

```
opencv_annotation --annotations=info.txt --images=positive/
opencv_createsamples -info info.txt -vec vector.vec -w 30 -h 30
opencv_traincascade -data model -vec vector.vec -bg negative.txt -numPos 30 -numNeg 200 -w 30 -h 30 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages 30 -acceptanceRatioBreakValue 1.0e-5
```



then everything is ok. You'd better read the reference to learn more about how to use it

```
https://www.cnblogs.com/xixixing/p/12308605.html
https://github.com/PatrickLauermann/OpenCV
https://zhuanlan.zhihu.com/p/340640174
```

 

## About how to choose parameter

```
https://blog.csdn.net/u014587123/article/details/78507649
```



