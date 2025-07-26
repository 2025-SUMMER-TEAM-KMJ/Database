# 마스터 사용자 프로필 스키마 (master_user_profile.schema.json)

사용자 정보를 표준화하여 저장하기 위한 마스터 스키마입니다. 개인 정보, 학력, 경력, 보유 역량 등을 포함합니다.

---

### 주요 필드 설명

- **`name`** (string, **필수**): 이름.
- **`age`** (integer, **필수**): 나이.
- **`gender`** (string, **필수**): 성별.
- **`email`** (string, **필수**): 이메일.
- **`phone`** (string, **필수**): 연락처.
- **`education`** (array of objects): 학력 정보 목록.
- **`workExperience`** (array of objects): 경력 정보 목록.
- **`experience`** (array of objects): 프로젝트, 대외활동 등 기타 경험 목록.
- **`competencies`** (array of strings): 보유 역량 (기술 스택, 소프트 스킬 등) 목록.
- **`preferredPosition`** (array of objects): 희망 직무/직군 목록.
- **`certifications`** (array of objects): 자격증 및 수상 내역.
- **`personalNarratives`** (object): 개인 서술 (성격, 가치관 등).

---

### Python 클래스 활용

`main.py`의 `MasterUserProfile` 클래스를 사용하여 이 스키마를 따르는 데이터를 생성하고 검증할 수 있습니다.

```python
from main import MasterUserProfile

# 딕셔너리로부터 객체 생성
user_data = {
    "name": "홍길동",
    "age": 28,
    "gender": "Male",
    "email": "gildong@example.com",
    "phone": "010-1234-5678"
}

instance = MasterUserProfile.from_dict(user_data)
print(instance)
```