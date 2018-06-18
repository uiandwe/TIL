```

쿠팡에서는 판매자들로부터 새 상품들을 등록받을때 이미 쿠팡에 등록되어 있는 상품들과 중복되는 상품이 있는지 확인합니다.
새 상품명과 (newProductName) 기존 상품명들이 주어졌을때 (existingProductNames), 새 상품명과 가장 유사한 기존 상품명의 인덱스를 찾아주세요.

문제를 풀때 다음 사항들을 유의해주세요.
* 문제를 간단히 하기위해 새 상품명과 기존 상품명간의 유사도는 상품명에서 나온 단어들의 자카드 지수로 정의합니다.
* 상품명의 단어들은 스페이스로만 구분됩니다.
* 같은 점수가 나왔을때는 먼저 나온 아이템이 우선 순위를 가집니다.


자카드 지수의 (위키) 예:
newProductName = 에스트라 아토 베리어 보습 로션 200ml
새상품명 단어세트 = Set(에스트라,아토,베리어,보습,로션,200ml)
existingProductName = 에스트라 아토 베리어 크림 영양 보습 스킨케어 200ml
기존상품명 단어세트 = Set(에스트라,아토,베리어,크림,영양,보습,스킨케어,200ml)
자카드계수분모 = Set(에스트라,아토,베리어,보습,로션,200ml,크림,영양,스킨케어)
자카드계수분자 = Set(에스트라,아토,베리어,보습,200ml)
자카드계수 = 자카드계수분자갯수 / 자카드계수분모갯수 = 5개 / 9개 = 0.5556 


실제 문제의 예:
입력 (쉼표로 분류된 상품명들. 첫 번째 값을 새상품명, 그 뒤의 값을 기존 상품명으로 정의한다): 
에스트라 아토 베리어 보습 로션 200ml,아토팜 판테놀 로션 200ml,사노산 베이비 케어 로션 200ml,에스트라 아토 베리어 로션 200ml,일리윤 세라마이드 아토 집중크림 무향 100ml,에스트라 리제덤 RX 듀얼 썬크림 50ml

newProductName = 에스트라 아토 베리어 보습 로션 200ml
existingProductNames = [

아토팜 판테놀 로션 200ml, 
사노산 베이비 케어 로션 200ml,
에스트라 아토 베리어 로션 200ml,
일리윤 세라마이드 아토 집중크림 무향 100ml,
에스트라 리제덤 RX 듀얼 썬크림 50ml

]

가장비슷한 인덱스: 2 (세번째 아이템: 에스트라 아토 베리어 로션 200ml, 첫번째 아이템의 인덱스는 0으로 본다) 

입력1
에스트라 아토 베리어 보습 로션 200ml,아토팜 판테놀 로션 200ml,사노산 베이비 케어 로션 200ml,에스트라 아토 베리어 로션 200ml,일리윤 세라마이드 아토 집중크림 무향 100ml,에스트라 리제덤 RX 듀얼 썬크림 50ml

출력 1
2



```


```

var products = [
    { "product_name" : "아토팜 판테놀 로션 200ml"},
    { "product_name" : "사노산 베이비 케어 로션 200ml"},
    { "product_name" : "에스트라 아토 베리어 로션 200ml"},
    { "product_name" : "일리윤 세라마이드 아토 집중크림 무향 100ml"},
    { "product_name" : "에스트라 리제덤 RX 듀얼 썬크림 50ml"}
];
var existingProductName = "에스트라 아토 베리어 크림 영양 보습 스킨케어 200ml";

var existingProduct = existingProductName.split(" ");
var maxCount = 0;
var maxIndex = -1;
for(var i=0; i<products.length; i++){
    var temp_product = products[i]["product_name"].split(" ");
    var temp_count = 0;
    for(var j=0; j<existingProduct.length; j++){
        if(temp_product.indexOf(existingProduct[j])>-1){
            temp_count++;
        }
    }
    if(temp_count > maxCount){
        maxCount = temp_count;
        maxIndex = i;
    }
    
}

console.log(maxIndex)

```
