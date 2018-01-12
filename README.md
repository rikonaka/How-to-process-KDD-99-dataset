# How-to-process-KDD-99-dataset
Use Introduction

### Other undecided authors go round the curve
you can insert the dataset into database like mysql or sqlite3, but I do not recommend doing this

## I will replace the KDD-99 data string as a value

The original data is like this

```
0,tcp,http,SF,181,5450,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,8,8,0.00,0.00,0.00,0.00,1.00,0.00,0.00,9,9,1.00,0.00,0.11,0.00,0.00,0.00,0.00,0.00,normal.
```

And we could replace string at the 2, 3, 4 position and the result will like this

```
0,1,22,10,181,5450,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,8,8,0.00,0.00,0.00,0.00,1.00,0.00,0.00,9,9,1.00,0.00,0.11,0.00,0.00,0.00,0.00,0.00,normal.
```

and if we do this, the accuracy of clustering will be `improved`

when i use the initial data without replace the string as a value, the accuracy of clustering is `97.79%`

and i use the data which replace the string as a value, the accuracy of clustering is `98.47%`

This confirms that the accuracy of clustering can be improved with this method

The replacement method we used is simple, like this
```
#example TCP->1
#example UDP->2
#example ICMP->3
```
and then
```
#example aol->1
#example Z39_50->70
```
and then
```
#example OTH->1
#example SH->11
```

---

### At the beginning of the time

You should make sure that place KDD dataset and programs `replace_string_to_value.py` in the same directory

and then open the programs with IDE

<del>add you file name in `You_file_path' at the beginning</del>
input you file path and name while the program runing

and the run the programs

## next we will use the Spark to clusering the data

We use the `KDD_pyspark.py`

I strongly recommend that you set the max_k value should not be too large

and if you do that
### the later processing will take a lot of time

So, you can try mak_k as `10` or `30`

Unless you have sufficient time and computing resources, it is not recommended do set the max_k value to 60, or 120.

and if you run the programs named `KDD_pyspark.py`, it will two directories are generated in the mian directory of the Spark

* The sample_standardized directory under the file named `re0`, `re1`, `re2`
* And the labels directory under the file named `la0`, `la1`, `la2`
* It must be name d in the order

## Now put them all in another directory

You can names this directory as `Text` or `Workstation`

put the programs `merge_show.py` into `Text` or `Workstation` directory

also put the `re0` to `rex`, and `la0` to `lax`

and run the `merge_show.py`

### It will be a long process...
### Next do
* Watch a movie that you want to see for a long time
* Play some funny things with you family
* Learn a new programs language
* ....

if you finish merge all the data 

## Let's move on to the next step

put the `statistical_result.py` in the directory
run the programs and out put the result

##That's all

* if you have any question with this introduce, send me a email super_big_hero@sina.com
* see you
* 具体实现细节可参考我前年的论文(这里有一份,信息安全学报2016-7月刊第一篇也是) (2018-1-12)
