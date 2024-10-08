from bot.model.model import Model

# https://huggingface.co/jphme/em_german_13b_leo_gguf
class EmGermanLeoMistralSettings(Model):
    # https://huggingface.co/MaziyarPanahi/em_german_leo_mistral-Mistral-7B-Instruct-v0.2-slerp-GGUF/resolve/main/em_german_leo_mistral-Mistral-7B-Instruct-v0.2-slerp.Q6_K.gguf
    # url = "https://huggingface.co/TheBloke/em_german_leo_mistral-GGUF/resolve/main/em_german_leo_mistral.Q5_K_M.gguf"
    url = "https://huggingface.co/MaziyarPanahi/em_german_leo_mistral-Mistral-7B-Instruct-v0.2-slerp-GGUF/resolve/main/em_german_leo_mistral-Mistral-7B-Instruct-v0.2-slerp.Q6_K.gguf"
    file_name = "em_german_leo_mistral-Mistral-7B-Instruct-v0.2-slerp.Q6_K.gguf"
    config = {
        "n_ctx": 4096,  # The max sequence length to use - note that longer sequence lengths require much more resources
        "n_threads": 8,  # The number of CPU threads to use, tailor to your system and the resulting performance
        "n_gpu_layers": 32,  # The number of layers to offload to GPU, if you have GPU acceleration available
    }
    config_answer = {"temperature": 0.7}
