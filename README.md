CFDs are complex instruments and come with a high risk of losing money rapidly due to leverage.

**70.24% of retail investor accounts lose money when trading CFDs with this provider.**

You should consider whether you understand how CFDs work and whether you can afford to take the high risk of losing your money.

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
6) ForexConnect sample code for Android/iOS/macOS/Python/Linux/Windows, at [here](https://github.com/gehtsoft/forex-connect/tree/master/samples).
7) ForexConnect on Python at [here](http://fxcodebase.com/code/viewforum.php?f=51)

## Connect parameters:
1) URL="www.fxcorporate.com/Hosts.jsp"
2) Username="you username"
3) Password="your password"
4) Connection="demo"
5) You can ignore SessionID and PIN

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

## Release Note:
Our price streams are moving from http to https using TLSv1.2 since 6/16/2019, to increase security on our price servers. 
Please make sure client side software is compatible with TLSv1.2.
Clients use ForexConnect API, Java API will be affected.
The error you will get: ‘Can't connect to price server.’
if you have any questions, please reach out to api@fxcm.com.

## Disclaimer:

High Risk Investment Notice: 

Trading Forex/CFDs on margin carries a high level of risk and may not be suitable for all investors. The products are intended for retail, professional, and eligible counterparty clients. Retail clients who maintain account(s) with Forex Capital Markets Limited (“FXCM LTD”) could sustain a total loss of deposited funds but are not subject to subsequent payment obligations beyond the deposited funds but professional clients and eligible counterparty clients could sustain losses in excess of deposits. Clients who maintain account(s) with FXCM Australia Pty. Limited (“FXCM AU”), FXCM South Africa (PTY) Ltd (“FXCM ZA”) or FXCM Markets Limited (“FXCM Markets”) could sustain losses in excess of deposits. Prior to trading any products offered by [FXCM LTD](https://www.fxcm.com/uk/), inclusive of all EU branches, [FXCM AU](https://www.fxcm.com/au/), [FXCM ZA](https://www.fxcm.com/za/), any affiliates of aforementioned firms, or other firms within the FXCM group of companies [collectively the “FXCM Group”], carefully consider your financial situation and experience level. If you decide to trade products offered by FXCM AU (AFSL 309763), you must read and understand the [Financial Services Guide](https://docs.fxcorporate.com/financial-services-guide-au.pdf), [Product Disclosure Statement](https://www.fxcm.com/au/legal/product-disclosure-statements/), and [Terms of Business](https://docs.fxcorporate.com/tob_au_en.pdf). Our Forex/CFD prices are set by FXCM, are not made on an Exchange and are not governed under the Financial Advisory and Intermediary Services Act. The FXCM Group may provide general commentary, which is not intended as investment advice and must not be construed as such. Seek advice from a separate financial advisor. The FXCM Group assumes no liability for errors, inaccuracies or omissions; does not warrant the accuracy, completeness of information, text, graphics, links or other items contained within these materials. Read and understand the Terms and Conditions on the FXCM Group’s websites prior to taking further action. 
