API 명세
=
냉장고 등록
-
``` 
    GET /register/<string:id>
```
- Request
```
{

}
```
- Response
```
{
    SUCCESS { "code" : 200, "message": "register success" }
    FAIL { "code" : 400, "message" : "fail" }
}
```

재료 목록 조회
-
```
    GET /show/<string:id>
```
- Request
```

```
- Response
```
    SUCCESS { "code": 200,
            "data": [
                {
                    "id": "내 냉장고1",
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
    GET /late/<string:id>
```
- Request
```
```
- Response
```
    SUCCESS {"code": 200,
            "data": [
                {
                    "id" : "내 냉장고1",
                    "ex_date" : "Mon, 31 Aug 2020 00:00:00 GMT",
                    "name": "가지",
                    "number" : 4
                }, ...
            ],
            "message" : "success"
    }

    FAIL { "code" : 404, "message" : "fail" }
```

재료 추가
-
```
    POST /insert/<stirng:id>
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
    SUCCESS { "code": 200, "message": "insert success" }
    FAIL { "code": 404, "message": "fail" }
    FAIL { "code": 404, "message": "already exist" }
```
재료 수량 수정
-
```
    POST /update/<string:id>
```
- Request
```
{   
    "name" : "오이",
    "number" : 5
}
```
- Response
```
    SUCCESS { "code": 200, "message": "update success" }
    FAIL { "code": 404, "message": "fail" }
```
재료 삭제
-
```
    GET /delete/<string:id>?name=value
```
- Request
```
```
- Response
```
    SUCCESS { "code": 200, "message": "delete success" }
    FAIL { "code": 404, "message": "fail" }
```