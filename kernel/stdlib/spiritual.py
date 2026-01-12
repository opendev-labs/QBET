"""
QBET Standard Library - Spiritual Functions
Spiritual and metaphysical operations.
"""

from qbet_types import *
import random

def setup_spiritual_functions(env):
    """Register spiritual built-in functions"""
    
    def balance_chakra(chakra, amount=None):
        """Balance a chakra"""
        if not isinstance(chakra, Chakra):
            return Null()
        
        if amount:
            amt = amount.value if isinstance(amount, Number) else 10
            chakra.level = min(100, max(0, chakra.level + amt))
        else:
            # Auto-balance to 50
            chakra.level = 50
        
        return chakra
    
    def charge_energy(energy, amount):
        """Charge energy"""
        if not isinstance(energy, Energy):
            return Null()
        
        amt = amount.value if isinstance(amount, Number) else 10
        energy.amount += amt
        return energy
    
    def set_frequency(energy, freq):
        """Set energy frequency"""
        if not isinstance(energy, Energy):
            return Null()
        
        freq_val = freq.value if isinstance(freq, Number) else 1.0
        energy.frequency = freq_val
        return energy
    
    def set_vibration(energy, vib):
        """Set energy vibration"""
        if not isinstance(energy, Energy):
            return Null()
        
        vib_val = vib.value if isinstance(vib, Number) else 1.0
        energy.vibration = vib_val
        return energy
    
    def karma_action(action, consequence):
        """Execute karma (cause and effect)"""
        action_str = action.value if isinstance(action, String) else str(action)
        consequence_str = consequence.value if isinstance(consequence, String) else str(consequence)
        
        # Log karma action
        result = f"Karma: {action_str} -> {consequence_str}"
        return String(result)
    
    def dharma_purpose(process, purpose):
        """Define dharma (purpose)"""
        process_str = process.value if isinstance(process, String) else str(process)
        purpose_str = purpose.value if isinstance(purpose, String) else str(purpose)
        
        result = f"Dharma: {process_str} serves {purpose_str}"
        return String(result)
    
    def manifest(intention):
        """Manifest intention (Law of Attraction)"""
        intention_str = intention.value if isinstance(intention, String) else str(intention)
        return String(f"Manifesting: {intention_str}")
    
    def attract(entity1, entity2):
        """Attract two entities (Law of Attraction)"""
        return String("Entities attracted through resonance")
    
    def transmute_energy(energy, new_form):
        """Transmute energy to new form"""
        if not isinstance(energy, Energy):
            return Null()
        
        form_str = new_form.value if isinstance(new_form, String) else "light"
        return String(f"Energy transmuted to {form_str}")
    
    def raise_consciousness(entity, level):
        """Raise consciousness level"""
        level_val = level.value if isinstance(level, Number) else 1
        return String(f"Consciousness raised by {level_val} levels")
    
    def connect_astral(entity1, entity2):
        """Connect entities on astral plane"""
        return String("Astral connection established")
    
    def higher_self_guide(task):
        """Receive guidance from higher self"""
        task_str = task.value if isinstance(task, String) else str(task)
        guidance = [
            "Trust your intuition",
            "Follow the path of love",
            "Seek balance and harmony",
            "Embrace your divine purpose",
            "Connect with universal consciousness"
        ]
        return String(random.choice(guidance))
    
    def meditate(duration):
        """Meditate for spiritual growth"""
        dur = duration.value if isinstance(duration, Number) else 5
        return String(f"Meditated for {dur} minutes. Inner peace achieved.")
    
    def align_chakras():
        """Align all chakras"""
        chakras = ["Root", "Sacral", "Solar Plexus", "Heart", "Throat", "Third Eye", "Crown"]
        return String(f"All {len(chakras)} chakras aligned")
    
    def create_sacred_geometry(pattern):
        """Create sacred geometry pattern"""
        pattern_str = pattern.value if isinstance(pattern, String) else "Flower of Life"
        return String(f"Sacred geometry created: {pattern_str}")
    
    def invoke_element(element):
        """Invoke elemental energy"""
        elem_str = element.value if isinstance(element, String) else "earth"
        elements = {
            "earth": "Stability and grounding",
            "water": "Flow and emotion",
            "fire": "Transformation and energy",
            "air": "Intellect and movement",
            "ether": "Spirit and connection"
        }
        return String(elements.get(elem_str.lower(), "Unknown element"))
    
    def golden_ratio():
        """Return the golden ratio (phi)"""
        return Number(1.618033988749895)
    
    def fibonacci(n):
        """Generate Fibonacci number"""
        n_val = int(n.value) if isinstance(n, Number) else 1
        if n_val <= 0:
            return Number(0)
        elif n_val == 1:
            return Number(1)
        
        a, b = 0, 1
        for _ in range(2, n_val + 1):
            a, b = b, a + b
        return Number(b)
    
    def tesla_369(operation):
        """Apply Tesla's 369 principle"""
        op_str = operation.value if isinstance(operation, String) else "amplify"
        return String(f"369 principle applied: {op_str}")
    
    # Register spiritual functions
    env.define('balance_chakra', balance_chakra)
    env.define('charge_energy', charge_energy)
    env.define('set_frequency', set_frequency)
    env.define('set_vibration', set_vibration)
    env.define('karma', karma_action)
    env.define('dharma', dharma_purpose)
    env.define('manifest', manifest)
    env.define('attract', attract)
    env.define('transmute', transmute_energy)
    env.define('raise_consciousness', raise_consciousness)
    env.define('connect_astral', connect_astral)
    env.define('higher_self_guide', higher_self_guide)
    env.define('meditate', meditate)
    env.define('align_chakras', align_chakras)
    env.define('sacred_geometry', create_sacred_geometry)
    env.define('invoke_element', invoke_element)
    env.define('golden_ratio', golden_ratio)
    env.define('fibonacci', fibonacci)
    env.define('tesla_369', tesla_369)
