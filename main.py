import asyncio
from src.api.cms_client import CMSClient
from src.api.metadata_client import MetadataClient
from src.core.audit_engine import AuditEngine
from src.core.models import AuditResult
from src.reporting.excel_writer import ExcelReportWriter
from src.utils.logger import logger
import pandas as pd

class AuditProcessor:
    def __init__(self, cms_client: CMSClient, metadata_client: MetadataClient, concurrency_limit: int = 10):
        self.cms_client = cms_client
        self.metadata_client = metadata_client
        self.semaphore = asyncio.Semaphore(concurrency_limit)

    async def process_title(self, title_rank) -> AuditResult:
        async with self.semaphore:
            try:
                metadata = await self.metadata_client.get_metadata(title_rank.title_id)
                return AuditEngine.audit(title_rank, metadata)
            except Exception as e:
                logger.error(f"Failed to process title {title_rank.title_id}: {e}")
                return AuditEngine.create_error_result(title_rank, str(e))

    async def run(self, output_path: str):
        logger.info("Starting Metadata Audit Process...")
        
        ranked_titles = await self.cms_client.get_ranked_titles()
        logger.info(f"Fetched {len(ranked_titles)} titles from CMS.")

        tasks = [self.process_title(title) for title in ranked_titles]
        audit_results = await asyncio.gather(*tasks)

        df = pd.DataFrame([res.dict() for res in audit_results])

        writer = ExcelReportWriter(output_path)
        writer.generate(df)
        
        logger.info(f"Audit report generated successfully at {output_path}")

async def main():
    # Configuration (In production, these would come from env vars)
    CMS_BASE_URL = "https://api.cms.internal"
    METADATA_BASE_URL = "https://api.metadata.internal"
    OUTPUT_FILE = "Premium_Homepage_Audit_Report.xlsx"

    cms_client = CMSClient(CMS_BASE_URL)
    metadata_client = MetadataClient(METADATA_BASE_URL)
    
    processor = AuditProcessor(cms_client, metadata_client)
    await processor.run(OUTPUT_FILE)

if __name__ == "__main__":
    asyncio.run(main())
