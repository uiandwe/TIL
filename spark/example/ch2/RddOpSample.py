# -*- coding: utf-8 -*-
from pyspark import SparkContext, SparkConf
import random

def increase(numbers):
    print("db 연결!!")
    return (i + 1 for i in numbers)


# MapPartitionsWithIndex
def increaseWithIndex(idx, numbers):
    for i in numbers:
        if (idx == 1):
            yield i

def test1(l):
    print(l)

def sideEffect(values):
    print("Partition Side Effect!!")
    for v in values:
        print("Value Side Effect: %s" % v)

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

    rdd = sc.parallelize([("Math", 100), ("Eng", 80), ("Math", 50), ("Eng", 70), ("Eng", 90)])
    result = rdd.aggregateByKey(0, lambda k, v: int(v) + k,lambda v, k: k + v)
    print(result.collect())

    ###### pip 와 파티션 관련 연산
    rdd = sc.parallelize(["1,2,3", "4,5,6", "7,8,9"])
    result = rdd.pipe("cut -f 1,3 -d ,")
    print(result.collect()) # [u'1,3', u'4,6', u'7,9']

    rdd1 = sc.parallelize(list(range(1, 11)), 10)
    # 파티션 재조정
    rdd2 = rdd1.coalesce(5)
    rdd3 = rdd2.repartition(10)
    print("partition size: %d" % rdd1.getNumPartitions()) # 10
    print("partition size: %d" % rdd2.getNumPartitions()) # 5
    print("partition size: %d" % rdd3.getNumPartitions()) # 10

    data = [random.randrange(1, 100) for i in range(0, 10)]
    rdd1 = sc.parallelize(data).map(lambda v: (v, "-"))
    # 파티션을 나눌때 앞의 숫자로 정렬 (3이라면 3으로 나눌때 나머지0, 1, 2 로 3개로 나뉨)
    rdd2 = rdd1.repartitionAndSortWithinPartitions(3, lambda x: x)
    rdd2.foreachPartition(lambda values: test1(list(values)))

    rdd1 = sc.parallelize([("apple", 1), ("mouse", 1), ("monitor", 1)], 5)
    # 파티션 재조정
    rdd2 = rdd1.partitionBy(3)
    print("rdd1: %d, rdd2: %d" % (rdd1.getNumPartitions(), rdd2.getNumPartitions()))

    ###### 필터와 정렬

    rdd1 = sc.parallelize(range(1, 6))
    # 필터로 참인 애들만
    rdd2 = rdd1.filter(lambda i: i > 2)
    print(rdd2.collect())

    rdd = sc.parallelize([("q", 1), ("z", 1), ("a", 1)])
    # 키로 정렬
    result = rdd.sortByKey()
    print(result.collect())

    rdd = sc.parallelize([("k1", "v1"), ("k2", "v2"), ("k3", "v3")])
    print(rdd.keys().collect())
    print(rdd.values().collect())

    rdd = sc.parallelize(range(1, 101))
    # 샘플링
    result1 = rdd.sample(False, 0.5, 100)
    result2 = rdd.sample(True, 1.5, 100)
    print(result1.take(5))
    print(result2.take(5))

    ###### RDD 액션

    rdd = sc.parallelize([5, 4, 1])
    result = rdd.first()
    print(result) # 5

    rdd = sc.parallelize(range(1, 100))
    result = rdd.take(5)
    print(result) # 1, 2, 3, 4, 5

    rdd = sc.parallelize(range(1, 100))
    result = rdd.takeSample(False, 20)
    print(len(result), result) # (20, [99, 82, 45, 7, 44, 4, 69, 54, 96, 60, 25, 46, 3, 94, 23, 41, 87, 49, 93, 19])

    rdd = sc.parallelize([1, 1, 2, 3, 3])
    result = rdd.countByValue()
    for k, v in result.items():
        print(k, "->", v)
    # (1, '->', 2)
    # (2, '->', 1)
    # (3, '->', 2)

    rdd = sc.parallelize(range(1, 11), 3)
    # 임의의 두 수에 대한 연산(여기선 덧셈), 파티션 별로 작동
    result = rdd.reduce(lambda v1, v2: v1 + v2)
    print(result) # 55

    rdd = sc.parallelize(range(1, 11), 3)
    # 첫번째 인자 부터 임의의 수에 대한 연산 (  reduced와 같으나, 초기값을 지정할수 있음)
    result = rdd.fold(0, lambda v1, v2: v1 + v2)
    print(result)

    rdd = sc.parallelize(range(1, 11))
    result = rdd.sum()
    print(result) # 55

    rdd = sc.parallelize(range(1, 11))
    result = rdd.foreach(lambda v: test1("Value Side Effect: %s" % v))

    rdd = sc.parallelize(range(1, 11), 3)
    result = rdd.foreachPartition(sideEffect)

    sc.stop()
