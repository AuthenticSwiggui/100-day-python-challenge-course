
def ui() -> None:
    while True:
        a = int(input("Number A: "))
        b = int(input("Number B: "))
        for symbol in operations:
            print(symbol)
        operation = input("Which operation do you wanna make? ")
        
        resultado = operations[operation](a, b)
        print(f"{a} {operation} {b} = {resultado}")
        choice = input("Do you wanna continue? y?n \n").lower()
        if choice == "no":
            break
        ui()
    
    


def zuma(a, b) -> int:
    return a + b

def resta(a, b) -> int:
    return a - b

def multiply(a, b) -> float:
    return a * b

def divide(a, b) -> float:
    if b == 0:
        print("Operación imposible de realizar")
        return None
    return a / b

operations = {
        "+": zuma,
        "-": resta,
        "*": multiply,
        "/": divide
    }

def main() -> None:
    ui()

if __name__ == "__main__":
    main()