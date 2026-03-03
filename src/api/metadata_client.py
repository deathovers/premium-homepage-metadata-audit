from src.api.base_client import BaseClient
from src.core.models import MetadataResponse

class MetadataClient(BaseClient):
    async def get_metadata(self, title_id: str) -> MetadataResponse:
        # In a real scenario, this calls GET /v1/metadata/{title_id}
        # Mocking response logic
        mock_db = {
            "m1": {"imdb_id": "tt0137523", "summary_text": "Dreams...", "asset_links": {"trailer": "http://trailer.com/1"}},
            "s1": {"imdb_id": "tt0903747", "summary_text": "Chemistry...", "asset_links": {"trailer": None}},
            "m2": {"imdb_id": None, "summary_text": "Simulation...", "asset_links": {"trailer": "http://trailer.com/2"}},
            "m3": {"imdb_id": None, "summary_text": None, "asset_links": {"trailer": None}},
        }
        data = mock_db.get(title_id, {})
        return MetadataResponse(
            imdb_id=data.get("imdb_id"),
            summary_text=data.get("summary_text"),
            trailer_url=data.get("asset_links", {}).get("trailer")
        )
