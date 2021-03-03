from mycroft import MycroftSkill, intent_file_handler


class ExercicosPermitidos(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('permitidos.exercicos.intent')
    def handle_permitidos_exercicos(self, message):
        self.speak_dialog('permitidos.exercicos')


def create_skill():
    return ExercicosPermitidos()

