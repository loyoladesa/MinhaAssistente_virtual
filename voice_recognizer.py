
import speech_recognition as sr


def EscreveArquivo(mensagem):
    try:
        with open("transcricao_audio.txt", "a") as file:
            file.write(str(mensagem) + "\n")
            file.close()
    except:
        print("Erro na Escrita da " + mensagem)


r = sr.Recognizer()
mensagem = ""

while(mensagem != "desligar"):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Diga Algo:")
        audio = r.listen(source)
        print("Hello")


    try:
        mensagem = r.recognize_google(audio, language='pt-BR')
        print("Você falou: " + mensagem)
    except sr.UnknownValueError:
        print("Google Speech Recognition não pode entender o que você falou!")
    except sr.RequestError as e:
        print("Não foram obtidos resultados do  Google Speech Recognition service; {0}".format(e))

    EscreveArquivo(mensagem)