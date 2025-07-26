# scripts/apply_mongo_config.py (CI/CD 전용 버전)
import os
import sys
import yaml
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure


# 스크립트 파일의 절대 경로를 가져옴
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 설정 파일의 절대 경로를 계산
DEFAULT_CONFIG_PATH = os.path.join(SCRIPT_DIR, 'mongo_config.yml')

def load_config(config_path: str) -> dict:
    """YAML 설정 파일을 로드하여 'databases' 섹션을 반환합니다."""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f).get('databases', {}) or {}
    except FileNotFoundError:
        print(f"오류: 설정 파일 '{config_path}'을(를) 찾을 수 없습니다.", file=sys.stderr)
        sys.exit(1)

def get_mongo_client() -> MongoClient:
    """환경 변수에서 URI를 가져와 MongoDB 클라이언트를 반환합니다."""
    mongo_uri = os.getenv('MONGO_URI')
    if not mongo_uri:
        print("오류: MONGO_URI 환경 변수가 설정되지 않았습니다.", file=sys.stderr)
        sys.exit(1)
    
    try:
        client = MongoClient(mongo_uri)
        client.admin.command('ping') # 연결 테스트
        return client
    except ConnectionFailure as e:
        print(f"오류: MongoDB 연결 실패 - {e}", file=sys.stderr)
        sys.exit(1)

def sync_collections_for_db(db: any, desired_collections: list):
    """단일 데이터베이스 내의 컬렉션들을 동기화합니다."""
    print(f"--- 데이터베이스 '{db.name}' 처리 중 ---")
    try:
        current_collections = set(db.list_collection_names())
    except OperationFailure:
        # DB가 아직 존재하지 않아 컬렉션 목록을 가져올 수 없을 때
        current_collections = set()
        
    desired_set = set(desired_collections or [])

    # 삭제할 컬렉션 처리
    for col_name in current_collections - desired_set:
        print(f"  🔥 컬렉션 '{col_name}'을(를) 삭제합니다.")
        db.drop_collection(col_name)

    # 생성할 컬렉션 처리
    for col_name in desired_set - current_collections:
        print(f"  ✨ 컬렉션 '{col_name}'을(를) 생성합니다.")
        db.create_collection(col_name)

    if (current_collections == desired_set):
        print("  👍 모든 컬렉션이 설정과 일치합니다.")


def main():
    """메인 동기화 로직을 실행합니다."""
    
    # 설정 및 클라이언트 준비
    desired_schema = load_config('scripts/mongo_config.yml')
    client = get_mongo_client()
    print("✅ MongoDB 연결 성공 및 설정 파일 로드 완료.")

    try:
        # 1. 데이터베이스 레벨 동기화
        desired_dbs = set(desired_schema.keys())
        # 시스템 DB는 비교 대상에서 제외
        current_dbs = set(client.list_database_names()) - {'admin', 'local', 'config'}
        
        # 삭제할 데이터베이스 처리
        for db_name in current_dbs - desired_dbs:
            print(f"🔥 데이터베이스 '{db_name}'을(를) 삭제합니다 (설정 파일에 없음).")
            client.drop_database(db_name)

        # 2. 컬렉션 레벨 동기화 (각 DB별로)
        for db_name, desired_collections in desired_schema.items():
            sync_collections_for_db(client[db_name], desired_collections)

        print("\n✅ 모든 동기화 작업이 성공적으로 완료되었습니다.")

    except Exception as e:
        print(f"오류: 심각한 예외 발생 - {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if client:
            client.close()
            print("\nMongoDB 연결을 종료합니다.")


if __name__ == "__main__":
    # 자동화 환경에서 직접 실행
    main()
