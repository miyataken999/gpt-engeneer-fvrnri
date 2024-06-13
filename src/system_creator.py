from dataclasses import dataclass

@dataclass
class SystemConfig:
    """Represents a system configuration"""
    name: str
    description: str
    components: list

class SystemCreator:
    """Creates a system based on a configuration"""
    def __init__(self, config: SystemConfig):
        self.config = config

    def create_system(self):
        """Creates a system based on the configuration"""
        # Create system components
        components = [component() for component in self.config.components]
        # Initialize system
        system = System(self.config.name, self.config.description, components)
        return system

class System:
    """Represents a system"""
    def __init__(self, name: str, description: str, components: list):
        self.name = name
        self.description = description
        self.components = components