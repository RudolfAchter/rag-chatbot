ln -s ~/git/uni_passau/basisdienste_docs/ basisdienste_docs

# Die vorher installierte Python Umgebung aktivieren
. .venv/bin/activate

# Die Dokumente sammeln
python chatbot/memory_builder.py --chunk-size 1000