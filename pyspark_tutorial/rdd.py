from pyspark.sql import SparkSession
import os 
import array
# import psutil
# print(psutil.__version__)
# import sys
# print(sys.path)

spark = SparkSession.builder.appName("Explaespark.com").getOrCreate()

print (spark)

rdd = spark.sparkContext.textFile(os.getcwd()+"/input.txt")

for element in rdd.collect():
    print (element)
    
rdd1 = rdd.flatMap(lambda x : x.split(" "))
print (rdd1)
for element in rdd1.collect():
    print (element)
    
rdd2 = rdd1.map(lambda x : (x,1))
for element in rdd2.collect():
    print (element)    
    
rdd3 = rdd2.reduceByKey(lambda a,b : a+b) 
for element in rdd3.collect():
    print (element)
    
rdd4 = rdd3.map(lambda x: (x[1],x[0])).sortByKey()     
for element in rdd4.collect():
    print (element) 
    
rdd5 = rdd4.filter(lambda x : 'm' in x[1])
for element in rdd5.collect():
    print("filtered:",element)     
    
    
#ACTIONS

#spark1 = SparkSession.builder.appName("spark_actions.com").getOrCreate()

data = [("z", 2), ("f", 4), ("B", 23), ("C", 89), ("G", 90), ("W", 12),  ("W", 12)]

inputrdd = spark.sparkContext.parallelize(data)

listrdd = spark.sparkContext.parallelize([1,2,3,4,5,6,7,7])

seq0p = (lambda x,y : x+y)
com0p = (lambda x,y : x+y)

agg = listrdd.aggregate(0, seqOp=seq0p, combOp=com0p)
print ("aggregate:", agg)

treeagg = listrdd.treeAggregate(0, seqOp=seq0p, combOp=com0p)
print ("treeagg:", treeagg)

from operator import add

foldres = listrdd.fold(0, add)
print ("fold", foldres)

print ("count:", str(listrdd.count()))

print("countApprox : "+str(listrdd.countApprox(1200)))
print("countApproxDistinct : "+str(inputrdd.countApproxDistinct()))

print ("countbyvalue:", listrdd.countByValue())

print ("first:", listrdd.first())

print("top : "+str(listrdd.top(2)))
print("min : "+str(listrdd.min()))

print("max : "+str(listrdd.max()))

print ("take:", listrdd.take(3))
print ("takeordered:", listrdd.takeOrdered(2))

print ("takesample:", listrdd.takeSample(1,2))


# Create DataFrame
data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]

df = spark.createDataFrame(data=data, schema=columns)
df.printSchema()
df.show()


# Create spark session with local[5]
rdd = spark.sparkContext.parallelize(range(0,20))
print("From local[5] : "+str(rdd.getNumPartitions()))


# Use parallelize with 6 partitions
rdd1 = spark.sparkContext.parallelize(range(0,25), 6)
#redistributes (increase or decrease partitions) data evenly across a specified number of partitions
rdd2 = rdd1.repartition(9)
print("parallelize : "+str(rdd2.getNumPartitions()))

#used only to decrease the number of partitions
rdd2 = rdd1.coalesce(2)
print("parallelize coalesce : "+str(rdd2.getNumPartitions()))

broadcast = spark.sparkContext.broadcast(array.array('i', [12,1,2,3,4,5,6]))
print (broadcast.value)

states = {"NY":"New York", "CA":"California", "FL":"Florida"}

broadcastStates = spark.sparkContext.broadcast(states)
print (broadcastStates.value)

data = [("James","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL")
  ]

rdd = spark.sparkContext.parallelize(data)
def state_conversion(code):
    return broadcastStates.value[code]

result = rdd.map(lambda x : (x[0],x[1],x[2], state_conversion(x[3]))).collect()
print (result)

rdd1 = spark.sparkContext.parallelize([12,3,4,5,5,4,3,44])

accum = spark.sparkContext.accumulator(0)
rdd1.foreach(lambda x : accum.add(x))
print ("addition:", accum.value)

accum = spark.sparkContext.accumulator(0)
rdd1.foreach(lambda x : accum.add(1))
print ("accum_count:", accum.value)

#Creates Empty RDD using parallelize
rdd1 = spark.sparkContext.parallelize([])

#Creates Empty RDD
emptyRDD = spark.sparkContext.emptyRDD()
print (type(emptyRDD))

data = [("Saayan", "Das")]
#Create Empty DataFrame with Schema (StructType)

from pyspark.sql.types import StructField, StructType, StringType
schema = StructType([
    StructField("first_name", StringType(), True),
    StructField("Last_name", StringType(), True)
])

df = spark.createDataFrame(schema=schema, data=data)
df.printSchema()
df.show(truncate=False)

df.select(df.first_name).show()

#using col function
from pyspark.sql.functions import col, lit

df.select(col("last_name")).show()
#Convert Spark Nested Struct DataFrame to Pandas
pandasdf = df.toPandas()
print (pandasdf)

#create dataframe using row 
from pyspark.sql import Row

data = [Row(name="James", prop=Row(hair="black", eye="blue")),
        Row(name="Ann", prop=Row(hair="brown", eye="black"))]

df = spark.createDataFrame(data)
df.printSchema()
df.show()

df.select(col("name")).show()
df.select(df["prop.hair"]).show()
df.select(col("prop.*")).show()

from pyspark.sql.functions import expr

data=[("James","Bond","100",None),
      ("Ann","Varsa","200",'F'),
      ("Tom Cruise","XXX","400",''),
      ("Tom Brand",None,"400",'M')] 
columns=["fname","lname","id","gender"]
df=spark.createDataFrame(data,columns)

df.select(df.fname.alias("first_name"),\
          df.lname.alias("last_name")
          ).show()

df.select(expr(" fname ||', '|| lname").alias("fulname") \
          ).show()

#contains
df.filter(df.fname.contains("Cruise")).show()

#startswith, endswith()
df.filter(df.fname.startswith("T")).show()
df.filter(df.fname.endswith("Cruise")).show()
#isNull & isNotNull
df.filter(df.lname.isNull()).show()
df.filter(df.lname.isNotNull()).show()
#like , rlike
df.select(df.fname,df.lname,df.id) \
  .filter(df.fname.like("%om"))
  
data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.printSchema()
df.show(truncate=False)

df2 = df.withColumn("salary", col("salary").cast("Integer"))
df2.printSchema()
df2.show(truncate=False)

df3 = df.withColumn("salary", col("salary")*1000)
df3.printSchema()
df3.show(truncate=False)

df4 = df.withColumn("CopiedColumn", col("salary")* -1)
df4.printSchema()
df4.show(truncate=False)

df5 = df.withColumn("Country", lit("USA"))
df5.printSchema()
df5.show(truncate=False)

df6 = df.withColumn("Country", lit("USA")) \
    .withColumn("anotherColumn", lit("anotheValue"))
df6.printSchema()
df6.show(truncate=False)

df = df.withColumnRenamed("gender", "Sex")
df.printSchema()
df.show(truncate=False)

df6 = df6.drop("anotherColumn")
df6.printSchema()
df6.show(truncate=False)

