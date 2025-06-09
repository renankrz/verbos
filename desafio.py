import csv
import random
from enum import Enum, auto


class Pronome(Enum):
    I = "I"
    YOU = "You"
    HE = "He"
    SHE = "She"
    IT = "It"
    WE = "We"
    THEY = "They"


class TipoDaSentenca(Enum):
    AFIRMATIVA = "Afirmativa"
    INTERROGATIVA = "Interrogativa"


class PolaridadeDaSentenca(Enum):
    POSITIVA = "Positiva"
    NEGATIVA = "Negativa"


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


class Bases(tuple):
    def __new__(cls, *args):
        if len(args) != 8:
            raise ValueError("Bases deve conter exatamente 8 strings")
        return super().__new__(cls, args)

    def get_afirmativa_positiva(self):
        return [self[0]] if self[1] is None else [self[0], self[1]]

    def get_afirmativa_negativa(self):
        return [self[2]] if self[3] is None else [self[2], self[3]]

    def get_interrogativa_positiva(self):
        return [self[4]] if self[5] is None else [self[4], self[5]]

    def get_interrogativa_negativa(self):
        return [self[6]] if self[7] is None else [self[6], self[7]]


class Conjugador:
    @staticmethod
    def get_bases(pessoa: Pronome, tipo: TipoDaSentenca, polaridade: PolaridadeDaSentenca, tempo: TempoVerbal) -> str:
        """Retorna a base correta para a pessoa, tipo, polaridade e tempo"""
        bases = {
            TempoVerbal.PRESENT_SIMPLE: {
                Pronome.I: Bases("I", None, "I do not", "I don't", "Do I", None, "Do I not", "Don't I"),
                Pronome.YOU: Bases("You", None, "You do not", "You don't", "Do you", None, "Do you not", "Don't you"),
                Pronome.HE: Bases("He", None, "He does not", "He doesn't", "Does he", None, "Does he not", "Doesn't he"),
                Pronome.SHE: Bases("She", None, "She does not", "She doesn't", "Does she", None, "Does she not", "Doesn't she"),
                Pronome.IT: Bases("It", None, "It does not", "It doesn't", "Does it", None, "Does it not", "Doesn't it"),
                Pronome.WE: Bases("We", None, "We do not", "We don't", "Do we", None, "Do we not", "Don't we"),
                Pronome.THEY: Bases("They", None, "They do not", "They don't", "Do they", None, "Do they not", "Don't they")
            },
            TempoVerbal.PRESENT_CONTINUOUS: {
                Pronome.I: Bases("I am", "I'm", "I am not", "I'm not", "Am I", None, "Am I not", "Aren't I"),
                Pronome.YOU: Bases("You are", "You're", "You are not", "You aren't", "Are you", None, "Are you not", "Aren't you"),
                Pronome.HE: Bases("He is", "He's", "He is not", "He isn't", "Is he", None, "Is he not", "Isn't he"),
                Pronome.SHE: Bases("She is", "She's", "She is not", "She isn't", "Is she", None, "Is she not", "Isn't she"),
                Pronome.IT: Bases("It is", "It's", "It is not", "It isn't", "Is it", None, "Is it not", "Isn't it"),
                Pronome.WE: Bases("We are", "We're", "We are not", "We aren't", "Are we", None, "Are we not", "Aren't we"),
                Pronome.THEY: Bases("They are", "They're", "They are not", "They aren't", "Are they", None, "Are they not", "Aren't they")
            },
            TempoVerbal.PAST_SIMPLE: {
                Pronome.I: Bases("I", None, "I did not", "I didn't", "Did I", None, "Did I not", "Didn't I"),
                Pronome.YOU: Bases("You", None, "You did not", "You didn't", "Did you", None, "Did you not", "Didn't you"),
                Pronome.HE: Bases("He", None, "He did not", "He didn't", "Did he", None, "Did he not", "Didn't he"),
                Pronome.SHE: Bases("She", None, "She did not", "She didn't", "Did she", None, "Did she not", "Didn't she"),
                Pronome.IT: Bases("It", None, "It did not", "It didn't", "Did it", None, "Did it not", "Didn't it"),
                Pronome.WE: Bases("We", None, "We did not", "We didn't", "Did we", None, "Did we not", "Didn't we"),
                Pronome.THEY: Bases("They", None, "They did not", "They didn't", "Did they", None, "Did they not", "Didn't they")
            },
            TempoVerbal.PAST_CONTINUOUS: {
                Pronome.I: Bases("I was", None, "I was not", "I wasn't", "Was I", None, "Was I not", "Wasn't I"),
                Pronome.YOU: Bases("You were", None, "You were not", "You weren't", "Were you", None, "Were you not", "Weren't you"),
                Pronome.HE: Bases("He was", None, "He was not", "He wasn't", "Was he", None, "Was he not", "Wasn't he"),
                Pronome.SHE: Bases("She was", None, "She was not", "She wasn't", "Was she", None, "Was she not", "Wasn't she"),
                Pronome.IT: Bases("It was", None, "It was not", "It wasn't", "Was it", None, "Was it not", "Wasn't it"),
                Pronome.WE: Bases("We were", None, "We were not", "We weren't", "Were we", None, "Were we not", "Weren't we"),
                Pronome.THEY: Bases("They were", None, "They were not", "They weren't", "Were they", None, "Were they not", "Weren't they")
            },
            TempoVerbal.PRESENT_PERFECT: {
                Pronome.I: Bases("I have", "I've", "I have not", "I haven't", "Have I", None, "Have I not", "Haven't I"),
                Pronome.YOU: Bases("You have", "You've", "You have not", "You haven't", "Have you", None, "Have you not", "Haven't you"),
                Pronome.HE: Bases("He has", "He's", "He has not", "He hasn't", "Has he", None, "Has he not", "Hasn't he"),
                Pronome.SHE: Bases("She has", "She's", "She has not", "She hasn't", "Has she", None, "Has she not", "Hasn't she"),
                Pronome.IT: Bases("It has", "It's", "It has not", "It hasn't", "Has it", None, "Has it not", "Hasn't it"),
                Pronome.WE: Bases("We have", "We've", "We have not", "We haven't", "Have we", None, "Have we not", "Haven't we"),
                Pronome.THEY: Bases("They have", "They've", "They have not", "They haven't", "Have they", None, "Have they not", "Haven't they")
            },
            TempoVerbal.PRESENT_PERFECT_CONTINUOUS: {
                Pronome.I: Bases("I have been", "I've been", "I have not been", "I haven't been", "Have I been", None, "Have I not been", "Haven't I been"),
                Pronome.YOU: Bases("You have been", "You've been", "You have not been", "You haven't been", "Have you been", None, "Have you not been", "Haven't you been"),
                Pronome.HE: Bases("He has been", "He's been", "He has not been", "He hasn't been", "Has he been", None, "Has he not been", "Hasn't he been"),
                Pronome.SHE: Bases("She has been", "She's been", "She has not been", "She hasn't been", "Has she been", None, "Has she not been", "Hasn't she been"),
                Pronome.IT: Bases("It has been", "It's been", "It has not been", "It hasn't been", "Has it been", None, "Has it not been", "Hasn't it been"),
                Pronome.WE: Bases("We have been", "We've been", "We have not been", "We haven't been", "Have we been", None, "Have we not been", "Haven't we been"),
                Pronome.THEY: Bases("They have been", "They've been", "They have not been", "They haven't been", "Have they been", None, "Have they not been", "Haven't they been")
            },
            TempoVerbal.FUTURE_SIMPLE: {
                Pronome.I: Bases("I will", "I'll", "I will not", "I won't", "Will I", None, "Will I not", "Won't I"),
                Pronome.YOU: Bases("You will", "You'll", "You will not", "You won't", "Will you", None, "Will you not", "Won't you"),
                Pronome.HE: Bases("He will", "He'll", "He will not", "He won't", "Will he", None, "Will he not", "Won't he"),
                Pronome.SHE: Bases("She will", "She'll", "She will not", "She won't", "Will she", None, "Will she not", "Won't she"),
                Pronome.IT: Bases("It will", "It'll", "It will not", "It won't", "Will it", None, "Will it not", "Won't it"),
                Pronome.WE: Bases("We will", "We'll", "We will not", "We won't", "Will we", None, "Will we not", "Won't we"),
                Pronome.THEY: Bases("They will", "They'll", "They will not", "They won't", "Will they", None, "Will they not", "Won't they")
            },
            TempoVerbal.FUTURE_BE_GOING_TO: {
                Pronome.I: Bases("I am going to", "I'm going to", "I am not going to", "I'm not going to", "Am I going to", None, "Am I not going to", "Aren't I going to"),
                Pronome.YOU: Bases("You are going to", "You're going to", "You are not going to", "You aren't going to", "Are you going to", None, "Are you not going to", "Aren't you going to"),
                Pronome.HE: Bases("He is going to", "He's going to", "He is not going to", "He isn't going to", "Is he going to", None, "Is he not going to", "Isn't he going to"),
                Pronome.SHE: Bases("She is going to", "She's going to", "She is not going to", "She isn't going to", "Is she going to", None, "Is she not going to", "Isn't she going to"),
                Pronome.IT: Bases("It is going to", "It's going to", "It is not going to", "It isn't going to", "Is it going to", None, "Is it not going to", "Isn't it going to"),
                Pronome.WE: Bases("We are going to", "We're going to", "We are not going to", "We aren't going to", "Are we going to", None, "Are we not going to", "Aren't we going to"),
                Pronome.THEY: Bases("They are going to", "They're going to", "They are not going to", "They aren't going to", "Are they going to", None, "Are they not going to", "Aren't they going to")
            },
            TempoVerbal.FUTURE_CONTINUOUS: {
                Pronome.I: Bases("I will be", "I'll be", "I will not be", "I won't be", "Will I be", None, "Will I not be", "Won't I be"),
                Pronome.YOU: Bases("You will be", "You'll be", "You will not be", "You won't be", "Will you be", None, "Will you not be", "Won't you be"),
                Pronome.HE: Bases("He will be", "He'll be", "He will not be", "He won't be", "Will he be", None, "Will he not be", "Won't he be"),
                Pronome.SHE: Bases("She will be", "She'll be", "She will not be", "She won't be", "Will she be", None, "Will she not be", "Won't she be"),
                Pronome.IT: Bases("It will be", "It'll be", "It will not be", "It won't be", "Will it be", None, "Will it not be", "Won't it be"),
                Pronome.WE: Bases("We will be", "We'll be", "We will not be", "We won't be", "Will we be", None, "Will we not be", "Won't we be"),
                Pronome.THEY: Bases("They will be", "They'll be", "They will not be", "They won't be", "Will they be", None, "Will they not be", "Won't they be")
            },
            TempoVerbal.CONDITIONAL_SIMPLE: {
                Pronome.I: Bases("I would", "I'd", "I would not", "I wouldn't", "Would I", None, "Would I not", "Wouldn't I"),
                Pronome.YOU: Bases("You would", "You'd", "You would not", "You wouldn't", "Would you", None, "Would you not", "Wouldn't you"),
                Pronome.HE: Bases("He would", "He'd", "He would not", "He wouldn't", "Would he", None, "Would he not", "Wouldn't he"),
                Pronome.SHE: Bases("She would", "She'd", "She would not", "She wouldn't", "Would she", None, "Would she not", "Wouldn't she"),
                Pronome.IT: Bases("It would", "It'd", "It would not", "It wouldn't", "Would it", None, "Would it not", "Wouldn't it"),
                Pronome.WE: Bases("We would", "We'd", "We would not", "We wouldn't", "Would we", None, "Would we not", "Wouldn't we"),
                Pronome.THEY: Bases("They would", "They'd", "They would not", "They wouldn't", "Would they", None, "Would they not", "Wouldn't they")
            }
        }
        if tipo == TipoDaSentenca.AFIRMATIVA:
            if polaridade == PolaridadeDaSentenca.POSITIVA:
                return bases.get(tempo, {}).get(pessoa, []).get_afirmativa_positiva()
            else:
                return bases.get(tempo, {}).get(pessoa, []).get_afirmativa_negativa()
        else:
            if polaridade == PolaridadeDaSentenca.POSITIVA:
                return bases.get(tempo, {}).get(pessoa, []).get_interrogativa_positiva()
            else:
                return bases.get(tempo, {}).get(pessoa, []).get_interrogativa_negativa()

    @staticmethod
    def get_forma_verbal(pronome: Pronome, tipo: TipoDaSentenca, polaridade: PolaridadeDaSentenca, tempo: TempoVerbal) -> str:
        """Retorna a forma correta do verbo com base no pronome, tipo, polaridade e tempo."""

        # Casos especiais:
        # 1. Past Simple em frases negativas/interrogativas: usa BASE_FORM (não PAST_SIMPLE)
        if tempo == TempoVerbal.PAST_SIMPLE and (tipo == TipoDaSentenca.INTERROGATIVA or polaridade == PolaridadeDaSentenca.NEGATIVA):
            return 'BASE_FORM'

        # 2. Present Simple para he/she/it em afirmativas positivas: usa PRESENT_3RD
        if (tempo == TempoVerbal.PRESENT_SIMPLE and
            tipo == TipoDaSentenca.AFIRMATIVA and
            polaridade == PolaridadeDaSentenca.POSITIVA and
                pronome in [Pronome.HE, Pronome.SHE, Pronome.IT]):
            return 'PRESENT_3RD'

        # Caso geral
        formas = {
            TempoVerbal.PRESENT_SIMPLE: 'BASE_FORM',
            TempoVerbal.PRESENT_CONTINUOUS: 'CONTINUOUS_FORM',
            TempoVerbal.PAST_SIMPLE: 'PAST_SIMPLE',
            TempoVerbal.PAST_CONTINUOUS: 'CONTINUOUS_FORM',
            TempoVerbal.PRESENT_PERFECT: 'PAST_PARTICIPLE',
            TempoVerbal.PRESENT_PERFECT_CONTINUOUS: 'CONTINUOUS_FORM',
            TempoVerbal.FUTURE_SIMPLE: 'BASE_FORM',
            TempoVerbal.FUTURE_BE_GOING_TO: 'BASE_FORM',
            TempoVerbal.FUTURE_CONTINUOUS: 'CONTINUOUS_FORM',
            TempoVerbal.CONDITIONAL_SIMPLE: 'BASE_FORM'
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


def normalizar_resposta(resposta):
    if not resposta.startswith("i ") and not resposta.startswith("i'"):
        return resposta[0].upper() + resposta[1:]
    return resposta


def sortear_desafio(pesos_pronomes, pesos_tipo_sentenca, pesos_polaridade_sentenca, pesos_tempos):
    verbos = carregar_verbos('verbos.csv')
    conjugador = Conjugador()

    pronome = random.choices(list(Pronome), weights=[pesos_pronomes[p] for p in Pronome], k=1)[0]
    tipo = random.choices(list(TipoDaSentenca), weights=[pesos_tipo_sentenca[t] for t in TipoDaSentenca], k=1)[0]
    polaridade = random.choices(list(PolaridadeDaSentenca), weights=[pesos_polaridade_sentenca[p] for p in PolaridadeDaSentenca], k=1)[0]
    tempo = random.choices(list(TempoVerbal), weights=[pesos_tempos[t] for t in TempoVerbal], k=1)[0]
    verbo = random.choice(verbos)

    bases = conjugador.get_bases(pronome, tipo, polaridade, tempo)
    verbo_flexionado = verbo[conjugador.get_forma_verbal(pronome, tipo, polaridade, tempo)]

    respostas = [f"{b} {v}" for b in bases for v in verbo_flexionado.split("/")]

    if tipo == TipoDaSentenca.INTERROGATIVA:
        respostas = [r + "?" for r in respostas]

    print()
    print(f"Pessoa                  : {pronome.value}")
    print(f"Verbo                   : {verbo['BASE_FORM'][0].upper() + verbo['BASE_FORM'][1:]}")
    print(f"Tempo verbal            : {conjugador.get_nome_tempo(tempo)}")
    print(f"Tipo de sentença        : {tipo.value}")
    print(f"Polaridade de sentença  : {polaridade.value}")

    acertou = False

    while not acertou:
        resposta_usuario = input("\n> ").strip()

        if normalizar_resposta(resposta_usuario) in [resp for resp in respostas]:
            acertou = True
            print("\n✅ Correto")
            outras_respostas = [resp for resp in respostas if resp != normalizar_resposta(resposta_usuario)]
            if outras_respostas:
                print(f"Outras respostas corretas: {', '.join(outras_respostas)}")
        else:
            print(f"\n❌ Incorreto. Respostas corretas: {', '.join(respostas)}")

    return input("\nPressione Enter para continuar ou digite 'sair' para terminar: ").strip().lower() != 'sair'


if __name__ == "__main__":
    print("=== Verbos Irregulares ===")
    print("Para sair, digite 'sair' quando solicitado")

    pesos_pronomes = {
        Pronome.I: 1,
        Pronome.YOU: 1,
        Pronome.HE: 1,
        Pronome.SHE: 1,
        Pronome.IT: 1,
        Pronome.WE: 1,
        Pronome.THEY: 1
    }

    pesos_tipo_sentenca = {
        TipoDaSentenca.AFIRMATIVA: 3,
        TipoDaSentenca.INTERROGATIVA: 1
    }

    pesos_polaridade_sentenca = {
        PolaridadeDaSentenca.POSITIVA: 3,
        PolaridadeDaSentenca.NEGATIVA: 1
    }

    pesos_tempos = {
        TempoVerbal.PRESENT_SIMPLE: 1,
        TempoVerbal.FUTURE_SIMPLE: 1,
        TempoVerbal.FUTURE_BE_GOING_TO: 1,
        TempoVerbal.CONDITIONAL_SIMPLE: 1,
        TempoVerbal.PRESENT_CONTINUOUS: 1,
        TempoVerbal.PAST_CONTINUOUS: 1,
        TempoVerbal.PRESENT_PERFECT_CONTINUOUS: 1,
        TempoVerbal.FUTURE_CONTINUOUS: 1,
        TempoVerbal.PAST_SIMPLE: 5,
        TempoVerbal.PRESENT_PERFECT: 3
    }

    continuar = True
    while continuar:
        continuar = sortear_desafio(pesos_pronomes, pesos_tipo_sentenca, pesos_polaridade_sentenca, pesos_tempos)

    print("\nAté a próxima! Pratique verbos irregulares regularmente!")
