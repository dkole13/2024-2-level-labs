"""
Laboratory Work #4 starter.
"""

# pylint:disable=duplicate-code, too-many-locals, too-many-statements, unused-variable
from lab_4_retrieval_w_clustering.main import (
    DocumentVectorDB,
    get_paragraphs,
    VectorDBAdvancedSearchEngine,
)


def open_files() -> tuple[list[str], list[str]]:
    """
    # stubs: keep.

    Open files.

    Returns:
        tuple[list[str], list[str]]: Documents and stopwords.
    """
    paths_to_texts = [
        "assets/texts/Master_and_Margarita_chapter1.txt",
        "assets/texts/Master_and_Margarita_chapter2.txt",
        "assets/texts/Master_and_Margarita_chapter3.txt",
        "assets/texts/Master_and_Margarita_chapter4.txt",
        "assets/texts/Master_and_Margarita_chapter5.txt",
        "assets/texts/Master_and_Margarita_chapter6.txt",
        "assets/texts/Master_and_Margarita_chapter7.txt",
        "assets/texts/Master_and_Margarita_chapter8.txt",
        "assets/texts/Master_and_Margarita_chapter9.txt",
        "assets/texts/Master_and_Margarita_chapter10.txt",
        "assets/texts/War_and_Peace_chapter1.txt",
        "assets/texts/War_and_Peace_chapter2.txt",
        "assets/texts/War_and_Peace_chapter3.txt",
        "assets/texts/War_and_Peace_chapter4.txt",
        "assets/texts/War_and_Peace_chapter5.txt",
        "assets/texts/War_and_Peace_chapter6.txt",
        "assets/texts/War_and_Peace_chapter7.txt",
        "assets/texts/War_and_Peace_chapter8.txt",
        "assets/texts/War_and_Peace_chapter9.txt",
        "assets/texts/War_and_Peace_chapter10.txt",
    ]
    documents = []
    for path in sorted(paths_to_texts):
        with open(path, "r", encoding="utf-8") as file:
            documents.append(file.read())
    with open("assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    return (documents, stopwords)


def main() -> None:
    """
    Launch an implementation.
    """
    docs, stopwords = open_files()
    documents = ''.join(docs)
    paragraphs = get_paragraphs(documents)
    db = DocumentVectorDB(stopwords)
    db.put_corpus(paragraphs)

    query = "Первый был не кто иной, как Михаил Александрович Берлиоз, председатель правления"
    vector_search_advanced = VectorDBAdvancedSearchEngine(db)
    vector_search_advanced_relevant_documents = vector_search_advanced.retrieve_relevant_documents(
        query, 5)
    print('VectorDBAdvancedSearchEngine relevant documents:',
          vector_search_advanced_relevant_documents)

    result = vector_search_advanced_relevant_documents
    assert result, "Result is None"


if __name__ == "__main__":
    main()
