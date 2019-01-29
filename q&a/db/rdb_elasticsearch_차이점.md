
#### 저장 형태
RDB 테이블

|PK   |Text   | 
|---|---|---|---|---|
|Doc1   |blue sky green   | 
|Doc2   |blue ocean green   | 
|Doc3   |red flower blue sky   |

Elasticasearch
|검색어   |검색어가 있는 문서   | 
|---|---|---|---|---|
|blue  |Doc1, Doc2, Doc3| 
|sky   |Doc1, Doc3| 
|green   |Doc1, Doc2|

- RDB는 문서를 그대로 저장
- Elasticasearch는 단어별로 해당 단어가 있는 문서를 저장 (그래서 검색에 강함)


