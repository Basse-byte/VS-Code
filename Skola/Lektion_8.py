import shutil
from pathlib import Path


## Inte rätt, öppnar sårbarhet för någon att injecera sin egen kod: ####################################################
# shutil.copy("Script.py", "Script.py.bak")
# print("File has been copied")

## Detta är bättre, hårdkodad path: ####################################################################################

# shutil.copy("C:\Users\bazze\OneDrive\Dokument\Plugg\Applied Script\VS Code\Skola\Script.py", "\opt\Script.py.bak")
# print("File has been copied")


########################################################################################################################


## Ta bort filer: ######################################################################################################

# shutil.rmtree("test_folder")
# print("Folder deleted")

## Flyttar fil eller bibliotek till ett annat dir ######################################################################

# shutil.move("test1", "test2")


## Skapa en zip ########################################################################################################

# shutil.make.archive("filen vi vill packa ner", "zip", "Vart vi vill flytta zip filen, som filsökväg")
# print("Backup created")


## Pathlib #############################################################################################################


# p = Path("Users\bazze\OneDrive\Dokument\Plugg\Applied Script\VS Code\Skola\sesttest.txt")
# ## Eller:
# p = Path.home() / "dokument" / "python" / "backup"
# print(p)

## Bestämmer exakt vart filen ska finnas, skapar nya dir vid behov. ##########################
# p = Path.cwd() / "dokument" / "*.txt" # *.txt betyder alla .txt filer
# dest = Path.cwd() / "backup" / "file.txt"

# print(p)
# print(dest)


## Kontrollerar om en viss fil har en viss filändelse ########################################

# file_path = p /"example_file.txt"
# if file_path.suffix == ".txt":
#     print("Detta är en textfil.")

