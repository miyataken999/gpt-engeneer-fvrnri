import pytest
from src.test_system import create_test_system

def test_system_creation():
    """Tests system creation"""
    system = create_test_system()
    assert system.name == "Test System"
    assert system.description == "A test system"
    assert len(system.components) == 2

def test_component_a():
    """Tests ComponentA"""
    component = ComponentA()
    assert isinstance(component, ComponentA)

def test_component_b():
    """Tests ComponentB"""
    component = ComponentB()
    assert isinstance(component, ComponentB)