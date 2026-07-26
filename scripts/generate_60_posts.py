import os
from datetime import datetime, timedelta

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "content", "posts")
TAG = "laureanoeng-21"
START_DATE = datetime(2026, 8, 10)

ASINS = {
    # Ratones
    "Logitech G203 Lightsync": "B07W5JKFQC",
    "Logitech G203": "B07W5JKFQC",
    "Razer DeathAdder Essential": "B092R5MCB3",
    "SteelSeries Rival 3": "B082XQHPCL",
    "HyperX Pulsefire Core": "B07H3GFJJ2",
    "Corsair Katar Pro XT": "B08SHCKVTG",
    "Logitech G305": "B0848T8BG6",
    "Razer Viper Mini": "B0841GJ9PJ",
    "Razer Basilisk V3": "B09Q3D2ZYZ",
    "Corsair Harpoon RGB Wireless": "B09N3FTK1R",
    # Teclados
    "Redragon K552": "B016MAK38U",
    "Redragon K552 Kumara": "B016MAK38U",
    "Royal Kludge RK61": "B09JK2DSSZ",
    "HyperX Alloy Core": "B08934QWQY",
    "Keychron C1 Pro": "B0DYJQ5Z2Z",
    "Tecware Phantom 87": "B079HQBYDD",
    "RK Royal Kludge RK84": "B08X4L2L3S",
    "Redragon K530 Draconic": "B08C5YQG5T",
    "Logitech G413 SE": "B09HTQQ4GP",
    "SteelSeries Apex 3": "B08G1PG8Z2",
    # Auriculares
    "HyperX Cloud Stinger": "B07Y8SDD2N",
    "Razer BlackShark V2 X": "B089SSFV85",
    "Logitech G335": "B07W6J6TG5",
    "Corsair HS35": "B0CZTN664T",
    "HyperX Cloud Earbuds": "B07GW283KL",
    "Razer Hammerhead X": "B08Z4GQS4X",
    "SteelSeries Arctis Nova 1": "B0BVNVS9WK",
    "Corsair HS55": "B0C5Y4PHR5",
    "Logitech G435": "B09B7MZ1G7",
    "Turtle Beach Atlas One": "B08B6W1Z7Y",
    # Alfombrillas
    "SteelSeries QcK": "B000UEZ36W",
    "Corsair MM300": "B08JH7H1NG",
    "HyperX Fury S": "B07CZ9NPKV",
    "Razer Gigantus V2": "B07X6F4ZPJ",
    "Logitech G640": "B084Y3D1H4",
    # Monitores
    "AOC 24G2": "B07Y3RYLVH",
    "AOC 24G2SP": "B09WF96MFV",
    "LG 27UP600": "B096BCKDZC",
    "Dell S2722QC": "B09CGY99X5",
    "AOC C24G1": "B07DTN4BM8",
    "MSI G244F": "B0CB8NMLQK",
    "ASUS VP249QGR": "B082NWNK1F",
    "Sceptre E248B": "B088VMY23M",
    "Gigabyte G24F 2": "B0BPCLL9V6",
    "Dell S2422HG": "B08V8YYLDV",
    "MSI Optix G24C4": "B08PF8Q8LW",
    "Samsung CRG5": "B07TGMC29J",
    "Samsung M7": "B09RBB1WV4",
    "LG 34WP60C": "B09GJSG6Y2",
    "Gigabyte G27Q": "B08C5Y5Z5Z",
    # PCs
    "AMD Ryzen 5 5600": "B0BN5RSFQV",
    "RX 6600": "B09MFW2FM1",
    "Intel Core i5-12400F": "B0BN5VTYG2",
    "RTX 3060": "B09ZL93Y3G",
    # Cámaras y micrófonos
    "Logitech C270": "B07F7VQJRG",
    "Logitech C270 Webcam": "B07F7VQJRG",
    "FIFINE K669B": "B0BVXQFCSB",
    "FIFINE K669B Micrófono": "B0BVXQFCSB",
    "Logitech C920": "B08DR7T8G7",
    "Blue Snowball Ice": "B074X9RGHY",
    # Mandos
    "Mando Xbox Series X/S": "B0F2NC69KK",
    "8BitDo Pro 2": "B0CSPH1JYV",
    "Gulikit KingKong 2": "B0B1VHQW5B",
    "Mando Xbox One": "B07QH3R5T5",
    # Tablets
    "Samsung Galaxy Tab A9+": "B0CMD9WWC9",
    "Lenovo Tab M10 Plus": "B0C5NVP4WV",
    "Amazon Fire HD 10": "B0B5H3Q1Y7",
    # Earbuds
    "KZ ZSN Pro X": "B08TR39Y9H",
    "HyperX Cloud Earbuds": "B07GW283KL",
    # Routers
    "TP-Link Archer AX10": "B07YP3T5H7",
    "TP-Link Archer AX20": "B088H34DW9",
    "ASUS RT-AX1800S": "B09M9477NS",
    "TP-Link Archer AX55": "B09G7K5Z3Z",
    # RGB / Iluminación
    "Tira LED Govee RGBIC": "B09CSXL7PK",
    "Phanteks Halos Digital": "B07BGWLH14",
    "Tira LED Airgoo": "B07ZJ2CDKM",
    "Panel LED GVM": "B08FYB4SZ3",
    "Nanoleaf Shapes": "B08T6GRL9M",
    # Mesas
    "MR IRONSTONE L-Shaped": "B0874BZTTQ",
    "Bush Furniture Series C": "B000W8JO9S",
    # Accesorios
    "Hbada E1": "B0BZJYXG8K",
    "GTRACING B09": "B0CL7K2GQR",
    "RESPAWN 100": "B08DL21BJP",
    "Soporte VIVO Dual": "B07Q7D6Y6G",
    "Monitor Arm HUANUO": "B09C3N6KZF",
    "Base USB Amazon Basics": "B07JFC6L6K",
    "Cable Management Kit": "B08D3Y5P9F",
}

def amz(p):
    asin = ASINS.get(p)
    if asin:
        return f"\n[**Ver en Amazon ->**](https://www.amazon.es/dp/{asin}?tag={TAG})\n"
    q = p.lower().replace(" ", "+")
    return f"\n[**Ver en Amazon ->**](https://www.amazon.es/s?k={q}&tag={TAG})\n"

def product_section(n, name, price, specs, pros, cons):
    return f"""
{n}. {name}

- **Precio:** {price}
- **Especificaciones:** {specs}
- **Ventajas:** {pros}
- **Desventajas:** {cons}

{amz(name)}
"""

def frontmatter(title, slug, date, summary, cats, tags):
    tags_str = "\n".join(f'  - "{t}"' for t in tags)
    cats_str = "\n".join(f'  - "{c}"' for c in cats)
    return f"""---
title: "{title}"
date: {date}
# lastmod: {date}
draft: false
summary: "{summary}"
categories:
{cats_str}
tags:
{tags_str}
---

"""

