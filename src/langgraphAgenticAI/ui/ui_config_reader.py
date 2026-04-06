from configparser import ConfigParser

class UIConfigReader:
    def __init__(self, config_file="src/langgraphAgenticAI/ui/ui_config.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_lmm_options(self):
        return self.config['DEFAULT'].get('LMM_OPTIONS', '').split(',')
    
    def get_usecase_options(self):
        return self.config['DEFAULT'].get('USECASE_OPTIONS', '').split(',')

    def get_groq_model_options(self):
        return self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS', '').split(',')
    
    def get_page_title(self):
        return self.config['DEFAULT'].get('PAGE_TITLE')


    