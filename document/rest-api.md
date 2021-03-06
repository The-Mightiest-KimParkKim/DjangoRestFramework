# API정보



## 1. 요청 domain 정보

lambda :  https://8i8wxh81q2.execute-api.us-east-1.amazonaws.com

drf :  

- (구버전)http://3.92.44.79 또는 http://ec2-3-92-44-79.compute-1.amazonaws.com/
- (신버전)http://13.209.95.229
- (빅데이터음성부분)http://3.93.61.7

AI올린 EC2:

- http://13.209.95.229:8888



## 2. 요청 method 정보

### POST dev/s3(사용안함)

- lambda
- S3 이미지 업로드 시 AI에게 전달
  - 이미지를 업로드 하되 파일명(냉장고번호)을 받아 S3에 있는 것과 비교하여 해당 파일만 저장될 수 있도록 해야함
- **body** : {fridge_number : str(냉장고번호), reg_date : str(현재날짜, 형식 : 2020-12-12 11:01:25.518280)}
- date형태 : '%Y-%m-%d %H:%M:%S.%f'
- return: HTTP_200_OK | HTTP_400_BAD_REQUEST
- 만든이 : snchoi


### POST dev/sensor

- lambda
- 센서값 저장 및 문자전송
  - 센서값 저장
  - 불꽃 센서(fire)값 50이하 시 보호자에게 문자 발송
- **body** : {fridge_number : str(냉장고번호), name: str(센서이름), value: int(센서값), reg_date: str(현재날짜)}
- date형태 : '%Y-%m-%d %H:%M:%S.%f'
- return: HTTP_200_OK | HTTP_400_BAD_REQUEST
- 만든이 : snchoi


### POST api/ai-img-grocery/

- DRF
- S3 이미지 업로드 시 AI에게 전달
  - 이미지를 업로드 하되 파일명(냉장고번호)을 받아 S3에 있는 것과 비교하여 해당 파일만 저장될 수 있도록 해야함
- **body** : {url : str(버킷에올라가 이미지 url), fridge_number : str(냉장고번호), reg_date : str(현재날짜, 형식 : 2020-12-12 11:01:25.518280)}
- date형태 : '%Y-%m-%d %H:%M:%S.%f'
- return: HTTP_200_OK | HTTP_400_BAD_REQUEST
- 만든이 : snchoi


### GET api/sensorvalue/?email=str(이메일)&name=str(센서이름)

- DRF
- 센서값 조회
- return: SENSOR[{id: int(pk), email: str(이메일), name: str(센서이름), value: int(센서값), reg_date: str(등록일-> 형식:2020-12-15T11:01:25.518280)}]
- 만든이 : snchoi



### GET api/all-grocery-name/

- DRF
- 전채 식재료 조회
- return: ALL_GROCERY[{id: int(식재료 번호), name: str(식재료 이름)},{}]
- 만든이 : snchoi



### GET api/user-input-grocery/?gubun=int&email=str

- DRF
- 사용자 냉장고 재료 조회(직접입력, 이미지 인식 구분하여 조회)
- **parameter**: 
  - gubun = int(1(이미지 인식) or 2(직접입력)) 
  - email = str(사용자email)
- return  : GROCERY [{"id": int, "email": str, "all_grocery_id": int,  "name": str, "count": int, "reg_date": str(date), "gubun": int, "coordinate": "str(list)", "expiration_date": str(0000-00-00) },{}]
- 만든이 : snchoi



### GET api/grocery-count/?email=str&all_grocery_id=int

- DRF
- 특정 식재료 갯수 조회
- **parameter**: 
  - email = str(사용자email)
  - all_grocery_id = int(전체식재료id)
- return  : {"count": int(갯수)}
- 만든이 : snchoi



### 1) GET api/user-input-grocery/?email=str

### 2) GET api/user-input-grocery/?email=str&gubun=int

- DRF
- 1) 사용자 냉장고 재료 조회(구분 없이 전체 재료 조회)
- 2) 사용자 냉장고 재료 조회(이미지인식/직접입력 구분하여 )
- **parameter**: 
  - gubun = int(1(이미지 인식) or 2(직접입력)) 
  - email = str(사용자email)
