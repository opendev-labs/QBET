"""
QBET Environment (Scope Management)
Manages variable scopes and symbol tables.
"""

from errors import NameError as QBETNameError

class Environment:
    """Manages variable scopes"""
    
    def __init__(self, parent=None):
        self.parent = parent
        self.variables = {}
    
    def define(self, name, value):
        """Define a new variable in current scope"""
        self.variables[name] = value
    
    def get(self, name):
        """Get variable value"""
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise QBETNameError(name)
    
    def set(self, name, value):
        """Set variable value (must exist)"""
        if name in self.variables:
            self.variables[name] = value
        elif self.parent:
            self.parent.set(name, value)
        else:
            raise QBETNameError(name)
    
    def exists(self, name):
        """Check if variable exists"""
        if name in self.variables:
            return True
        elif self.parent:
            return self.parent.exists(name)
        return False
