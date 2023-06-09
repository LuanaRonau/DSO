class Funcionario():
    def __init__(self, nome: str, cpf: str, data_nasc: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nasc = str
        self.__atividade = True

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def data_nasc(self):
        return self.__data_nasc

    @property
    def atividade(self):
        return self.__atividade

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf
    
    @data_nasc.setter
    def data_nasc(self, data_nasc: str):
        self.__data_nasc = data_nasc
    
    @atividade.setter
    def atividade(self, atividade: bool):
        self.__atividade = atividade