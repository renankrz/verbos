import csv
import random
from enum import Enum, auto


class Pessoa(Enum):
    I = "I"
    YOU = "you"
    HE = "he"
    SHE = "she"
    IT = "it"
    WE = "we"
    THEY = "they"


class TempoVerbal(Enum):
    PRESENT_SIMPLE = auto()
    PRESENT_CONTINUOUS = auto()
    PAST_SIMPLE = auto()
    PAST_CONTINUOUS = auto()
    PRESENT_PERFECT = auto()
    PRESENT_PERFECT_CONTINUOUS = auto()
    FUTURE_SIMPLE = auto()
    FUTURE_BE_GOING_TO = auto()
    FUTURE_CONTINUOUS = auto()
    CONDITIONAL_SIMPLE = auto()


class Conjugador:
    @staticmethod
    def get_auxiliar(pessoa: Pessoa, tempo: TempoVerbal) -> str:
        """Retorna o auxiliar correto para a pessoa e tempo verbal"""
        auxiliares = {
            TempoVerbal.PRESENT_CONTINUOUS: {
                Pessoa.I: "am",
                Pessoa.YOU: "are",
                Pessoa.HE: "is",
                Pessoa.SHE: "is",
                Pessoa.IT: "is",
                Pessoa.WE: "are",
                Pessoa.THEY: "are"
            },
            TempoVerbal.PAST_CONTINUOUS: {
                Pessoa.I: "was",
                Pessoa.YOU: "were",
                Pessoa.HE: "was",
                Pessoa.SHE: "was",
                Pessoa.IT: "was",
                Pessoa.WE: "were",
                Pessoa.THEY: "were"
            },
            TempoVerbal.PRESENT_PERFECT: {
                Pessoa.I: "have",
                Pessoa.YOU: "have",
                Pessoa.HE: "has",
                Pessoa.SHE: "has",
                Pessoa.IT: "has",
                Pessoa.WE: "have",
                Pessoa.THEY: "have"
            },
            TempoVerbal.PRESENT_PERFECT_CONTINUOUS: {
                Pessoa.I: "have been",
                Pessoa.YOU: "have been",
                Pessoa.HE: "has been",
                Pessoa.SHE: "has been",
                Pessoa.IT: "has been",
                Pessoa.WE: "have been",
                Pessoa.THEY: "have been"
            },
            TempoVerbal.FUTURE_SIMPLE: {
                Pessoa.I: "will",
                Pessoa.YOU: "will",
                Pessoa.HE: "will",
                Pessoa.SHE: "will",
                Pessoa.IT: "will",
                Pessoa.WE: "will",
                Pessoa.THEY: "will"
            },
            TempoVerbal.FUTURE_BE_GOING_TO: {
                Pessoa.I: "am going to",
                Pessoa.YOU: "are going to",
                Pessoa.HE: "is going to",
                Pessoa.SHE: "is going to",
                Pessoa.IT: "is going to",
                Pessoa.WE: "are going to",
                Pessoa.THEY: "are going to"
            },
            TempoVerbal.FUTURE_CONTINUOUS: {
                Pessoa.I: "will be",
                Pessoa.YOU: "will be",
                Pessoa.HE: "will be",
                Pessoa.SHE: "will be",
                Pessoa.IT: "will be",
                Pessoa.WE: "will be",
                Pessoa.THEY: "will be"
            },
            TempoVerbal.CONDITIONAL_SIMPLE: {
                Pessoa.I: "would",
                Pessoa.YOU: "would",
                Pessoa.HE: "would",
                Pessoa.SHE: "would",
                Pessoa.IT: "would",
                Pessoa.WE: "would",
                Pessoa.THEY: "would"
            }
        }
        return auxiliares.get(tempo, {}).get(pessoa, "")

    @staticmethod
    def get_forma_verbal(tempo: TempoVerbal) -> str:
        """Retorna qual coluna do CSV deve ser usada para cada tempo"""
        formas = {
            TempoVerbal.PRESENT_SIMPLE: "BASE_FORM",
            TempoVerbal.PRESENT_CONTINUOUS: "CONTINUOUS_FORM",
            TempoVerbal.PAST_SIMPLE: "PAST_SIMPLE",
            TempoVerbal.PAST_CONTINUOUS: "CONTINUOUS_FORM",
            TempoVerbal.PRESENT_PERFECT: "PAST_PARTICIPLE",
            TempoVerbal.PRESENT_PERFECT_CONTINUOUS: "CONTINUOUS_FORM",
            TempoVerbal.FUTURE_SIMPLE: "BASE_FORM",
            TempoVerbal.FUTURE_BE_GOING_TO: "BASE_FORM",
            TempoVerbal.FUTURE_CONTINUOUS: "CONTINUOUS_FORM",
            TempoVerbal.CONDITIONAL_SIMPLE: "BASE_FORM"
        }
        return formas.get(tempo)

    @staticmethod
    def get_nome_tempo(tempo: TempoVerbal) -> str:
        """Retorna o nome formatado do tempo verbal"""
        nomes = {
            TempoVerbal.PRESENT_SIMPLE: "Present Simple",
            TempoVerbal.PRESENT_CONTINUOUS: "Present Continuous",
            TempoVerbal.PAST_SIMPLE: "Past Simple",
            TempoVerbal.PAST_CONTINUOUS: "Past Continuous",
            TempoVerbal.PRESENT_PERFECT: "Present Perfect",
            TempoVerbal.PRESENT_PERFECT_CONTINUOUS: "Present Perfect Continuous",
            TempoVerbal.FUTURE_SIMPLE: "Future Simple (will)",
            TempoVerbal.FUTURE_BE_GOING_TO: "Future (be going to)",
            TempoVerbal.FUTURE_CONTINUOUS: "Future Continuous",
            TempoVerbal.CONDITIONAL_SIMPLE: "Conditional Simple"
        }
        return nomes.get(tempo, "")


