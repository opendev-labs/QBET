"""
QBET Standard Library - Core Functions
Basic I/O, data structures, and utilities.
"""

from qbet_types import *

def setup_core_functions(env):
    """Register core built-in functions"""
    
    # I/O Functions
    def qbet_print(*args):
        """Print values to console"""
        values = [str(arg.value) if hasattr(arg, 'value') else str(arg) for arg in args]
        print(' '.join(values))
        return Null()
    
    def qbet_input(prompt=None):
        """Get user input"""
        prompt_str = prompt.value if prompt and hasattr(prompt, 'value') else ""
        result = input(prompt_str)
        return String(result)
    
    # Type conversion
    def qbet_number(value):
        """Convert to number"""
        if isinstance(value, Number):
            return value
        elif isinstance(value, String):
            try:
                return Number(float(value.value))
            except ValueError:
                return Null()
        elif isinstance(value, Boolean):
            return Number(1.0 if value.value else 0.0)
        return Null()
    
    def qbet_string(value):
        """Convert to string"""
        if isinstance(value, String):
            return value
        return String(str(value.value) if hasattr(value, 'value') else str(value))
    
    def qbet_boolean(value):
        """Convert to boolean"""
        if isinstance(value, Boolean):
            return value
        if isinstance(value, Null):
            return Boolean(False)
        if isinstance(value, Number):
            return Boolean(value.value != 0)
        if isinstance(value, String):
            return Boolean(len(value.value) > 0)
        return Boolean(True)
    
    # Math functions
    def qbet_abs(value):
        """Absolute value"""
        if not isinstance(value, Number):
            return Null()
        return Number(abs(value.value))
    
    def qbet_sqrt(value):
        """Square root"""
        if not isinstance(value, Number):
            return Null()
        import math
        return Number(math.sqrt(value.value))
    
    def qbet_sin(value):
        """Sine"""
        if not isinstance(value, Number):
            return Null()
        import math
        return Number(math.sin(value.value))
    
    def qbet_cos(value):
        """Cosine"""
        if not isinstance(value, Number):
            return Null()
        import math
        return Number(math.cos(value.value))
    
    def qbet_floor(value):
        """Floor"""
        if not isinstance(value, Number):
            return Null()
        import math
        return Number(math.floor(value.value))
    
    def qbet_ceil(value):
        """Ceiling"""
        if not isinstance(value, Number):
            return Null()
        import math
        return Number(math.ceil(value.value))
    
    def qbet_round(value):
        """Round"""
        if not isinstance(value, Number):
            return Null()
        return Number(round(value.value))
    
    # Array functions
    def qbet_len(value):
        """Get length"""
        if isinstance(value, String):
            return Number(len(value.value))
        elif hasattr(value, 'value') and isinstance(value.value, list):
            return Number(len(value.value))
        return Null()
    
    def qbet_push(array, element):
        """Add element to array"""
        if hasattr(array, 'value') and isinstance(array.value, list):
            array.value.append(element)
            return array
        return Null()
    
    def qbet_pop(array):
        """Remove last element from array"""
        if hasattr(array, 'value') and isinstance(array.value, list) and len(array.value) > 0:
            return array.value.pop()
        return Null()
    
    # Utility functions
    def qbet_type(value):
        """Get type of value"""
        if hasattr(value, 'type'):
            return String(str(value.type.name))
        return String("unknown")
    
    def qbet_range(start, end=None, step=None):
        """Create range array"""
        if end is None:
            start_val = 0
            end_val = int(start.value) if isinstance(start, Number) else 0
            step_val = 1
        else:
            start_val = int(start.value) if isinstance(start, Number) else 0
            end_val = int(end.value) if isinstance(end, Number) else 0
            step_val = int(step.value) if step and isinstance(step, Number) else 1
        
        result = [Number(i) for i in range(start_val, end_val, step_val)]
        return QBETValue(result, QBETType.ARRAY)
    
    # Register all functions
    env.define('print', qbet_print)
    env.define('input', qbet_input)
    env.define('number', qbet_number)
    env.define('string', qbet_string)
    env.define('boolean', qbet_boolean)
    env.define('abs', qbet_abs)
    env.define('sqrt', qbet_sqrt)
    env.define('sin', qbet_sin)
    env.define('cos', qbet_cos)
    env.define('floor', qbet_floor)
    env.define('ceil', qbet_ceil)
    env.define('round', qbet_round)
    env.define('len', qbet_len)
    env.define('push', qbet_push)
    env.define('pop', qbet_pop)
    env.define('type', qbet_type)
    env.define('range', qbet_range)
