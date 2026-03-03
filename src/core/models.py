from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class ContentType(str, Enum):
    MOVIE = "MOVIE"
    SHOW = "SHOW"

class TitleRank(BaseModel):
    title_id: str
    rank: int
    content_type: ContentType
    has_summary: bool
    display_name: str = "Unknown Title"

class MetadataResponse(BaseModel):
    imdb_id: Optional[str] = None
    summary_text: Optional[str] = None
    trailer_url: Optional[str] = None

class AuditResult(BaseModel):
    rank: int
    title_name: str
    content_type: str
    imdb_id: str
    trailer_url: str
    summary_status: bool
    audit_status: str
    is_gap: bool
