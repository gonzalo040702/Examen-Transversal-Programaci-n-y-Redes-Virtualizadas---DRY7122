from ncclient import manager
import xml.dom.minidom

# Datos de conexión al router
HOST = "192.168.1.161"
PORT = 830
USER = "cisco"
PASS = "cisco123!"

# Payload para cambiar el hostname
cambiar_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Nunez-Burgos</hostname>
  </native>
</config>
"""

# Payload para crear loopback 111
crear_loopback = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>111</name>
        <ip>
          <address>
            <primary>
              <address>111.111.111.111</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

print("Conectando al router CSR1000v via NETCONF...")

with manager.connect(
    host=HOST,
    port=PORT,
    username=USER,
    password=PASS,
    hostkey_verify=False
) as m:
    print("✅ Conexión NETCONF establecida!")

    # Cambiar hostname
    print("\nCambiando hostname a Nunez-Burgos...")
    m.edit_config(target="running", config=cambiar_hostname)
    print("✅ Hostname cambiado!")

    # Crear loopback 111
    print("\nCreando interfaz Loopback 111...")
    m.edit_config(target="running", config=crear_loopback)
    print("✅ Loopback 111 creada con IP 111.111.111.111/32!")

    print("\n===== CONFIGURACIÓN COMPLETADA =====")
