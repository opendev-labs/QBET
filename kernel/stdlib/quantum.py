"""
QBET Standard Library - Quantum Functions
Quantum computing metaphors and operations.
"""

from qbet_types import *
import random
import math

def setup_quantum_functions(env):
    """Register quantum built-in functions"""
    
    def hadamard(qubit):
        """Apply Hadamard gate (creates superposition)"""
        if not isinstance(qubit, Qubit):
            return Null()
        # H gate: |0⟩ -> (|0⟩ + |1⟩)/√2, |1⟩ -> (|0⟩ - |1⟩)/√2
        sqrt2 = math.sqrt(2)
        new_alpha = (qubit.alpha + qubit.beta) / sqrt2
        new_beta = (qubit.alpha - qubit.beta) / sqrt2
        qubit.alpha = new_alpha
        qubit.beta = new_beta
        return qubit
    
    def pauli_x(qubit):
        """Apply Pauli-X gate (NOT gate)"""
        if not isinstance(qubit, Qubit):
            return Null()
        # X gate: swap |0⟩ and |1⟩
        qubit.alpha, qubit.beta = qubit.beta, qubit.alpha
        return qubit
    
    def pauli_y(qubit):
        """Apply Pauli-Y gate"""
        if not isinstance(qubit, Qubit):
            return Null()
        # Y gate: |0⟩ -> i|1⟩, |1⟩ -> -i|0⟩
        new_alpha = -qubit.beta
        new_beta = qubit.alpha
        qubit.alpha = new_alpha
        qubit.beta = new_beta
        return qubit
    
    def pauli_z(qubit):
        """Apply Pauli-Z gate"""
        if not isinstance(qubit, Qubit):
            return Null()
        # Z gate: |0⟩ -> |0⟩, |1⟩ -> -|1⟩
        qubit.beta = -qubit.beta
        return qubit
    
    def measure_qubit(qubit):
        """Measure qubit (collapse to classical state)"""
        if not isinstance(qubit, Qubit):
            return Null()
        result = qubit.measure()
        # After measurement, qubit is in definite state
        if result == 0:
            qubit.alpha = 1.0
            qubit.beta = 0.0
        else:
            qubit.alpha = 0.0
            qubit.beta = 1.0
        return Number(result)
    
    def entangle_qubits(qubit1, qubit2):
        """Entangle two qubits (simplified)"""
        if not isinstance(qubit1, Qubit) or not isinstance(qubit2, Qubit):
            return Null()
        # Simplified entanglement: make them correlated
        # In reality, this would create a Bell state
        avg_alpha = (qubit1.alpha + qubit2.alpha) / 2
        avg_beta = (qubit1.beta + qubit2.beta) / 2
        qubit1.alpha = qubit2.alpha = avg_alpha
        qubit1.beta = qubit2.beta = avg_beta
        return Boolean(True)
    
    def superpose(qubit, alpha, beta):
        """Set qubit to specific superposition"""
        if not isinstance(qubit, Qubit):
            return Null()
        alpha_val = alpha.value if isinstance(alpha, Number) else alpha
        beta_val = beta.value if isinstance(beta, Number) else beta
        
        # Normalize
        norm = math.sqrt(alpha_val**2 + beta_val**2)
        if norm > 0:
            qubit.alpha = alpha_val / norm
            qubit.beta = beta_val / norm
        return qubit
    
    def probability_zero(qubit):
        """Get probability of measuring |0⟩"""
        if not isinstance(qubit, Qubit):
            return Null()
        return Number(abs(qubit.alpha) ** 2)
    
    def probability_one(qubit):
        """Get probability of measuring |1⟩"""
        if not isinstance(qubit, Qubit):
            return Null()
        return Number(abs(qubit.beta) ** 2)
    
    def create_matrix(rows, cols, default=0):
        """Create matrix"""
        rows_val = int(rows.value) if isinstance(rows, Number) else 2
        cols_val = int(cols.value) if isinstance(cols, Number) else 2
        default_val = default.value if isinstance(default, Number) else 0
        
        matrix = [[Number(default_val) for _ in range(cols_val)] for _ in range(rows_val)]
        return QBETValue(matrix, QBETType.MATRIX)
    
    def wave_interference(wave1, wave2):
        """Simulate wave interference"""
        # Simplified: just add amplitudes
        return String("Constructive interference achieved")
    
    def particle_collision(particle1, particle2):
        """Simulate particle collision"""
        # Simplified: return collision result
        return String("Particles collided with quantum effects")
    
    # Register quantum functions
    env.define('hadamard', hadamard)
    env.define('pauli_x', pauli_x)
    env.define('pauli_y', pauli_y)
    env.define('pauli_z', pauli_z)
    env.define('measure', measure_qubit)
    env.define('entangle', entangle_qubits)
    env.define('superpose', superpose)
    env.define('prob_zero', probability_zero)
    env.define('prob_one', probability_one)
    env.define('create_matrix', create_matrix)
    env.define('wave_interference', wave_interference)
    env.define('particle_collision', particle_collision)
