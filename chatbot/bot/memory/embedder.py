from abc import ABC
from typing import Any

from langchain.embeddings import HuggingFaceEmbeddings


class Embedder(ABC):
    embedder: Any

    def get_embedding(self):
        return self.embedder


class EmbedderHuggingFace(Embedder):
    # https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2
    # https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
    # paraphrase-multilingual-MiniLM-L12-v2 
    def __init__(self, model_name: str = "paraphrase-multilingual-mpnet-base-v2"):
        # default: all-MiniLM-L6-v2 | paraphrase-multilingual-mpnet-base-v2 | paraphrase-multilingual-MiniLM-L12-v2
        self.embedder = HuggingFaceEmbeddings(model_name=model_name)
