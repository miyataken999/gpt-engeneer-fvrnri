from .system_creator import SystemCreator, SystemConfig

def create_test_system() -> System:
    """Creates a test system"""
    config = SystemConfig(
        name="Test System",
        description="A test system",
        components=[ComponentA, ComponentB]
    )
    creator = SystemCreator(config)
    return creator.create_system()

class ComponentA:
    """A test component"""
    def __init__(self):
        pass

class ComponentB:
    """Another test component"""
    def __init__(self):
        pass