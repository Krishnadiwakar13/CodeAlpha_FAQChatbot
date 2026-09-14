import streamlit as st

from src.retriever import FAQRetriever
from src.llm import generate_response


# Page configuration
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)


# Initialize FAQ retriever
retriever = FAQRetriever("data/faqs.json")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Header
st.title("🤖 FAQ Chatbot")
st.caption(
    "Ask questions and get answers from our FAQ knowledge base."
)


# Sidebar
with st.sidebar:

    st.header("About")

    st.write(
        "This chatbot uses NLP-based FAQ retrieval "
        "with TF-IDF and cosine similarity. "
        "The retrieved FAQ information is then used "
        "by a Groq-hosted LLM to generate a natural response."
    )

    st.divider()

    st.subheader("Features")

    st.write("✓ NLP preprocessing")
    st.write("✓ TF-IDF retrieval")
    st.write("✓ Cosine similarity")
    st.write("✓ Groq LLM")
    st.write("✓ Conversational interface")

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.caption("Built by Krishna Diwakar")


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
user_question = st.chat_input(
    "Ask your question..."
)


if user_question:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_question)


    # Retrieve relevant FAQs
    results = retriever.retrieve(
        user_question,
        top_k=3
    )


    # Check similarity threshold
    if not results or results[0]["score"] < 0.10:

        response = (
            "I'm sorry, but I couldn't find enough information "
            "in the FAQ knowledge base to answer that question. "
            "Please contact customer support for further assistance."
        )

    else:

        # Use the best matching FAQ
        best_faq = results[0]

        faq_context = (
            f"Question: {best_faq['question']}\n"
            f"Answer: {best_faq['answer']}"
        )

        try:

            with st.chat_message("assistant"):

                with st.spinner("Thinking..."):

                    response = generate_response(
                        user_question=user_question,
                        faq_context=faq_context
                    )

                st.markdown(response)

        except Exception:

            response = (
                "I found a relevant FAQ, but I'm unable to "
                "generate a response right now.\n\n"
                f"{best_faq['answer']}"
            )

            with st.chat_message("assistant"):
                st.markdown(response)


    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
