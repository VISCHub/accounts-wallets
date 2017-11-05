COMPRESSED = 'COMPRESSED'
UNCOMPRESSED = 'UNCOMPRESSED'
MAINNET = 'MAINNET'
TESTNET = 'TESTNET'
PUBKEY = 'PUBKEY'
PRIVKEY = 'PRIVKEY'

NETWORK_TYPES = {
    MAINNET: {
        PUBKEY: b'\x00',
        PRIVKEY: b'\x80'
    },
    TESTNET: {
        PUBKEY: b'\x6F',
        PRIVKEY: b'\xEF'
    },
}
