# Clone some Docs repositories
cd docs
git clone https://vcs.zim.uni-passau.de/referat-basisdienste/ansible.git
git clone https://vcs.zim.uni-passau.de/referat-basisdienste/public-docs.git

# activate python virtual environment
. .venv/bin/activate

# Save Docs into memory as "embeddings" for the chatbot
python chatbot/memory_builder.py --chunk-size 1000
