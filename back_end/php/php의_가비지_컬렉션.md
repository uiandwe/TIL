 zval은 값에 변경이 이루어지기 전에는 여러 개의 함수 또는 변수에 의해 공유될 수 있습니다. 대신에 zval의 refcount가 값을 공유하는 변수/함수의 개수를 나타내고 있습니다. $a=17 같이 값이 변경되는 순간 $b에 새로 메모리가 할당되면서 각각의 refcount도 감소되는 것을 볼 수 있습니다. 실제로 $b=$a 이후, $a=17이전 시점에 실제 메모리 할당이 일어나지 않습니다. 추후 unset($a)를 실행하면 해당 zval의 refcount=0이 되면서 메모리 해제가 일어납니다. unset()은 refcount–와 같은 의미로 해석하면 될 듯합니다.

refcount가 특정값을 공유하는 변수/함수의 개수를 나타내고 있다면 is_ref는 실제 참조 유무 정보를 보여주고 있습니다.

![/img/1_1_.png](/img/1_1_.png)
```
   $a = 1;   -- $a = zval_1(value=1, refcount=1, is_ref=0)
   $b = $a;   -- $b = $a = zval_1(value=1, refcount=2, is_ref=0)
   $c =& $b; -- $c = $b = zval_1(value=1, refcount=2, is_ref=1),  $a = zval_1(value=1, refcount=1, is_ref=0)
   $b++;   -- $c = $b = zval_1(value=2, refcount=2, is_ref=1)
```
$c는 $b를 직접 참조하고 있습니다. is_ref= 1로서 그 정보를 표시하게 되는데 이는, $b값이 변경되는 시점에 copy가 아닌 실제 값 변경이 일어나는 것을 알 수 있습니다. &-참조는 참조하고 있는 변수값($b)도 변경되어야 하기 때문에 copy on write와 비교하여 실행이 느려질 수 있습니다.

Garbage Collection 전통적인 PHP Reference counting memory 메커니즘은 circular reference 현상을 해결하는 데 실패하였고 이 현상을 커버하기 위해 PHP 5.3은 Garbage Collector를 탑재하게 되었습니다.

단순히 Garbage Collector를 사용하면 더이상 메모리에 할당된 Object에 대한 링크 및 메모리 관리 그리고 사용 후 메모리 해제 등의 이슈는 개발자가 고려하지 않아도 되는 이슈인 걸까요?

다음의 간단한 샘플 코드를 통해 생각해 보도록 하겠습니다.

1. Circular reference createRelationship()을 수행하면 parent와 child라는 객체를 생성하게 되고, parent의 멤버변수 childNodes는 child를, child의 멤버변수 parentNode는 parent를 참조하게 되는 현상을 circular reference라고 볼 수 있습니다. 샘플 코드에는 구체적으로 메모리 해제 시점이 나오지 않았지만, for문을 실행하면서 생성된 객체가 오랫동안 사용되지 않는 채로 유지되고 있어 내부적으로 쓰레기로 판단하여 메모리 해제 처리된다고 가정하고 생각해 봅시다. Parent와 child객체를 해제시킴으로써 각각의 멤버변수인 parentNode와 childNodes에 접근할 수 있는 link가 소실되는 반면 실제 parentNode와 childNodes에 할당된 메모리 해제가 일어나지는 않습니다. Reference counting 메커니즘에 의하면 서로를 참조하고 있기 때문에 refcount가 0이 되지 않았기 때문입니다. 이는 즉, 잠재적인 memory leak의 원인이 될 수 있습니다.

2. 해결방안 Circular reference는 PHP뿐 만 아니라 다른 프로그래밍 언어에서도 흔히 발생하는 일반적인 케이스로, memory leak을 방지하기 위한 최선의 방법은 circular reference를 없애거나 구조를 개선하는 것일 것입니다. 하지만 circular reference구조를 피할 수 없다면? Memory leak을 발생시키지 않을 방법은 무엇이 있을까요?

● Solution 1 – destroy() 추가로 인한 순환 참조 해제 위의 샘플코드를 destroy()를 추가하여 개선한 코드는 다음과 같습니다.
```
   class Node {
       public $parentNode;
       public $childNodes = array();
       function Node() {
           $this->nodeValue = str_repeat('0123456789', 128);
       }
       function destroy()
       {
           $this->parentNode = null;
           $this->childNodes = array();
       }
   }
   function createRelationship() {
       $parent = new Node();
       $child = new Node();
       $parent->childNodes[] = $child;
       $child->parentNode = $parent;
       $parent->destroy();
   }
```
실행결과:
```
   Initial: 328,416 bytes
   Peak: 335,304 bytes
   End: 328,520 bytes
```
__destruct() 같은 경우는 해당 인스턴스가 더 이상 참조되거나 사용되지 않는 경우, 스크립트 실행의 마지막 시점에서 인스턴스가 메모리로부터 제거되기 바로 전에 이 소멸자가 호출됩니다. 그러므로 해당 인스턴스에 종속된, 문제가 되는 childNode, 또는 parentNode의 메모리 해제를 해결하기에는 시점이 늦어져, 활용 가능 대상 함수는 아니게 되네요. 해당 코드에서는 destroy()라는 함수를 정의하여 문제를 해결 하고 있습니다. 즉 메모리 해제 시점에 destroy()를 호출해 그때 그때 해당 변수에 할당된 메모리를 해제하고 있습니다.

