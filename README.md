# How-to-process-KDD-99-dataset
Use Introduction

### Some people choose be different from others
you can insert the dataset into DataBase,and find a new road to Rome,but I didn't choose this road

## I will replace the KDD-99 data string as a value

Initial data is like this
```
0,tcp,http,SF,181,5450,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,8,8,0.00,0.00,0.00,0.00,1.00,0.00,0.00,9,9,1.00,0.00,0.11,0.00,0.00,0.00,0.00,0.00,normal.
```
and we can replace string at the 2, 3, 4 position and the result is like this
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
	#example #SH->11
```
### At the beginning of the time
You should make sure that place KDD dataset and programs in the same directory

and then open the programs with IDE

add you file name in `You_file_path' at the beginning

and the run the programs
