import argparse

parser = argparse.ArgumentParser(description="Mitt krypteringsverktyg") # Startar argparse

parser.add_argument("name", help="Ange ditt problem ")
parser.add_argument("age", type=int, help="Ange din ålder")

parser.add_argument("-v","--verbose", action="store_true", help="Visa mer information") # -v == --verbose.

args = parser.parse_args()

if args.verbose: # Om man skriver i terminalen: filnamn.py Basse 30 -v så händer:
    print(f"Hej {args.name}, din ålder: {args.age}")
else:
    print(f"Hej {args.name}")



## Kör olika funktioner beroende på vad användaren skriver. T.ex. encrypt (kör func_encrypt).
