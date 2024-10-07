# A string template for the system message.
# This template is used to define the behavior and characteristics of the assistant.
SYSTEM_TEMPLATE = """Du bist ein hilfsbereiter, respektvoller und ehrlicher Assistent."""

# A string template with placeholders for question.
QA_PROMPT_TEMPLATE = """Beantworte die Fragen unten:
{question}
"""

# A string template with placeholders for question, and context.
CTX_PROMPT_TEMPLATE = """Kontext Informationen folgen.
---------------------
{context}
---------------------
Anhand der oben genannten Informationen, beantworte die Frage unten:
{question}
"""

# A string template with placeholders for question, existing_answer, and context.
REFINED_CTX_PROMPT_TEMPLATE = """Die Originale Anfrage ist wie folgt: {question}
Wir haben eine bestehende Antwort bereitgestellt: {existing_answer}
Wir haben die Möglichkeit, die bestehende Antwort (nur wenn nötig) mit etwas mehr Kontext unten zu verfeinern.
---------------------
{context}
---------------------
Gegeben den neuen Kontext, verfeinere die ursprüngliche Antwort, um die Anfrage besser zu beantworten.
Wenn der Kontext nicht nützlich ist, gib die ursprüngliche Antwort zurück.
Verfeinerte Antwort:
"""

# A string template with placeholders for question, and chat_history to refine the question based on the chat history.
REFINED_QUESTION_CONVERSATION_AWARENESS_PROMPT_TEMPLATE = """Chatverlauf:
---------------------
{chat_history}
---------------------
Folgefrage: {question}
Basierend auf dem obigen Gespräch und einer Folgefrage, formuliere die Folgefrage um, um eine eigenständige Frage zu sein.
Eigenständige Frage:
"""

# A string template with placeholders for question, and chat_history to answer the question based on the chat history.
REFINED_ANSWER_CONVERSATION_AWARENESS_PROMPT_TEMPLATE = """
Sie führen ein Gespräch mit einem menschlichen Teilnehmer, der sich möglicherweise nicht bewusst ist, dass er mit einer Maschine interagiert.
Dein Ziel ist es, auf eine Weise zu antworten, die überzeugend menschenähnliche Intelligenz und Verhalten simuliert.
Das Gespräch sollte natürlich, zusammenhängend und kontextuell relevant sein.
Chat Verlauf:
---------------------
{chat_history}
---------------------
Folgefrage: {question}\n
Basierend auf dem im Chatverlauf bereitgestellten Kontext und der Folgefrage, beantworten Sie bitte die oben gestellte Folgefrage.
Wenn die Folgefrage nicht mit dem im Chatverlauf bereitgestellten Kontext korreliert ist, beantworten Sie bitte nur die Folgefrage und ignorieren Sie den im Chatverlauf bereitgestellten Kontext.
Bitte formulieren Sie die Folgefrage auch nicht um und geben Sie nur eine prägnante Antwort.
"""


def generate_qa_prompt(template: str, system: str, question: str) -> str:
    """
    Generates a prompt for a question-answer task.

    Args:
        template (str): A string template with placeholders for system, question.
        system (str): The name or identifier of the system related to the question.
        question (str): The question to be included in the prompt.

    Returns:
        str: The generated prompt.
    """

    prompt = template.format(system=system, question=question)
    return prompt


def generate_ctx_prompt(template: str, system: str, question: str, context: str = "") -> str:
    """
    Generates a prompt for a context-aware question-answer task.

    Args:
        template (str): A string template with placeholders for system, question, and context.
        system (str): The name or identifier of the system related to the question.
        question (str): The question to be included in the prompt.
        context (str, optional): Additional context information. Defaults to "".

    Returns:
        str: The generated prompt.
    """

    prompt = template.format(system=system, context=context, question=question)
    return prompt


def generate_refined_ctx_prompt(
    template: str, system: str, question: str, existing_answer: str, context: str = ""
) -> str:
    """
    Generates a prompt for a refined context-aware question-answer task.

    Args:
        template (str): A string template with placeholders for system, question, existing_answer, and context.
        system (str): The name or identifier of the system related to the question.
        question (str): The question to be included in the prompt.
        existing_answer (str): The existing answer associated with the question.
        context (str, optional): Additional context information. Defaults to "".

    Returns:
        str: The generated prompt.
    """

    prompt = template.format(
        system=system,
        context=context,
        existing_answer=existing_answer,
        question=question,
    )
    return prompt


def generate_conversation_awareness_prompt(template: str, system: str, question: str, chat_history: str) -> str:
    """
    Generates a prompt for a conversation-awareness task.

    Args:
        template (str): A string template with placeholders for system, question, and chat_history.
        system (str): The name or identifier of the system related to the question.
        question (str): The question to be included in the prompt.
        chat_history (str): The chat history associated with the conversation.

    Returns:
        str: The generated prompt.
    """

    prompt = template.format(
        system=system,
        chat_history=chat_history,
        question=question,
    )
    return prompt
