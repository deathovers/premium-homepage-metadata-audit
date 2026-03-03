import pandas as pd
from src.utils.logger import logger

class ExcelReportWriter:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def generate(self, df: pd.DataFrame):
        try:
            with pd.ExcelWriter(self.file_path, engine='openpyxl') as writer:
                # Filter and write Movies
                movies_df = df[df['content_type'] == 'MOVIE'].drop(columns=['content_type'])
                movies_df.to_sheet(writer, sheet_name='Movies', index=False)

                # Filter and write Shows
                shows_df = df[df['content_type'] == 'SHOW'].drop(columns=['content_type'])
                shows_df.to_sheet(writer, sheet_name='Shows', index=False)
                
            logger.info(f"Excel report saved to {self.file_path}")
        except Exception as e:
            logger.error(f"Failed to generate Excel report: {e}")
            raise

# Monkey patch to handle empty dataframes or specific formatting if needed
def to_sheet(df, writer, sheet_name, index=False):
    df.to_excel(writer, sheet_name=sheet_name, index=index)
pd.DataFrame.to_sheet = to_sheet
