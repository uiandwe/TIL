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
    print(rdd3.collect()) # [('a', 2), ('b', 2), ('c', 2)]

    rdd1 = sc.parallelize([(1, "a,b"), (2, "b,c"), (3, "a,c")])
    # key, value 면서 리턴값이 다를때 사용
    rdd2 = rdd1.flatMapValues(lambda s: s.split(","))
    print(rdd2.collect()) # [(1, 'a'), (1, 'b'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'c')]

    ###### zip 연산들( 두개 이상의  RDD를 하나로 )

    rdd1 = sc.parallelize(["a", "b", "c"])
    rdd2 = sc.parallelize([1, 2, 3])
    # 서로 갯수가 맞지 않으면 에러
    result = rdd1.zip(rdd2)
    print(result.collect()) #[('a', 1), ('b', 2), ('c', 3)]

    rdd1 = sc.parallelize(range(1, 11))
    # 특정 그룹으로 지정
    rdd2 = rdd1.groupBy(lambda v: "even" if v % 2 == 0 else "odd")
    for x in rdd2.collect():
        print(x[0], list(x[1]))
    # ('even', [2, 4, 6, 8, 10])
    # ('odd', [1, 3, 5, 7, 9])

    rdd1 = sc.parallelize(["a", "b", "c", "b", "c"])
    rdd1 = rdd1.map(lambda v: (v, 1))
    # key, value 일때만
    rdd2 = rdd1.groupByKey()
    for x in rdd2.collect():
        print(x[0], list(x[1]))
    # ('c', [1, 1])
    # ('b', [1, 1])
    # ('a', [1])

    rdd1 = sc.parallelize([("k1", "v1"), ("k1", "v3"), ("k2", "v2")])
    rdd2 = sc.parallelize([("k1", "v4")])
    # col 합치기
    result = rdd1.cogroup(rdd2)
    for x in result.collect():
        print(x[0])
        for y in x[1]:
            print(list(y))

    ###### 집합과 관련된 연산들

    rdd1 = sc.parallelize([1, 2, 3, 123, 123, 123, 123, 123, 1, 2, 3, 1, 2, 3])
    result = rdd1.distinct()
    print(result.collect()) #[1, 2, 123, 3]

    rdd1 = sc.parallelize([1, 2, 3])
    rdd2 = sc.parallelize(["a", "b", "c"])
    # 두 rdd의 모든 경우의 수
    result = rdd1.cartesian(rdd2)
    print(result.collect()) # [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

    rdd1 = sc.parallelize(["a", "b", "c", "d", "e"])
    rdd2 = sc.parallelize(["d", "e"])
    # 빼기
    result = rdd1.subtract(rdd2)
    print(result.collect()) # ['c', 'a', 'b']

    rdd1 = sc.parallelize(["a", "b", "c", "d", "e"])
    rdd2 = sc.parallelize(["f", "g", "a"])
    # 합치기 (중복됨)
    result = rdd1.union(rdd2)
    print(result.collect()) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a']

    rdd1 = sc.parallelize(["a", "b", "c", "d", "e"])
    rdd2 = sc.parallelize(["f", "g", "a"])
    # 공통의 것만 리턴
    result = rdd1.intersection(rdd2)
    print(result.collect()) # ['a']

    rdd1 = sc.parallelize(["a", "b", "c", "d", "e"]).map(lambda v: (v, 1))
    rdd2 = sc.parallelize(["b", "c"]).map(lambda v: (v, 2))
    # 공통의 것들의 value값들을 리턴
    result = rdd1.join(rdd2)
    print(result.collect()) # [('c', (1, 2)), ('b', (1, 2))]

    rdd1 = sc.parallelize(["a", "b", "c"]).map(lambda v: (v, 1))
    rdd2 = sc.parallelize(["b", "c"]).map(lambda v: (v, 2))

    result = rdd1.leftOuterJoin(rdd2)
    print("leftOuterJoin", result.collect()) # ('leftOuterJoin', [('c', (1, 2)), ('a', (1, None)), ('b', (1, 2))])
    result = rdd1.rightOuterJoin(rdd2)
    print("rightOuterJoin", result.collect()) # ('rightOuterJoin', [('c', (1, 2)), ('b', (1, 2))])

    rdd1 = sc.parallelize(["a", "b", "c"]).map(lambda v: (v, 1))
    rdd2 = sc.parallelize(["b", "c"]).map(lambda v: (v, 2))
    # 키가 같은것은 제외
    result = rdd1.subtractByKey(rdd2)
    print(result.collect()) # [('a', 1)]

    ###### 집계 관련 함수
    rdd = sc.parallelize(["a", "b", "b"]).map(lambda v: (v, 1))
    # 공통된 키 값을 하나로 하면서 value값을 더해서 리턴하고 싶을때 (공통된 애들의 value 값을 모두 더하고 싶을때)
    result = rdd.reduceByKey(lambda v1, v2: v1+v2)
    print(result.collect()) # [('b', 2), ('a', 1)]

    
    

    sc.stop()