- return  : GROCERY [{"id": int, "email": str, "all_grocery_id": int,  "name": str, "count": int, "reg_date": str(date), "gubun": int, "coordinate": "str(list)", "expiration_date": str(0000-00-00)},{}]
- 만든이 : snchoi



### POST api/user-input-grocery/

- DRF
- 재료 직접 입력 삽입
- **body** : GROCERY {"email": str, "all_grocery_id": int, "name": str, "count": int, "expiration_date": str(유통기한)}
- date형식 "2020-12-24"
- return : HTTP_201_CREATED | HTTP_400_BAD_REQUEST
- 만든이 : snchoi



### PUT api/user-input-grocery/

- DRF
- 재료 직접 입력 수정
- **body** : GROCERY {"email": str, "all_grocery_id": int, "name": str, "count": int, "expiration_date": str(0000-00-00)}
- return : HTTP_201_CREATED | HTTP_400_BAD_REQUEST
- 만든이 : snchoi



### DELETE api/user-input-grocery/?email=str&all_grocery_id=int

- DRF
- 재료 직접 입력 삭제
- **parameter** 
  - "email": str(사용자email)
  - "all_grocery_id": int(식재료id)
- return : HTTP_201_CREATED | HTTP_400_BAD_REQUEST
- 만든이 : snchoi





### PUT api/insert-email-to-fridge/ 

- DRF
- 존재하는 냉장고 정보라면, 사용자 저장 / 존재하지 않는 냉장고 정보라면 오류
- **body**: {fridge_number: str, email: str}
- return: HTTP_201_CREATED| HTTP_404_NOT_FOUND
- 만든이 : snchoi



### PUT api/going-out-mode/

- DRF
- 외출 모드 ON OFF 변경
- **body**: {email: str(이메일), outing_mode: int(외출모드 ,default=0)}
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST
- 만든이 : snchoi


### PUT api/alarm-mode/

- DRF
- 알림 모드 ON OFF 변경
- **body**: {email: str(이메일), alarm_mode: int(알림모드 ,default=0)}
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST
- 만든이 : snchoi



### PUT api/follow/

