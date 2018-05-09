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
5) ForexConnect with Matlab, at [here](https://apiwiki.fxcorporate.com/api/StrategyRealCaseStudy/ForexConnectAPI/FXCM-MATLAB-master.zip).

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

## How to get current balance?
You need to request the table from server. please refer to NonTableManagerSamples/PrintTable example program.

      private static O2GAccountRow GetAccount(O2GSession session)
      {
          O2GResponseReaderFactory readerFactory = session.getResponseReaderFactory();
          if (readerFactory == null)
          {
              throw new Exception("Cannot create response reader factory");
          }
          O2GLoginRules loginRules = session.getLoginRules();
          O2GResponse response = loginRules.getTableRefreshResponse(O2GTableType.Accounts);
          O2GAccountsTableResponseReader accountsResponseReader = readerFactory.createAccountsTableReader(response);
          for (int i = 0; i < accountsResponseReader.Count; i++)
          {
              O2GAccountRow accountRow = accountsResponseReader.getRow(i);
              Console.WriteLine("AccountID: {0}, Balance: {1}", accountRow.AccountID, accountRow.Balance);
          }
          return accountsResponseReader.getRow(0);
      }

## How to get price history:
For pricehistory, you need to use non-table manage. 
You can see examples under NonTableManagerSamples/GetHistPrices


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

## Disclaimer:

Trading forex/CFDs on margin carries a high level of risk and may not be suitable for all investors as you could sustain losses in excess of deposits. Leverage can work against you. The products are intended for retail and professional clients. Due to the certain restrictions imposed by the local law and regulation, German resident retail client(s) could sustain a total loss of deposited funds but are not subject to subsequent payment obligations beyond the deposited funds. Be aware and fully understand all risks associated with the market and trading. Prior to trading any products, carefully consider your financial situation and experience level. If you decide to trade products offered by FXCM Australia Pty. Limited (“FXCM AU”) (AFSL 309763), you must read and understand the [Financial Services Guide](https://docs.fxcorporate.com/financial-services-guide-au.pdf), [Product Disclosure Statement](https://www.fxcm.com/au/legal/product-disclosure-statements/), and [Terms of Business](https://docs.fxcorporate.com/tob_au_en.pdf). Any opinions, news, research, analyses, prices, or other information is provided as general market commentary, and does not constitute investment advice. FXCM will not accept liability for any loss or damage, including without limitation to, any loss of profit, which may arise directly or indirectly from use of or reliance on such information. FXCM will not accept liability for any loss or damage, including without limitation to, any loss of profit, which may arise directly or indirectly from use of or reliance on such information.
