"""
VERIFICADOR DE SOLUCIONES
=========================
Ejecuta TODAS las soluciones de este directorio y comprueba que ninguna
falla. Util si acabas de modificar algo o si quieres ver de un vistazo que
las respuestas esperadas siguen siendo correctas.

Uso:
    python verificar_soluciones.py
    python verificar_soluciones.py 09        (solo los que empiezan por 09)

Un archivo se considera correcto si:
    - se ejecuta sin SyntaxError
    - la salida NO contiene "[ERROR]"
"""

import subprocess
import sys
from pathlib import Path

# resolve() convierte la ruta en absoluta: asi los archivos que crean los
# ejercicios (datos.txt, biblioteca.json...) van siempre a esta carpeta,
# este donde ejecutes el script
CARPETA = Path(__file__).resolve().parent
CARPETA_SOLUCIONES = CARPETA / "soluciones"


def ejecutar(ruta):
    """Ejecuta un archivo y devuelve (nombre, ok, salida)."""
    # capture_output: el archivo se ejecuta sin ensuciar esta consola
    proceso = subprocess.run(
        [sys.executable, str(ruta)],
        capture_output=True,
        text=True,
        cwd=str(CARPETA),   # los archivos se crean en la carpeta ejercicios/
        encoding="utf-8",
        errors="replace",
    )
    salida = (proceso.stdout or "") + (proceso.stderr or "")

    if "SyntaxError" in salida or "IndentationError" in salida:
        return ruta.name, False, salida
    if "[ERROR]" in salida:
        return ruta.name, False, salida
    if proceso.returncode != 0:
        return ruta.name, False, salida
    return ruta.name, True, salida


def main():
    filtro = sys.argv[1] if len(sys.argv) > 1 else ""

    archivos = sorted(CARPETA_SOLUCIONES.glob("*.py"))
    if filtro:
        archivos = [a for a in archivos if a.name.startswith(filtro)]

    print(f"Verificando {len(archivos)} archivo(s) de solucion...\n")

    fallidos = []
    for ruta in archivos:
        nombre, ok, salida = ejecutar(ruta)
        if ok:
            print(f"  [OK]   {nombre}")
        else:
            print(f"  [FALLO] {nombre}")
            fallidos.append((nombre, salida))

    if fallidos:
        print("\n" + "=" * 62)
        print("DETALLE DE LOS FALLOS")
        print("=" * 62)
        for nombre, salida in fallidos:
            print(f"\n--- {nombre} ---")
            for linea in salida.splitlines():
                if "[ERROR]" in linea or "Error" in linea:
                    print("   ", linea.strip())
        print(f"\nResumen: {len(fallidos)} fallo(s).")
        return 1

    print("\nTodas las soluciones funcionan correctamente.")
    return 0


if __name__ == "__main__":
    sys.exit(main())