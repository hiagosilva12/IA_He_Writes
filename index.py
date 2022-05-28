from asyncore import loop
import speech_recognition as sr
import os

from sympy import true

# funcao para reconhecimento de voz


def ouvir_microfone():

    # habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()

    # usando o microfone para capturar a fala
    with sr.Microphone() as source:

        # chama o algoritmo de reducao de ruido
        microfone.adjust_for_ambient_noise(source)
        os.system("clear")
        # fala para o usuario falar
        print("Adicionei apenas duas tarefas")
        print("Teste dizendo, abrir o navegador ou abrir o gerenciador de tarefas ")
        # pergunta para o usuario qual sistema operacional ele quer utilizar
        print("Qual sistema operacional você utiliza?")

        # armazena a informacao que o usuario falou
        audio = microfone.listen(source)
    try:
        # passa a variavel para o algoritmo reconhecedor de padrao de linguagem
        frase = microfone.recognize_google(audio, language='pt-BR')

        # retorna a frase falada
        print("Você disse: " + frase)

        # gerencia para o Linux
        if frase == 'Linux':
            os.system("python3 linux.py")
        elif frase == 'Windows':
            os.system("python3 windows.py")
    except sr.UnknownValueError:
        print("Não entendi")
    except sr.RequestError as e:
        print("Não consegui ouvir")
    return frase


loop()

ouvir_microfone()
