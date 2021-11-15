from api_verif.data.interieur import INTERIEUR
from api_verif.data.exterieur import EXTERIEUR
from api_verif.data.secours import SECOURS


class ApiVerif:
    """
    Verif = Vérifications du permis de conduire B francais.
    Ces vérifs sont des questions liés au véhicule ou à
    la sécurité routiere ou encore aux premiers secours.
    Durant l'épreuve du permis de conduire 3 questions sont posées aux candidats:
        1/ verification interieur ou exterieur du véhicule (pair pour exterieur).
        2/ Question securité routiere sur le sujet de la qestion précédente.
        3/ Question Premiers secours.
    
    Toutes ces vérif ont un ou plusieurs numeros permettant de les identifier.
    Exemple, la question portant sur les gicleurs de lave glave, à pour numero 100 et 15.
    Les Verif de premiers secours elles peuvent posseder jusqu'à 4 identifiants.

    L'objet VERIFS a les 100 clefs representants les idenfiants (0 à 99) et en valeur
    possede deux numeros qui sont des references unique vers la bonne question(cf. les import).
    """
    # cle=0 a 99 : Value=(Identifiant verifs, Identifiant premiers-secours).
    VERIFS = {
        0: (10, 30),
        1: (1, 1),
        2: (3, 17),
        3: (30, 15),
        4: (25, 7),
        5: (19, 20),
        6: (23, 18),
        7: (6, 6),
        8: (8, 2),
        9: (7, 12),
        10: (9, 8),
        11: (14, 24),
        12: (7, 35),
        13: (21, 3),
        14: (20, 5),
        15: (10, 10),
        16: (17, 9),
        17: (5, 28),
        18: (21, 22),
        19: (29, 4),
        20: (13, 2),
        21: (22, 14),
        22: (6, 16),
        23: (11, 34),
        24: (4, 25),
        25: (12, 3),
        26: (12, 4),
        27: (13, 13),
        28: (13, 11),
        29: (8, 19),
        30: (11, 21),
        31: (18, 17),
        32: (26, 6),
        33: (27, 7),
        34: (28, 12),
        35: (24, 23),
        36: (5, 31),
        37: (25, 5),
        38: (27, 1),
        39: (9, 15),
        40: (24, 10),
        41: (4, 32),
        42: (29, 33),
        43: (17, 27),
        44: (15, 30),
        45: (28, 9),
        46: (16, 13),
        47: (7, 26),
        48: (1, 29),
        49: (23, 21),
        50: (3, 25),
        51: (16, 14),
        52: (14, 11),
        53: (3, 29),
        54: (32, 28),
        55: (12, 35),
        56: (18, 11),
        57: (26, 8),
        58: (19, 16),
        59: (20, 24),
        60: (30, 31),
        61: (31, 20),
        62: (31, 32),
        63: (15, 26),
        64: (1, 33),
        65: (1, 1),
        66: (10, 30),
        67: (30, 15),
        68: (25, 7),
        69: (19, 20),
        70: (13, 2),
        71: (6, 6),
        72: (7, 35),
        73: (21, 3),
        74: (20, 5),
        75: (10, 10),
        76: (21, 22),
        77: (5, 28),
        78: (13, 2),
        79: (22, 14),
        80: (6, 16),
        81: (12, 3),
        82: (12, 4),
        83: (13, 13),
        84: (26, 6),
        85: (18, 17),
        86: (27, 1),
        87: (25, 5),
        88: (29, 33),
        89: (9, 15),
        90: (16, 13),
        91: (17, 27),
        92: (14, 11),
        93: (23, 21),
        94: (32, 28),
        95: (16, 14),
        96: (18, 19),
        97: (20, 24),
        98: (19, 16),
        99: (15, 26)
    }

    @staticmethod
    def get_id(number: int) -> dict:
        """Retourn un dict avec les identifiants des verifs."""
        assert isinstance(number, int), "Number must be integer"
        return {number: ApiVerif.VERIFS.get(number)}

    @staticmethod
    def get_ask(obj: dict) -> dict:
        """
        Retourn un dict contenant les questions et les reponses
        pour chaque numero.
        dict = {numero : {
                        verif:           "str",
                        secu:            "str",
                        secours:         "str",
                        verif_reponse:   "str",
                        secu_reponse:    "str",
                        secours_reponse: "str"
                        }
                    }    
        """
        assert isinstance(obj, dict), "obj must be a dict"
        ask_answer = {}
        for num, ids in obj.items(): # Pour chaque numero.
            if num % 2 == 0: # Questions pair sont dans EXTERIEUR.
                verif = EXTERIEUR
            else:            # Questions impair sont dans EXTERIEUR.
                verif = INTERIEUR
            ask_answer[num] = {
                "verif":     verif[ids[0]]["verif"],
                "verif_r":   verif[ids[0]]["verif_r"],
                "secu":      verif[ids[0]]["secu"],
                "secu_r":    verif[ids[0]]["secu_r"],
                "secours":   SECOURS[ids[1]]["verif"],
                "secours_r": SECOURS[ids[1]]["verif_r"]
                }
        return ask_answer

    @staticmethod
    def get_verif(verif_number: int) -> dict:
        """
        Recois un integer retourne un dictionnaire
        contenant question et reponse.
        Si integer n'est pas entre 0 et 100 on retoune None.
        """
        assert (0 <= verif_number < 100), "Verif_number must be between 0, 99"
        ids        = ApiVerif.get_id(int(verif_number))
        ask_answer = ApiVerif.get_ask(ids)
        return ask_answer


if __name__ == '__main__':
    test = ApiVerif.get_verif(12)
    print(test)