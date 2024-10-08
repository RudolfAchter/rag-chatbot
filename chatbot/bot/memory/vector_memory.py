from typing import Any, Dict, List, Tuple

from cleantext import clean
from helpers.log import get_logger
from langchain.vectorstores import Chroma
from langchain_core.documents import Document

logger = get_logger(__name__)


class VectorMemory:
    """
    Class for managing vector memory operations.

    Parameters:
    -----------
    embedding : Any
        The embedding object used for vectorization.

    verbose : bool, optional
        Whether to enable verbose mode (default is False).

    """

    def __init__(self, vector_store_path: str, embedding: Any, verbose=False) -> None:
        self.embedding = embedding
        self.verbose = verbose

        if self.embedding is None:
            logger.error("No embedder passed to VectorMemory")
            raise Exception("No embedder passed to VectorMemory")

        self.index = self.load_memory_index(vector_store_path)

    def load_memory_index(self, vector_store_path: str) -> Chroma:
        """
        Loads the Chroma memory index from the given vector store path.

        Parameters:
        -----------
        vector_store_path : str
            The path to the vector store.

        Returns:
        -------
        Chroma
            The loaded Chroma memory index.

        """
        # FIXME https://github.com/langchain-ai/langchain/issues/10864
        # https://github.com/rajib76/langchain_examples/blob/main/examples/how_to_execute_retrievalqa_chain.py
        # https://app.semanticdiff.com/gh/langchain-ai/langchain/pull/16969/changes#libs/community/langchain_community/vectorstores/chroma.py?ignore_comments=false
        # SIEHE site-packages/langchain_community/vectorstores/chroma.py -> _select_relevance_score_fn
        index = Chroma(persist_directory=str(vector_store_path), 
                       embedding_function=self.embedding,
                       collection_metadata={"hnsw:space": "ip"})
                                                          # (cosine|l2|ip)

        return index

    def similarity_search(
        self, query: str, k: int = 4, threshold: float = 0.2
    ) -> Tuple[List[Document], List[Dict[str, Any]]]:
        """
        Performs similarity search on the given query.

        Parameters:
        -----------
        query : str
            The query string.

        index : Chroma
            The Chroma index to perform the search on.

        k : int, optional
            The number of retrievals to consider (default is 4).

        threshold : float, optional
            The threshold for considering similarity scores (default is 0.2).


        Returns:
        -------
        Tuple[List[Document], List[Dict[str, Any]]]
            A tuple containing the list of matched documents and a list of their sources.

        """
        # `similarity_search_with_score` return docs and scores
        # lower score means better match
        matched_docs = self.index.similarity_search_with_score(query, k=k)


        # filtered_docs_by_threshold = [doc for doc in matched_docs if doc[1] > threshold]
        sorted_matched_docs_by_score = sorted(matched_docs, key=lambda x: x[1], reverse=False)
        retrieved_contents = [doc[0] for doc in sorted_matched_docs_by_score]
        sources = []
        for doc, score in sorted_matched_docs_by_score:
            sources.append(
                {
                    "score": round(score, 3),
                    "document": doc.metadata.get("source"),
                    "content_preview": f"{doc.page_content[0:300]}...",
                }
            )

        return retrieved_contents, sources

    @staticmethod
    def create_memory_index(embedding: Any, chunks: List, vector_store_path: str):
        texts = [clean(doc.page_content, no_emoji=True) for doc in chunks]
        metadatas = [doc.metadata for doc in chunks]
        memory_index = Chroma.from_texts(
            texts=texts,
            embedding=embedding,
            metadatas=metadatas,
            persist_directory=vector_store_path,
        )
        memory_index.persist()
