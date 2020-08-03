API 명세
=
데이터베이스 생성
-
``` 
    GET /init
```
- Request
```
{

}
```
- Response
```
{
    SUCCESS { "code" : 200, "message": "success" }
    FAIL { "code" : 404, "message" : "fail" }
}
```

재료 목록 조회
-
```
    GET /show
```
- Request
```

```
- Response
```
    SUCCESS { "code": 200,
            "data": [
                {
                "ex_date": "Mon, 31 Aug 2020 00:00:00 GMT",
                "name": "가지",
                "number": 4
                }, ...
            ],
            "message" : "success"
    }

    FAIL { "code" : 404, "message" : "fail" }
```


유통기한 지난 재료 조회
-
```
    GET /late
```
- Request
```
```
- Response
```
    SUCCESS {"code": 200,
            "data": [
                {
                "ex_date": "Mon, 31 Aug 2020 00:00:00 GMT",
                "name": "가지",
                "number": 4
                }, ...
            ],
            "message" : "success"
    }

    FAIL { "code" : 404, "message" : "fail" }
```

재료 추가
-
```
    POST /insert
```
- Request
```
{
    "name" : "가지",
    "number" : 3, #양수
    "ex_date" : 20230807
}
```
- Response
```
    SUCCESS { "code": 200, "message": "success" }
    FAIL { "code": 404, "message": "fail" }
    FAIL { "code": 404, "message": "already exist" }
```
재료 수량 수정
-
```
    POST /update
```
- Request
```
#재료 수량 수정
{   
    "name" : "오이",
    "number" : 5
}
```
- Response
```
    SUCCESS { "code": 200, "message": "success" }
    FAIL { "code": 404, "message": "fail" }
```
재료 삭제
-
```
    GET /delete?name=value
```
- Request
```
```
- Response
```
    SUCCESS { "code": 200, "message": "success" }
    FAIL { "code": 404, "message": "fail" }
```

음성인식모드 실행
-
```
    GET /speech
```
- Request
```
```
- Response
```
    SUCCESS { "code": 200,
            "data": [
                {
                "ex_date": "Mon, 31 Aug 2020 00:00:00 GMT",
                "name": "가지",
                "number": 4
                }, ...
            ],
            "message" : "success"
    }

    SUCCESS { "code": 200,
            "data": {
                "[요리제목0]" : "[레시피 설명 링크0]",
                "[요리제목1]" : "[레시피 설명 링크1]",
                "[요리제목2]" : "[레시피 설명 링크2]",
                ...
                },
            "message" : "success"
     }

    FAIL { "code": 404, "message": "fail" }
```