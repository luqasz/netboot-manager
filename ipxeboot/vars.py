IPXE_HEADER_REGEXP = r'User-Agent:iPXE\/[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}.*'
IPXE_SCRIPT_HEADER = '#!ipxe'
# Dict with mapping of http parameters to ipxe variables.
# Key is parameter passed to app,
# Value is ipxe variable expression.
IPXE_HTTP_VARS = dict(
    uuid='${uuid}',
    mac_address='${mac}',
    asset_tag='${asset}',
    motherboard_serial='${board-serial}',
    motherboard_manufacturer='${manufacturer}',
    product_name='${product}',
    product_serial='${serial}',
    internal_ip_address='${ip}',
    hostname='${hostname}',
    ipxe_version='${version}',
)
