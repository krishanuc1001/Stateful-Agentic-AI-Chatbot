from configparser import ConfigParser

class UIConfigReader:
    def __init__(self, config_file='ui_config.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config['DEFAULT'].get('PAGE_TITLE', 'Stateful Agentic AI Chatbot')

    def get_lmm_options(self):
        options = self.config['DEFAULT'].get('LMM_OPTIONS', '')
        return [option.strip() for option in options.split(',') if option.strip()]

    def get_usecase_options(self):
        options = self.config['DEFAULT'].get('USECASE_OPTIONS', '')
        return [option.strip() for option in options.split(',') if option.strip()]

    def get_groq_model_options(self):
        options = self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS', '')
        return [option.strip() for option in options.split(',') if option.strip()]