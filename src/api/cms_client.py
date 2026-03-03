from typing import List
from src.api.base_client import BaseClient
from src.core.models import TitleRank, ContentType

class CMSClient(BaseClient):
    async def get_ranked_titles(self) -> List[TitleRank]:
        # In a real scenario, this calls GET /v1/homepage/ranked-titles
        # Mocking response for implementation
        mock_data = [
            {"title_id": "m1", "rank": 1, "content_type": "MOVIE", "has_summary": True, "display_name": "Inception"},
            {"title_id": "s1", "rank": 2, "content_type": "SHOW", "has_summary": True, "display_name": "Breaking Bad"},
            {"title_id": "m2", "rank": 3, "content_type": "MOVIE", "has_summary": True, "display_name": "The Matrix"},
            {"title_id": "m3", "rank": 4, "content_type": "MOVIE", "has_summary": False, "display_name": "Untitled Movie"},
        ]
        return [TitleRank(**item) for item in mock_data]
