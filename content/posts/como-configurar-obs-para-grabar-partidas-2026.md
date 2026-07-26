---
title: "Como Configurar OBS para Grabar Partidas (2026)"
date: 2026-09-25T00:00:00+02:00
# lastmod: 2026-09-25T00:00:00+02:00
draft: false
summary: "Guia completa para grabar tus partidas con OBS Studio sin perder rendimiento."
categories:
  - "Guias"
tags:
  - "OBS"
  - "grabar partidas"
  - "configurar"
---


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
