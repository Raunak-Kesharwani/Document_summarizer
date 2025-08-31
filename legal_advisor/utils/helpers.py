import re 
from langchain.schema import Document

class Cleaner:

    def __init__(self, docs: list[Document] | str):
        self.docs = docs

    def combiner(self):
        if isinstance(self.docs, list):
            text = ""
            for content in self.docs:
                text += content.page_content + " "
            self.docs = text
        return self   

    def clean_legal_text(self):
        """Clean and normalize legal text. Works on self.docs string."""

        if not isinstance(self.docs, str):
            raise TypeError("clean_legal_text requires self.docs to be a string. Run combiner() first.")

        text = self.docs

        # 1. Remove page markers
        text = re.sub(r'Page \d+ of \d+', '', text, flags=re.IGNORECASE)

        # 2. Remove fractions like "12/36"
        text = re.sub(r'\b\d+\s*/\s*\d+\b', '', text)

        # 3. Remove repeating boilerplate
        text = re.sub(r'\b(Confidential|Draft|Proprietary)\b', '', text, flags=re.IGNORECASE)

        # 4. Remove newlines
        text = text.replace("\n", " ")

        # 5. Remove dots/underscores/symbols
        text = re.sub(r'[_*•·]+', ' ', text)
        text = re.sub(r'\.{2,}', '.', text)

        # 6. Normalize spaces
        text = re.sub(r'\s+', ' ', text)

        # 7. Remove non-ASCII if needed
        text = re.sub(r'[^\x00-\x7F]+', '', text)

        self.docs = text.strip()
        return text.strip()