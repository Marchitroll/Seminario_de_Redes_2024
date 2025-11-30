# Seminario de Redes 2024

Repositorio de scripts de Python para el curso **Seminario de Redes 2024**.  
Contiene ejemplos prácticos de programación de sockets TCP/UDP y utilidades de red.

---

## 📋 Requisitos

- **Python 3.6** o superior
- No requiere dependencias externas (solo biblioteca estándar)

Para verificar tu versión de Python:
```bash
python --version
```

---

## 📁 Contenido del Repositorio

### 🔌 Sockets TCP

| Script | Descripción |
|--------|-------------|
| `02_servidor_tcp_saludo.py` | Servidor TCP que acepta conexiones y envía un mensaje de bienvenida |
| `03_cliente_tcp_saludo.py` | Cliente TCP que se conecta al servidor y recibe el saludo |
| `04_servidor_tcp_archivo.py` | Servidor TCP que genera y envía un archivo al cliente |
| `05_cliente_tcp_archivo.py` | Cliente TCP que recibe y guarda un archivo del servidor |

### 📡 Sockets UDP

| Script | Descripción |
|--------|-------------|
| `11_servidor_udp.py` | Servidor UDP que recibe mensajes y envía respuestas |
| `12_cliente_udp.py` | Cliente UDP que envía mensajes al servidor |

### 🌐 Utilidades de Red

| Script | Descripción |
|--------|-------------|
| `01_conexion_basica_udp.py` | Demostración de conexión básica con sockets |
| `06_analizador_ipv4.py` | Analiza propiedades de una dirección IPv4 (privada, pública, loopback, etc.) |
| `07_calculadora_cidr.py` | Calcula parámetros de red a partir de notación CIDR |
| `08_info_red_local.py` | Obtiene nombre del host y direcciones IP del equipo local |
| `09_dns_lookup.py` | Resuelve un nombre de dominio a su dirección IP |
| `10_dns_reverso.py` | Obtiene el nombre de dominio a partir de una IP (DNS inverso) |

---

## 🚀 Uso

### Ejemplo: Servidor y Cliente TCP (saludo)

**Terminal 1 - Iniciar el servidor:**
```bash
python sockets/02_servidor_tcp_saludo.py
```

**Terminal 2 - Ejecutar el cliente:**
```bash
python sockets/03_cliente_tcp_saludo.py
```

### Ejemplo: Servidor y Cliente UDP

**Terminal 1 - Iniciar el servidor:**
```bash
python sockets/11_servidor_udp.py
```

**Terminal 2 - Ejecutar el cliente:**
```bash
python sockets/12_cliente_udp.py
```

### Ejemplo: Utilidades de red

```bash
python sockets/06_analizador_ipv4.py
python sockets/07_calculadora_cidr.py
python sockets/09_dns_lookup.py
```

---

## 🔒 Notas de Seguridad

Los servidores están configurados para escuchar en `127.0.0.1` (localhost) por seguridad.  
Si necesitas que el servidor acepte conexiones de otras máquinas en la red, cambia el host a `0.0.0.0`.

**Puertos utilizados:**
- Servidores TCP: `8080`
- Servidor UDP: `8081`

---

## 📄 Licencia

Este proyecto está bajo la licencia GPL v2. Ver el archivo [LICENSE](LICENSE) para más detalles.
