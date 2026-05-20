"""
Script para obtener estadísticas de jugadores del FC Barcelona en los últimos 20 años.
Este script consolida la información en un formato ordenado (Top Mayor a Menor).
"""

import os
import pandas as pd

def obtener_datos_barca():
    print("Iniciando la extracción de datos de los jugadores del FC Barcelona (Últimos 20 años)...")
    
    # Datos consolidados de las principales figuras del FC Barcelona en los últimos 20 años
    # que cubren competiciones oficiales (LaLiga, Champions League, Copa del Rey, etc.)
    jugadores_historicos = [
        {"jugador": "Lionel Messi", "partidos": 778, "goles": 672, "asistencias": 305},
        {"jugador": "Luis Suárez", "partidos": 283, "goles": 198, "asistencias": 113},
        {"jugador": "Neymar Jr", "partidos": 186, "goles": 105, "asistencias": 76},
        {"jugador": "Cesc Fàbregas", "partidos": 151, "goles": 42, "asistencias": 50},
        {"jugador": "Xavi Hernández", "partidos": 767, "goles": 85, "asistencias": 184},
        {"jugador": "Andrés Iniesta", "partidos": 674, "goles": 57, "asistencias": 138},
        {"jugador": "Pedro Rodríguez", "partidos": 321, "goles": 99, "asistencias": 46},
        {"jugador": "Samuel Eto'o", "partidos": 199, "goles": 130, "asistencias": 40},
        {"jugador": "Thierry Henry", "partidos": 121, "goles": 49, "asistencias": 27},
        {"jugador": "Ronaldinho", "partidos": 207, "goles": 94, "asistencias": 70},
        {"jugador": "Robert Lewandowski", "partidos": 95, "goles": 59, "asistencias": 19},
        {"jugador": "Ousmane Dembélé", "partidos": 185, "goles": 40, "asistencias": 43},
        {"jugador": "Ivan Rakitić", "partidos": 310, "goles": 35, "asistencias": 42},
        {"jugador": "Gerard Piqué", "partidos": 616, "goles": 53, "asistencias": 15},
        {"jugador": "Dani Alves", "partidos": 408, "goles": 22, "asistencias": 105},
        {"jugador": "Alexis Sánchez", "partidos": 141, "goles": 47, "asistencias": 35},
        {"jugador": "David Villa", "partidos": 119, "goles": 48, "asistencias": 24},
        {"jugador": "Antoine Griezmann", "partidos": 102, "goles": 35, "asistencias": 17},
        {"jugador": "Raphinha", "partidos": 80, "goles": 20, "asistencias": 25},
        {"jugador": "Ansu Fati", "partidos": 112, "goles": 29, "asistencias": 10},
    ]
    
    # Convertir a DataFrame de Pandas para procesar y ordenar fácilmente
    df = pd.DataFrame(jugadores_historicos)
    
    # Ordenar por goles de mayor a menor
    df_ordenado_goles = df.sort_values(by="goles", ascending=False)
    
    print("\n--- TOP JUGADORES POR GOLES ---")
    print(df_ordenado_goles.to_string(index=False))
    
    # Crear carpeta de resultados
    os.makedirs("resultados", exist_ok=True)
    
    # Guardar resultados ordenados
    df_ordenado_goles.to_csv("resultados/barca_stats_goles.csv", index=False, encoding="utf-8-sig")
    
    # También ordenamos por asistencias para generar un top alternativo
    df_ordenado_asistencias = df.sort_values(by="asistencias", ascending=False)
    df_ordenado_asistencias.to_csv("resultados/barca_stats_asistencias.csv", index=False, encoding="utf-8-sig")
    
    # Guardar un reporte general resumido en Markdown
    with open("resultados/README.md", "w", encoding="utf-8") as f:
        f.write("# Reporte Estadístico del FC Barcelona (Últimos 20 años)\n\n")
        f.write("Generado automáticamente mediante GitHub Actions.\n\n")
        f.write("## Top Jugadores por Goles\n\n")
        f.write(df_ordenado_goles.to_markdown(index=False))
        f.write("\n\n## Top Jugadores por Asistencias\n\n")
        f.write(df_ordenado_asistencias.to_markdown(index=False))

    print("\nProceso completado con éxito. Archivos guardados en la carpeta 'resultados/'.")

if __name__ == "__main__":
    obtener_datos_barca()
