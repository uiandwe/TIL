php 기본 구조

zval은 zend value의 줄임말로, PHP의 value를 의미함 PHP언어는 변수를 선언할떄 데이터 타입 정보를 명시 하지 않음. 이는 컴파일이 아닌 런타임 변수 지정되는 스크립트 언어이기 때문이며 변수즤 생명이 끝나기 전에는 언제든지 타입이 바뀔수 있다는것을 의미.

[1-1] 데이터 value와 타입 정볼르 담은 Union
```
   typedef union _zvalue_value{
      long lval;
      double dval;
      struct{
          char *val;
          int len;
      } str;
      Hashtable *ht;
      Zend_object_Value obj;
  } zvalue_value;
```
php의 가능한 모든 형태의 테이터 타입은 C의 union으로 선언되어 있음. Union은 여러 형태의 멤버를 가지고 있는 집합체 이지만 한 시점에 한개의 형태의 데이터만이 사용될수 있음.

최종 구조는 unoin 과 refcount , 타입 tag의 멤버를 가진 구조체 이다.
```
  struct _zvalue_struct {
     zvalue_value value;       // value
     zend_unit refcount__gc;
     zend_uchar type;         // active type 
     zend_uchar is_ref__gc;
  }; 
```
출처 : http://tmondev.blog.me/220367194049
