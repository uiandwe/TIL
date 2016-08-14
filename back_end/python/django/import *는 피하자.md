#import *는 피하자

```
from django.forms import *
from django.db.models import *
```

다른 모듈의 같은 이름이 추가 로딩되거나 기존 것 위에 덮여 로딩된다면 예상치 못한 에러가 발생한다. 

```
from django.forms import CharField
from django.db.models import CharField
```

임포트 선언은 언제나 신중히!
