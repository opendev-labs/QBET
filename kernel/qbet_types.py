"""
QBET Type System
Defines all types used in the QBET language including primitive, quantum, and spiritual types.
"""

from enum import Enum, auto

class QBETType(Enum):
    """Enumeration of all QBET types"""
    # Primitive types
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()
    NULL = auto()
    
    # Quantum types
    QUBIT = auto()
    WAVE = auto()
    PARTICLE = auto()
    MATRIX = auto()
    
    # Spiritual types
    SPIRIT = auto()
    SOUL = auto()
    CONSCIOUSNESS = auto()
    CHAKRA = auto()
    ENERGY = auto()
    FREQUENCY = auto()
    VIBRATION = auto()
    
    # Biological types
    DNA = auto()
    CELL = auto()
    NEURON = auto()
    
    # Cosmic types
    PLANET = auto()
    STAR = auto()
    GALAXY = auto()
    
    # Collection types
    UNIVERSE = auto()
    MULTIVERSE = auto()
    ARRAY = auto()
    
    # Function type
    FUNCTION = auto()
    
    # Object type
    OBJECT = auto()

class QBETValue:
    """Base class for all QBET values"""
    def __init__(self, value, qtype):
        self.value = value
        self.type = qtype
    
    def __repr__(self):
        return f"QBETValue({self.value}, {self.type})"
    
    def __str__(self):
        return str(self.value)

class Number(QBETValue):
    """Numeric value"""
    def __init__(self, value):
        super().__init__(float(value), QBETType.NUMBER)

class String(QBETValue):
    """String value"""
    def __init__(self, value):
        super().__init__(str(value), QBETType.STRING)

class Boolean(QBETValue):
    """Boolean value"""
    def __init__(self, value):
        super().__init__(bool(value), QBETType.BOOLEAN)

class Null(QBETValue):
    """Null/None value"""
    def __init__(self):
        super().__init__(None, QBETType.NULL)

class Qubit(QBETValue):
    """Quantum bit with superposition"""
    def __init__(self, alpha=1.0, beta=0.0):
        self.alpha = alpha  # Probability amplitude for |0⟩
        self.beta = beta    # Probability amplitude for |1⟩
        super().__init__({'alpha': alpha, 'beta': beta}, QBETType.QUBIT)
    
    def measure(self):
        """Collapse to classical bit"""
        import random
        prob_zero = abs(self.alpha) ** 2
        return 0 if random.random() < prob_zero else 1

class Chakra(QBETValue):
    """Chakra energy center"""
    def __init__(self, name, level=50):
        self.name = name
        self.level = level  # Energy level 0-100
        super().__init__({'name': name, 'level': level}, QBETType.CHAKRA)

class Energy(QBETValue):
    """Energy value with frequency and vibration"""
    def __init__(self, amount, frequency=1.0, vibration=1.0):
        self.amount = amount
        self.frequency = frequency
        self.vibration = vibration
        super().__init__({
            'amount': amount,
            'frequency': frequency,
            'vibration': vibration
        }, QBETType.ENERGY)

class Universe(QBETValue):
    """Universe container"""
    def __init__(self):
        self.entities = {}
        super().__init__(self.entities, QBETType.UNIVERSE)
    
    def add(self, name, entity):
        self.entities[name] = entity

class Function(QBETValue):
    """Function value"""
    def __init__(self, params, body, env):
        self.params = params
        self.body = body
        self.env = env
        super().__init__({'params': params, 'body': body}, QBETType.FUNCTION)
