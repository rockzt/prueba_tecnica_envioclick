from ExcelSheet import ExcelSheet

import sys
import os

def display_menu():
    # Clears the terminal screen for a cleaner look (os.system works on most systems)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*20)
    print("MENU Excel")
    print("="*20)
    print("1. Insertar Informacion en Celda")
    print("2. Actualizar Informacion en Celda")
    print("3. Validar Informacion en Celda")
    print("4. Preview Celdas")
    print("5. Sumar Valores en Fila")
    print("6. Sumar Valores en Columna")
    print("7. Exit")
    print("="*20)

def handle_choice(choice, sheet):
    if choice == '1':
        print("Insertar Informacion en celda.")
        sheet.preview()
        row = input("Elige la fila: ").strip()
        column = input("Elige la columna: ").strip()
        value = input("Escribe el valor a insertar: ").strip()
        sheet.insert(int(row), int(column), int(value))
    elif choice == '2':
        print("Actualizar Informacion en celda.")
        sheet.preview()
        row = input("Elige la fila: ").strip()
        column = input("Elige la columna: ").strip()
        value = input("Escribe el valor a insertar: ").strip()
        sheet.update(int(row), int(column), int(value))
    elif choice == '3':
        print("Validar informacin en celda.")
        row = input("Elige la fila: ").strip()
        column = input("Elige la columna: ").strip()
        print(f"Celda ({row},{column}): {"contiene informacion" if sheet.has_value(int(row), int(column)) else "no contiene informacion"}")
    elif choice == '4':
        print("Preview.")
        sheet.preview()
    elif choice == '5':
        print("Sumar valores en fila.")
        sheet.preview()
        choice = input("Elige la file: ").strip()
        print(sheet.sum_row(int(choice)))
    elif choice == '6':
        print("Sumar valores en columna.")
        sheet.preview()
        choice = input("Elige la columna: ").strip()
        print(sheet.sum_column(int(choice)))
    elif choice == '7':
        print("Cerrando programa....")
        sys.exit()
    else:
        print("Opcion invalida. Prueba de nuevo.")

    input("\nPresiona Enter para continuar...")

def main():
    print("Establece el tamano de la hoja de excel")
    rows = input("Filas: ").strip()
    columns = input("Columnas: ").strip()
    sheet = ExcelSheet(rows=int(rows), cols=int(columns))
    while True:
        display_menu()
        choice = input("Elige una opcion (1-7): ").strip()
        handle_choice(choice, sheet)

if __name__ == "__main__":
    main()