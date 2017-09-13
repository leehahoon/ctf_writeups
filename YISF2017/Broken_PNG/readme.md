# Broken_PNG

2017 YISF Final MISC 문제

  - Broken PNG files
  - File Recovery

## Overview

  - 정체 불명의 파일 3개씩 여러 폴더에 존재한다.
  - 문제명과 PNG 헤더로 PNG 이미지 파일인 것을 확인할 수 있다.

## Solution

- 파일을 각각 바이트단위로 읽은 후, 합쳐서 이미지 파일을 만든다.
- 그리고 구글에서 발견한 이미지 합성 프로그램을 이용해 잘라진 PNG 파일을 복구한다.
- Python PIL 라이브러리를 통해 풀 수도 있다.

