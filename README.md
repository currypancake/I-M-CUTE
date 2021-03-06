# I M CUTE
나 는 귀엽다

## 다운 받기
[링크](https://github.com/currypancake/wiki-info-macro)
이거 따라하면 됩니다.

## 필수 파트
### 라이브러리 설치
(이미 설치되있으면 설치 안해도 됩니다.)
~~~bash
pip install bs4
pip install requests
~~~

### 쿠키 설정
이번엔 직접 코드를 편집하지 않습니다.

[자신의 쿠키값 가져오기](https://github.com/currypancake/SaveImage)
여기 링크 들어가서 밑으로 내리다보면 자신의 쿠키값을 찾는 법 나오는데 따라서 쿠키 찾고
값 복사하고 utils폴더에 login_cookie.txt 파일에 붙여넣습니다.


## 사용법
1. src폴더에 들어간다.
2. 파워쉘을 켠다.
3. 아래 명령어를 입력한다. [파워쉘을 여는 법](https://www.manualfactory.net/11724)
~~~bash
python main.py
~~~

그럼 아래 사진과 같은 창이 뜹니다.
![ex](https://github.com/currypancake/I-M-CUTE/blob/master/img/ex.png)

각각 해당 정보를 입력한 후 확인 버튼을 누르면 됩니다.

* 이벤트 명 - 이벤트 이름을 입력하면 됩니다.
* 가챠명 - 이벤트와 연동된 가챠 이름을 입력하면 됩니다.
* 거불카 가챠 - 거불카 가챠명을 적으면 됩니다. 
  * 위 이름들은 위키 페이지 링크로 사용이 됩니다. 
  * [[이벤트 명]] <= 이런식으로 입력이 됩니다.

* 카드 보안코드 - 카드 보안코드를 입력해주세요 (언더바 포함)
* 이벤트 보안코드 - 이벤트 보안코드를 입력해주세요 (언더바 포함)
  * 이벤트 보안코드는 배너링크에서 알 수 있습니다.
  * 이벤트 배너들만 다운로드가 됩니다. 헤더 이미지는 직접 다운해야합니다.

* 이벤트 번호 - 몇번째 이벤트인지 숫자로 적습니다.
  * 이벤트 번호는 위키 이벤트 목록 페이지에서 확인할 수 있습니다.
  * 혹은 브마 주소....

* 이벤트 기간 - 몇일짜리 이벤트인지 숫자만 적습니다.
  * ex) 13일 마라톤일 경우 '13' 만 적습니다. 

* 포인트 보상 - 해당 이벤트 포보 아이돌의 이름을 **풀 네임**으로 적습니다.
* 랭킹(R) 보상 - 해당 이벤트 랭보 레어 아이돌의 이름을 **풀 네임**으로 적습니다.
* 랭킹(SR) 보상 - 해당 이벤트 상위 아이돌의 이름을 **풀 네임**으로 적습니다.

탐색 범위
위에 써있는 유닛에만 적용이 됩니다.

* 시작 번호 - 탐색을 시작할 카드 번호를 입력해주세요.
* 끝 번호 - 마지막으로 탐색할 카드 번호를 입력해주세요.
  * 만약 토우마의 30번쨰 스알카드 에서  33번 스알카드까지 확인하고 싶으면
  30과 33을 적어주시면 됩니다.
  * '깃발 ~ 레제'와 '레제' 부분은 0으로 입력하면 각각 '쥬피터\~코가도', '쥬피터\~깃발' 과 같은 범위를 탐색합니다.
  * 끝번호는 항상 **시작번호보다 큰 숫자**로 입력해주세요.


아래는 예시입니다.
![res](https://github.com/currypancake/I-M-CUTE/blob/master/img/res.jpeg)


오류가 나거나 이해가 안되는 부분이 있으면 호출 ㄱㄱ 해주세요.
