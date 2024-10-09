# Activate python virtual environment
. .venv/bin/activate

# Start a default chatbot app
streamlit run chatbot/chatbot_app.py -- --model openchat-3.6 --max-new-tokens 1024

# Get Help for the rag-chatbot app
python chatbot/rag_chatbot_app.py -h

# RAG Chatbot
# 
# options:
#   -h, --help            show this help message and exit
#   --model [{stablelm-zephyr,openchat-3.5,openchat-3.6,starling,phi-3,llama-3,llama-3-big,refact,yi-coder,codeqwen,em-german-leo,em-german-leo-mistral}]
#                         Model to be used. Defaults to stablelm-zephyr.
#   --synthesis-strategy [{create-and-refine,tree-summarization,async-tree-summarization}]
#                         Model to be used. Defaults to create-and-refine.
#   --k K                 Number of chunks to return from the similarity search. Defaults to 2.


# Start a rag chatbot app with a specific model
streamlit run chatbot/rag_chatbot_app.py -- --k 8 --model stablelm-zephyr
streamlit run chatbot/rag_chatbot_app.py -- --k 4 --model llama-3
streamlit run chatbot/rag_chatbot_app.py -- --k 8 --model openchat-3.6

# Start a rag chatbot app with a specific model and synthesis strategy
streamlit run chatbot/rag_chatbot_app.py -- --k 8 --model stablelm-zephyr --synthesis-strategy tree-summarization
streamlit run chatbot/rag_chatbot_app.py -- --k 4 --model llama-3 --synthesis-strategy async-tree-summarization
streamlit run chatbot/rag_chatbot_app.py -- --k 8 --model openchat-3.6 --synthesis-strategy create-and-refine



