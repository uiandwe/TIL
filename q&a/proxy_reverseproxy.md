## proxy / reverse proxy
### proxy (forward proxy)
- backend->frontend 로 응답시 endpoint에 대해 신경쓸 필요 없는 경우
- backend 앞에 웹서버인 apache / nginx를 통해 frontend 요청에 의한 backend의 로직을 수행

### reverse proxy
- frontend -> backend 로 응답시 frontend가 서버에 대해서 신경 쓸 필요가 없는 경우
- backend 앞에 proxy서버를 통해 요청에 의한 api를 어떤 서버로 보낼지 판단(msa아키텍처에서의 하나의 서버를 통한 서버 통합)
- proxy서버에서 logging / access / 캐싱 등의 기능을 처리
