#클리어링(Clearing) 기술에는 어떤 것들이 있으며, 어떠한 경우에 어떻게 사용하는 것이 적절한지 설명하세요.

float 속성에 대한 영향을 받지 않게 하려할 때 사용한다.
float 속성을 감싸고 있는 element의 height를 알맞게 조정하기 위해 사용한다.

```html
<div class="wrap">
    <div class="left">left</div>
    <div class="right">right</div>
    <div class="clear">clear</div>
</div>
````

```css

.wrap { width:320px; background-color:#eee; }
.left { float:left; padding:50px; background-color:red; }
.right { float:right; padding:50px; background-color:blue; }

/* 방법1. */ .clear { clear:both; }
/* 방법2. */ .wrap { overflow:auto; }
/* 방법3. */ .wrap:after { content:""; display:block; clear:both; }
/* 방법4. */ .wrap { min-height:contain-floats; } 
```

http://jsfiddle.net/zinee/x6tv9hgo/?utm_source=website&utm_medium=embed&utm_campaign=x6tv9hgo
