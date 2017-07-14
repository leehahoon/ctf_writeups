# babypwn

2017 CODEGATE CTF babypwn 문제

  - 32bit binary
  - BOF
  - canary leak
  - rop

## Overview

  - 전형적인 bof 문제로 canary를 leak하고 rop를 통해 문제를 풀 수 있다.
  - socket으로 8181포트를 열어 서비스를 실행한다.

## Vulnerability

- made_recv( )에서 v2의 크기는 40bytes 이지만 입력은 100bytes까지 가능하다.
- v2 변수를 가득채워서 canary를 leak 한다.
- ROP를 이용해 recv( )로 원하는 명령어를 입력받고, system( )으로 실행한다.

```c
while ( 1 )
    {
        made_send("\n===============================\n");
        made_send("1. Echo\n");
        made_send("2. Reverse Echo\n");
        made_send("3. Exit\n");
        made_send("===============================\n");
        v1 = select_menu();
        if ( v1 != 1 )
          break;
        made_send("Input Your Message : ");
        made_recv(&v2, 0x64u);
        made_send(&v2);
    }
```

