# 자소서 스키마 (jobkorea_cover_letter.schema.json)

AI 학습 데이터로 사용될 자기소개서 데이터의 구조를 정의하는 스키마입니다. 지원자의 기본 정보와 자기소개서 문항 및 답변을 포함합니다.

---

### 주요 필드 설명

- **`status`** (string): 합격/불합격 여부. (`accepted`, `rejected`, `unknown`)
- **`companyName`** (string, **필수**): 지원한 기업의 이름.
- **`positionName`** (string, **필수**): 지원한 직무의 이름.
- **`applicationAt`** (string): 지원한 시기 (예: `2025-07-01`).
- **`applicant`** (array of strings, **필수**): 지원자의 특징을 나타내는 키워드 목록 (예: `["컴퓨터공학", "Python"]`).
- **`essays`** (array of objects, **필수**): 자기소개서 문항과 답변의 목록.
  - `question` (string, **필수**): 자소서 문항.
  - `answer` (string, **필수**): 문항에 대한 답변.
  - `maxLength` (integer): 문항의 최대 글자 수 제한.
- **`metadata`** (object, **필수**): 데이터 수집에 대한 메타 정보.
  - `source` (string, **필수**): 데이터 출처.
  - `sourceUrl` (string, **필수**): 원본 데이터 URL.
  - `crawledAt` (string, **필수**): 수집 시각.
- **`sourceData`** (object or string, **필수**): 파싱 전의 원본 데이터.

---

### Python 클래스 활용

`main.py`의 `JobkoreaCoverLetter` 클래스를 사용하여 이 스키마를 따르는 데이터를 생성하고 검증할 수 있습니다.

```python
from main import JobkoreaCoverLetter

# 딕셔너리로부터 객체 생성
cover_letter_data = {
    "companyName": "구글",
    "positionName": "소프트웨어 엔지니어",
    "applicant": ["CS 전공", "알고리즘"],
    "essays": [{"question": "왜 구글인가요?", "answer": "..."}],
    "metadata": {
        "source": "Jobkorea",
        "sourceUrl": "https://example.com",
        "crawledAt": "2025-07-25T12:00:00Z"
    },
    "sourceData": "..."
}

instance = JobkoreaCoverLetter.from_dict(cover_letter_data)
print(instance)
```