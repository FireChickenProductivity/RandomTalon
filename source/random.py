from talon import Module, actions
import random

def generate_random_digit() -> str:
    return str(random.randint(0, 9))

def generate_random_lowercase_letter() -> str:
    return chr(random.randint(97, 122))

def generate_random_character() -> str:
    return chr(random.randint(32, 126))

module = Module()
@module.action_class
class Actions:
    def random_insert_random_digit():
        """Insert a random digit"""
        actions.insert(generate_random_digit())
    
    def random_insert_random_lowercase_letter():
        """Insert a random lowercase letter"""
        actions.insert(generate_random_lowercase_letter())
    
    def random_insert_random_character():
        """Insert a random character"""
        actions.insert(generate_random_character())