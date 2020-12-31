'''

Dicas:

Atualize a versão do pip;
Verifique se a versão do Chrome Driver está compatível com a do Google Chrome

Obs.: Há o risco que o nome das classes do navegador mude, em casos de uma refatoração por exemplo...


'''

# Fonte: https://www.youtube.com/watch?v=ISYHWfWvp3E


from selenium import webdriver
import time 


class whatsappBot:
  
    def __init__(self): 
        self.mensagem = "Mensagem de Teste"
        self.grupos = ["Teste","Teste2"] 

     #Configurando as opções do webdriver
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br") 
        self.driver = webdriver.Chrome(executable_path=r'../main/driver/chromedriver.exe')
        

    def EnviarMensagens(self):
         print("Teste")
         self.driver.get("https://web.whatsapp.com/")
         time.sleep(15) # Para por o shortcode
         
         for grupo in self.grupos:                  
          grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
          time.sleep(3)  # Sempre que encontrar um elemento, usa o sleep para dar tempo da página atualizar alguns componentes: classes
          grupo.click()  # Acredito que faça sentido usar o sleep em toda vez que há classe dinâmica               
          time.sleep(3)
          chat_box = self.driver.find_element_by_class_name("_3uMse") # Vai procurar pela classe por ser mais simples
          time.sleep(3)
          chat_box.click() # clicou na área da classe 
          time.sleep(3)
          chat_box.send_keys(self.mensagem) # a mensagem é inserida no campo
          botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")  
          time.sleep(3)
          botao_enviar.click()
          time.sleep(3)

         self.driver.quit()



