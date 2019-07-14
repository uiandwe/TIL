# -*- coding: utf-8 -*-
from pyspark import SparkContext, SparkConf


def increase(numbers):
    print("db 연결!!")
    return (i + 1 for i in numbers)


# MapPartitionsWithIndex
def increaseWithIndex(idx, numbers):
    for i in numbers:
        if (idx == 1):
            yield i


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

    ###### rdd 의 map 연산들 ####

    rdd1 = sc.parallelize(["apple,orange", "grape,apple,mango", "blueberry,tomato,orange"])
    # in / out 데이터형식이 다를때
    rdd2 = rdd1.flatMap(lambda s : s.split(","))
    print(rdd2.collect())

    rdd1 = sc.parallelize(range(1, 11), 3)
    # 각 파티션별로 동작 (ex: 파티션별 디비 연결이나, 공유 데이터로 활용)
    rdd2 = rdd1.mapPartitions(increase)
    print("mapPartitions")
    print(rdd2.collect())

    rdd1 = sc.parallelize(range(1, 11), 3)
    rdd2 = rdd1.mapPartitionsWithIndex(increaseWithIndex)
    print("mapPartitionsWithIndex")
    print(rdd2.collect())

    rdd1 = sc.parallelize(["a", "b", "c"])
    rdd2 = rdd1.map(lambda v : (v, 1))
    # rdd가 key, value 일때만 사용 가능, 키는 변경 불가
    rdd3 = rdd2.mapValues(lambda i: i+1)
    print(rdd3.collect())

    rdd1 = sc.parallelize([(1, "a,b"), (2, "b,c"), (3, "a,c")])
    # key, value 면서 리턴값이 다를때 사용
    rdd2 = rdd1.flatMapValues(lambda s: s.split(","))
    print(rdd2.collect())

    ###### zip 연산들( 두개 이상의  RDD를 하나로 )

    rdd1 = sc.parallelize(["a", "b", "c"])
    rdd2 = sc.parallelize([1, 2, 3])
    # 서로 갯수가 맞지 않으면 에러
    result = rdd1.zip(rdd2)
    print(result.collect())

    rdd1 = sc.parallelize(range(1, 11))
    # 특정 그룹으로 지정
    rdd2 = rdd1.groupBy(lambda v: "even" if v % 2 == 0 else "odd")
    for x in rdd2.collect():
        print(x[0], list(x[1]))

    rdd1 = sc.parallelize(["a", "b", "c", "b", "c"])
    rdd1 = rdd1.map(lambda v: (v, 1))
    # key, value 일때만
    rdd2 = rdd1.groupByKey()
    for x in rdd2.collect():
        print(x[0], list(x[1]))

    rdd1 = sc.parallelize([("k1", "v1"), ("k1", "v3"), ("k2", "v2")])
    rdd2 = sc.parallelize([("k1", "v4")])
    # col 합치기
    result = rdd1.cogroup(rdd2)
    for x in result.collect():
        print(x[0])
        for y in x[1]:
            print(list(y))

    ### 집합과 관련된 연산들 










    sc.stop()
