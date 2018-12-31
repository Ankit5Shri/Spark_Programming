

```python
from pyspark import SparkContext
sc = SparkContext()
```


```python
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
```


```python
df= sqlContext.read.json('people.json')
```


```python
type(df)
```




    pyspark.sql.dataframe.DataFrame




```python
df.collect()
```




    [Row(age=None, name='Michael'),
     Row(age=30, name='Andy'),
     Row(age=19, name='Justin')]




```python
df.show()
```

    +----+-------+
    | age|   name|
    +----+-------+
    |null|Michael|
    |  30|   Andy|
    |  19| Justin|
    +----+-------+
    



```python

```
