from pyspark.sql import SparkSession
import os 
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