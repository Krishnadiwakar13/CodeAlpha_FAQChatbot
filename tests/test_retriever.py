from src.retriever import FAQRetriever


retriever = FAQRetriever("data/faqs.json")


questions = [
    "When will my package arrive?",
    "I want to send something back",
    "Can I get my money back?",
    "I forgot my password",
    "My order came damaged"
]


for question in questions:

    print(f"\nUser: {question}")

    results = retriever.retrieve(question, top_k=1)

    if results:
        result = results[0]

        print(f"Matched FAQ: {result['question']}")
        print(f"Similarity: {result['score']:.3f}")
        print(f"Answer: {result['answer']}")
