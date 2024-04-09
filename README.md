# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> My profitable path is tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129888.
> 
> For the first swap, the amountIn is 5 tokenB, and the amountOut is 5×(997/1000)×(17/(10+(5×(997/1000))))=5.655322 tokenA.
> 
> For the second swap, the amountIn is 5.655322 tokenA, and the amountOut is 5.655322×(997/1000)×(9/(15+(5.655322×(997/1000))))=2.458781 tokenD.
> 
> For the third swap, the amountIn is 2.458781 tokenD, and the amountOut is 2.458781×(997/1000)×(30/(12+(2.458781×(997/1000))))= 5.088927 tokenC.
> 
> For the third swap, the amountIn is 5.088927 tokenC, and the amountOut is 5.088927×(997/1000)×(36/(4+(5.088927×(997/1000))))= 20.129888 tokenB.
> 
> The final reward is 20.129888 tokenB.

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Slippage is the difference between the expected price of a trade and the price at which the trade is executed. This often occurs in large trades because they significantly change the ratio of the token pool, thereby affecting the price.
> 
> Uniswap V2 reduces slippage by using the constant product formula `x * y = k`, where `x` and `y` are the quantities of the two tokens in the pool, and `k` is a constant. The smaller the trade volume relative to the pool size, the smaller the slippage. Additionally, Uniswap allows users to set a minimum amount received (or maximum amount paid) for trades; if the trade would result in receiving less than this amount, the trade is reverted.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> In Uniswap V2, a minimum amount of liquidity tokens is subtracted when initially minting liquidity to prevent someone from acquiring the entire pool at an extremely low cost. This minimum liquidity token is permanently locked in the contract, ensuring that the pool always has a certain size of liquidity, thereby preventing potential manipulation and abuse in setting initial prices.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Uniswap V2 mints liquidity tokens in this manner with the aim of creating a trading environment, where the provision and acquisition of liquidity are proportional, preventing potential market manipulation and ensuring stability between trading pairs.
> 
> It help preventing slippage, and reduces the opportunity for malicious actors to affect the value of the liquidity pool by manipulating market prices.
It also can maintaining pool ratios, helps maintain the stability and liquidity of the pool, as any disproportionate addition could lead to temporary market imbalances.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> A sandwich attack is a strategy where attackers place two trades around a pending large transaction, detecting an imminent large trade, executing a trade before and after it. The attacker executes a trade to raise the price, then the victim's trade is executed at a higher price, and finally, the attacker sells at the higher price, making a profit. 
This attack causes the initiator of the original trade to pay an excessive price and or receive fewer tokens than expected, by increasing transaction cost, thereby losing funds.

