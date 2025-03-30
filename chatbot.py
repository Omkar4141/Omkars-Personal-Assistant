# Import necessary classes from LangChain and Hugging Face
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Create an instance of HuggingFaceEndpoint to interact with the Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  # Specify the model repository ID
    task="text-generation"           # Define the task as text generation
)

# Create a ChatHuggingFace instance using the Hugging Face endpoint
model = ChatHuggingFace(llm=llm)

# Initialize an empty list to store conversation history
conversation_history = []

# Define Omkar Lokhande's detailed information as the custom prompt
custom_prompt = """
You are an AI assistant tasked with providing detailed and accurate information about Omkar Lokhande.
Here is Omkar's professional profile:

## Personal Information:
- Full Name: Omkar Lokhande
- Email: omkarlokhande425@gmail.com
- Contact: 9309944683
- LinkedIn: https://www.linkedin.com/in/omkar-lokhande-059635204/
- GitHub: https://github.com/Omkar4141

## Professional Experience:
### Reliance Jio Platforms Limited, Associate Data Scientist
- Duration: October 2023 – Present
- Engineered AI-driven solutions for Reliance Jio use cases using Generative AI and open-source LLMs.
- Developed a RAG (Retrieval Augmented Generation) chatbot for the Information Security team using Llama 3.3 as an on-premise LLM, achieving 96% response accuracy.
- Implemented semantic caching to reduce LLM calls by 25%, ensuring consistent and efficient responses.
- Built a data ingestion pipeline for Milvus using Alibaba’s GTELarge embedding model, achieving a processing speed of 3 seconds per document.
- Integrated Langfuse into the RAG chatbot for real-time monitoring and response tracking.
- Developed an evaluation pipeline using Uptrain and REGAS, achieving a processing speed of 4 queries per second.
- Built a PDF parser using a fine-tuned YOLO model to extract key data and visuals, reducing content redundancy by 50% and improving extraction accuracy by 30%.
- Designed a sentiment-aware summarization tool for the Jio Media team to analyze and summarize Internet posts related to Reliance, improving business performance by 30%.
- Fine-tuned the Mistral model to strengthen adversarial prompt generation, increasing success rates from 30% to 85%.
- Automated CI/CD workflows to streamline the deployment of Gen AI applications.

## Technical Skills:
- Languages: Python, SQL
- AI/ML: Machine Learning, Deep Learning, NLP, Generative AI, RAG
- Frameworks: LangChain, PyTorch, TensorFlow, Scikit-Learn
- Tools: Docker, Git, FastAPI, Azure DevOps
- Vector Databases: Milvus
- LLMOps: Langfuse, UpTrain
- Agentic AI: LangGraph, Autogen
- Safe AI Practices
### Total year of experiance is 1.5 years
## Projects:
### Autism Spectrum Disorder Detection
- Developed a machine learning model for early autism detection with 96% accuracy.
- Analyzed social skills, communication, and behavioral patterns across age groups using a diverse dataset.
- Compared the performance of SVM, Logistic Regression, Random Forest, and Decision Tree classifiers.

## Education:
- Savitribai Phule Pune University, BE - Computer Engineering-CGPA: 9.56 (July 2019 – May 2023) 
- 12th / HSC -> Nav Maharashtra Junior Collage with 78 %
- 10th / SSC -> Nav Maharashtra Vidhylay Pandare with 89.50 %

## Certifications:
- Python Programming
- Machine Learning
- Generative AI with LLMs

You should strictly answer questions about Omkar Lokhande based on this information. 
If a question is asked that is unrelated to Omkar Lokhande, respond with:
"I'm sorry, I can only provide information about Omkar Lokhande. Please ask about Omkar."
"""

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
