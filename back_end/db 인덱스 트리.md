#db 인덱스 트리 



![http://wiki.gurubee.net/download/attachments/12517389/Index_0.JPG](http://wiki.gurubee.net/download/attachments/12517389/Index_0.JPG)



트리구조의 최상위에 하나의 루트 노드가 존재하고 그 하위에 자기 노드가 붙어 있는 형태.
인덱스의 키값은 모두 정렬돼 있지만 데이터 파일의 레코드는 정렬돼 있지 않고 임의의 순서대로 저장돼 있다.

만일 레코드가 삭제되어 빈 공간이 생기면 그 다음의 insert 는 가능한 삭제된 공간을 재활용하도록 되어 있어 
insert된 순서로 저장되진 않는다.
