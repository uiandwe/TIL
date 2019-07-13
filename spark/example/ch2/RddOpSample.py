# -*- coding: utf-8 -*-
from pyspark import SparkContext, SparkConf


def increase(numbers):
    print("db 연결!!")
    return (i + 1 for i in numbers)


if __name__ == '__main__':
    conf = SparkConf()
    sc = SparkContext(master="local[*]", appName="RDDOpSample", conf=conf)

    rdd = sc.parallelize(range(1, 11))
    # 전체 갯수를 리스트로 만들기 때문에 충분한 메모리 필요(잘못사용하면 서버 터짐)
    result = rdd.collect()
    print(result)

    result = rdd.count()
    print(result)

    rdd2 = rdd.map(lambda v : v + 1)
    print(rdd2.collect())

    rdd1 = sc.parallelize(["apple,orange", "grape,apple,mango", "blueberry,tomato,orange"])
    # in / out 데이터형식이 다를때 
    rdd2 = rdd1.flatMap(lambda s : s.split(","))
    print(rdd2.collect())

    rdd1 = sc.parallelize(range(1, 11))
    # 각 파티션별로 동작 (ex: 파티션별 디비 연결이나, 공유 데이터로 활용)
    rdd2 = rdd1.mapPartitions(increase)
    print(rdd2.collect())
