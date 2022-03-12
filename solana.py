from pythclient.pythaccounts import PythPriceAccount, PythPriceStatus
from pythclient.solana import SolanaClient, SolanaPublicKey, SOLANA_MAINNET_HTTP_ENDPOINT, SOLANA_MAINNET_WS_ENDPOINT


async def get_price(price_account):
    account_key = SolanaPublicKey(price_account)
    solana_client = SolanaClient(endpoint=SOLANA_MAINNET_HTTP_ENDPOINT, ws_endpoint=SOLANA_MAINNET_WS_ENDPOINT)
    price: PythPriceAccount = PythPriceAccount(account_key, solana_client)
    await price.update()
    price_status = price.aggregate_price_status
    if price_status == PythPriceStatus.TRADING:
        await solana_client.close()
        return price.aggregate_price
    else:
        await solana_client.close()
        return 0.0
