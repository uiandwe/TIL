# list comprehensions이 더 빠른 이유.


## Why are list comprehensions faster than for loops in Python?

The speed of list comprehensions is notably better than for-loops when appending items to the list.

List comprehensions perform better here because you don’t need to load the append attribute off of the list and call it
as a function. Instead, in a comprehension, a specialized LIST_APPEND bytecode is generated for a fast append onto the 
result list.

Much more information and a better explanation in the source below.

한마디로 list의 append()함수를 불러오지 않기 때문. append()는 다시 list객체를 불러 와야 하며 손실이 생기지만
list comprehensions는 바로 리스트 에 넣어버림.



http://blog.cdleary.com/2010/04/efficiency-of-list-comprehensions/

