Asynchronous JavaScript and XML 의 약자로서 XMLHttpRequest 객체를 이용하여 비동기 방식으로 서버와 통신을 하는 것을 말한다.

웹 브라우저의 클라이언트와 서버간 통신은 url를 이용한 http 통신으로 이루어진다. 즉 브라우저가 서버로 request를 날리기 위해서는
해당 브라우저의 url 주소를 변경하여야 하는데 이때는 페이지 이동이 일어나게 된다.

하지만 ajax 의 경우 브라우저의 url 주소의 변경을 이용하지 않고 내부적으로 통신하여 response 를 받아오기 때문에 특정 데이터만 
불러오거나 비동기로 데이터를 불러와야하는 경우 사용된다.

이때 Same Origin Policy 정책으로 인해 cross domain 을 허용하지 않기 때문에 외부 도메인을 사용하여야 하는경우 JSONP, XML 등을 
이용하여야 한다.
