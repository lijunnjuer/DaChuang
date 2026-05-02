class CacheService:
    """缓存与 ETag 管理骨架。"""

    def get(self, key: str):
        return None

    def set(self, key: str, value, ttl: int | None = None):
        return True
