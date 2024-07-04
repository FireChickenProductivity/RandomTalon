from talon import Module, actions
import random

def generate_random_digit() -> str:
    return str(random.randint(0, 9))

def generate_random_lowercase_letter() -> str:
    return chr(random.randint(97, 122))

def generate_random_character() -> str:
    return chr(random.randint(32, 126))

def generate_random_alpha_numeric_character():
    lowercase_letters = [chr(i) for i in range(97, 123)]
    digits = [str(i) for i in range(10)]
    uppercase_letters = [letter.upper() for letter in lowercase_letters]
    return random.choice(lowercase_letters + digits + uppercase_letters)

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

    def random_insert_random_upper_case_letter():
        """Insert a random uppercase letter"""
        upper_case_letter = generate_random_lowercase_letter().upper()
        actions.insert(upper_case_letter)

    def random_insert_random_alphanumeric_character():
        """Insert a random alphanumeric character"""
        actions.insert(generate_random_alpha_numeric_character())