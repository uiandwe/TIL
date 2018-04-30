

![Alt text](/img/css_fixed1.png)
![Alt text](/img/css_fixed2.png)

```
{
    position: fixed;
    top: 0;
    left: 50%;
    margin-left: 216px;
    overflow: auto;
    height: 100%;
}
```

## position을 fixed로 할시 반응형일 경우 옆의 개체와 일정한 간격을 유지 하기 위해서 left 50%와  maring-left값을 해당 태그 사이즈/2 + 떨어지는 간격 px로 주면 된다. 
