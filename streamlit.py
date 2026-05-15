import streamlit as st

from app.graph.blog_graph import create_blog_graph


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Blog Writing Agent",
    page_icon="✍️",
    layout="wide"
)


# ---------------------------------------------------
# GRAPH
# ---------------------------------------------------

graph = create_blog_graph()


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("✍️ AI Blog Writing Agent")

st.caption(
    "Generate complete AI-powered blogs using LangGraph + LangChain"
)


# ---------------------------------------------------
# CHAT HISTORY
# ---------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# ---------------------------------------------------
# DISPLAY OLD MESSAGES
# ---------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------

topic = st.chat_input(
    "Enter your blog topic..."
)


# ---------------------------------------------------
# GENERATE BLOG
# ---------------------------------------------------

if topic:

    # USER MESSAGE

    st.session_state.messages.append({
        "role": "user",
        "content": topic
    })

    with st.chat_message("user"):

        st.markdown(topic)


    # AI MESSAGE

    with st.chat_message("assistant"):

        with st.spinner("Generating Blog..."):

            final_state = graph.invoke({
                "topic": topic
            })

            final_blog = final_state["final_blog"]

            st.markdown(final_blog)


    # SAVE CHAT

    st.session_state.messages.append({
        "role": "assistant",
        "content": final_blog
    })