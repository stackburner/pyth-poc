import pandas as pd
import panel as pn
from streamz.dataframe import PeriodicDataFrame
from hvplot import pandas, streamz
import solana
import asyncio
import nest_asyncio
nest_asyncio.apply()

assets = {
            "BTC/USD": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
            "AAPL": "5yixRcKtcs5BZ1K2FsLFwmES1MyA92d6efvijjVevQCw",
            "SOL/USD": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG"
}


def callback(**kwargs):
    df = pd.DataFrame([])
    for asset in assets:
        df[asset] = [asyncio.run(solana.get_price(assets[asset]))]
    df['time'] = [pd.Timestamp.now()]
    return df.set_index('time')


df = PeriodicDataFrame(callback, interval='1s')
pn_realtime = pn.Column()
for asset in assets:
    pn_realtime.append(pn.Column(df[[asset]].hvplot.line(title=asset, backlog=1000)))
pane = pn.Tabs(('Real Time Pyth Network Data', pn_realtime)).servable()
