# ForexConnectAPI

This SDK is designed to get trading data, trade, load price histories and subscribe for the most recent prices. 
It is intended to be used by FXCM clients on auto-trading robots and systems, 
chart and market analysis application, custom trading application on FXCM accounts.

Forex Connect supports C++, C#, Java, VB, VBA, Windows, Linux and smart phones. And it is free.

You can use ForexConnect on Trading station account, no extra setup required.

If using O2G2 namespace, keep in mind that it is currently deprecated as it has not been updated since the beginning of 2015. 
It may give the users errors or not be compatible in certain cases.

## How to start:
1) A FXCM TSII account. You can apply for a demo account [here](https://www.fxcm.com/uk/algorithmic-trading/api-trading/). 
2) Download [**ForexConnect SDK**](http://www.fxcodebase.com/wiki/index.php/Download)
3) Examples codes and documents are at ForexConnectAPI packages after installed.
4) Online documents: [**Getting Started**](https://apiwiki.fxcorporate.com/api/Getting%20Started.pdf)

## Suggested Popular Development Platform IDE:
[**Windows 32bit and 64bit – Visual Studio 2005 and up**](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx)

[**Linux 32bit and 64bit – Eclipse**](https://eclipse.org/)

[**iOS – Xcode**](https://developer.apple.com/xcode/ide/)

[**Android - Android Studio**](https://developer.android.com/studio/intro/index.html)

## Table manager vs Non-table manager:
Table manager preload all tables to your local memoery, it is an in-memory representation of API tables. The table manager allows you to subscribe to table change events such as updates, adding rows, or removing rows. It is important to note that the 
SummaryTable is only accessible through the table manager.  
Table manager presents a performance decrease because it is constantly recalculating fields.
Non-table manager allow you to capture table updates adhoc via the use of a class that implements theIO2GResponseListener interface. It give performance advantage but you need to calculate some fields such as PipCost or P/L.

## Real Case Study:
1. Learn how to build and backtest Rsi signals using ForexConnect API at <a href="https://apiwiki.fxcorporate.com/api/StrategyRealCaseStudy/ForexConnectAPI/RsiSignals_via_ForexConnectAPI.zip">here</a>.
2. Learn how to build and backtest CCI Oscillator strategy using ForexConnect API at <a href="https://apiwiki.fxcorporate.com/api/StrategyRealCaseStudy/ForexConnectAPI/2.1.CCI_via_FC_API.zip">here</a>.
3. Learn how to build and backtest Breakout strategy using ForexConnect API at <a href="https://apiwiki.fxcorporate.com/api/StrategyRealCaseStudy/ForexConnectAPI/3.1.BreakoutStrategy_via_FC_API.zip">here</a>.
4. Learn how to build and backtest Range Stochastic Strategy using ForexConnect API at <a href="https://apiwiki.fxcorporate.com/api/StrategyRealCaseStudy/ForexConnectAPI/4.1.StochasticStrategy_via.FC.API.zip">here</a>.
5. Learn how to build and backtest Mean Reversion Strategy using ForexConnect API at <a href="https://apiwiki.fxcorporate.com/api/StrategyRealCaseStudy/ForexConnectAPI/5.1.MeanReverionStrategy_via_FC_API.zip">here</a>.
6. Some examples like attached stop limit to position, create if-then ELS order, get rollover <a href="https://apiwiki.fxcorporate.com/api/StrategyRealCaseStudy/ForexConnectAPI/FC-examples-master.zip">at here</a>.
7. ForexConnect with Matlab, is coming....
8. Using ForexConnect downloading historical data <a href="https://apiwiki.fxcorporate.com/api/StrategyRealCaseStudy/ForexConnectAPI/FXCMHDD-master.zip">at here</a>.

## Note:
o	This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula/)

o	For more information, you may contact us: api@fxcm.com
