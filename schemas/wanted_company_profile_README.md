# 원티드 기업 프로필 스키마 (wanted_company_profile.schema.json)

원티드(Wanted)에서 수집한 기업의 프로필 원본 데이터를 정의하는 스키마입니다.

---

### 주요 필드 설명

- **`companyName`** (string, **필수**): 기업명.
- **`source`** (object, **필수**): 데이터 출처 정보.
  - `url` (string, **필수**): 원본 기업 프로필 URL.
  - `platform` (string): 크롤링 플랫폼.
  - `crawledAt` (string): 크롤링 시각.
- **`profile`** (object): 시스템이 분석한 프로필 정보 (특징, 평균 연봉, 주소 등).
- **`metadata`** (object): 데이터 수집에 대한 표준 메타 정보.
- **`sourceData`** (object or string): 파싱 전의 원본 데이터.

---

### Python 클래스 활용

`main.py`의 `WantedCompanyProfile` 클래스를 사용하여 이 스키마를 따르는 데이터를 생성하고 검증할 수 있습니다.

```python
from main import WantedCompanyProfile

# 딕셔너리로부터 객체 생성
company_data = {
    "companyName": "토스",
    "source": {"url": "https://www.wanted.co.kr/company/123"}
}

instance = WantedCompanyProfile.from_dict(company_data)
print(instance)
```