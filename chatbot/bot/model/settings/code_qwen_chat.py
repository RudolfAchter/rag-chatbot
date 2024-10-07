from bot.model.model import Model


class CodeQwenSettings(Model):
    # https://huggingface.co/bartowski/Yi-Coder-9B-Chat-GGUF/resolve/main/Yi-Coder-9B-Chat-Q8_0.gguf
    url = "https://huggingface.co/Qwen/CodeQwen1.5-7B-Chat-GGUF/resolve/main/codeqwen-1_5-7b-chat-q4_0.gguf"
    file_name = "codeqwen-1_5-7b-chat-q4_0.gguf"
    config = {
        "n_ctx": 4096,  # The max sequence length to use - note that longer sequence lengths require much more resources
        "n_threads": 8,  # The number of CPU threads to use, tailor to your system and the resulting performance
        "n_gpu_layers": 32,  # The number of layers to offload to GPU, if you have GPU acceleration available
    }
    config_answer = {"temperature": 0.7}
