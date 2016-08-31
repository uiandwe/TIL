```
<a>       :  하이퍼링크 정의 
<addrss>  :  article나 body에 대한 연락처 정보를 제공
<map>     :  이미지의 특정 부분을 지정하여 링크를 걸때 사용
<area>    :  map태그의 자식으로 map의 크기 및 링크를 정의

<base>    :  해당 페이지의 절대경로를 표기 <head>태그안에 들어가면 페이지에 오직 하나만 존재
             <body>안의 각종 href가 선언될시 base를 기준으로 링크를 선택하게됨.
             
<blockquote>  : 감싸진 텍스트가 긴 인용문임을 가리킵니다. 일반적으로 이것은 들여쓰기로 렌더링됨
                <blockquote cite="http://developer.mozilla.org">
                  <p>This is a quotation taken from the Mozilla Developer Center.</p>
                </blockquote>

<body>    :   HTML 문서의 내용. 페이지에 오직 하나만 존재
<br>      :   텍스트에서 줄바꿈



<caption> :   표의 제목을 나타낸다.  이것은 항상  <table>의 첫 번쨰 자손이지만, CSS를 사용한 styling은
              표와 관련된 다른 곳에서 배치할 수 있다.
              
<cite>    :   창작물에 대한 참조
              More information can be found in <cite>[ISO-0000]</cite>.
              
<code>    :   프로그래밍 코드를 그대로 표시 <pre>태그와 함께 사용
              <pre><code>alert("!");</code></pre>
              
<COL>     :   표 내부의 열을 정의하며 모든 공통 셀들의 공통 시멘틱을 정의하기 위해 사용됩니다. 
              이것은 일반적으로 <colgroup> 요소 내부에 있습니다.
<colgroup>:   표 내부의 칸의 그룹을 정의


<dd>      :   정의 목록 요소(<dl>)에서 용어의 정의를 나타냅니다. 
              이것은 정의 목록 요소의 자식 요소로서만 등장할수 있으며, 뒤에 <dt> 요소가 따라와야합니다.
              <dl>
                <dt>Firefox</dt>
                <dd>A free, open source, cross-platform, graphical web browser
                    developed by the Mozilla Corporation and hundreds of volunteers.</dd>
              </dl>
<dl>      :   요소의 하위 요소가 이름-값 짝을 하나 가지고 있으면뚜렷한 콘텐츠(보통 사전 인용에 사용)
              <dl>
                <dt>단ㅇㅓ</dt>
                <dd>정의</dd>
              </dl>
<!DOCTYPE>: 
<DT>      :    정의 목록에서 용어를 구분

<em>      :    강조를 표시 이탤릭체로 표기됨 (<i>는 그냥 이탤릭체 <em>은 강조)

<form>    :    서버에 정보를 제출하기 위한 대화형 컨트롤을 포함한 문서의 구획을 나타냅니다.

<H1>, ...<H6> : 
<head>    :   문서의 제목과 스크립트,스타일 시트의 링크 또는 선언을 포함하는 문서의 일반적인 정보 (메타데이터)
<hr>      :   문단 레벨 요소들 사이에서 주제의 분리
<html>    :    HTML 문서의 루트를 나타냅니다. 모든 다른 요소들은 이 요소의 후손입니다.
<i>       :   특정 이유로 인하여 평범한 글자와 구분하기 위해 사용됩니다. 예를 들면, 기술적인 용어, 외국어 문구, 소설속 인물의 
              생각이 있습니다. 이것은 일반적으로 이탤릭체로 표기됩니다.
<img>     :   문서의 이미지를 나타냅
<input>   :   입력할수 있는 
              type : button, checkbox, color, date, datetime, datetime-local, email, file, hidden, image, month, number
                     password, radio, range, reset, search, submit, tel, text, time, url, week
                     
<kbd>     :    키보드의 특정 키를 나타낼 때 사용하며, 원래 글자 크기보다 2point 작게 브라우저에 랜더링

<li>      :   리스트 항목을 나타낼때 사용됩니다. 이 요소는 자신이 리스트에서 하나의 개체를 나타내는 정렬된 리스트(<ol>),
              정렬되지 않은 리스트(<ul>), 메뉴(<menu>) 에 포함되어야 합니다
<link>    :   현재 문서와 외부 리소스와의 관계를 명시  스타일 시트에 링크


<map>     : 이미지 맵(클릭 가능한 링크 영역)을 정의하기 위해 <area>와 함께 사용
<menu>    : 사용자가 수행하거나 하는 명령 묶음을 말합니다. 
            이것은 스크린 위에 나오는 목록 메뉴와 눌려진 버튼 아래에 나오는 것과 같은 맥락 메뉴를 포함

<ol>      : Ordered List는 정렬된 리스트의 항목들
            번호는 순자,문자,로마 숫자,간단한 점과 같이 어떤 형태로든 나타날수 있습니다
            

```


