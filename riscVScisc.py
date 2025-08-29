
# Memoria Predefinida
memory = [
    {0: 1}, {1: 2}, {2: 3}, {3: 4}, {4: 5}, {5: 6}, {6: 7}, {7: 8}, {8: 9}, {9: 10},
    {100: 10}, {101: 20}, {102: 30}, {103: 40}, {104: 50}, {105: 60}, {106: 70}, {107: 80}, {108: 90}, {109: 100},
    {200: 0}, {201: 0}, {202: 0}, {203: 0}, {204: 0}, {205: 0}, {206: 0}, {207: 0}, {208: 0}, {209: 0}
]

"""
Class: CISC_CPU

Attributes:
    - memory (list[dict]): Memoria principal simulada.
    - instrs (int): Número total de instrucciones ejecutadas.
    - cycles (int): Número total de ciclos de reloj consumidos.
    - cycles_per_instrs (int): Ciclos consumidos por instrucción (valor fijo en 3).

Constructor:
    - __init__(memory): Inicializa la CPU CISC con la memoria dada, y pone a cero las estadísticas.

Methods:
    - update_stats(): Actualiza el número de instrucciones ejecutadas y ciclos consumidos.
    - SUMMEM(addr1, addr2, dest): Suma los valores de dos direcciones de memoria y guarda el resultado en una tercera.
"""
class CISC_CPU:
    cycles_per_instrs = 3

    """
    Constructor de la clase CISC_CPU
    """
    def __init__(self, memory):
        self.memory = memory
        self.instrs = 0
        self.cycles = 0

    """
    Function: update_stats
    Actualiza las estadisticas de instrucciones y ciclos
    """
    def update_stats(self):
        self.instrs += 1
        self.cycles += self.cycles_per_instrs

    """
    Function: SUMMEM
    Suma los valores de dos direcciones de memoria y almacena el resultado en una tercera dirección
    
    Params: 
        - addr1: Dirección de memoria del primer operando
        - addr2: Dirección de memoria del segundo operando
        - dest: Dirección de memoria donde se almacenará el resultado
    
    Returns: None
    """
    def SUMMEM(self, addr1: int, addr2: int, dest: int):
        for cell in self.memory:
            if addr1 in cell:
                val1 = cell[addr1]
            if addr2 in cell:
                val2 = cell[addr2]
            if dest in cell:
                cell[dest] = val1 + val2
        self.update_stats()

"""
Class: RISC_CPU

Attributes:
    - memory (list[dict]): Memoria principal simulada.
    - instrs (int): Número total de instrucciones ejecutadas.
    - cycles (int): Número total de ciclos de reloj consumidos.
    - cycles_per_instrs (int): Ciclos consumidos por instrucción (valor fijo en 1).
    - rA (int): Registro de entrada A.
    - rB (int): Registro de entrada B.
    - rR (int): Registro de resultado.

Constructor:
    - __init__(memory): Inicializa la CPU RISC con la memoria dada, los registros en cero y las estadísticas vacías.

Methods:
    - update_stats(): Actualiza el número de instrucciones ejecutadas y ciclos consumidos.
    - load_rA(addr): Carga un valor desde memoria en el registro rA.
    - load_rB(addr): Carga un valor desde memoria en el registro rB.
    - add(rA, rB): Suma los valores de rA y rB, almacenando el resultado en rR.
    - write(addr, data): Escribe el valor en el registro rR hacia una dirección de memoria.
"""
class RISC_CPU:
    cycles_per_instrs = 1

    """
    Constructor de la clase RISC_CPU
    """
    def __init__(self, memory):
        self.memory = memory
        self.instrs = 0
        self.cycles = 0

        self.rA = 0
        self.rB = 0
        self.rR = 0

    """
    Function: update_stats()
    Actualiza el número de instrucciones ejecutadas y los ciclos consumidos.
    
    Params: None
    
    Returns: None
    """
    def update_stats(self):
        self.instrs += 1
        self.cycles += self.cycles_per_instrs

    """
    Function: load_rA
    Carga el valor de la memoria en el registro rA
    
    Params: 
        - addr: Dirección de memoria a cargar

    Returns: None
    """
    def load_rA(self, addr: int):
        for cell in self.memory:
            if addr in cell:
                self.rA = cell[addr]
                break
        self.update_stats()

    """
    Function: load_rB
    Carga el valor de la memoria en el registro rB

    Params: 
        - addr: Dirección de memoria a cargar

    Returns: None
    """
    def load_rB(self, addr: int):
        for cell in self.memory:
            if addr in cell:
                self.rB = cell[addr]
                break
        self.update_stats()

    """
    Function: add
    Suma los valores de los registros rA y rB

    Params:
        - rA: Valor del registro rA
        - rB: Valor del registro rB

    Returns: None
    """
    def add(self, rA: int, rB:int):
        self.rR = rA + rB
        self.update_stats()

    """
    Function: write
    Escribe un valor en la memoria

    Params:
        - addr: Dirección de memoria donde se escribirá el valor
        - data: Valor a escribir en la memoria

    Returns: None
    """
    def write(self, addr: int, data: int):
        for cell in self.memory:
            if addr in cell:
                cell[addr] = data
                break
        self.update_stats()

"""
Function: print_results(cpu)  
Imprime el contenido de la memoria de resultados (direcciones 200–209) y las estadísticas de rendimiento de la CPU.  

Params:  
    - cpu (CISC_CPU | RISC_CPU): Instancia de CPU sobre la cual se imprimen los resultados.  

Returns: None 
"""
def print_results(cpu):
    # Imprimir resultados de la memoria
    print("Resultados de la memoria:")
    for i in range(200, 210):
        for cell in cpu.memory:
            if i in cell:
                print(f"Mem[{i}] = {cell[i]}")
                break
    # Imprimir resultados de rendimiento
    print("Rendimiento:")
    print("Instrucciones: ", cpu.instrs)
    print("Ciclos: ", cpu.cycles)

"""
Function: main()  
Función principal que ejecuta la simulación de los procesadores RISC y CISC.  
    - Suma dos vectores de tamaño 10 usando RISC_CPU.  
    - Suma los mismos vectores usando CISC_CPU.  
    - Imprime resultados y estadísticas de ambos procesadores.  

Params: None  

Returns: None 
"""
def main():
    RISC = RISC_CPU(memory)
    # Sumar dos vectores y guardar el resultado 
    for i in range(10):
        RISC.load_rA(i)
        RISC.load_rB(i + 100)
        RISC.add(RISC.rA, RISC.rB)
        RISC.write(i + 200, RISC.rR)

    print("========RISC========")
    print_results(RISC)

    CISC = CISC_CPU(memory)
    # Sumar dos vectores y guardar el resultado
    for i in range(10):
        CISC.SUMMEM(i, i + 100, i + 200)
    print("========CISC========")
    print_results(CISC)

if __name__ == "__main__":
    main()