def carregar_verbos(caminho_csv):
    with open(caminho_csv, mode='r', encoding='utf-8') as arquivo:
        return list(csv.DictReader(arquivo, delimiter=';'))


def sortear_desafio():
    verbos = carregar_verbos('verbos.csv')
    conjugador = Conjugador()

    pessoa = random.choice(list(Pessoa))
    verbo = random.choice(verbos)

    pesos_tempos = {
        TempoVerbal.PRESENT_SIMPLE: 1,
        TempoVerbal.FUTURE_SIMPLE: 1,
        TempoVerbal.FUTURE_BE_GOING_TO: 1,
        TempoVerbal.CONDITIONAL_SIMPLE: 1,
        TempoVerbal.PRESENT_CONTINUOUS: 1,
        TempoVerbal.PAST_CONTINUOUS: 1,
        TempoVerbal.PRESENT_PERFECT_CONTINUOUS: 1,
        TempoVerbal.FUTURE_CONTINUOUS: 1,
        TempoVerbal.PAST_SIMPLE: 3,
        TempoVerbal.PRESENT_PERFECT: 3
    }

    tempo = random.choices(list(TempoVerbal), weights=[
                           pesos_tempos[t] for t in TempoVerbal], k=1)[0]

    if tempo == TempoVerbal.PRESENT_SIMPLE and pessoa in [Pessoa.HE, Pessoa.SHE, Pessoa.IT]:
        forma_verbal = verbo["PRESENT_3RD"]
        auxiliar = ""
    else:
        forma_verbal = verbo[conjugador.get_forma_verbal(tempo)]
        auxiliar = conjugador.get_auxiliar(pessoa, tempo)

    print(f"\n=== Desafio ===")
    print(f"Pessoa       : {pessoa.value}")
    print(f"Verbo        : {verbo['BASE_FORM']}")
    print(f"Tempo verbal : {conjugador.get_nome_tempo(tempo)}")

    resposta_correta = f"{pessoa.value} {auxiliar} {forma_verbal}".replace(
        "  ", " ").strip()

    if "/" in forma_verbal:
        alternativas = forma_verbal.split("/")
        formas_corretas = [f"{pessoa.value} {auxiliar} {alt}".replace("  ", " ").strip()
                           for alt in alternativas]
    else:
        formas_corretas = [resposta_correta]

    acertou = False

    while not acertou:

        resposta_usuario = input("\nSua resposta: ").strip()

        if resposta_usuario.lower() in [resp.lower() for resp in formas_corretas]:
            acertou = True
            print("\n✅ Correto! Parabéns!")
        else:
            print(
                f"\n❌ Incorreto. A resposta correta seria: {formas_corretas[0]}")
            if len(formas_corretas) > 1:
                print(f"   (Ou também: {', '.join(formas_corretas[1:])})")

    print("\nPressione Enter para continuar ou digite 'sair' para terminar")
    return input().strip().lower() != 'sair'


if __name__ == "__main__":
    print("=== Desafio de Verbos Irregulares em Inglês ===")
    print("Para sair, digite 'sair' quando solicitado\n")

    continuar = True
    while continuar:
        continuar = sortear_desafio()

    print("\nAté a próxima! Pratique verbos irregulares regularmente!")
