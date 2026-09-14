from src.llm import generate_response


question = "When will my package arrive?"

context = """
Question: How long does delivery take?

Answer: Standard delivery usually takes 3 to 5 business days.
Express delivery usually takes 1 to 2 business days.
"""


response = generate_response(
    user_question=question,
    faq_context=context
)

print("\nUser:", question)
print("Bot:", response)
