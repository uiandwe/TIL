# -*- coding: utf-8 -*-

from pyspark import SparkContext, SparkConf

if __name__ == '__main__':
    conf = SparkConf()
    sc = SparkContext(master="local[*]", appName="RDDOpSample", conf=conf)

    # 잡이 실행될 동안의 전역 변수
    bu = sc.broadcast(set(["u1", "u2"]))
    rdd = sc.parallelize(["u1", "u2", "u3", "u4", "u5"], 3)
    result = rdd.filter(lambda v: v in bu.value)
    print(result.collect())

    
    def accumulate(v, acc):
        if(len(v.split(":")) != 2):
            acc.add(1)

    acc1 = sc.accumulator(0)
    data = ["U1:Addr1", "U2:Add2", "U3", "U4:Add4", "U5;Add5", "U6:Add6", "U7::Add7"]
    rdd = sc.parallelize(data)
    rdd.foreach(lambda v: accumulate(v, acc1))
    print(acc1.value)

    sc.stop()
