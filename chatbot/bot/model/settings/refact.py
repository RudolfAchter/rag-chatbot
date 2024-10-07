from bot.model.model import Model


class RefactSettings(Model):
    # https://huggingface.co/smallcloudai/Refact-1_6-base/resolve/main/pytorch_model.bin
    url = "https://huggingface.co/smallcloudai/Refact-1_6-base/resolve/main/pytorch_model.bin"
    file_name = "refact_pytorch_model.gguf"
    config = {
        "n_ctx": 4096,  # The max sequence length to use - note that longer sequence lengths require much more resources
        "n_threads": 8,  # The number of CPU threads to use, tailor to your system and the resulting performance
        "n_gpu_layers": 50,  # The number of layers to offload to GPU, if you have GPU acceleration available
    }
    config_answer = {"temperature": 0.7}
