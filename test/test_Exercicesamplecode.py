# Do the same for the following functions
# Functions in src/user_functions.py and tests in tests/test_user_functions.py
#import sys
#sys.path+=['../src']

from src.Exerciceuser_functions import *

    # Tests (copy to tests/test_user_functions.py)
import pytest
import io


def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'


def test_check_password_if_has_not_any_numeric_character():
    assert check_password_if_has_a_numeric_character('monpassword')==False

def test_check_password_if_has_a_numeric_character():
    assert check_password_if_has_a_numeric_character('monp3ssword')==True

def test_check_password_if_is_enought_long():
    assert check_password_if_is_enought_long('passwor')==False
    assert check_password_if_is_enought_long('passworfezfsdcz')==True
    assert check_password_if_is_enought_long('')==False

def test_check_password_if_has_an_alpha_character():
    assert check_password_if_has_an_alpha_character('1234a678')==True
    assert check_password_if_has_an_alpha_character('12345678')==False

def test_check_password_if_has_a_special_character():
    assert check_password_if_has_a_special_character('1234*678')==True
    assert check_password_if_has_a_special_character('1234a678')==False

def test_check_password_all_rules():
    assert check_password_all_rules('passwor')==False
    assert check_password_all_rules('passworfezfsdcz')==False
    assert check_password_all_rules('')==False
    assert check_password_all_rules('1234a678')==False
    assert check_password_all_rules('12345678')==False
    assert check_password_all_rules('1234*678')==False
    assert check_password_all_rules(':*"(è_ç&^)')==False
    assert check_password_all_rules('1$34a678')==True


def test_check_username_all_rules():
    assert check_username_all_rules('')==False
    assert check_username_all_rules('azf a')==False
    assert check_username_all_rules('asd')==True
