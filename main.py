from pythclient.pythclient import PythClient
from pythclient.pythaccounts import PythPriceAccount
from pythclient.utils import get_key
import asyncio

solana_network="devnet"
use_program=True
async def test():
    async with PythClient(
        first_mapping_account_key=get_key(solana_network, "mapping"),
        program_key=get_key(solana_network, "program") if use_program else None,
    ) as c:
        await c.refresh_all_prices()
        products = await c.get_products()
        for p in products:
            print(p.attrs)
            prices = await p.get_prices()
            for _, pr in prices.items():
                print(
                    pr.price_type,
                    pr.aggregate_price_status,
                    pr.aggregate_price,
                    "p/m",
                    pr.aggregate_price_confidence_interval,
                )

asyncio.run(test())


import asyncio
from pythclient.pythaccounts import PythPriceAccount, PythPriceStatus
from pythclient.solana import SolanaClient, SolanaPublicKey, SOLANA_DEVNET_HTTP_ENDPOINT, SOLANA_DEVNET_WS_ENDPOINT

async def get_price():
    account_key = SolanaPublicKey("HovQMDrbAgAYPCmHVSrezcSmkMtXSSUsLDFANExrZh2J")
    solana_client = SolanaClient(endpoint=SOLANA_DEVNET_HTTP_ENDPOINT, ws_endpoint=SOLANA_DEVNET_WS_ENDPOINT)
    price: PythPriceAccount = PythPriceAccount(account_key, solana_client)
    await price.update()
    price_status = price.aggregate_price_status
    if price_status == PythPriceStatus.TRADING:
        print("BTC/USD currently stands at", price.aggregate_price, "±", price.aggregate_price_confidence_interval)
    else:
        print("Price is not valid now. Status is", price_status)
    await solana_client.close()

asyncio.run(get_price())