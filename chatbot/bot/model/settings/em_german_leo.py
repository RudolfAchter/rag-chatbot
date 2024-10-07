from bot.model.model import Model

# https://huggingface.co/jphme/em_german_13b_leo_gguf
class EmGermanLeoSettings(Model):
    url = "https://huggingface.co/jphme/em_german_13b_leo_gguf/resolve/main/em_german_13b_leo_Q4_K_S.gguf"
    file_name = "em_german_13b_leo_Q4_K_S.gguf"
    config = {
        "n_ctx": 4096,  # The max sequence length to use - note that longer sequence lengths require much more resources
        "n_threads": 8,  # The number of CPU threads to use, tailor to your system and the resulting performance
        "n_gpu_layers": 32,  # The number of layers to offload to GPU, if you have GPU acceleration available
    }
    config_answer = {"temperature": 0.7}
