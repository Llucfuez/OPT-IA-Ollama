import argparse
import ollama

def main():
    parser = argparse.ArgumentParser(description="Genera text amb Gemma3:4b.")
    parser.add_argument("prompt", help="El prompt a generar.")
    parser.add_argument("--vegades", type=int, default=5, help="Número de vegades a repetir el prompt.")
    parser.add_argument("--temperature", type=float, default=0.8, help="Temperatura per a la generació (0.0 - 1.0).")

    args = parser.parse_args()

    print(f"Prompt: {args.prompt}")
    print(f"vegades: {args.vegades}")
    print(f"temperature: {args.temperature}")
    print("\n")

    for i in range(1, args.vegades + 1):
        try:
            response = ollama.generate(
                model="gemma3:4b",
                prompt=args.prompt,
                options={
                    "temperature": args.temperature,
                    "seed": i,  # Utilitzem el número de repetició com a semilla
                    "top_k": 50,
                    "top_p": 0.95,
                    "num_predict": 256 # Ajustat per millorar la fluïdesa
                }
            )
            print(f"{i}. {response['response']}")
        except Exception as e:
            print(f"Error al generar la resposta {i}: {e}")

if __name__ == "__main__":
    main()