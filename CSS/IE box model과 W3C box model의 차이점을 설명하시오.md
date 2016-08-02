#IE box model과 W3C box model의 차이점을 설명하시오.

W3C box model =  content-box (only content)

Internet Explorer box model = border-box(include content, padding, border)


![http://i.stack.imgur.com/y0Tkz.png](http://i.stack.imgur.com/y0Tkz.png)


그래서 css reset 시 

```css
*{
    box-sizing:border-box;
    margin: 0px;
    padding: 0px;
}
```

을 집어 넣어서 border-box 적용

