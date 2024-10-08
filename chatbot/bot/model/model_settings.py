from enum import Enum

from bot.model.settings.llama_3 import Llama3Settings
from bot.model.settings.openchat import OpenChat35Settings, OpenChat36Settings
from bot.model.settings.phi_3 import PhiThreeSettings
from bot.model.settings.stablelm_zephyr import StableLMZephyrSettings
from bot.model.settings.starling import StarlingSettings
from bot.model.settings.refact import RefactSettings
from bot.model.settings.yi_coder_chat import YiCoderSettings
from bot.model.settings.code_qwen_chat import CodeQwenSettings
from bot.model.settings.em_german_leo import EmGermanLeoSettings
from bot.model.settings.em_german_leo_mistral import EmGermanLeoMistralSettings
from bot.model.settings.llama_3_big import Llama3BigSettings

class ModelType(Enum):
    ZEPHYR = "zephyr"
    MISTRAL = "mistral"
    DOLPHIN = "dolphin"
    STABLELM_ZEPHYR = "stablelm-zephyr"
    OPENCHAT_3_5 = "openchat-3.5"
    OPENCHAT_3_6 = "openchat-3.6"
    STARLING = "starling"
    PHI_3 = "phi-3"
    LLAMA_3 = "llama-3"
    LLAMA_3_BIG = "llama-3-big"
    REFACT = "refact"
    YICODER = "yi-coder"
    CODEQWEN = "codeqwen"
    EM_GERMAN_LEO = "em-german-leo"
    EM_GERMAN_LEO_MISTRAL = "em-german-leo-mistral"


SUPPORTED_MODELS = {
    ModelType.STABLELM_ZEPHYR.value: StableLMZephyrSettings,
    ModelType.OPENCHAT_3_5.value: OpenChat35Settings,
    ModelType.OPENCHAT_3_6.value: OpenChat36Settings,
    ModelType.STARLING.value: StarlingSettings,
    ModelType.PHI_3.value: PhiThreeSettings,
    ModelType.LLAMA_3.value: Llama3Settings,
    ModelType.LLAMA_3_BIG.value: Llama3BigSettings,
    ModelType.REFACT.value: RefactSettings,
    ModelType.YICODER.value: YiCoderSettings,
    ModelType.CODEQWEN.value: CodeQwenSettings,
    ModelType.EM_GERMAN_LEO.value: EmGermanLeoSettings,
    ModelType.EM_GERMAN_LEO_MISTRAL.value: EmGermanLeoMistralSettings,
}


def get_models():
    return list(SUPPORTED_MODELS.keys())


def get_model_setting(model_name: str):
    model_settings = SUPPORTED_MODELS.get(model_name)

    # validate input
    if model_settings is None:
        raise KeyError(model_name + " is a not supported model")

    return model_settings
