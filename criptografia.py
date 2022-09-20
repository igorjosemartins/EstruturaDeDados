# 5) Crie um programa para realizar a criptografia e a descriptografia uma mensagem informada pelo usuário.  Utilize programação orientada a objeto e dentro do objeto adicione o alfabeto como uma lista.

class Cripto:

    # def = método
    def __init__(self, mensagem):
        self.alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        self.alfabetoCripto = ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x","y", "z", "a", "b", "c", "d", "e", "f", "g", "h"]

        self.mensagem = mensagem
        self.mensagemCripto = ""

    def __str__(self):
        return "Mensagem: " + self.mensagem + ", Mensagem Criptografada: " + self.mensagemCripto

    def criptografar(self):
        for i in range(len(self.mensagem)):
            self.mensagemCripto += self.buscarLetra(self.mensagem[i])

    def buscarLetra(self, letra):
        for i in range(len(self.alfabeto)):
            if letra == self.alfabeto[i]:
                return self.alfabetoCripto[i]
        return "$"


cripto = Cripto("paulo")
cripto.criptografar()

print(cripto)