# 크롤러 로그 스키마 (master_crawler_log.schema.json)

크롤러가 수집해야 할 URL과 각 URL의 처리 상태를 기록하기 위한 스키마입니다.

---

### 주요 필드 설명

- **`urls`** (array of objects): URL과 처리 상태 객체의 목록.
  - `url` (string, **필수**): 수집 대상의 전체 URL.
  - `crawled` (array of strings, **필수**): 해당 URL에서 성공적으로 파싱한 데이터의 목적 목록 (예: `["job_posting", "company_profile"]`).

---

### Python 클래스 활용

`main.py`의 `MasterCrawlerLog` 클래스를 사용하여 이 스키마를 따르는 데이터를 생성하고 검증할 수 있습니다.

```python
from main import MasterCrawlerLog

# 딕셔너리로부터 객체 생성
log_data = {
    "urls": [
        {"url": "https://example.com/job/1", "crawled": ["job_posting"]},
        {"url": "https://example.com/job/2", "crawled": []}
    ]
}

instance = MasterCrawlerLog.from_dict(log_data)
print(instance)
```