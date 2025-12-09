#!/bin/bash

# 1. Obtención de la MAC del Endpoint
# Usamos 'ip address' y filtramos para encontrar la MAC de la primera interfaz de red
# que no es el loopback (generalmente eth0 o wlan0).
MAC_ADDRESS=$(ip a | awk '/ether/{print $2; exit}')

# 2. Obtención del Sistema Operativo (OS)
# Usamos 'lsb_release -ds' (si está disponible, en la mayoría de las distribuciones modernas) o 'cat /etc/os-release' como respaldo
if command -v lsb_release &> /dev/null; then
    OS_INFO=$(lsb_release -ds)
elif [ -f /etc/os-release ]; then
    OS_INFO=$(grep -E '^(PRETTY_NAME|NAME)=' /etc/os-release | head -n 1 | sed 's/PRETTY_NAME=//;s/NAME=//;s/"//g')
else
    # Si los métodos anteriores fallan, se usa el resultado de 'uname -a'
    OS_INFO=$(uname -a)
fi

# 3. Obtención del Nombre del Equipo (Hostname)
HOSTNAME=$(hostname)

# 4. Obtención del Usuario Actual
CURRENT_USER=$(whoami)

# Finalmente ostramos toda la información en un único mensaje
echo "Información del Equipo Sobre el que se ha ejecutado el Script"
echo "Dirección MAC del Equipo:        ${MAC_ADDRESS}"
echo "Sistema Operativo Concreto:      ${OS_INFO}"
echo "Nombre del Equipo (Hostname):    ${HOSTNAME}"
echo "Usuario que ha lanzado el Script: ${CURRENT_USER}"
