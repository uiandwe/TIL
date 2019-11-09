# pep-7 c 코드용 스타일 가이드

1. C 코드 가이드라인
    1. 3.6 이전의 python 버전은 ansi/sio 표준 c를 사용한다. 
    2. 3.6 이상의 python 버전은 C89 을 사용하며 C99의 몇몇 기능을 사용할 수 있다.
        * stdint.h / tintype.h 표준 정수 유형
        * 정적 인라인 함수
        * intermingled declarations
        * booleans
        * C++-style line comments 
    3. GCC extensions을 사용하면 안된다. 
    4. 모든 함수 선언은 프로토 타입을 사용해야 한다. ( 모든 인수의 유형을 지정해야 한다. )
    5. Python 3.6 이상에서는 c++ 스타일의 주석만을 사용한다. 
    6. 주요 컴파일러의 경고는 없다. 


2. 코드 레이아웃
    * 탭없이 4칸 들여쓰기를 사용한다. 
    * 줄은 79자를 초과 할수 없다. 
        * 너무 복잡하다면 서브 루틴 사용을 고려한다. 
    * 공백으로 끝나느 줄은 없어야 한다. 
    * 함수 정의 
        * 1열에 함수 이름
        * 다음열에 중괄호 
        * 지역 변수 선언 후 빈줄 추가 
        * 예시
<pre>                     
static int
extra_ivars(PyTypeObject *type, PyTypeObject *base)
{
    int t_size = PyType_BASICSIZE(type);
    int b_size = PyType_BASICSIZE(base);


    assert(t_size >= b_size); /* type smaller than base! */
    ...
    return 1;
}
</pre>

* If / for 의 구문 사이엔 공백이 하나 있어야 한다. 
    
<pre>
if (mro != NULL) {
    ...
}
else {
    ...
}
</pre>


* 긴줄은 쉼표를 기준으로 적절하게 들여쓰기를 한다. 


<pre>
PyErr_Format(PyExc_TypeError,
             "cannot create '%.100s' instances",
             type->tp_name);
</pre>


* 주석은 설명하는 코드 앞에 온다
* 모든 함수와 전역변수는 게시된 인터페이스에 속하지 않는 한 정적으로 선언한다















