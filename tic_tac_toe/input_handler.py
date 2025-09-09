# input_handler.py

class InputHandler:
    """Abstract input handler interface"""
    def get_input(self, prompt):
        raise NotImplementedError


class ConsoleInputHandler(InputHandler):
    """Console-based input handler"""
    def get_input(self, prompt):
        return input(prompt)
