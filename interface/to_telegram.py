
class ToTelegram:
    """Class interface entre l'api Verif et Telegram"""

    @staticmethod
    def compose_messages(source):
        """Compose les messages textes de apiVerif vers bot_telegram,
        mise en forme, retours de ligne et markdowns.

        Args:
            source ([dict]): [Dictionnaire contenant tout les textes.]

        Returns:
            messages ([tuple]): [Listes de textes formatés]
        """
        number = list(source.keys())[0]
        # Question/reponse de la vérif.
        msg_verif = f"*Vérification n°{number}*\n"
        for elt in ("verif", "verif_r"):
            msg_verif += ToTelegram.write_message(source, number, elt)

        # Question/reponse de la securité routiere.
        msg_secu = f"*Sécurité routière n°{number}* \n"
        for elt in ("secu", "secu_r"):
            msg_secu += ToTelegram.write_message(source, number, elt)

        # Question/reponse des premiers secours.
        msg_ps = f"*Premiers secours n°{number}*\n"
        for elt in ("secours", "secours_r"):
            msg_ps += ToTelegram.write_message(source, number, elt)
        return (msg_verif, msg_secu, msg_ps)
        

    @staticmethod        
    def write_message(source: dict, number: int, elt: str) -> str:
        """Composition et mise en forme du texte."""
        markdown_ = ""
        closer = '-'*45  # Separation entre question/reponse.
        if elt[-1] == "r":  # Si finit par "r" on applique le style italique pour les reponses.
            markdown_ = "_"  # Italique.
            closer = ".\n"  # Ajout un saut de ligne pour aerer les reponses.
        return f"{markdown_}{source[number][elt]}{markdown_}\n{closer}\n"