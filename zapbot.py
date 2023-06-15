from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia, essa mensagem é automática e foi enviada por um chatbot"
        self.contatos = ["Nascimento"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome()

    def EnviarMensagens(self):
        print('cwicdbwidcb')
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for contato in self.contatos:
            try:
                contato = self.driver.find_element_by_xpath(f'//span[(@title="{contato}"]')
                contato.click()
                chat_box = self.driver.find_element_by_class_name("_3Uu1_")
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
                botao_enviar.click()
                time.sleep(5)
            except Exception as e:
                print(f"Problema ao enviar mensagem para: {contato}")
                print(e)


bot = WhatsappBot()
bot.EnviarMensagens()

#<span dir="auto" title="Álvaro T.I" 
#<div tabindex="-1" class="_3Uu1_">