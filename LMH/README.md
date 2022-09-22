# commit script 사용법

algorithm commit log 의 일관성과 입력의 편의성을 위해 commit script를 사용합니다. :-)

## commit.sh 등록 방법

1. 사용자 홈 디렉토리에서 `commit.sh` 생성
   ```bash
   $ cd ~
   $ vi commit.sh
   ```
2. 아래 내용 붙여넣은 후 `:wq` 로 저장 및 파일 닫기
   ```bash
   #!/bin/sh
   
   echo "The script for git-commit is running..."
   read -p "platform(BOJ/PGS/SEA/ETC): " platform
   read -p "문제이름: " name
   read -p "난이도: " difficulty
   read -p "걸린시간: " time
   read -p "url: " url
   
   echo
   echo "\"git show\" 를 통해 최신 commit을 확인하세요."
   echo "commit 취소는 \"git reset --soft HEAD^\""
   echo
   echo git commit -m \"[$platform] $name / $difficulty / $time\" -m \"$url\"
   git commit -m "[$platform] $name / $difficulty / $time" -m "$url"
   echo
   ```

3. `.bashrc` 열어서 alias 추가 (`:wq`로 저장)

   ```bash
   alias gc="~/commit.sh" 
   ```

4. 수정한 `.bashrc` 적용

   ```bash
   $ source ~/.bashrc
   ```



## git commit 방법

1. git add

2. git commit 대신 gc 명령어 사용

   ```bash
   $ gc
   The script for git-commit is running...
   platform(BOJ/PGS/SEA/ETC): BOJ
   문제이름: a
   난이도: b
   걸린시간: c
   url: d
   
   "git show" 를 통해 최신 commit을 확인하세요.
   commit 취소는 "git reset --soft HEAD^"
   
   git commit -m "[BOJ] a / b / c" -m "d"
   [master 9c87f27] [BOJ] a / b / c
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 mhlee21/test
   ```

   > 💡 잘못 입력했거나 add하지 않은 파일 있는 경우 ctrl + c 로 종료 후 gc 를 재실행 해주세요.

3. git push