● Solution 2 – PHP 엔진에 탑재된 GC 활용 또다른 해결 방법으로는 circular reference를 분석하여 이를 자동으로 해제시켜주는, PHP 5.3 이후 탑재된 Garbage Collector를 활용하는 것입니다. GC활성화를 위해서는 php.ini의 zend_enable_gc항목을 참조하면 됩니다.

Garbage_collector를 통한 샘플 스크립트 실행결과는 다음과 같습니다.
```
   Initial: 327,136 bytes
   Peak: 18,059,504 bytes
   End: 825,656 bytes
```
실행 결과, 사실상 destroy()를 이용한 방법보다 2배가량 더 나은 결과를 보여주고 있습니다. Circular reference를 해결해 준다고는 하지만 메모리 optimization 관점에서 본다면 이는 비효율적인 관리 방법일 수 있습니다. 왜냐하면 우선, GC가 항상 동작한다고 볼 수 없을 뿐더러, 메모리상의 더 이상 참조되지 않는 쓰레기 객체를 수거하기 위해서 걸리는 비용(리소스, 시간)도 만만치 않기 때문입니다. GC는 메모리에 할당된 각 변수들의 refcount 값이 감소하는 시점에 일일이 반응하여 Collection Cycles(쓰레기 수거)를 실행하지는 않습니다.

간단하게 Collection Cycles 알고리즘 설명 시작하기에 앞서, 기본 원칙에 대해 정리하자면 다음과 같습니다. 1.Refcount가 증가한다면 이는 사용 중이고 그러므로 Garbage가 아니다. 2.Refcount가 감소하여, 곧 0에 도달하게 된다면 zval은 메모리를 해제할 것이다. 3.garbage cycles 생성 시점은 즉, refcount가 감소하는 시점이며, refcount를 임의로 1 감소시켜봄으로써 잠재적인 garbage대상을 분별 체크할 수 있는 기능을 가지고 있다.

![/img/3.png](/img/3.png)

Refcount가 감소되는 시점에 일일이 비효율적으로 garbage checking cycle이 수행하는 것을 막기 위해 (refcount가 감소되는 시점의 대상 객체는 곧 garbage로서의 잠재 가능성이 있는 것으로 판단하여..) root노드를 생성하여 대상과 연결시킨 후 해당 root를 root buffer에 등록시킵니다. 이 root buffer가 꽉 차면 비로소 collecting 수행이 시작되면서 등록된 모든 대상들을 훑게 됩니다. 이는 refcount가 감소하는 시점에 GC가 항상 수행되지는 않는다는 것을 보여주고 있습니다.

Root buffer가 꽉차서 Collecting cycles가 시작되면 depth-first-search방식을 이용하여 root buffer에 등록된 모든 대상의 상태를 체크하고 메모리 해제할 대상을 선별하여 정상적으로 메모리가 해제됩니다.

depth-first-search방식에 대한 이해는 이 주제를 벗어난 것이라 판단하여 참고자료로 넘기도록 하겠습니다만, depth-first-search로 Root buffer에 등록된 모든 대상을 최소 한번 훑으면서 garbage 대상 선별하는 작업까지 하는데 각 노드를 두번 이상 검색하게 된다는 사실은 많은 과부하로 인해 성능 저하가 일어날 수 있다는 것을 의미하고 있습니다.

Garbage Collector를 활용하되, 이러한 성능문제를 피하기 위해서는 개발자가 메모리 릭이 발생할 소지가 있는 부분에 다음과 같이 GC 관련 API를 이용하여 부분적으로 문제를 해결하는게 더 나은 차선책으로 보입니다.
```
function createRelationship() {

       $parent = new Node();
       $child = new Node();
       $parent->childNodes[] = $child;
       $child->parentNode = $parent;
       gc_collect_cycles();
   }
```
실행결과
```
   Initial: 327,136 bytes
   Peak: 18,059,504 bytes
   End: 825,656 bytes
   ```

결국 Garbage Collector 의 사용은 circular reference를 해결하는 방책이 될 수 있는 반면 성능면에서 그 한계가 있음을 확인하게 됩니다. 
