from pyspark import SparkContext
sc = SparkContext()

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

df= sqlContext.read.json('people.json')

type(df)

#pyspark.sql.dataframe.DataFrame

df.collect()

 #     [Row(age=None, name='Michael'),
 #     Row(age=30, name='Andy'),
 #     Row(age=19, name='Justin')]

df.show()

    # +----+-------+
    # | age|   name|
    # +----+-------+
    # |null|Michael|
    # |  30|   Andy|
    # |  19| Justin|
    # +----+-------+
    

