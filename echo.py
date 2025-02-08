# echo.py

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    virt_echo=""
    for i in range(repetitions, 0, -1):
        virt_echo += text[-i:] + "\n" #Takes our last i characters, gives us our fading effect and a newline
    return virt_echo




if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
