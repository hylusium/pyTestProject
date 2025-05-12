import pytest
from main import hello


def test_hello():
    assert (
        hello() == "Hello, John Doe!"
    )  # Mise à jour pour correspondre aux valeurs par défaut


def test_hello_custom_name():
    assert hello("EPSI") == "Hello, EPSI Doe!"  # Inclut le lastname par défaut


def test_hello_non_string_input():
    with pytest.raises(TypeError):
        hello(123)


def test_hello_performance():
    for _ in range(1000):
        assert (
            hello("Performance") == "Hello, Performance Doe!"
        )  # Inclut le lastname par défaut


def test_hello_full_name():
    assert (
        hello("Jane", "Smith") == "Hello, Jane Smith!"
    )  # Test avec firstname et lastname