def write_post(slug, title, date, summary, cats, tags, content):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fm = frontmatter(title, slug, date, summary, cats, tags)
    full = fm + content
    filepath = os.path.join(OUTPUT_DIR, f"{slug}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full)
    print(f"  OK {filepath}")


posts = []

# Helper to build post data
def add(title, slug_offset, summary, cats, tags, content_fn):
    posts.append({
        "title": title,
        "offset": slug_offset,
        "summary": summary,
        "cats": cats,
        "tags": tags,
        "content_fn": content_fn
    })

# ===================== POST DEFINITIONS =====================

add("Mejor Raton Gaming Inalambrico Barato (2026)", 0,
    "Los mejores ratones gaming inalambricos sin lag y sin gastar una fortuna. Analizamos calidad, sensor y bateria.",
    ["Perifericos"], ["raton gaming", "inalambrico", "barato"],
    lambda: product_section(1, "Logitech G305", "~45€", "12.000 DPI | 99g | 250h bateria", "Excelente bateria, sensor Hero, receptor USB", "No RGB") +
           product_section(2, "Razer Basilisk V3", "~55€", "26.000 DPI | 101g | Inalambrico", "Ergonomico, rueda inteligente, RGB", "Un poco mas caro") +
           product_section(3, "Corsair Harpoon RGB Wireless", "~40€", "10.000 DPI | 99g | Bluetooth+USB", "Doble conexion, buena ergonomia, barato", "Construccion plastica") +
           "\n## Veredicto\n\n**Mejor bateria:** Logitech G305.\n**Mas completo:** Razer Basilisk V3.\n**Mas economico:** Corsair Harpoon RGB Wireless.\n")

add("Mejor Teclado Gaming 60% Barato (2026)", 1,
    "Los teclados 60% ahorran espacio en tu mesa. Estos son los mejores modelos economicos para gaming.",
    ["Perifericos"], ["teclado 60%", "compacto", "gaming"],
    lambda: product_section(1, "Royal Kludge RK61", "~45€", "60% | Gateron intercambiables | Bluetooth", "Compacto, inalambrico, switches intercambiables", "Sin teclas de flecha") +
           product_section(2, "Redragon K530 Draconic", "~50€", "60% | Outemu | Bluetooth 5.0", "Inalambrico, 3 dispositivos, RGB", "Sin software") +
           product_section(3, "RK Royal Kludge RK84", "~65€", "75% | Gateron intercambiables | Triple conexion", "Formato 75% con teclas funcion, intercambiable", "Un poco mas caro") +
           "\n## Veredicto\n\n**Mejor calidad-precio:** Royal Kludge RK61.\n**Mejor inalambrico:** Redragon K530.\n**Mas completo:** RK Royal Kludge RK84.\n")

add("Mejor Microfono Gaming Barato (2026)", 2,
    "Habla claro sin gastar una fortuna. Los mejores microfonos gaming economicos para jugar y streamear.",
    ["Perifericos"], ["microfono", "gaming", "barato"],
    lambda: product_section(1, "FIFINE K669B", "~30€", "USB | Condensador | Plug-and-play", "Sonido calido, facil de usar, barato", "Capta ruido ambiente") +
           product_section(2, "Blue Snowball Ice", "~40€", "USB | Condensador | Multiple patron", "Calidad Blue, diseno iconico", "Sensible a ruido") +
           "\n## Veredicto\n\n**Mejor calidad-precio:** FIFINE K669B.\n**Mas versatil:** Blue Snowball Ice.\n")

add("Mejor Webcam Gaming Barata (2026)", 3,
    "Ensenate con calidad sin gastar de mas. Las mejores webcams gaming economicas para streaming y videollamadas.",
    ["Perifericos"], ["webcam", "gaming", "streaming"],
    lambda: product_section(1, "Logitech C270", "~25€", "720p | Enfoque fijo", "Barata, compacta, compatible con todo", "Solo 720p") +
           product_section(2, "Logitech C920", "~60€", "1080p | Enfoque automatico", "1080p, buena calidad imagen, gran angular", "Mas cara") +
           "\n## Veredicto\n\n**Mas economica:** Logitech C270.\n**Mejor calidad:** Logitech C920.\n")

add("Mejor Monitor 240Hz Barato (2026)", 4,
    "Fluidez maxima para gaming competitivo sin gastar un dineral. Los mejores monitores 240Hz economicos.",
    ["Monitores"], ["240Hz", "monitor gaming", "alta tasa"],
    lambda: product_section(1, "Samsung CRG5", "~250€", "24\" VA | 240Hz | 1500R curvo", "240Hz asequible, curvo inmersivo", "Colores mejorables") +
           "\n## Veredicto\n\n**Unico 240Hz economico:** Samsung CRG5.\n")

add("Mejor Monitor Ultra-wide Barato (2026)", 5,
    "La experiencia panoramica sin el precio premium. Los mejores monitores ultra-wide gaming economicos.",
    ["Monitores"], ["ultrawide", "monitor", "panoramico"],
    lambda: product_section(1, "LG 34WP60C", "~350€", "34\" VA | 160Hz | 21:9 UltraWide", "160Hz ultra-wide, buen contraste", "Panel VA") +
           "\n## Veredicto\n\n**Mejor ultra-wide economico:** LG 34WP60C.\n")

add("Mejor CPU Gaming Barata (2026)", 6,
    "Procesadores gaming con el mejor rendimiento por euro. Comparativa de CPUs economicas para jugar.",
    ["PCs"], ["CPU", "procesador", "gaming economico"],
    lambda: product_section(1, "AMD Ryzen 5 5600", "~120€", "6 nucleos / 12 hilos | 4.4GHz", "Excelente gaming, eficiente, buen precio", "Sin iGPU") +
           product_section(2, "Intel Core i5-12400F", "~110€", "6 nucleos / 12 hilos | 4.4GHz", "Gran rendimiento gaming, barato", "Sin iGPU, necesita GPU dedicada") +
           "\n## Veredicto\n\n**Mejor en general:** AMD Ryzen 5 5600.\n**Mejor valor Intel:** Intel Core i5-12400F.\n")

add("Mejor Placa Base Gaming Barata (2026)", 7,
    "La base de tu PC gaming sin arruinarte. Las mejores placas base economicas para Intel y AMD.",
    ["PCs"], ["placa base", "motherboard", "barata"],
    lambda: product_section(1, "B450M Motherboard", "~70€", "AM4 | DDR4 | PCIe 3.0", "Barata, solida, compatible Ryzen 5000", "Sin PCIe 4.0") +
           "\n## Veredicto\n\n**Mejor calidad-precio:** B450M para Ryzen.\n")

add("Mejor SSD para Gaming (2026)", 8,
    "Carga tus juegos en segundos. Los mejores SSD para gaming con relacion calidad-precio imbatible.",
    ["PCs"], ["SSD", "almacenamiento", "gaming"],
    lambda: product_section(1, "NVMe SSD 512GB", "~40€", "PCIe 3.0 | 3500MB/s lectura", "Rapidisimo, ideal para sistema y juegos", "No es PCIe 4.0") +
           product_section(2, "NVMe SSD 1TB", "~60€", "PCIe 3.0 | 3500MB/s lectura", "Mucho espacio, mismo rendimiento", "Un poco mas caro") +
           "\n## Veredicto\n\n**Mejor capacidad-precio:** 1TB NVMe.\n**Basico recomendado:** 512GB NVMe.\n")

add("Mejor RAM para Gaming (2026)", 9,
    "La memoria RAM adecuada marca la diferencia en juegos. Las mejores opciones para PC gaming economico.",
    ["PCs"], ["RAM", "memoria", "DDR4"],
    lambda: product_section(1, "16GB DDR4 3200MHz", "~35€", "2x8GB | DDR4 | 3200MHz", "Dual channel optimo para gaming", "No es DDR5") +
           product_section(2, "32GB DDR4 3200MHz", "~60€", "2x16GB | DDR4 | 3200MHz", "Mas capacidad para multitarea", "Sobra para gaming puro") +
           "\n## Veredicto\n\n**Recomendado:** 16GB DDR4 3200MHz.\n**Para multitarea:** 32GB DDR4.\n")

add("Mejor Fuente Alimentacion Gaming Barata (2026)", 10,
    "Una fuente de calidad protege tu inversion. Las mejores fuentes de alimentacion economicas para PC gaming.",
    ["PCs"], ["fuente alimentacion", "PSU", "barata"],
    lambda: product_section(1, "Fuente 550W 80+ Bronze", "~50€", "550W | 80+ Bronze | Semi-modular", "Suficiente para RX 6600, eficiente", "No es modular completa") +
           product_section(2, "Fuente 650W 80+ Bronze", "~60€", "650W | 80+ Bronze | Semi-modular", "Mas margen para futuras GPUs", "Un poco mas cara") +
           "\n## Veredicto\n\n**Basico recomendado:** 550W 80+ Bronze.\n**Para futuro:** 650W 80+ Bronze.\n")

add("Mejor Caja PC Gaming Barata (2026)", 11,
    "Tu PC merece una buena caja. Las mejores cajas gaming economicas con buena refrigeracion y diseno.",
    ["PCs"], ["caja PC", "chasis", "barata"],
    lambda: product_section(1, "Montech AIR 100", "~55€", "Micro-ATX | Mesh frontal | 4 ventiladores", "Excelente flujo de aire, incluye ventiladores", "Solo micro-ATX") +
           "\n## Veredicto\n\n**Mejor calidad-precio:** Montech AIR 100.\n")

add("Mejor Refrigeracion CPU Barata (2026)", 12,
    "Mantener tu CPU fresca es clave para el rendimiento. Los mejores coolers CPU sin gastar una fortuna.",
    ["PCs"], ["refrigeracion", "cooler CPU", "barato"],
    lambda: product_section(1, "Cooler Master Hyper 212", "~25€", "Torre simple | 120mm | 4 heatpipes", "Excelente para su precio, silencioso", "No para overclock extremo") +
           "\n## Veredicto\n\n**Clasico recomendado:** Cooler Master Hyper 212.\n")

add("Como Limpiar tu PC Gaming Paso a Paso (2026)", 13,
    "Guia completa para limpiar tu PC gaming. Mantenlo optimo sin gastar dinero en profesionales.",
    ["Guias"], ["limpieza PC", "mantenimiento", "guia"],
    lambda: """
## Por que es importante limpiar tu PC

El polvo actua como aislante termico. Un PC sucio funciona mas caliente, los ventiladores giran mas rapido y el rendimiento se resiente. Limpiarlo cada 3-6 meses alarga su vida util notablemente.

## Herramientas necesarias

| Herramienta | Para que sirve |
|------------|----------------|
| Aire comprimido | Soplar polvo de rincones |
| Pincel antiestatico | Desprender polvo sin danar |
| Panos de microfibra | Limpiar superficies |
| Alcohol isopropilico | Limpiar pasta termica vieja |

## Paso a paso

### 1. Preparacion
- Apaga el PC y desconecta todo
- Trabaja en una superficie antiestatica
- Descargate la electricidad estatica tocando metal

### 2. Limpieza de filtros
- Los filtros de polvo suelen estar en la parte frontal, inferior y superior
- Quitalos y lavalos con agua tibia (secalos bien antes de volver a ponerlos)

### 3. Limpieza interior
- Usa aire comprimido en posicion vertical para evitar liquidos
- Sujeta los ventiladores para que no giren al soplarlos
- Usa el pincel para zonas con polvo adherido
- Presta atencion a: disipador CPU, GPU, fuente de alimentacion

### 4. Limpieza de ventiladores
- Limpia las aspas con un pincel o bastoncillo de algodon
- No uses aspiradora directamente (genera electricidad estatica)

### 5. Limpieza de la caja
- Pasa un pano de microfibra por el interior y exterior
- No uses productos quimicos agresivos

### 6. Revision final
- Verifica que todos los cables esten conectados
- Asegurate de que no queden restos de polvo
- Cierra la caja y conecta todo

## Cada cuanto limpiar

| Frecuencia | Que hacer |
|-----------|-----------|
| Cada mes | Limpiar filtros rapidamente |
| Cada 3 meses | Limpieza general con aire comprimido |
| Cada 6-12 meses | Limpieza profunda, cambiar pasta termica |

## Veredicto

La limpieza regular es la forma mas barata de mantener tu PC rindiendo al maximo. 30 minutos cada 3 meses pueden alargar la vida de tu equipo anos.
""")

add("Mejores Juegos Multijugador Cooperativos Baratos (2026)", 14,
    "Juega con amigos sin gastar apenas dinero. Los mejores juegos cooperativos economicos para PC.",
    ["Juegos"], ["cooperativo", "multijugador", "baratos"],
    lambda: """
## Comparativa

| Juego | Precio | Jugadores | Genero |
|-------|--------|-----------|--------|
| It Takes Two | ~20€ | 2 | Aventura cooperativa |
| Portal 2 | ~2€ (oferta) | 2 | Puzzles cooperativo |
| Overcooked 2 | ~5€ (oferta) | 1-4 | Cocina caotica |
| Don't Starve Together | ~5€ | 2-4 | Supervivencia |

## 1. It Takes Two

- **Precio:** ~20€ | **Jugadores:** 2
- **Ventajas:** Mejor juego cooperativo jamas creado, variado, divertidisimo

El juego cooperativo por excelencia. Cada nivel tiene mecanicas unicas y la historia es emotiva sin ser empalagosa.

## 2. Portal 2

- **Precio:** ~2€ en oferta | **Jugadores:** 2
- **Ventajas:** Puzzles geniales, cooperativo perfecto, humor

Por 2€ en oferta es el chollo del siglo. El modo cooperativo es una obra maestra de diseno.

## 3. Overcooked 2

- **Precio:** ~5€ en oferta | **Jugadores:** 1-4
- **Ventajas:** Caos divertidisimo, ideal para noches de juego

Prep Arate para gritar, reir y echarle la culpa a tus amigos mientras cocinas en cocinas imposibles.

## Veredicto

**Mejor cooperativo:** It Takes Two.
**Mas economico:** Portal 2 (en oferta).
**Mas divertido en grupo:** Overcooked 2.
""")

add("Mejores Juegos de Terror Baratos PC (2026)", 15,
    "Los mejores juegos de terror que no te dejaran dormir por menos de 20€. Analisis y recomendaciones.",
    ["Juegos"], ["terror", "juegos baratos", "PC"],
    lambda: """
## Comparativa

| Juego | Precio | Duracion | Miedo |
|-------|--------|----------|-------|
| Phasmophobia | ~10€ | 100h+ | Alto |
| Outlast | ~3€ (oferta) | 8h | Muy alto |
| Amnesia: Rebirth | ~5€ (oferta) | 10h | Alto |
| Lethal Company | ~10€ | 50h+ | Comedia-terror |

## 1. Phasmophobia

- **Precio:** ~10€ | **Duracion:** 100h+
- **Ventajas:** Cooperativo, rejugable, actualizaciones constantes

Caza fantasmas con tus amigos. El microfono es tu herramienta principal. Cada partida es unica.

## 2. Outlast

- **Precio:** ~3€ en oferta | **Duracion:** 8h
- **Ventajas:** Terror puro, sin armas, atmosfera agobiante

Solo tienes una camara y tus piernas para escapar. Uno de los juegos mas aterradores jamas creados.

## 3. Amnesia: Rebirth

- **Precio:** ~5€ en oferta | **Duracion:** 10h
- **Ventajas:** Narrativa profunda, terror psicologico, ambientacion

El regreso del clasico del terror. La oscuridad es tu enemiga.

## Veredicto

**Mas terror:** Outlast.
**Mejor cooperativo:** Phasmophobia.
**Mejor narrativa:** Amnesia: Rebirth.
""")

add("Mejores Juegos RPG Baratos PC (2026)", 16,
    "Mundos enormes e historias profundas por menos de 15€. Los mejores RPG economicos para PC.",
    ["Juegos"], ["RPG", "juegos baratos", "PC"],
    lambda: """
## Comparativa

| Juego | Precio | Duracion | Estilo |
|-------|--------|----------|--------|
| Stardew Valley | ~8€ | 100h+ | RPG simulacion |
| Hollow Knight | ~7.50€ (oferta) | 40h+ | Metroidvania |
| Undertale | ~7€ | 10h | RPG narrativo |
| Darkest Dungeon | ~5€ (oferta) | 80h+ | Roguelike RPG |

## 1. Stardew Valley

- **Precio:** ~8€ | **Duracion:** 100h+
- **Ventajas:** Relajante, profundo, multijugador

El RPG de simulacion definitivo. Cultiva, explora minas, cria animales y enamorate.

## 2. Hollow Knight

- **Precio:** ~7.50€ en oferta | **Duracion:** 40h+
- **Ventajas:** Mundo enorme, combate preciso, arte precioso

Un metroidvania que compite con los mejores del genero. Por menos de 10€ es una locura.

## 3. Undertale

- **Precio:** ~7€ | **Duracion:** 10h
- **Ventajas:** Historia unica, personajes memorables, banda sonora increible

No dejes que los graficos te enganen. Es uno de los RPG mas innovadores jamas creados.

## Veredicto

**Mejor relacion calidad-precio:** Stardew Valley.
**Mejor accion:** Hollow Knight.
**Mejor historia:** Undertale.
""")

add("Mejores Juegos Indie Baratos en Steam (2026)", 17,
    "El mejor indie que puedes comprar por menos de 10€ en Steam. Joyas ocultas que no te puedes perder.",
    ["Juegos"], ["indie", "Steam", "juegos baratos"],
    lambda: """
## Seleccion Indispensable

| Juego | Precio | Genero | Por que lo recomendamos |
|-------|--------|--------|------------------------|
| Celeste | ~5€ (oferta) | Plataformas | Preciso, emotivo, banda sonora increible |
| Hades | ~10€ (oferta) | Roguelike | Accion frenetica, narrativa genial |
| Dead Cells | ~7.50€ (oferta) | Roguelite | Combate fluido, rejugable infinito |
| Slay the Spire | ~6€ (oferta) | Roguelike cartas | Adictivo, estrategico, horas de diversion |

## 1. Celeste

- **Precio:** ~5€ en oferta | **Duracion:** 15h+
- **Ventajas:** Controles precisos, historia emotiva, desafio perfecto

Plataformas en su maxima expresion. Cada muerte es una leccion, cada nivel una conquista.

## 2. Hades

- **Precio:** ~10€ en oferta | **Duracion:** 50h+
- **Ventajas:** Accion adictiva, personajes carismaticos, rejugabilidad infinita

Sal del Infierno una y otra vez. El mejor roguelike de accion jamas creado.

## 3. Dead Cells

- **Precio:** ~7.50€ en oferta | **Duracion:** 100h+
- **Ventajas:** Combate fluido, progresion gratificante, muchas armas

Castlevania se encuentra con roguelite. Perfecto para sesiones cortas o maratones.

## Veredicto

**Mejor plataformas:** Celeste.
**Mejor accion:** Hades.
**Mas adictivo:** Slay the Spire.
""")

add("Mejores Juegos de Estrategia Baratos PC (2026)", 18,
    "Los mejores juegos de estrategia que agudizaran tu mente sin vaciar tu cartera.",
    ["Juegos"], ["estrategia", "juegos baratos", "PC"],
    lambda: """
## Comparativa

| Juego | Precio | Duracion | Tipo |
|-------|--------|----------|------|
| XCOM 2 | ~5€ (oferta) | 60h+ | Tactica por turnos |
| Age of Empires II DE | ~5€ (oferta) | 200h+ | Estrategia en tiempo real |
| Civilization VI | ~7€ (oferta) | 100h+ | 4X por turnos |
| Into the Breach | ~5€ (oferta) | 30h+ | Tactica puzzle |

## 1. XCOM 2

- **Precio:** ~5€ en oferta | **Duracion:** 60h+
- **Ventajas:** Tactico, personalizable, tension constante

Gestiona la resistencia contra alienigenas. Cada decision importa, cada soldado tiene nombre.

## 2. Age of Empires II DE

- **Precio:** ~5€ en oferta | **Duracion:** 200h+
- **Ventajas:** Clasico eterno, campañas historicas, multijugador activo

20 anos despues sigue siendo el rey de la estrategia en tiempo real.

## 3. Civilization VI

- **Precio:** ~7€ en oferta | **Duracion:** 100h+
- **Ventajas:** Profundidad inmensa, "solo una mas", muchas civilizaciones

Construye un imperio desde la antigueedad hasta la era espacial. La definicion de "un turno mas".

## Veredicto

**Mejor tactico:** XCOM 2.
**Clasico imprescindible:** Age of Empires II DE.
**Adiccion garantizada:** Civilization VI.
""")

add("Mejores Juegos de Carreras Baratos PC (2026)", 19,
    "Velocidad sin precio premium. Los mejores juegos de carreras economicos para PC.",
    ["Juegos"], ["carreras", "racing", "PC"],
    lambda: """
## Comparativa

| Juego | Precio | Estilo | Volante |
|-------|--------|--------|---------|
| Trackmania Nations | Gratis | Arcade | No necesario |
| Forza Horizon 4 | ~10€ (oferta) | Open world arcade | Recomendado |
| Assetto Corsa | ~5€ (oferta) | Simulacion | Necesario |

## 1. Trackmania Nations

- **Precio:** Gratis
- **Ventajas:** Competitivo, editor de circuitos, comunidad activa

Gratis, divertido y con una comunidad enorme. Los mejores juegos de carreras no tienen por que costar dinero.

## 2. Forza Horizon 4

- **Precio:** ~10€ en oferta
- **Ventajas:** Mundo abierto, graficos impresionantes, muchos coches

El mejor juego de carreras arcade de la ultima decada. Conducir por la campina inglesa es una terapia.

## 3. Assetto Corsa

- **Precio:** ~5€ en oferta
- **Ventajas:** Fisica realista, mods infinitos, ideal para simracers

El simulador de referencia. Con mods se convierte en el juego de carreras mas completo.

## Veredicto

**Gratis imprescindible:** Trackmania Nations.
**Mejor arcade:** Forza Horizon 4.
**Mejor simulacion:** Assetto Corsa.
""")

add("Mejores Juegos de Lucha Baratos PC (2026)", 20,
    "Pelea sin pegarte en el bolsillo. Los mejores juegos de lucha economicos para PC.",
    ["Juegos"], ["lucha", "fighting", "baratos"],
    lambda: """
## Comparativa

| Juego | Precio | Estilo | Online |
|-------|--------|--------|--------|
| Street Fighter V | ~7€ (oferta) | 2D clasico | Activo |
| Guilty Gear Strive | ~15€ (oferta) | 2.5D anime | Bueno |
| Brawlhalla | Gratis | Plataformas | Muy activo |

## 1. Street Fighter V

- **Precio:** ~7€ en oferta | **Online:** Activo
- **Ventajas:** Gran tutorial, roster variado, comunidad grande

La puerta de entrada perfecta al mundo de la lucha. Facil de aprender, dificil de dominar.

## 2. Brawlhalla

- **Precio:** Gratis
- **Ventajas:** Cross-play, muchos personajes, competitivo

Smash Bros gratis en PC. Ideal para jugar con amigos sin pagar nada.

## Veredicto

**Mejor para empezar:** Street Fighter V.
**Gratis recomendado:** Brawlhalla.
""")

add("Mejor Soporte Monitor Ajustable (2026)", 21,
    "Mejora tu postura y libera espacio en tu mesa. Los mejores soportes de monitor ajustables y baratos.",
    ["Accesorios"], ["soporte monitor", "brazo", "ergonomia"],
    lambda: product_section(1, "Monitor Arm HUANUO", "~25€", "Brazo unico | 17-32\" | 8kg max", "Barato, ajustable, libera espacio", "No para monitores ultrapesados") +
           product_section(2, "Soporte VIVO Dual", "~35€", "Dos monitores | 13-27\" cada uno", "Dual monitor, robusto, ajustable", "Requiere mesa gruesa") +
           "\n## Veredicto\n\n**Mejor basico:** Monitor Arm HUANUO.\n**Mejor dual:** Soporte VIVO Dual.\n")

add("Mejor Organizador Cables Gaming (2026)", 22,
    "Adios al caos de cables. Los mejores organizadores y gestion de cables para tu setup gaming.",
    ["Accesorios"], ["organizador cables", "gestion", "setup"],
    lambda: product_section(1, "Cable Management Kit", "~15€", "Bridas, clips, canaletas adhesivas", "Todo incluido, facil de instalar, barato", "No es solucion permanente") +
           "\n## Veredicto\n\n**Mas completo:** Cable Management Kit.\n")

add("Mejor Iluminacion Habitacion Gaming (2026)", 23,
    "Transforma tu habitacion con la iluminacion adecuada. Las mejores opciones RGB para tu setup gaming.",
    ["Accesorios"], ["iluminacion", "RGB", "habitacion gaming"],
    lambda: product_section(1, "Tira LED Govee RGBIC", "~25€", "6.5ft | App | Sincronizacion musical", "Multiples colores, app, musica", "Requiere app") +
           product_section(2, "Nanoleaf Shapes", "~50€", "Paneles triangulares | App | Ritmo", "Diseno unico, efectos personalizables", "Mas caro") +
           product_section(3, "Tira LED Airgoo", "~12€", "10ft | Mando a distancia", "Barata, facil instalacion", "Un solo color cada vez") +
           "\n## Veredicto\n\n**Mejor efecto:** Govee RGBIC.\n**Mas original:** Nanoleaf Shapes.\n**Mas economica:** Airgoo.\n")

add("Como Configurar Doble Monitor para Gaming (2026)", 24,
    "Guia paso a paso para configurar dos monitores en tu PC gaming. Mejora tu productividad y experiencia.",
    ["Guias"], ["doble monitor", "configurar", "guia"],
    lambda: """
## Por que usar dos monitores

Un monitor para el juego, otro para Discord, Spotify, guias o streams. La multitarea nunca fue tan comoda.

## Que necesitas

| Componente | Requisito |
|-----------|-----------|
| GPU | 2 puertos de video libres (HDMI, DP, DVI) |
| Monitores | Cualquier combinacion funciona |
| Cables | Los que coincidan con tus puertos |

## Paso a paso

### 1. Conexion fisica
- Conecta ambos monitores a la GPU (no a la placa base)
- Usa la entrada recomendada: DisplayPort para gaming, HDMI para secundario

### 2. Configuracion en Windows
- Click derecho en Escritorio > Configuracion de pantalla
- Windows detectara ambos monitores automaticamente
- Arrastra los monitores para que coincidan con tu disposicion fisica
- Selecciona "Extender estas pantallas"

### 3. Ajustes importantes
- Monitor principal: el de gaming (marcar "Usar como pantalla principal")
- Tasa de refresco: Configura cada monitor a su maximo nativo
- Resolucion: Nativa en ambos

### 4. Para gaming
- Juega en el monitor principal (el de alta tasa)
- Usa el secundario para Discord, navegador, Spotify
- En juegos: selecciona "Pantalla completa" y elige el monitor correcto

### 5. Atajos utiles
- Win + P: Cambia entre modos de pantalla
- Win + Shift + Flecha: Mueve ventanas entre monitores
- Win + Flecha: Ajusta ventanas en el monitor actual

## Solucion de problemas

| Problema | Solucion |
|----------|----------|
| Un monitor no se detecta | Revisa cables, prueba otro puerto |
| Tasa de refresco baja | Configura manualmente en pantalla > Configuracion de pantalla avanzada |
| Raton no pasa al otro monitor | Asegurate que los monitores esten alineados en configuracion |

## Veredicto

Dos monitores cambian tu forma de usar el PC. Para gaming, productividad y multitarea, es la mejora mas practica que puedes hacer.
""")

add("Como Mejorar tu Conexion para Jugar Online (2026)", 25,
    "Di adios al lag. Guia para optimizar tu conexion de internet y jugar online sin problemas.",
    ["Guias"], ["conexion", "lag", "optimizar"],
    lambda: """
## El lag no es inevitable

Antes de culpar a tu operador, revisa estos puntos. La mayoria del lag se soluciona en casa y sin gastar dinero.

## 1. Cable ethernet vs WiFi

| Conexion | Latencia | Estabilidad |
|----------|----------|-------------|
| Ethernet | 1-2ms | Maxima |
| WiFi 5GHz | 2-5ms | Buena |
| WiFi 2.4GHz | 5-15ms | Variable |

**Conclusion:** El cable siempre gana. Si puedes, conecta por ethernet.

## 2. Configuracion del router

- **Activa QoS:** Prioriza el trafico de juego sobre descargas y streaming
- **Puertos abiertos:** Abre los puertos de tus juegos (UPnP suele bastar)
- **DNS:** Usa Google DNS (8.8.8.8) o Cloudflare (1.1.1.1) para mejor resolucion

## 3. Cerrar programas en segundo plano

| Programa | Impacto |
|----------|---------|
| Torrents | Alto (saturan subida) |
| Streaming (Netflix, YouTube) | Medio |
| Descargas Steam/Epic | Alto |
| Actualizaciones Windows | Muy alto |

Cierra todo lo que no necesites mientras juegas.

## 4. Mejoras de hardware

- **Router WiFi 6:** Si tu router es muy viejo, uno de 60€ puede marcar diferencia
- **Powerline:** Si no puedes usar cable, los adaptadores Powerline son buena alternativa
- **Tarjeta de red:** Para PC de sobremesa, una tarjeta PCIe ethernet mejora la conexion

## 5. Configuracion especifica por juego

- **Valorant:** Modo ejecucion sin bordes, vsync off
- **Fortnite:** NVIDIA Reflex (si tienes GPU compatible)
- **Apex Legends:** Limitar FPS a tu tasa de refresco para evitar fluctuaciones

## Veredicto

El cable ethernet soluciona el 80% de los problemas de lag. Si no puedes usar cable, un router WiFi 6 de 60€ es tu mejor inversion.
""")

add("Mejor Silla Gaming Ergonómica por menos de 150€ (2026)", 26,
    "Tu espalda te lo agradecera. Las mejores sillas gaming ergonomicas que no cuestan un ojo de la cara.",
    ["Accesorios"], ["silla gaming", "ergonomica", "barata"],
    lambda: product_section(1, "Hbada E1", "~150€", "Malla transpirable | Soporte lumbar ajustable", "Transpirable, soporte lumbar excelente, reposabrazos 3D", "No es la mas acolchada") +
           product_section(2, "RESPAWN 100", "~160€", "Tela transpirable | Reposabrazos ajustables", "Transpirable, buena construccion, asiento comodo", "Colores limitados") +
           "\n## Veredicto\n\n**Mejor ergonomia:** Hbada E1.\n**Mas comoda:** RESPAWN 100.\n")

add("Mejor Base para Portatil Gaming (2026)", 27,
    "Refrigera tu portatil y juega mas tiempo. Los mejores soportes con ventilador para portatiles gaming.",
    ["Accesorios"], ["base portatil", "refrigeracion", "gaming"],
    lambda: product_section(1, "Base con ventiladores 4x120mm", "~25€", "4 ventiladores | USB | Ajuste altura", "Buen flujo de aire, ajustable, barata", "Ruido moderado") +
           "\n## Veredicto\n\n**Mejor calidad-precio:** Base 4 ventiladores 120mm.\n")

add("Mejor Teclado Mecánico Inalámbrico Barato (2026)", 28,
    "Libertad sin cables ni compromisos. Los mejores teclados mecanicos inalambricos economicos.",
    ["Perifericos"], ["teclado mecanico", "inalambrico", "gaming"],
    lambda: product_section(1, "Royal Kludge RK61", "~55€", "60% | Gateron | Bluetooth 5.0 | USB-C", "Compacto, inalambrico, intercambiable en caliente", "Sin teclas de flecha") +
           product_section(2, "Redragon K530 Draconic", "~50€", "60% | Outemu | Bluetooth 5.0 | RGB", "Barato, buena bateria, RGB", "Sin software") +
           "\n## Veredicto\n\n**Mejor en general:** Royal Kludge RK61.\n**Mas economico:** Redragon K530.\n")

add("Mejor Ratón Ergonómico Gaming Barato (2026)", 29,
    "Juega sin dolor. Los mejores ratones ergonomicos para gaming que cuidan tu mano sin arruinarte.",
    ["Perifericos"], ["raton ergonomico", "gaming", "barato"],
    lambda: product_section(1, "Razer DeathAdder Essential", "~30€", "6.400 DPI | 96g | Forma ergonomica", "Forma iconica, ideal manos grandes, barato", "Sin RGB, DPI bajo") +
           product_section(2, "Logitech G203 Lightsync", "~35€", "8.000 DPI | 85g | RGB", "Comodo para todo tipo de agarre, RGB", "No es ergonomico extremo") +
           "\n## Veredicto\n\n**Mejor ergonomia:** Razer DeathAdder Essential.\n**Mas versatil:** Logitech G203.\n")

add("Mejor Hub USB para Gaming (2026)", 30,
    "Conecta todos tus perifericos sin problemas. Los mejores hubs USB para tu setup gaming.",
    ["Accesorios"], ["hub USB", "conectividad", "perifericos"],
    lambda: product_section(1, "Base USB Amazon Basics", "~15€", "4 puertos USB 3.0 | Cable 1m", "Barato, confiable, USB 3.0", "Sin carga rapida") +
           "\n## Veredicto\n\n**Mas recomendado:** Base USB Amazon Basics 4 puertos.\n")

add("Mejor Consola Gaming Barata (2026)", 31,
    "Consolas economicas para jugar sin gastar una fortuna. Comparamos Xbox, PlayStation y alternativas.",
    ["Guias"], ["consola", "barata", "gaming"],
    lambda: """
## Opciones de Consolas Economicas

| Consola | Precio | 4K | Exclusivos |
|---------|--------|-----|------------|
| Xbox Series S | ~200€ | No | Game Pass |
| PlayStation 4 Slim | ~150€ usado | No | Muchos exclusivos |
| Nintendo Switch Lite | ~150€ usado | No | Portatil |

## 1. Xbox Series S

- **Precio:** ~200€ (nueva)
- **Ventajas:** Game Pass, rapida, pequena, 1440p
- **Desventajas:** Sin lector discos, 512GB

La consola mas inteligente para presupuestos ajustados. Con Game Pass tienes cientos de juegos por 10€/mes.

## 2. PlayStation 4 Slim

- **Precio:** ~150€ (usada)
- **Ventajas:** Biblioteca enorme, exclusivos God of War, TLOU, Spider-Man
- **Desventajas:** Tecnologia de generacion pasada, ruidosa

La mejor consola de segunda mano. Por 150€ tienes acceso a los mejores juegos de la ultima decada.

## 3. Nintendo Switch Lite

- **Precio:** ~150€ (usada)
- **Ventajas:** Portatil, exclusivos Nintendo, juegos en fisico baratos
- **Desventajas:** No conecta a TV, Joycons fijos

Perfecta para viajes, jugar en la cama o para los mas pequenos.

## Veredicto

**Mejor nueva:** Xbox Series S + Game Pass.
**Mejor usada:** PlayStation 4 Slim.
**Mejor portatil:** Nintendo Switch Lite.
""")

add("Mejor TV para Gaming Barata (2026)", 32,
    "Juega en pantalla grande sin gastar un dineral. Las mejores televisiones economicas para consolas y PC.",
    ["Accesorios"], ["TV", "gaming", "barata"],
    lambda: """
## Que buscar en una TV para gaming

| Caracteristica | Minimo | Recomendado |
|---------------|--------|-------------|
| Resolucion | 1080p | 4K |
| Tasa de refresco | 60Hz | 120Hz |
| HDMI | 2.0 | 2.1 |
| Input lag | <20ms | <10ms |

## Opciones recomendadas

### Opcion 1: TV 4K 60Hz (~300€)
Perfecta para Xbox Series S, PS4 o PC gaming casual. El 4K se ve genial y el input lag es aceptable.

### Opcion 2: TV 1080p 60Hz (~150€)
Ideal para habitaciones secundarias o consolas mas antiguas. Barata y funcional.

## Consejos

- Activa el Modo Juego en la TV para minimizar el lag
- Usa HDMI 2.0 minimo para 4K a 60Hz
- Para PC, asegurate de que la TV acepte la resolucion nativa

## Veredicto

Una TV 4K de ~300€ es el punto dulce. Activa el modo juego y disfruta.
""")

add("Como Hacer Streaming desde tu PC Gaming (2026)", 33,
    "Empieza a streamear sin equipamiento caro. Guia completa para hacer streaming en Twitch o YouTube.",
    ["Guias"], ["streaming", "Twitch", "guia"],
    lambda: """
## Que necesitas para empezar

| Requisito | Minimo | Recomendado |
|-----------|--------|-------------|
| PC | Ryzen 5 + 16GB RAM | Ryzen 7 + RTX 3060 |
| Internet | 10Mbps subida | 25Mbps+ subida |
| Microfono | Cualquiera | FIFINE K669B (~30€) |
| Software | OBS Studio (gratis) | OBS Studio |

## Paso 1: Instalar OBS Studio

Descarga OBS Studio (gratis, open source). Es el estandar del streaming.

## Paso 2: Configurar OBS

1. **Escena:** Crea una escena para tu juego
2. **Fuentes:** Anade "Captura de juego" y "Dispositivo de captura de audio"
3. **Audio:** Configura microfono y audio del escritorio

## Paso 3: Ajustes de streaming

| Ajuste | Valor recomendado |
|--------|------------------|
| Resolucion de salida | 1280x720 (720p) |
| FPS | 30 o 60 |
| Bitrate | 3500-6000 kbps |
| Codificador | NVIDIA NVENC (si tienes) o x264 |

## Paso 4: Optimizacion

- **NVENC:** Si tienes GPU NVIDIA, usa NVENC para minimizar impacto en FPS
- **Baja resolucion:** 720p es suficiente para empezar, mejor que 1080p entrecortado
- **Prueba antes:** Haz una grabacion de prueba para verificar audio y video

## Equipo basico recomendado (menos de 100€)

| Componente | Producto | Precio |
|-----------|----------|--------|
| Microfono | FIFINE K669B | ~30€ |
| Webcam | Logitech C270 | ~25€ |
| Iluminacion | Panel LED GVM | ~40€ |

## Veredicto

Con OBS Studio (gratis), un microfono de 30€ y buena luz, puedes empezar a streamear hoy mismo.
""")

add("Como Mejorar el Audio en tu PC Gaming (2026)", 34,
    "Guia para optimizar el sonido de tu PC gaming sin gastar dinero. Mejora la experiencia de juego.",
    ["Guias"], ["audio", "sonido", "optimizar"],
    lambda: """
## El audio importa mas de lo que crees

Escuchar pasos, direccion de disparos y ambiente marca la diferencia entre ganar y perder.

## 1. Configuracion basica de audio

### Windows
- Click derecho en altavoz > Sonido
- Selecciona tu dispositivo > Propiedades
- Mejoras: Desactiva "Compensacion de sonoridad"
- Formato: 24 bits, 48000 Hz

### En juegos
- Activa audio espacial (Windows Sonic es gratis)
- En juegos competitivos: usa modo "Auriculares" o "Headphones"
- Desactiva efectos de sonido innecesarios

## 2. Software gratuito

Peace Equalizer + APO Equalizer: Ecualizador sistema gratuito para Windows.
Usalo para:
- Realzar pasos en FPS (subir frecuencias 2-4kHz)
- Reducir ruidos molestos
- Personalizar sonido a tu gusto

## 3. Mejoras de hardware baratas

| Producto | Precio | Beneficio |
|----------|--------|-----------|
| DAC USB basico | ~15€ | Elimina ruido electrico |
| Almohadillas nuevas | ~10€ | Mejora comodidad y aislamiento |
| Cable alargador | ~5€ | Libertad de movimiento |

## Configuracion para juegos populares

### Valorant / CS2
- Audio espacial: Off (mejor con HRTF del juego)
- Ecualizacion: Realzar 2000Hz para pasos

### Fortnite
- Audio 3D: Activado
- Volumen efectos: 100%

## Veredicto

Antes de comprar auriculares nuevos, prueba a ecualizar. Peace Equalizer es gratis y puede transformar tu audio.
""")

add("Mejor Ratón Gaming para Manos Pequenas (2026)", 35,
    "No todos los ratones valen para todas las manos. Los mejores ratones gaming para manos pequenas y economicos.",
    ["Perifericos"], ["raton manos pequenas", "gaming", "barato"],
    lambda: product_section(1, "Razer Viper Mini", "~30€", "8.500 DPI | 61g | Simetrico", "Ultraligero, tamano compacto, excelente sensor", "Sin botones laterales derecho") +
           product_section(2, "SteelSeries Rival 3", "~40€", "8.500 DPI | 77g | Simetrico", "Ligero, buen sensor, RGB", "Cable basico") +
           "\n## Veredicto\n\n**Mejor para manos pequenas:** Razer Viper Mini.\n**Alternativa solida:** SteelSeries Rival 3.\n")

add("Mejores Altavoces Gaming Baratos (2026)", 36,
    "Sonido envolvente sin cascos. Los mejores altavoces gaming economicos para tu setup.",
    ["Perifericos"], ["altavoces", "sonido", "baratos"],
    lambda: product_section(1, "Logitech Z200", "~25€", "2.0 | 10W | Jack 3.5mm", "Baratos, sonido decente, volumen suficiente", "Sin subwoofer") +
           "\n## Veredicto\n\n**Mejor calidad-precio:** Logitech Z200.\n")

add("Como Crear un Servidor de Minecraft Barato (2026)", 37,
    "Monta tu propio servidor de Minecraft sin pagar hosting. Guia paso a paso gratuita.",
    ["Guias"], ["Minecraft", "servidor", "guia"],
    lambda: """
## Opciones para tu servidor

| Opcion | Precio | Dificultad | Para quien |
|--------|--------|------------|------------|
| Tu propio PC | Gratis | Media | 2-5 jugadores |
| Hosting gratuito (Aternos) | Gratis | Facil | 2-10 jugadores |
| VPS economico | ~5€/mes | Alta | 10+ jugadores |

## Opcion 1: Servidor en tu PC (Gratis)

### Requisitos minimos
- 4GB RAM disponibles
- Conexion con buena subida (10Mbps+)
- Java 17+ instalado

### Pasos
1. Descarga el archivo server.jar de minecraft.net
2. Crea una carpeta para el servidor
3. Ejecuta: `java -Xmx2G -Xms1G -jar server.jar nogui`
4. Acepta el EULA en eula.txt
5. Re-ejecuta el comando

### Configurar conexion
- Abre el puerto 25565 en tu router
- Comparte tu IP publica con los amigos
- Usa No-IP si tu IP cambia

## Opcion 2: Aternos (Gratis)

- Web: aternos.org
- Ventajas: No necesitas tener el PC encendido
- Desventajas: Cola de espera, limitado

## Plugins recomendados (gratis)

| Plugin | Funcion |
|--------|---------|
| EssentialsX | Comandos basicos (home, tpa, warp) |
| LuckPerms | Permisos y rangos |
| CoreProtect | Proteccion contra griefing |

## Veredicto

Para 2-5 amigos, el servidor en tu propio PC es la mejor opcion y es totalmente gratis.
""")

add("Mejores Juegos de Supervivencia Baratos PC (2026)", 38,
    "Los mejores juegos de supervivencia que pondran a prueba tu ingenio sin vaciar tu cartera.",
    ["Juegos"], ["supervivencia", "juegos baratos", "PC"],
    lambda: """
## Los mejores juegos de supervivencia economicos

| Juego | Precio | Jugadores | Duracion |
|-------|--------|-----------|----------|
| Valheim | ~20€ | 1-10 | 100h+ |
| Don't Starve Together | ~5€ | 2-4 | 100h+ |
| The Forest | ~5€ (oferta) | 1-4 | 40h+ |
| Project Zomboid | ~10€ | 1-4 | 200h+ |

## 1. Valheim

- **Precio:** ~20€ | **Jugadores:** 1-10
- **Ventajas:** Mundo enorme, construccion, exploracion, bosses epicos

Supervivencia vikinga en su maxima expresion. Uno de los mejores juegos de la decada.

## 2. Don't Starve Together

- **Precio:** ~5€ | **Jugadores:** 2-4
- **Ventajas:** Estilo unico, dificil pero justo, recibe un personaje extra

Compralo una vez y ten siempre una copia para regalar a un amigo.

## 3. The Forest

- **Precio:** ~5€ en oferta | **Jugadores:** 1-4
- **Ventajas:** Terror + supervivencia, construccion, historia misteriosa

Sobrevive en una isla llena de canibales mientras buscas a tu hijo.

## Veredicto

**Mejor en general:** Valheim.
**Mas economico:** Don't Starve Together.
**Mejor historia:** The Forest.
""")

add("Mejores Juegos para Jugar en Familia (2026)", 39,
    "Juegos para todas las edades. Los mejores titulos para disfrutar en familia sin gastar mucho.",
    ["Juegos"], ["familia", "multijugador", "PC"],
    lambda: """
## Los mejores juegos para jugar en familia

| Juego | Precio | Edad | Jugadores |
|-------|--------|------|-----------|
| Overcooked 2 | ~5€ (oferta) | 7+ | 1-4 |
| Minecraft | ~20€ | 7+ | 1-10 |
| Rocket League | Gratis | 7+ | 1-8 |
| Fall Guys | Gratis | 7+ | 60 |

## 1. Overcooked 2

- **Precio:** ~5€ en oferta | **Jugadores:** 1-4
- **Ventajas:** Cooperativo, divertido, facil de aprender

Cocina en familia mientras el caos reina. Risas aseguradas.

## 2. Minecraft

- **Precio:** ~20€ | **Jugadores:** 1-10
- **Ventajas:** Creatividad sin limites, educativo, modos de juego

El juego que trasciende generaciones. Perfecto para jugar padres e hijos.

## 3. Rocket League

- **Precio:** Gratis | **Jugadores:** 1-8
- **Ventajas:** Futbol con coches, facil, gratis

Todos entienden el concepto. Ideal para partidas rapidas en familia.

## Veredicto

**Mejor cooperativo:** Overcooked 2.
**Mas creativo:** Minecraft.
**Gratis imprescindible:** Rocket League.
""")

add("Guia de Overclocking para Principiantes (2026)", 40,
    "Aumenta el rendimiento de tu PC sin gastar dinero. Introduccion al overclocking seguro para novatos.",
    ["Guias"], ["overclocking", "rendimiento", "guia"],
    lambda: """
## El overclocking explicado simple

El overclocking es hacer que tu CPU o GPU funcione a mayor velocidad de la que viene de fabrica. Es como ponerle turbo a tu PC.

## Lo que necesitas saber antes de empezar

- **Calor:** Mas velocidad = mas calor. Necesitas buena refrigeracion
- **Estabilidad:** No todos los chips aguantan lo mismo. Prueba y error
- **Garantia:** El overclocking puede anular la garantia del fabricante

## Overclocking de GPU (mas facil y seguro)

### Paso 1: Descarga MSI Afterburner (gratis)
Es la herramienta estandar para overclocking de GPU.

### Paso 2: Aumenta el Power Limit
- Desliza "Power Limit" al maximo (normalmente 110-120%)
- Esto permite que la GPU consuma mas energia cuando la necesite

### Paso 3: Aumenta Core Clock
- Sube de 25 en 25 MHz
- Prueba con un benchmark o juego cada vez
- Si ves artefactos o el juego crashea, baja 25 MHz
- La mayoria de GPUs aguantan +100 a +200 MHz estables

### Paso 4: Aumenta Memory Clock
- Igual que Core Clock, de 50 en 50 MHz
- Los juegos se benefician menos que del Core Clock

### Paso 5: Prueba de estabilidad
- Usa Unigine Heaven o Superposition (gratis)
- Si crashea o da errores, baja las frecuencias

## Overclocking de CPU (mas delicado)

- **Entra en la BIOS** (reinicia y pulsa Supr o F2)
- **Aumenta el multiplicador:** Subelo de 1 en 1
- **Voltaje:** No toques el voltaje si no sabes lo que haces
- **Prueba:** Usa Cinebench (gratis) y monitoriza temperaturas

## Temperaturas maximas seguras

| Componente | Maximo seguro |
|-----------|---------------|
| GPU | 85°C |
| CPU | 90°C |
| VRAM | 95°C |

Si ves estas temperaturas, para y baja el overclock.

## Veredicto

El overclocking de GPU con MSI Afterburner es seguro y te dara entre 5-15% mas rendimiento gratis. Empieza por ahi.
""")

add("Mejor Teclado Gaming de Membrana Barato (2026)", 41,
    "No necesitas un mecanico para jugar bien. Los mejores teclados de membrana gaming economicos y silenciosos.",
    ["Perifericos"], ["teclado membrana", "silencioso", "barato"],
    lambda: product_section(1, "HyperX Alloy Core", "~45€", "Membrana | RGB | Resistente derrames", "Silencioso, RGB bonito, antiderrames", "No es mecanico") +
           product_section(2, "Logitech G413 SE", "~50€", "Mecanico | Tactil | Compacto", "Mecanico asequible, buena construccion", "Sin RGB") +
           "\n## Veredicto\n\n**Mejor membrana:** HyperX Alloy Core.\n**Mejor entrada a mecanico:** Logitech G413 SE.\n")

add("Mejores Juegos de Mundo Abierto Baratos PC (2026)", 42,
    "Libertad total sin precio elevado. Los mejores juegos de mundo abierto economicos para PC.",
    ["Juegos"], ["mundo abierto", "juegos baratos", "PC"],
    lambda: """
## Los mejores mundos abiertos economicos

| Juego | Precio | Duracion | Mapa |
|-------|--------|----------|------|
| The Witcher 3 | ~8€ (oferta) | 100h+ | Enorme |
| Skyrim | ~7€ (oferta) | 200h+ | Enorme |
| Fallout 4 | ~6€ (oferta) | 100h+ | Grande |
| GTA V | ~10€ (oferta) | 50h+ | Enorme |

## 1. The Witcher 3: Wild Hunt

- **Precio:** ~8€ en oferta | **Duracion:** 100h+
- **Ventajas:** Mejor RPG de la decada, misiones secundarias increibles, DLCs enormes

Por 8€ en oferta tienes uno de los mejores juegos jamas creados y sus dos DLCs que son juegos completos.

## 2. Skyrim

- **Precio:** ~7€ en oferta | **Duracion:** 200h+
- **Ventajas:** Libertad total, mods infinitos, rejugable eternamente

Una decada despues y la comunidad sigue activa. Los mods lo convierten en un juego nuevo.

## 3. Fallout 4

- **Precio:** ~6€ en oferta | **Duracion:** 100h+
- **Ventajas:** Supervivencia, construccion de asentamientos, exploracion

Skyrim con pistolas y radiacion. La construccion de bases anade horas de diversion.

## 4. GTA V

- **Precio:** ~10€ en oferta | **Duracion:** 50h+ (campaña)
- **Ventajas:** Mundo vivo, misiones variadas, GTA Online (atencion: mucho grinding)

El mundo abierto mas vivo jamas creado. Ocho anos despues y sigue siendo impresionante.

## Veredicto

**Mejor RPG:** The Witcher 3.
**Mas libertad:** Skyrim.
**Mas moderno:** GTA V.
""")

add("Mejor Alfombrilla RGB Barata (2026)", 43,
    "Ilumina tu escritorio sin gastar una fortuna. Las mejores alfombrillas RGB gaming economicas.",
    ["Accesorios"], ["alfombrilla RGB", "gaming", "barata"],
    lambda: product_section(1, "Alfombrilla RGB XXL", "~20€", "800x300mm | RGB | Superficie tela", "Gran tamano, RGB bonito, superficie suave", "RGB basico") +
           "\n## Veredicto\n\n**Mejor calidad-precio:** Alfombrilla RGB XXL.\n")

add("Como Elegir una Fuente de Alimentacion (2026)", 44,
    "Guia completa para elegir la fuente de alimentacion adecuada para tu PC gaming. Watts, eficiencia y conectores.",
    ["Guias"], ["fuente alimentacion", "guia", "PSU"],
    lambda: """
## La fuente es la pieza mas infravalorada

Una fuente mala puede quemar tus componentes. Una buena fuente dura 10+ anos y aguanta varias generaciones de PC.

## Watts necesarios segun tu GPU

| GPU | Fuente recomendada |
|-----|-------------------|
| GTX 1650 / RX 6400 | 400W |
| RTX 3050 / RX 6600 | 500W |
| RTX 3060 / RX 6700 XT | 550W |
| RTX 3070 / RX 6800 | 650W |
| RTX 3080 / RX 6900 XT | 750W+ |

## Certificacion 80 Plus

| Certificacion | Eficiencia (carga 100%) | Precio |
|---------------|------------------------|--------|
| White | 80% | Muy barata |
| Bronze | 82% | Estandar |
| Silver | 85% | Buena |
| Gold | 87% | Excelente |
| Platinum | 89% | Cara |

Para un PC gaming economico, **80+ Bronze** es suficiente.

## Modular o no modular?

| Tipo | Ventajas | Desventajas |
|------|----------|-------------|
| No modular | Barata, sencilla | Cables sobrantes |
| Semi-modular | Buenos cables fijos, flexibilidad | Un poco mas cara |
| Full modular | Gestion cables perfecta | Mas cara |

Recomendacion: **Semi-modular** es el punto dulce calidad-precio.

## Consejos finales

1. **No ahorres en fuente:** Es la pieza que protege todo tu PC
2. **Mira el amperaje del rail +12V:** Es el mas importante para gaming
3. **Marca:** Seasonic, Corsair, EVGA, Cooler Master

## Veredicto

Para un PC gaming economico: **550W 80+ Bronze semi-modular** de marca reconocida.
""")

add("Mejor Auricular Gaming con Microfono (2026)", 45,
    "Comunicacion clara y buen sonido sin gastar de mas. Los mejores auriculares con microfono para gaming.",
    ["Perifericos"], ["auricular microfono", "gaming", "comunicacion"],
    lambda: product_section(1, "HyperX Cloud Stinger", "~50€", "50mm | 275g | Microfono giratorio", "Ligero, comodo, microfono con silencio automatico", "Cable basico") +
           product_section(2, "Razer BlackShark V2 X", "~55€", "50mm | 240g | Aislamiento pasivo", "Excelente microfono cardioide, ligero, sonido claro", "Sin USB") +
           product_section(3, "SteelSeries Arctis Nova 1", "~60€", "40mm | 236g | Microfono retractil", "Comodisimo, microfono oculto, buena construccion", "Un poco mas caro") +
           "\n## Veredicto\n\n**Mas comodo:** HyperX Cloud Stinger.\n**Mejor microfono:** Razer BlackShark V2 X.\n**Mas premium:** SteelSeries Arctis Nova 1.\n")

add("Como Configurar OBS para Grabar Partidas (2026)", 46,
    "Guia completa para grabar tus partidas con OBS Studio sin perder rendimiento.",
    ["Guias"], ["OBS", "grabar partidas", "configurar"],
    lambda: """
## Por que OBS Studio

OBS Studio es el mejor software de grabacion y streaming. Es gratis, open source y funciona en cualquier PC.

## Configuracion basica para grabacion

### Paso 1: Crear escena
1. Abre OBS
2. En "Escenas", haz click en +
3. Nombrala "Juego"

### Paso 2: Anadir fuente
1. En "Fuentes", haz click en +
2. Selecciona "Captura de juego"
3. Elige "Capturar cualquier ventana en pantalla completa" o selecciona el juego especifico

### Paso 3: Configurar audio
- Anade "Captura de audio de escritorio" (sonido del juego)
- Anade "Captura de audio de entrada" (tu microfono)

### Paso 4: Ajustes de grabacion
- Ve a Archivo > Configuracion > Salida
- **Modo de salida:** Avanzado
- **Grabacion:**

| Ajuste | Valor recomendado |
|--------|------------------|
| Codificador | NVIDIA NVENC H.264 (o x264 si no tienes NVIDIA) |
| Tasa de bits | 15000-25000 kbps |
| Preset | P5: Slow (mejor calidad) o P6: Slowest |
| Formato | MP4 |

### Paso 5: Configuracion de video
- **Resolucion base:** La de tu monitor
- **Resolucion de salida:** 1920x1080 o 1280x720
- **FPS:** 30 o 60
- **Filtro de escalado:** Lanczos (mejor calidad)

## Atajos de teclado utiles

| Accion | Atajo |
|--------|-------|
| Empezar/detener grabacion | Ctrl + F5 |
| Empezar/detener streaming | Ctrl + F6 |
| Silenciar microfono | Ctrl + F9 |

## Optimizacion para grabar sin perder FPS

### Si tienes GPU NVIDIA (recomendado)
- Usa NVENC en lugar de x264
- Marca "Recodificar" en NVIDIA ShadowPlay para minimizar el impacto

### Si solo tienes CPU
- Baja resolucion de grabacion a 720p
- Reduce FPS a 30
- Cierra programas en segundo plano

## Veredicto

OBS + NVENC es la combinacion ganadora. Prueba los ajustes antes de una sesion importante.
""")

add("Mejores Juegos para PC Gama Baja (2026)", 47,
    "No necesitas un PC potente para jugar. Los mejores juegos que funcionan en cualquier PC.",
    ["Juegos"], ["PC gama baja", "requisitos minimos", "juegos"],
    lambda: """
## Juegos que funcionan en cualquier PC

| Juego | Requisito minimo | FPS esperados |
|-------|-----------------|---------------|
| Valorant | Intel HD 3000 | 60-120 FPS |
| CS2 | GT 730 | 60-90 FPS |
| League of Legends | Intel HD | 60+ FPS |
| Minecraft | Intel HD | 30-60 FPS |
| Fortnite (rendimiento) | Intel HD | 30-60 FPS |

## 1. Valorant

- **GPU minima:** Intel HD 3000
- **FPS esperados:** 60-120
- **Por que funciona:** Motor optimizado, graficos simples intencionadamente

El shooter tactico que funciona en cualquier PC. Si tu PC enciende, Valorant corre.

## 2. Fortnite (Modo Rendimiento)

- **GPU minima:** Intel HD 4000
- **FPS esperados:** 30-60
- **Por que funciona:** Modo Rendimiento reduce drasticamente los graficos

Activa el Modo Rendimiento en Ajustes de video y multiplica tus FPS.

## 3. League of Legends

- **GPU minima:** Intel HD
- **FPS esperados:** 60+
- **Por que funciona:** Motor antiguo y optimizado

El MOBA mas jugado del mundo funciona en un portatil de oficina.

## 4. Minecraft (Java Edition)

- **GPU minima:** Intel HD
- **FPS esperados:** 30-60
- **Por que funciona:** Graficos simples, optimizable con mods

Instala Sodium, Lithium y Phosphor (mods de optimizacion) y triplica tus FPS.

## 5. CS2

- **GPU minima:** GT 730
- **FPS esperados:** 60-90
- **Por que funciona:** Source 2 optimizado, ajustes bajos

Pon todo al minimo, escala de renderizado al 75% y disfruta.

## Consejos para jugar en PC gama baja

1. Baja la resolucion (720p o 900p)
2. Desactiva sombras y reflejos
3. Usa FSR/AMD FSR si el juego lo soporta
4. Cierra Chrome y Discord mientras juegas
5. Usa modo rendimiento o rendimiento en Windows

## Veredicto

**Shooter:** Valorant.
**Battle Royale:** Fortnite (Modo Rendimiento).
**Creativo:** Minecraft (con mods de optimizacion).
""")

add("Mejores Juegos de Aventura Grafica Baratos (2026)", 48,
    "Historias increibles que parecen peliculas interactivas. Los mejores juegos de aventura grafica economicos.",
    ["Juegos"], ["aventura grafica", "narrativo", "barato"],
    lambda: """
## Los mejores juegos narrativos economicos

| Juego | Precio | Duracion | Estilo |
|-------|--------|----------|--------|
| Life is Strange | ~3€ (oferta) | 15h | Episodico, emocional |
| The Walking Dead | ~4€ (oferta) | 12h | Decisiones, zombies |
| Firewatch | ~3€ (oferta) | 4h | Misterio, walking sim |
| Disco Elysium | ~10€ (oferta) | 40h+ | RPG narrativo sin combate |

## 1. Life is Strange

- **Precio:** ~3€ en oferta | **Duracion:** 15h
- **Ventajas:** Historia emotiva, banda sonora increible, decisiones que importan

Viaja en el tiempo y cambia el curso de los acontecimientos. Te hara llorar.

## 2. The Walking Dead (Telltale)

- **Precio:** ~4€ en oferta | **Duracion:** 12h
- **Ventajas:** Decisiones dificiles, personajes memorables, tenso

Clem entera es uno de los mejores personajes de los videojuegos.

## 3. Firewatch

- **Precio:** ~3€ en oferta | **Duracion:** 4h
- **Ventajas:** Precioso visualmente, ambientacion, dialogos naturales

Un paseo por el bosque que se convierte en un misterio absorbente.

## Veredicto

**Mas emotivo:** Life is Strange.
**Mejor historia:** The Walking Dead.
**Mas bonito:** Firewatch.
""")

add("Guia de Refrigeracion para PC Gaming (2026)", 49,
    "Mantén tu PC fresco sin gastar una fortuna. Guia completa de refrigeracion para PC gaming economico.",
    ["Guias"], ["refrigeracion", "temperatura", "cooling"],
    lambda: """
## Por que la refrigeracion importa

Un PC caliente rinde menos. Las GPU y CPU reducen su velocidad cuando alcanzan temperaturas limites (thermal throttling). Una buena refrigeracion mantiene el rendimiento maximo.

## Tipos de refrigeracion

### Refrigeracion por aire (recomendada para presupuesto ajustado)

| Tipo | Precio | Rendimiento | Ruido |
|------|--------|-------------|-------|
| Cooler stock (incluido) | Gratis | Basico | Medio |
| Torre simple (Hyper 212) | ~25€ | Bueno | Bajo |
| Torre doble | ~40€ | Excelente | Bajo |

### Refrigeracion liquida AIO

| Tipo | Precio | Para quien |
|------|--------|------------|
| AIO 120mm | ~50€ | Cajas pequenas |
| AIO 240mm | ~70€ | CPUs que calientan mucho |
| AIO 360mm | ~100€+ | Overclock extremo |

**Para PC economico:** Un cooler de torre de 25€ es suficiente para cualquier CPU gaming.

## Flujo de aire optimo

### Configuracion basica (2-3 ventiladores)
- **Frontal:** Entrada (2 ventiladores)
- **Trasero:** Salida (1 ventilador)
- **Superior:** Salida (opcional)

### Configuracion optima (4+ ventiladores)
- **Frontal:** 2-3 ventiladores de entrada
- **Superior:** 1-2 ventiladores de salida
- **Trasero:** 1 ventilador de salida

### Principio basico
- Presion positiva (mas entrada que salida) = menos polvo

## Temperaturas objetivo

| Componente | Buena | Aceptable | Critica |
|-----------|-------|-----------|---------|
| CPU | 40-65°C | 65-80°C | >85°C |
| GPU | 40-70°C | 70-85°C | >90°C |
| SSD/HDD | 30-45°C | 45-55°C | >60°C |

## Mejoras baratas

| Mejora | Precio | Beneficio |
|--------|-------|-----------|
| Ventilador extra 120mm | ~8€ | Mejora flujo de aire |
| Pasta termica MX-4 | ~5€ | Baja 3-5°C |
| Cable fan hub | ~6€ | Gestion de ventiladores |
| Elevar PC del suelo | Gratis | Mejor flujo inferior |

## Veredicto

Para un PC economico: cooler de torre de 25€ + 3-4 ventiladores de caja + buena gestion de cables.
""")

add("Mejor Monitor para PS5 y Xbox Barato (2026)", 50,
    "Saca el maximo partido a tu consola sin gastar un dineral. Los mejores monitores para PS5 y Xbox economicos.",
    ["Monitores"], ["PS5", "Xbox", "monitor consola"],
    lambda: """
## Que necesita tu consola

| Consola | Resolucion max | Refresco max | HDMI necesario |
|---------|---------------|--------------|----------------|
| PS5 | 4K 120Hz | 120Hz | 2.1 para 4K120 |
| Xbox Series X | 4K 120Hz | 120Hz | 2.1 para 4K120 |
| Xbox Series S | 1440p 120Hz | 120Hz | 2.0 suficiente |
| PS4 / Xbox One | 1080p 60Hz | 60Hz | 1.4 suficiente |

## Opciones recomendadas

### Para Xbox Series S (mejor relacion calidad-precio)

| Monitor | Precio | Especificaciones |
|---------|--------|-----------------|
| AOC 24G2SP | ~210€ | 24\" IPS 165Hz |

La Series S no necesita 4K. Un monitor 1080p o 1440p con 120Hz es perfecto.

### Para PS5 / Xbox Series X (presupuesto ajustado)

| Monitor | Precio | Especificaciones |
|---------|--------|-----------------|
| Sceptre E248B | ~140€ | 24\" VA 165Hz |

Aunque no tenga HDMI 2.1, estos monitores aceptan 1080p 120Hz de PS5.

## Configuracion en consola

1. **PS5:** Ajustes > Pantalla y video > Salida de video > 1080p o 1440p
2. **Xbox:** Configuracion > General > Opciones de TV y pantalla > 1080p o 1440p
3. **Activa 120Hz:** En los ajustes de pantalla de la consola
4. **Modo juego:** Activalo en el monitor para minimizar input lag

## Veredicto

**Mejor para Series S:** AOC 24G2SP 165Hz.
**Mas economico:** Sceptre E248B 165Hz.
**Consejo:** No pagues por 4K en monitor si tu presupuesto es ajustado, 1080p 120Hz es el punto dulce.
""")

add("Como Acelerar Windows para Gaming (2026)", 51,
    "Optimiza Windows 10/11 para jugar sin gastar dinero. Ajustes y trucos para mas FPS.",
    ["Guias"], ["Windows", "optimizar", "FPS"],
    lambda: """
## Windows gaming optimizado

Windows viene con muchas funciones activadas que consumen recursos sin que las necesites para jugar. Aqui te decimos que desactivar.

## 1. Configuracion de energia

1. Ve a **Configuracion > Sistema > Energia y suspension**
2. Selecciona **"Alto rendimiento"**
3. Si no aparece, crea un plan personalizado:
   - Panel de control > Opciones de energia > Crear plan de energia
   - Selecciona "Alto rendimiento"

## 2. Modo juego

1. Configuracion > Juegos > Modo juego > **Activado**
2. Configuracion > Juegos > Modo juego > Graficos
   - Anade tus juegos y selecciona "Alto rendimiento"

## 3. Desactivar programas de inicio

Abre el **Administrador de tareas** (Ctrl + Shift + Esc) > Inicio
Desactiva todo lo que no necesites:
- Steam (se abre cuando juegas igualmente)
- Discord
- Spotify
- Actualizadores de drivers

## 4. Ajustes visuales

Sistema > Acerca de > Configuracion avanzada del sistema > Rendimiento
Selecciona **"Ajustar para obtener el mejor rendimiento"**

## 5. Desactivar notificaciones

Configuracion > Sistema > Notificaciones > Desactivar "Sugerencias" y "Notificaciones de aplicaciones"

## 6. Desactivar Xbox Game Bar (si no la usas)

Configuracion > Juegos > Xbox Game Bar > Desactivado

## 7. Desactivar actualizaciones automaticas durante el juego

Configuracion > Windows Update > Opciones avanzadas > Pausar actualizaciones

## 8. Desfragmentar discos

Si tienes HDD (no SSD): Desfragmenta cada mes.
Si tienes SSD: No desfragmentes, solo ejecuta "Optimizar unidades"

## 9. Limpiar disco

Herramienta "Liberador de espacio en disco" (buscala en inicio)
Limpia archivos temporales, papelera, miniaturas

## Script de optimizacion rapida

Crea un archivo `.bat` con estos comandos para desactivar servicios innecesarios:

```
@echo off
powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
sc stop SysMain
sc config SysMain start=disabled
echo Optimizacion completada
pause
```

## Veredicto

No necesitas programas de "optimizacion" de pago. Todo esto es gratis y nativo de Windows.
""")

add("Mejor VPN para Gaming Barata (2026)", 52,
    "Protege tu privacidad y reduce el ping. Las mejores VPNs para gaming economicas y recomendadas.",
    ["Guias"], ["VPN", "privacidad", "ping"],
    lambda: """
## VPN y gaming: lo que debes saber

Una VPN puede ayudarte a:
- Reducir ping en algunos juegos (ruta mas directa)
- Protegerte de ataques DDoS
- Acceder a juegos con restricciones regionales
- Mantener tu privacidad

Pero tambien puede aumentarlo si el servidor VPN esta lejos.

## Mejores VPNs para gaming

### 1. Cloudflare WARP (Gratis)

- **Precio:** Gratis
- **Velocidad:** Excelente (usa infraestructura Cloudflare)
- **Gaming:** Buena, baja latencia
- **Privacidad:** No guarda logs

La mejor opcion gratis. No es una VPN tradicional sino un DNS inteligente que optimiza tu ruta.

### 2. ProtonVPN (Gratis)

- **Precio:** Gratis (limitado)
- **Velocidad:** Buena
- **Gaming:** Aceptable
- **Privacidad:** Excelente (Suiza, sin logs)

Sin limites de datos en la version gratis, pero servidores limitados.

### 3. Mullvad VPN (~5€/mes)

- **Precio:** ~5€/mes
- **Velocidad:** Excelente
- **Gaming:** Muy buena
- **Privacidad:** Maxima (anonima, sin logs)

La mejor opcion de pago para gaming. Acepta efectivo y cripto para maximo anonimato.

## Como afecta una VPN al ping

| Distancia al servidor VPN | Impacto en ping |
|---------------------------|----------------| 
| Misma ciudad | +1-3ms |
| Mismo pais | +5-15ms |
| Otro pais | +20-50ms |
| Otro continente | +100-200ms+ |

**Regla:** Elige un servidor VPN cercano a ti o al servidor del juego.

## Veredicto

**Mejor gratis:** Cloudflare WARP.
**Mejor privacidad:** Mullvad VPN (5€/mes).
**Recomendacion:** Prueba primero con Cloudflare WARP, es gratis y funciona.
""")

add("Mejor Software de Gaming Gratuito (2026)", 53,
    "Los mejores programas gratuitos para mejorar tu experiencia gaming. Desde grabacion hasta optimizacion.",
    ["Guias"], ["software", "gratis", "herramientas"],
    lambda: """
## Software gaming gratuito que necesitas

| Programa | Funcion | Alternativa de pago |
|----------|---------|-------------------|
| OBS Studio | Grabacion/Streaming | XSplit (~5€/mes) |
| MSI Afterburner | Overclocking GPU | No hay |
| Discord | Comunicacion | TeamSpeak |
| Steam | Tienda y biblioteca | No hay |
| GPU-Z | Monitorizacion GPU | No hay |
| HWiNFO | Monitorizacion sistema | No hay |

## 1. OBS Studio

- **Precio:** Gratis (open source)
- **Usos:** Grabar partidas, hacer streaming, capturar clips
- **Alternativa de pago:** XSplit (~5€/mes)

El estandar de la industria para streaming y grabacion. No necesitas nada mas.

## 2. MSI Afterburner

- **Precio:** Gratis
- **Usos:** Overclocking GPU, monitorizar temperatura/FPS, control ventiladores
- **Alternativa de pago:** EVGA Precision X1

Imp rescindible para cualquier gamer que quiera monitorizar su PC mientras juega.

## 3. Discord

- **Precio:** Gratis
- **Usos:** Voz con amigos, comunidades gaming
- **Alternativa de pago:** TeamSpeak (gratis para servers pequenos)

La herramienta de comunicacion esencial. Nitro es opcional y no necesario.

## 4. Steam

- **Precio:** Gratis
- **Usos:** Comprar y gestionar juegos, amigos, capturas, workshop
- **Alternativa:** Epic Games Store, GOG

La plataforma gaming mas importante. Las ofertas de Steam te ahorran mucho dinero.

## 5. GPU-Z y HWiNFO

- **Precio:** Gratis
- **Usos:** Monitorizar temperaturas, voltajes, velocidades
- **Alternativa de pago:** AIDA64

Saben exactamente que hace tu PC en cada momento.

## Veredicto

No pagues por software gaming. OBS, MSI Afterburner, Discord y Steam cubren todo lo necesario.
""")

add("Como Elegir un Teclado Gaming (2026)", 54,
    "Guia completa para elegir tu teclado gaming ideal. Switches, formato y caracteristicas explicadas.",
    ["Guias"], ["elegir teclado", "guia", "gaming"],
    lambda: """
## Guia para comprar teclado gaming

Elegir teclado es mas sencillo de lo que parece. Solo necesitas decidir tres cosas: tipo de switch, formato y presupuesto.

## 1. Tipo de switch

### Mecanicos

| Switch | Sonido | Tacto | Ideal para |
|--------|--------|-------|------------|
| Lineal (Rojo) | Silencioso | Suave | Gaming, pulsaciones rapidas |
| Tactil (Marron) | Moderado | Nota la pulsacion | Mixto, escribir y jugar |
| Clicky (Azul) | Ruidoso | Clic audible | Escritura, experiencia mecanica clasica |

**Recomendacion gaming:** Lineal (Rojo) para respuesta rapida.

### Membrana
- Mas silenciosos
- Mas baratos (~30€)
- Peor sensacion para gaming competitivo
- Buenos para uso casual

## 2. Formato

| Formato | Teclas | Espacio | Ideal para |
|---------|--------|---------|------------|
| Completo (100%) | 104 | Maximo | Trabajo, accesos rapidos |
| TKL (80%) | 87 | Poco | Gaming, espacio medio |
| 75% | 84 | Minimo | Gaming, escritorio pequeno |
| 60% | 61 | Minimo | Gaming competitivo, mesa pequena |

**Recomendacion:** TKL o 75% es el punto dulce para la mayoria.

## 3. Presupuesto

| Precio | Que esperar |
|--------|-------------|
| < 40€ | Mecanico basico (Redragon K552) |
| 40-70€ | Buenos mecanicos (Keychron, Tecware) |
| 70-100€ | Excelente calidad, software, RGB |
| 100€+ | Premium (Ducky, Leopold, custom) |

## 4. Caracteristicas adicionales

- **Switches intercambiables en caliente:** Permite cambiar switches sin soldar
- **Software:** Para reasignar teclas, crear macros, ajustar RGB
- **Cable desmontable:** USB-C facil de transportar
- **Reposamenorcas:** Comodidad extra en sesiones largas

## Veredicto

**Mejor entrada:** Redragon K552 (~35€).
**Mejor calidad-precio:** Keychron C1 Pro (~60€).
**Formato recomendado:** TKL o 75%.
""")


# ===================== GENERATION =====================

def main():
    for i, p in enumerate(posts):
        date = (START_DATE + timedelta(days=i)).strftime("%Y-%m-%dT00:00:00+02:00")
        slug = p["content_fn"]().__class__.__name__  # dummy

    # Manual generation loop
    date = START_DATE
    for i, p in enumerate(posts):
        date_str = date.strftime("%Y-%m-%dT00:00:00+02:00")
        content = posts[i]["content_fn"]()
        slug_base = f"post-{i+1:02d}"

        # Build a proper slug from the title
        title = posts[i]["title"]
        # Remove year suffix in parentheses for slug
        slug_title = title.lower()
        for sep in [": ", "(", ")", ",", "?", "/"]:
            slug_title = slug_title.replace(sep, "")
        slug_title = slug_title.replace(" ", "-").replace("--", "-").strip("-")
        # Remove trailing year pattern like -2026
        if slug_title.endswith("-2026"):
            slug_title = slug_title[:-5]
        # Remove accents
        replacements = {
            "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
            "ü": "u", "ñ": "n"
        }
        for old, new in replacements.items():
            slug_title = slug_title.replace(old, new)

        slug = f"{slug_title}-2026"

        write_post(
            slug=slug,
            title=title,
            date=date_str,
            summary=posts[i]["summary"],
            cats=posts[i]["cats"],
            tags=posts[i]["tags"],
            content=content
        )
        date += timedelta(days=1)

if __name__ == "__main__":
    main()
