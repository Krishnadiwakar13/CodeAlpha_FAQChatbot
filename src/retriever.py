import json
import re
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQRetriever:
    """Retrieve relevant FAQs using TF-IDF and cosine similarity."""

    def __init__(self, faq_path: str):
        self.faq_path = Path(faq_path)
        self.faqs = self._load_faqs()

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english"
        )

        self.search_texts = []
        self.search_mapping = []

        for faq_index, faq in enumerate(self.faqs):

            texts = [faq["question"]] + faq.get("variations", [])

            for text in texts:
                self.search_texts.append(
                    self._preprocess(text)
                )

                self.search_mapping.append(faq_index)

        self.question_vectors = self.vectorizer.fit_transform(
            self.search_texts
        )

    def _load_faqs(self):
        """Load FAQ data from JSON."""

        with open(self.faq_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def _preprocess(text: str) -> str:
        """Clean text before vectorization."""

        text = text.lower()

        text = re.sub(
            r"[^a-zA-Z0-9\s]",
            "",
            text
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        ).strip()

        return text

    def retrieve(self, query: str, top_k: int = 3):
        """
        Retrieve the most relevant FAQs.

        Multiple question variations belonging to the same FAQ
        are treated as possible ways a user might ask the question.
        """

        cleaned_query = self._preprocess(query)

        if not cleaned_query:
            return []

        query_vector = self.vectorizer.transform(
            [cleaned_query]
        )

        similarities = cosine_similarity(
            query_vector,
            self.question_vectors
        )[0]

        faq_scores = {}

        for index, score in enumerate(similarities):

            faq_index = self.search_mapping[index]

            if (
                faq_index not in faq_scores
                or score > faq_scores[faq_index]
            ):
                faq_scores[faq_index] = float(score)

        ranked_faqs = sorted(
            faq_scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        results = []

        for faq_index, score in ranked_faqs[:top_k]:

            faq = self.faqs[faq_index]

            results.append(
                {
                    "question": faq["question"],
                    "answer": faq["answer"],
                    "score": score
                }
            )

        return results
