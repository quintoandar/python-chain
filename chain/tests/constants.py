ENTRYPOINT = "chain"
CHAIN = "chain.core.domains.chain.chain"
DECORATOR = "chain.core.domains.chain.decorator"
STATE = "chain.core.domains.state.state"

DEPEDENCIES_HASH_TABLE = {
    ENTRYPOINT: ("State", "Decorator"),
    CHAIN: ("State", "Context"),
    DECORATOR: ("update_wrapper", "Chain"),
    STATE: ("Context",),
}
