import base64
import base58
import solana
import asyncio
from solana.transaction import Transaction
from solana.rpc.async_api import AsyncClient

from solders.keypair import Keypair

# tx_params = '4hXTCkRzt9WyecNzV1XPgCDfGAZzQKNxLXgynz5QDuWWPSAZBZSHptvWRL3BjCvzUXRdKvHL2b7yGrRQcWyaqsaBCncVG7BFggS8w9snUts67BSh3EqKpXLUm5UMHfD7ZBe9GhARjbNQMLJ1QD3Spr6oMTBU6EhdB4RD8CP2xUxr2u3d6fos36PD98XS6oX8TQjLpsMwncs5DAMiD4nNnR8NBfyghGCWvCVifVwvA8B8TJxE1aiyiv2L429BCWfyzAme5sZW8rDb14NeCQHhZbtNqfXhcp2tAnaAT'

# decoded_tx = base58.b58decode(bytes(tx_params, 'utf-8'))

# transaction = Transaction.deserialize(decoded_tx)

# print(transaction.compile_message())

pk = ''
pk_bytes = base58.b58decode(pk)
wallet = Keypair.from_bytes(pk_bytes)
hyi = wallet.pubkey()

print(hyi)

async def main():
    async with AsyncClient("https://api.devnet.solana.com") as cl:
        balances = await cl.get_account_info(hyi)
        print(balances.value.lamports / 10**9)
        
asyncio.run(main())
