import speech_recognition as sr

# Função para o reconhecimento de voz

def ouvir_microfone():
    # Habilita o microfone para ouvir o usuário
    microfone = sr.Recognizer()
    # usando o microfone para capturar a fala
    with sr.Microphone() as source:
       # chama o algotimo de redução de ruído
        microfone.adjust_for_ambient_noise(source)
        # fala para o usuário falar
        print("Diga alguma coisa: ")
        # armazena a informação que o usuário falou
        audio = microfone.listen(source)
    try: 
        # passa a variável para o algoritmo reconhecedor de padrão de linguagem
        frase = microfone.recognize_google(audio, language='pt-BR')
        # retorna a frase falada
        print("Você disse: " + frase)

        # se nao reconheceu a frase, exibe esta mensagem
    except sr.UnknownValueError:
        print("Não entendi")
    except sr.RequestError as e:
        print("Não consegui ouvir")

    return frase
ouvir_microfone()