PROPERT_SEARCH_IDX = 'property_search_idx'

OPENSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
    'secure': {
        'hosts': [{"scheme": "https", "host": "192.30.255.112", "port": 9201}],
        'http_auth': ("admin", "password"),
        'timeout': 120,
    },
}