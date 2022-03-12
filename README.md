# The Oracle problem
One of the most challenging topics in decentralized finance infrastructure 
is for sure that most (if not every) smart contract relies on realiable off-chain
market data. While Chainlink serves as the oracle on the Ethereum chain, the Pyth-Network
seeks to do so on the Solana chain. 
When we think about trading processes latency and speed is key. The Pyth-Network is able to 
provide low-latency consensus market data which is the first step towards an 
infrastructure where market data is not a heavily monetized property of centralized vendors anymore.


### The Idea
Creating an application that is able to consume market data from the Solana chain with the look and feel 
of a real-time data feed we know from the largest vendors in the industry.

### The Implementation
I use the python pythclient for asynchronous requests of the Solana price accounts
togehter with a panel Bokeh server for visualizing the data in a chart:

![Alt text](images/example1.png?raw=True "Example 1")

Please note that non-crypto assets such as AAPL will show a 0 price outside regular trading 
hours (equities do not trade 24/7 yet ;))

In order to start the panel:

    panel serve gridview.py

This part is necessary because of the nested async structure created by the
PeriodicDataFrame and the async call of the Solana chain:

    import nest_asyncio
    nest_asyncio.apply()

The Pyth-Network [documentation](https://docs.pyth.network/#consumers)  was of great help in setting this up.