- DRF
- 팔로우 / 언팔로우 
- 클릭시 > 현재와 반대 값으로 업데이트 (인스타에서 하트 누르면 팔로우, 다시 누르면 언팔로우)
- **body**: {email: str(이메일), following_user_id: str(팔로잉하는 친구의 email}
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST
- 만든이 : snchoi



### GET api/follow-userinfo/?email=str

- DRF
- 이메일 조회시 해당 사용자 정보 조회
- **parameter**: email = str(친구 이메일)
- return: 
    {
        "email": str(이메일),
        "age": int(나이),
        "sex": int(성별),
        "phone_number": str(핸드폰번호),
        "name": str(이름),
        "guardian_name": str(보호자이름),
        "guardian_phone_number": str(보호자번호),
        "purpose": str(목적 - 다이어트 등등),
        "img_url": str(프로필 사진 이미지),
        "alarm_mode": int(알림모드) -> default 0,
        "outing_mode": int(외출모드) -> default 0,
        "motion_period" : int(모션센서 알림 설정기간) -> default 1
    }
- 만든이 : snchoi



### GET api/follow-latest-photo/?email=str

- DRF
- 팔로우 된 상태일 때 친구 냉장고 가장최근 사진 조회 (조건: read안읽은 순으로)
- //클릭시 > 현재와 반대 값으로 업데이트 (인스타에서 하트 누르면 팔로우, 다시 누르면 언팔로우)
- **parameter**: email = str(내 이메일)
- return: [{"email": str(친구 이메일), "url": str(친구 사진url), "reg_date": str(친구 사진 등록날짜), "name": str(친구이름), "img_url": str(프로필사진), "sex": int(성별), "read":boolean(읽음여부)}.{}]
- 만든이 : snchoi



### PUT api/follow-read/

- DRF
- 사진 읽음 표시, read=True로 변함
- **body**: {email: str(내 이메일), following_user_id: str(팔로잉하는 친구의 email}
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST
- 만든이 : snchoi



### POST api/sign-up/

- DRF
- 회원가입
- **body**: {email: str(이메일), age: int(나이), sex: int(성별), phone_number: str(핸드폰번호000-0000-0000형식으로 받아주세용), name: str(이름), password: str(비밀번호), guardian_name: str(보호자이름), guardian_phone_number: str(핸드폰번호000-0000-0000형식으로 받아주세용), purpose: str(목적-다이어트, 당뇨 등등)}
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST
- 만든이 : snchoi



### POST api/sign-in/

- DRF
- 로그인
- **body**: {email: str(이메일),  password: str(비밀번호)}
- return: HTTP_200_OK, token값(일치하는 경우) | HTTP_401_UNAUTHORIZED(비밀번호가 다른 경우) | HTTP_400_BAD_REQUEST(이메일 존재하지 않을 경우)
- 만든이 : snchoi


### PUT api/user-modify/

- DRF
- 회원정보 수정 (이메일, 비밀번호는 변경하지 않음)
- - **body**: {email: str(이메일), age: int(나이), sex: int(성별), phone_number: str(핸드폰번호000-0000-0000형식으로 받아주세용), name: str(이름), guardian_name: str(보호자이름), guardian_phone_number: str(핸드폰번호000-0000-0000형식으로 받아주세용), purpose: str(목적-다이어트, 당뇨 등등)}
- return: HTTP_200_OK | HTTP_400_BAD_REQUEST
- 만든이 : snchoi


### POST api/token-check/

- DRF
- 토큰 체크(인가된 사용자인지 확인)
- **body**: {token: str(토큰값)}
- return: HTTP_200_OK, token값(인가된 사용자일 경우) | HTTP_403_FORBIDDEN(인가된 사용자가 아닐 경우)
- 만든이 : snchoi


### GET api/register-check/?emails=str

- DRF
- 냉장고 번호 등록 시 이미 등록한 사람이지 체크
- **parameter**: 
  - email = str(이메일)
- {"result": false / true}
- 만든이 : snchoi





### PUT api/recipe-favorite/

- DRF
- 레시피 즐겨찾기 등록 / 취소 
  - 즐겨찾기 여부 확인 > 즐겨찾기 했다면 > 클릭시 즐겨찾기 취소
  - 즐겨찾기 여부 확인 > 즐겨찾기 하지 않았다면 > 클릭시 즐겨찾기 추가
- **body**: {email: str(내 이메일), all_recipe_id: int(레시피id)}
- return: HTTP_201_CREATED| HTTP_400_BAD_REQUEST
- 만든이 : snchoi



### GET api/recipe-favorite/?email=str

- DRF
- 즐겨찾기한 레시피 조회
- **parameter**: 
  - email = str(이메일)
- return: ALL_RECIPE [{ "id": int(pk),
      "name": str(레시피 이름),
      "ingredient": str(재료),
      "ingredient_name": str(재료 이름),
      "seasoning": str(양념),
      "seasoning_name": str(양념 이름),
      "howto": str(방법),
      "purpose": str(목적),
      "views": int(조회수),
      "img": str(레시피 이미지),
      "recipe_num": int(만개의 레시피 고유번호),
      "all_recipe_id": int(전체레시피 id값),
      "email": str(사용자이메일)}, {}]
- 만든이 : snchoi




### GET api/recomm-recipe-detail/?all_recipe_id=int

- DRF
- 레세피 조회 상세보기
- **parameter**: 
  - all_recipe_id = str(레시피id)
- return: ALL_RECIPE {
  "id": int(레시피id),
  "name": str(레시피 이름),
  "ingredient": str(재료),
  "ingredient_name": str(재료 이름),
  "seasoning": str(양념),
  "seasoning_name": str(양념 이름),
  "howto": str(방법),
  "purpose": str(목적),
  "views": int(조회수),
  "img": str(레시피 이미지),
  "recipe_num": int(만개의 레시피 고유번호)
  }
- 만든이 : snchoi


### POST api/grocery-alarm/

- DRF
- 식재료 알림 등록
- **body**: {email: str(내 이메일), all_grocery_id: int(식재료id), count: int(해당재료가 몇개일 때 알림받을지)}
- return: HTTP_201_CREATED| HTTP_400_BAD_REQUEST
- 만든이 : snchoi



### PUT api/grocery-alarm/

- DRF
- 식재료 알림 수정
- **body**: {email: str(내 이메일), all_grocery_id: int(식재료id), count: int(해당재료가 몇개일 때 알림받을지)}
- return: HTTP_201_CREATED| HTTP_400_BAD_REQUEST
- 만든이 : snchoi



### DELETE api/grocery-alarm/?email=str&all_grocery_id=int

- DRF
- 식재료 알림 삭제
- **parameter**
  - email: str(내 이메일)
  - all_grocery_id: int(식재료id)
- return: HTTP_201_CREATED| HTTP_400_BAD_REQUEST
- 만든이 : snchoi



### GET api/grocery-alarm/?email=str

- DRF
- 사용자별 식재료 알림 조회
- **parameter**: 
  - email = str(이메일)
- return: ALARM [
      [{
          "id": 3,
          "email": "sn0716@naver.com",
          "all_grocery_id": 12,
          "count": 2
      }, {}]
- 만든이 : snchoi


### 추천레시피 저장

- 추천레시피 조회시 호출되도록 구현
- 문의 사항 -> 최수녕, 류제룡


### 추천레시피 조회  api/recomm-recipe/?email=str

- DRF
- 사용자별 추천레시피 조회
- **parameter**: 
  - email = str(이메일)
- return: RECOMM_RECIPE [{
  "id": pk,
  "email": str(사용자아이디),
  "all_recipe_id": int(전체레시피pk),
  "name": str(레시피이름),
  "ingredient": str(재료종류 - 여러가지),
  "ingredient_name": str(재료이름),
  "seasoning": str(소스이름 + 양까지),
  "seasoning_name": str(소스이름만),
  "howto": str(방법),
  "purpose": str(목적),
  "views": int(조회수),
  "img": str(레시피이미지url),
  "recipe_num": int(레시피번호)
  }, {}]
- 만든이 : snchoi



### 목적에 맞는 추천레시피 조회  api/recomm-recipe-purpose/?email=str

- DRF
- 사용자별 목적에 맞는 추천레시피 조회
- **parameter**: 
  - email = str(이메일)
- return: RECOMM_RECIPE [{
  "id": pk,
  "email": str(사용자아이디),
  "all_recipe_id": int(전체레시피pk),
  "name": str(레시피이름),
  "ingredient": str(재료종류 - 여러가지),
  "ingredient_name": str(재료이름),
  "seasoning": str(소스이름 + 양까지),
  "seasoning_name": str(소스이름만),
  "howto": str(방법),
  "purpose": str(목적),
  "views": int(조회수),
  "img": str(레시피이미지url),
  "recipe_num": int(레시피번호)
  }, {}]
- 리턴 값 없을 경우 []
- 만든이 : snchoi



### 추천레시피 랜덤으로 1개만 조회 api/recomm-recipe-one/?email=str

- DRF
- 사용자별 추천레시피 랜덤으로 1개만 조회(메인페이지 사용)
- **parameter**: 
  - email = str(이메일)
- return: RECOMM_RECIPE {
  "id": pk,
  "email": str(사용자아이디),
  "all_recipe_id": int(전체레시피pk),
  "name": str(레시피이름),
  "ingredient": str(재료종류 - 여러가지),
  "ingredient_name": str(재료이름),
  "seasoning": str(소스이름 + 양까지),
  "seasoning_name": str(소스이름만),
  "howto": str(방법),
  "purpose": str(목적),
  "views": int(조회수),
  "img": str(레시피이미지url),
  "recipe_num": int(레시피번호)
  }
- 만든이 : snchoi



### POST api/answer-save/

- DRF
- 음성챗봇-재료몇개 (기존 재료 기반으로 데이터 저장) > 냉장고 문 닫힐시 호출 (3초)
- **body**: {email: str(내 이메일)}
- return: HTTP_201_CREATED| HTTP_400_BAD_REQUEST
- 만든이 : jr


### GET api/answer-count/?email=str&query=str

- DRF
- 사용자별 식재료 알림 조회 > 음성챗봇으로 재료 몇개인지 물어볼 때 호출(2초)
- **parameter**: 
  - email = str(이메일)
  - query = str(질문) > 가지몇개야?
- return: ANSWER_COUNT {"result":"가지는3개입니다."}
- 만든이 : jr
