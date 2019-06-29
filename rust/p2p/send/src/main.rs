extern crate p2p;
extern crate rust_sodium;

use rust_sodium::crypto::box_::curve25519xsalsa20poly1305::PrecomputedKey;

fn main() {
    p2p::msg_to_send("hello world".as_bytes(), &PrecomputedKey::from_slice("4a2e6cc15bb84c008c27a572bc7d1b24".as_bytes()).unwrap());
}
