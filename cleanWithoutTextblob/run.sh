hadoop fs -rm -r -f dataExtract/output

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input hdfs://quickstart.cloudera:8020/user/cloudera/dataExtract/input/ \
-output dataExtract/output \

