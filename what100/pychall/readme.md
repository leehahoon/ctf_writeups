# pychall

2017 선린모의해킹대회 pychall 문제

  - Python pickle vulnerability


## Overview

  - socket으로 8899 포트를 연 후, 데이터를 입력받는다.
  - 입력받은 데이터는 pickle.loads( )를 수행한다.


## Vulnerability

  - reduce 에서 취약점이 발생한다.


