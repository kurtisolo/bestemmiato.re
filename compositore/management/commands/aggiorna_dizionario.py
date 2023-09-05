from django.core.management.base import BaseCommand
from compositore.models import gods_crist_m, insulti_h_m, insulti_s_m, insulti_n_m


"""
LEGENDA:
s = Spazio vuoto
_m = Maschile
_f = Femminile
_h = Hardcore
_s = Soft
_n = Nonsense
_crist = Cristiani

NB la x davanti serve a differenziare dalle classi
"""

xgods_crist_m = [
    "Dio",
    "Gesù",
    "Cristo",
    "San Michele",
    "Arcangelo Gabriele",
    "Abramo",
    "Isaia",
    "Giuseppe",
    "Adamo",
    "Dio",
    "San Francesco",
    "Spirito Santo",
    "Signore",
    "San Pietro",
    "San Paolo",
    "Dio",
    "San Giovanni",
    "Mosè",
    "Noè",
    "Buddha",
    "Giacobbe",
    "Ezechiele",
]
xgods_crist_f = ["Vergine Maria", "Maria", "Madonna", "Maria Maddalena"]
xinsulti_h_m = [
    "abbietto",
    "abominevole",
    "antipatico",
    "arrogante",
    "babbeo",
    "bastardo",
    "blasfemo",
    "boia",
    "brutto",
    "buffone",
    "cafone",
    "canaglia",
    "cancaro",
    "cane",
    "coglione",
    "cornuto",
    "cretino",
    "deficiente",
    "detestabile",
    "disgustoso",
    "disonesto",
    "disprezzabile",
    "disumano",
    "fai cagare",
    "fastidioso",
    "fottiti",
    "hai rotto i coglioni",
    "idiota",
    "ignorante",
    "imbecille",
    "imbroglione",
    "immondo",
    "fai cagare",
    "sia dannato tu e il tuo figliolo comunista",
    "inadeguato",
    "incapace",
    "incivile",
    "indeciso",
    "indesiderabile",
    "inetto",
    "se ti avessi davanti ti sputerei",
    "infame",
    "infantile",
    "infausto",
    "infelice",
    "infido",
    "ingrato",
    "insensato",
    "insensibile",
    "insolente",
    "insopportabile",
    "inutile",
    "irrispettoso",
    "irritante",
    "lasciami stare",
    "ti odio",
    "lurido",
    "maldestro",
    "maledetto",
    "malvagio",
    "mascalzone",
    "menefreghista",
    "merdoso",
    "meschino",
    "minchione",
    "miserabile",
    "molesto",
    "mi hai stracciato le palle",
    "odioso",
    "offensivo",
    "ostinato",
    "patetico",
    "pazzo",
    "perverso",
    "pezzente",
    "porco",
    "presuntuoso",
    "quel mona",
    "repellente",
    "ridicolo",
    "rincoglionito",
    "ripugnante",
    "rotto in culo",
    "scellerato",
    "schifoso",
    "sciocco",
    "scorretto",
    "scortese",
    "scostumato",
    "sfigato",
    "sgradevole",
    "sporco",
    "squallido",
    "stronzo",
    "stupido",
    "stupratore",
    "subumano",
    "testa di cazzo",
    "ti odiano tutti",
    "triste",
    "turpe",
    "vergognati",
    "verme",
    "vigliacco",
    "villano",
    "violento",
    "volgare",
    "faresti passare la voglia di credere anche al papa",
    "come puoi pretendere che la gente ti preghi?",
    "vaffanculo tu e chi ti prega",
    "fascista",
    "sparati",
    "assassino",
    "alcolizzato",
    "drogato",
    "psicopatico",
    "misogino",
    "nazista",
    "accanito fan di Hitler",
]
xinsulti_s_m = [
    "santissimo",
    "beato",
    "poveretto",
    "bello",
    "glorioso",
    "dammi la forza",
    "portami la pace",
    "abbi pietà",
    "elevatissimo",
    "smettila",
    "ti prego",
    "per piacere",
    "non fai ridere",
    "non sei simpatico",
    "non farmi perdere la pazienza",
    "uffa",
    "ti diverti?",
    "stai nel tuo",
    "cretino chi ti prega",
    "ti diverti con poco",
    "splendente",
    "glorioso",
    "misericordioso",
    "onnipotente",
    "rispettabile",
    "eterno",
    "aiutami",
    "simpaticone",
    "altissimo",
    "onnipotente",
    "veglia su di noi",
    "oggi stai rischiando",
    "vuoi farmi bestemmiare?",
    "se vuoi che bestemmi continua così",
]
xinsulti_n_m = [
    "fastidoso",
    "stai bene attento",
    "non farmi incazzare",
    "mi sto alterando",
    "antipatico",
    "lo fai apposta?",
    "dispettoso",
    "fai sul serio?",
    "non fai ridere",
    "poi lamentati se non ti pregano",
    "che palle",
    "ignorante",
    "testimone di Geova",
    "rotto",
    "smerdato",
    "che noia",
    "che fastidio",
    "che tedio",
    "basta",
    "non costringermi a bestemmiare forte",
    "porca miseria",
    "se non bestemmio guarda",
    "oggi sei propenso alle minchiate",
    "donami pazienza, serenità e una spranga",
    "non hai proprio un cazzo di meglio da fare",
    "nucleare",
    "comunista",
    "generato da AI",
    "imbarazzante",
    "accanito",
    "ce l'hai con me",
    "cosa ti ho fatto?",
    "perché fai così?",
    "non ti ho fatto nulla",
    "perché mi punisci?",
    "se mi lasciassi in pace sarebbe fantastico",
    "noioso",
]


class Command(BaseCommand):
    help = "Popola il dizionario con le parole definite"

    def handle(self, *args, **options):
        count = 0

        for x in xgods_crist_m:
            created = gods_crist_m.objects.get_or_create(parola=x)
            if created:
                count += 1

        for x in xinsulti_h_m:
            created = insulti_h_m.objects.get_or_create(parola=x)
            if created:
                count += 1

        for x in xinsulti_s_m:
            created = insulti_s_m.objects.get_or_create(parola=x)
            if created:
                count += 1

        for x in xinsulti_n_m:
            created = insulti_n_m.objects.get_or_create(parola=x)
            if created:
                count += 1

        print(f"Parole aggiunte: {count}")
