from bot.model.model import Model


class Llama3BigSettings(Model):
    # based on META (the Facebook company) Llama: https://huggingface.co/collections/meta-llama/
    # https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF
    # url = "https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"
    url = "https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q6_K.gguf"
    file_name = "Meta-Llama-3.1-8B-Instruct-Q6_K.gguf"
    config = {
        "n_ctx": 8192,  # The max sequence length to use - note that longer sequence lengths require much more resources
        "n_threads": 8,  # The number of CPU threads to use, tailor to your system and the resulting performance
        "n_gpu_layers": 32,  # The number of layers to offload to GPU, if you have GPU acceleration available
    }
    config_answer = {"temperature": 0.7, "stop": []}
