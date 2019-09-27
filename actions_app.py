import os


class FitGetters():
    def start_conversation(self):
        response = {
            'expectUserResponse': True,
            'expectedInputs': [
                {
                    'possibleIntents': {'intent':'actions.intent.TEXT', 'actions.intent.PERMISSION'},
                }
            ]
        }