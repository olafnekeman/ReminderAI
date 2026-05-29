import streamlit as st

from dashboard.core import backend


def main() -> None:
    st.set_page_config(
        page_title="Chat",
        page_icon="⚡",
        layout="wide",
    )
    st.title("Chat")

    text = st.text_input("Enter your message")
    if st.button("Send"):
        message = backend.create_message(text)
        st.write(message)


if __name__ == "__main__":
    main()
