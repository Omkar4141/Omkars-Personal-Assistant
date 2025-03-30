def get_ai_response(user_input):
    """
    Generates a response from the AI model based on user input and conversation history.
    
    Args:
    - user_input (str): The user's message.
    
    Returns:
    - str: The AI's response.
    """
    global conversation_history

    # Handle basic greetings
    greetings = ["hi", "hello", "hey", "hola", "namaste"]
    user_input_lower = user_input.lower().strip()

    if any(user_input_lower.startswith(greet) for greet in greetings):
        return "Hello! How can I assist you with information about Omkar Lokhande today?"

    # Combine custom prompt, conversation history, and new user input
    context = "\n".join([custom_prompt] + conversation_history + [f"User: {user_input}"])

    # Invoke the model to generate a response based on the context
    response = model.invoke(context)

    # Get the model's response content
    ai_response = response.content

    # Check if the response is unrelated to Omkar
    if "I'm sorry, I can only provide information about Omkar Lokhande" in ai_response:
        ai_response = "I'm sorry, I can only provide information about Omkar Lokhande. Please ask about Omkar."

    # Add user input and AI response to the conversation history
    conversation_history.append(f"User: {user_input}")
    conversation_history.append(f"AI: {ai_response}")

    return ai_response
