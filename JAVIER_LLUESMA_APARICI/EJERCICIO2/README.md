#Información del Sistema (Script Bash)

## Descripción

Este script en Bash (`info_sistema_auditado.sh`) ha sido diseñado para recopilar y mostrar en un único mensaje la información esencial del equipo en el que se ejecuta. Es una herramienta básica de diagnóstico rápido.

## Información que Recopila

El script utiliza comandos estándar de la terminal (como `ip`, `hostname`, `whoami`) para obtener los siguientes datos:

1.  **Dirección MAC:** La dirección física de la primera interfaz de red no *loopback*.
2.  **Sistema Operativo:** El nombre y la versión concreta del sistema operativo (por ejemplo, "Ubuntu 24.04.3 LTS").
3.  **Nombre del Equipo (Hostname):** El nombre de red del dispositivo.
4.  **Usuario Actual:** El nombre del usuario que ha ejecutado el script.

## Pre-requisitos

* Un sistema operativo basado en Unix/Linux (como Ubuntu, Debian, CentOS, macOS, etc.).
* Tener instalado el paquete `iproute2` (para el comando `ip`).

## Instrucciones de Ejecución

Sigue estos pasos para guardar y ejecutar el script:

### 1. Guardar el Script

Crea un nuevo archivo llamado `info_sistema_auditado.sh` y pega el siguiente contenido:

```bash
#!/bin/bash
MAC_ADDRESS=$(ip a | awk '/ether/{print $2; exit}')

if command -v lsb_release &> /dev/null; then
    OS_INFO=$(lsb_release -ds)
elif [ -f /etc/os-release ]; then
    OS_INFO=$(grep -E '^(PRETTY_NAME|NAME)=' /etc/os-release | head -n 1 | sed 's/PRETTY_NAME=//;s/NAME=//;s/"//g')
else
    OS_INFO=$(uname -a)
fi

HOSTNAME=$(hostname)
CURRENT_USER=$(whoami)

echo "Información del Equipo Sobre el que se ha ejecutado el Script"
echo "Dirección MAC del Equipo:        ${MAC_ADDRESS}"
echo "Sistema Operativo Concreto:      ${OS_INFO}"
echo "Nombre del Equipo (Hostname):    ${HOSTNAME}"
echo "Usuario que ha lanzado el Script: ${CURRENT_USER}"


##2. Dar Permisos de Ejecución
Se deben otorgar permisos para que el archivo pueda ser ejecutado como un programa:
chmod +x info_sistema.sh

##3. Ejecutar el Script
Lanza el script desde la terminal:
./info_sistema.sh

##Ejemplo de Salida
Información del Equipo Sobre el que se ha ejecutado el Script
Dirección MAC del Equipo:        74:56:3c:bb:d3:27
Sistema Operativo Concreto:      Ubuntu 24.04.3 LTS
Nombre del Equipo (Hostname):    PC-LINUX-JAVIER
Usuario que ha lanzado el Script: javier


