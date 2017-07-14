# what100

2017 선린모의해킹대회 what100 문제

  - 64bit binary
  - Easy BOF

## Overview

  - 간단한 bof 문제로 리턴 주소를 go( )로 덮으면 쉘을 획득할 수 있다.


You can also:
  - Import and save files from GitHub, Dropbox, Google Drive and One Drive
  - Drag and drop markdown and HTML files into Dillinger
  - Export documents as Markdown, HTML and PDF


## vulnerability

- buf의 크기는 32bytes인데 입력은 256 bytes를 받으므로 BOF가 발생한다.

```c
puts("What The Hell");
printf("go? ", argv);
fflush(_bss_start);
read(0, &buf, 0x100uLL);
result = strcmp(bufbuf, "whatthehell");
if ( !result )
    result = go();
return result;
```

