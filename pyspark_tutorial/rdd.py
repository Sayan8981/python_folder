from pyspark.sql import SparkSession
import os 

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
    
rdd5 = rdd2.filter(lambda x : 'i' in x[1])
for element in rdd5.collect():
    print(element)     