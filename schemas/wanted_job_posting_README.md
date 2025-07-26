# 원티드 채용 공고 스키마 (wanted_job_posting.schema.json)

원티드(Wanted)에서 수집한 채용 공고 원본 데이터를 정의하는 스키마입니다. 이 데이터는 이후 `master_job_posting` 스키마로 표준화될 수 있습니다.

---

### 주요 필드 설명

- **`metadata`** (object, **필수**): 데이터 수집 메타 정보.
- **`sourceData`** (object or string, **필수**): 원본 데이터.
- **`externalUrl`** (string): 외부 채용 공고로 직접 연결되는 URL.
- **`status`** (string, **필수**): 공고 상태 (`active` 또는 `closed`).
- **`due_time`** (string or null): 공고 마감 시각.
- **`detail`** (object, **필수**): 공고의 상세 내용 (직무, 주요 업무, 자격 요건 등).
- **`company`** (object, **필수**): 공고에 명시된 회사 정보 (이름, 로고, 주소 등).
- **`skill_tags`** (array of strings): 요구 기술 스택 목록.
- **`title_images`** (array of strings): 공고 대표 이미지 URL 목록.

---

### Python 클래스 활용

`main.py`의 `WantedJobPosting` 클래스를 사용하여 이 스키마를 따르는 데이터를 생성하고 검증할 수 있습니다.

```python
from main import WantedJobPosting

# 딕셔너리로부터 객체 생성
job_data = {
    "metadata": {"source": "Wanted", "sourceUrl": "...", "crawledAt": "..."},
    "sourceData": "...",
    "status": "active",
    "detail": {
        "position": {"jobGroup": "개발", "job": "백엔드 개발자"},
        "main_tasks": "API 개발",
        "requirements": "Python 경험"
    },
    "company": {"name": "네이버", "address": {"full_location": "경기도 성남시"}}
}

instance = WantedJobPosting.from_dict(job_data)
print(instance)
```