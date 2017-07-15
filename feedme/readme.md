# feedme

DEFCON 2016 feedme

  - 32bit binary
  - BOF & Canary


## Overview

  - 첫 글자를 통해 입력받을 길이가 결정된다.
  - canary가 있기 때문에 brute forcing을 통해 leak 한다.


## Vulnerability

```c
 for ( i = 0; i <= 0x31F; ++i )
  {
    v5 = (int)sub_806CC70();
    if ( !v5 )
    {
      v1 = feed_me();
      sub_804F700("YUM, got %d bytes!\n", v1, v2);
      return;
    }
...
```

  - fork 로 800번 반복 실행되기 때문에 canary가 그 동안은 바뀌지 않는다.
  - system call 을 이용해 read( ), execve( )를 호출해서 문제를 해결했다.
  - 레지스터 eax엔 시스템콜 넘버를, 필요한 인자값은 ebx, ecx, edx, esi, edi, ebp 순으로 세팅한다.


