/*
Idea: Build a crypto trading bot in C++ to function
across multiple exchanges. Not all features will be
implemented at once, nor should they be. Current plan
is to build out basics first (MVP), then build out
features from there.
*/

/*
Helpers to gather info on:
 - Coins traded on different exchanges
 - Volume of trades of coins on exchanges
 - Current held assets
 - Internet traffic relating to coins
 - General crypto market trends
    - 1-52 wk high and low value on coins
    - 
 - Stock market trends (S&P -> effect on crypto)

Decision (per coin):
 - Volume to buy
 - Volume to hold (majority of time)
 - Volume to Sell (and volume to sell)

Execute (Different helper):
 - Plan order execution
 - Minimize total order placements
 - Identify suitable markets to exchange
 - Execute
*/