from asyncore import loop
import speech_recognition as sr
import os

# funcao para reconhecimento de voz
def ouvir_microfone():
    # habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    # usando o microfone para capturar a fala
    with sr.Microphone() as source:
        # chama o algoritmo de reducao de ruido
        microfone.adjust_for_ambient_noise(source)
        # fala para o usuario falar
        print("Adicionei apenas duas tarefas")
        print("Teste dizendo, abrir o navegador ou abrir o gerenciador de tarefas ")
        print("Diga alguma coisa: ")
        # armazena a informacao que o usuario falou
        audio = microfone.listen(source)
    try:
        # passa a variavel para o algoritmo reconhecedor de padrao de linguagem
        frase = microfone.recognize_google(audio, language='pt-BR')
        # retorna a frase falada
        print("Você disse: " + frase)
        # abre o browser
        if frase == 'Abrir o navegador':
            os.system("firefox")
        elif frase == 'abrir o gerenciador de tarefas':
            os.system("gnome-system-monitor")
    except sr.UnknownValueError:
        print("Não entendi")
    except sr.RequestError as e:
        print("Não consegui ouvir")
    return frase
loop()

ouvir_microfone()
