# CloseGallery

> OpenGallery라는 사이트를 클론코딩하였습니다.
>
> 장고를 학습하기 위해 만든 토이 프로젝트입니다.

모든 사진 작품은 unsplash에서 가져온 무료 이미지입니다.

## Live demo

none

## Preview

![image](https://user-images.githubusercontent.com/72514247/127777622-87e382da-d31e-4fa7-a0f1-7f3c0cb574da.png)

## Features

- 메인페이지 DB를 통해 저장된 데이터 표시(메인 슬라이드, 금주의 작품, 시즌별 작품, 이용 후기)
- 로그인/로그아웃
- 다양한 상호작용
- 백오피스

## Tech and libraries

- django
- jquery
- bootstrap
- swiper.js
- sqlite (postgresql을 사용하였으나, 배포를 용이하게 하고자 sqlite로 변경)

## Getting started

- you can check admin page using superuser (id: admin@admin.com, pw: aaabbbccc123)
- admin page is "/admin"

- Start dev server

```bash
$ python3 manage.py runserver
```

## Note

This project is ongoing.

## License

This project is licensed under the MIT License - see the LICENSE.md for details
