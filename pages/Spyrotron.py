import streamlit as st
import http.client
import json
import base64

def chatgpt_api(messages, image_bytes=None):
    """
    Makes a request to the ChatGPT API to get a response.
    The API key is hardcoded in this example.
    """
    conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")
    payload_dict = {
        "messages": messages,
        "web_access": False
    }
    # If image is provided, encode as base64 and add to payload
    if image_bytes is not None:
        image_b64 = base64.b64encode(image_bytes).decode("utf-8")
        payload_dict["image"] = image_b64

    payload = json.dumps(payload_dict)
    headers = {
        'x-rapidapi-key': "6af84cfbbfmsh9eec418d4774ab3p1ad704jsn65007407d974",
        'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
        'Content-Type': "application/json"
    }
    conn.request("POST", "/gpt4o", payload, headers)
    res = conn.getresponse()
    data = res.read()
    try:
        response_json = json.loads(data.decode("utf-8"))
        return response_json.get("result", "No response from ChatGPT API.")
    except Exception as e:
        return f"Error: {e}"

def ai_chatbot():
    """
    Renders the AI Chatbot UI and handles the chat logic using the API.
    """
    st.header("AI Chatbot")
    st.write("Chat with our AI assistant below:")

    # Inject CSS to apply border-radius to images
    st.markdown("""
    <style>
        img {
            border-radius: 8%;
        }
    </style>
    """, unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    uploaded_file = st.file_uploader("Upload an image for processing (optional)", type=["png", "jpg", "jpeg"])
    image_bytes = None
    if uploaded_file is not None:
        image_bytes = uploaded_file.read()
        st.image(image_bytes, caption="Uploaded Image", width=100)

    user_input = st.text_input("You:")
    
    if st.button("Send"):
        if user_input or uploaded_file:
            messages = []
            for sender, content in st.session_state.chat_history:
                role = "user" if sender == "You" else "assistant"
                # Add text content from chat history to the API message list
                messages.append({"role": role, "content": content.get("text", "")})
            
            # Create the final message for the current turn. Provide a default prompt
            # if only an image is uploaded.
            current_user_message = user_input if user_input else "Explain this image."
            messages.append({"role": "user", "content": current_user_message})

            response = chatgpt_api(messages, image_bytes)
            
            # Store the user's turn as a single dictionary in chat history
            st.session_state.chat_history.append(("You", {"text": user_input, "image": image_bytes}))
            st.session_state.chat_history.append(("AI", {"text": response}))

    # Display the chat history
    for sender, content in st.session_state.chat_history:
        if sender == "You":
            if content.get("image"):
                # Display the image with a caption
                st.image(content["image"], caption="You: [Image uploaded]", width=100)
            if content.get("text"):
                # Display the text message
                st.markdown(f"**You:** {content['text']}")
        else:
            # Display the AI's response
            st.markdown(f"**AI:** {content['text']}")
            if content.get("image"):
                st.image(content["image"], caption="AI: [Image response]", width=100)