from src.core.models import TitleRank, MetadataResponse, AuditResult

class AuditEngine:
    @staticmethod
    def audit(title: TitleRank, metadata: MetadataResponse) -> AuditResult:
        imdb_id = metadata.imdb_id or "MISSING"
        trailer_url = metadata.trailer_url or "MISSING"
        summary_exists = bool(metadata.summary_text)
        
        # Audit Status Logic
        if imdb_id != "MISSING" and trailer_url != "MISSING":
            status = "Complete"
        elif imdb_id == "MISSING" and trailer_url == "MISSING":
            status = "Missing Both"
        elif imdb_id == "MISSING":
            status = "Missing IMDB"
        else:
            status = "Missing Trailer"

        # Gap Analysis Logic: summary exists but assets missing
        is_gap = title.has_summary and (imdb_id == "MISSING" or trailer_url == "MISSING")

        return AuditResult(
            rank=title.rank,
            title_name=title.display_name,
            content_type=title.content_type.value,
            imdb_id=imdb_id,
            trailer_url=trailer_url,
            summary_status=summary_exists,
            audit_status=status,
            is_gap=is_gap
        )

    @staticmethod
    def create_error_result(title: TitleRank, error_msg: str) -> AuditResult:
        return AuditResult(
            rank=title.rank,
            title_name=title.display_name,
            content_type=title.content_type.value,
            imdb_id="ERROR",
            trailer_url="ERROR",
            summary_status=False,
            audit_status=f"Data Error: {error_msg}",
            is_gap=False
        )
