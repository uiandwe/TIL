# -*- coding: utf-8 -*-
from pyspark import SparkContext, SparkConf


if __name__ == '__main__':
    conf = SparkConf()
    sc = SparkContext(master="local[*]", appName="RDDOpSample", conf=conf)

    rdd = sc.parallelize(range(1, 11))
    # 전체 갯수를 리스트로 만들기 때문에 충분한 메모리 필요(잘못사용하면 서버 터짐)
    result = rdd.collect()
    print(result)

    result = rdd.count()
    print(result)

