# Die vorher installierte Python Umgebung aktivieren
. .venv/bin/activate

# yzhuang/Meta-Llama-3-8B-Instruct_fictional_arc_German_v2
streamlit run chatbot/chatbot_app.py -- --model openchat-3.6 --max-new-tokens 1024

# streamlit run chatbot/chatbot_app.py -- --model "yzhuang/Meta-Llama-3-8B-Instruct_fictional_arc_German_v2" --max-new-tokens 1024