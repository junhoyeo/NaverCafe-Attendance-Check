# 네이버 카페 자동 출석체크

## ⚙️ settings ⚙️

```json
// secret.json
{
    "url": "https://cafe.naver.com/???",
    "element": "a#menuLink46"
}
```

- `url`: naver cafe address
- `element`: attendance board element in naver cafe

## 🔥 mechanism 🔥

![](./struct.png)

1. Switch to `iframe#cafe_main`
2. Input message in `textarea#cmtinput`
3. Click `button#btn-submit-attendance`
