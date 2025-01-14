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
o	This is for personal use and abides by our [EULA](https://www.fxcm.com//forms/eula/)

o	For more information, you may contact us: api@fxcm.com

## Release Note:
Our price streams are moving from http to https using TLSv1.2 since 6/16/2019, to increase security on our price servers. 
Please make sure client side software is compatible with TLSv1.2.
Clients use ForexConnect API, Java API will be affected.
The error you will get: ‘Can't connect to price server.’
if you have any questions, please reach out to api@fxcm.com.

### Due to security enhancement on our server side, http request by ForexConnect API users need switch to https.
End user need to upgrade their FC API package on their side.
First round release will target to demo environments this coming weekend. 5/1/2021
This release to demo target at 7/9/2021 

### the above release to live will target in mid-end August/2021. 
Please make sure you are ready.
Please send mail to api@fxcm.com if you have any questions. 

please upgrade the latest version at 

https://pypi.org/project/forexconnect/

https://fxcodebase.com/wiki/index.php/Download

### Performance improvment release 
We did some performance improvement and released to Demo. It should transparent to API users.

However, you are welcome to test your current setting on Demo and contact api@fxcm.com if you experience any issues.

If everything goes well, we plan to release to Production by the end of next week. Dec 17 2022.


## Disclaimer:

Stratos Group is a holding company of Stratos Markets Limited, Stratos Europe Limited, Stratos Trading Pty. Limited, Stratos South Africa (Pty) Ltd, Stratos Global LLC and all affiliates of aforementioned firms, or other firms under the Stratos Group of companies (collectively "Stratos Group").
The Stratos Group is headquartered at 20 Gresham Street, 4th Floor, London EC2V 7JE, United Kingdom. Stratos Markets Limited is authorised and regulated in the UK by the Financial Conduct Authority. Registration number 217689. Registered in England and Wales with Companies House company number 04072877. Stratos Europe Limited (trading as "FXCM"), is a Cyprus Investment Firm ("CIF") registered with the Cyprus Department of Registrar of Companies (HE 405643) and authorised and regulated by the Cyprus Securities and Exchange Commission ("CySEC") under license number 392/20. Stratos Trading Pty. Limited (trading as "FXCM") (AFSL 309763, ABN 31 121 934 432) is regulated by the Australian Securities and Investments Commission. The information provided by FXCM is intended for residents of Australia and is not directed at any person in any country or jurisdiction where such distribution or use would be contrary to local law or regulation. Please read the full Terms and Conditions. Stratos South Africa (Pty) Ltd is an authorized Financial Services Provider and is regulated by the Financial Sector Conduct Authority under registration number 46534. Stratos Global LLC ("FXCM") is incorporated in St Vincent and the Grenadines with company registration No. 1776 LLC 2022 and is an operating subsidiary within the Stratos Group. FXCM is not required to hold any financial services license or authorization in St Vincent and the Grenadines to offer its products and services. Stratos Global Services, LLC is an operating subsidiary within the Stratos Group. Stratos Global Services, LLC is not regulated and not subject to regulatory oversight.
Stratos Markets Limited: CFDs are complex instruments and come with a high risk of losing money rapidly due to leverage. 63% of retail investor accounts lose money when trading CFDs with this provider. You should consider whether you understand how CFDs work and whether you can afford to take the high risk of losing your money.
Stratos Europe Limited: CFDs are complex instruments and come with a high risk of losing money rapidly due to leverage. 63% of retail investor accounts lose money when trading CFDs with this provider. You should consider whether you understand how CFDs work and whether you can afford to take the high risk of losing your money.
Stratos Trading Pty. Limited: Trading CFDs on margin and margin FX carries a high level of risk, and may not be suitable for all investors. Retail clients could sustain a total loss of the deposited funds, but wholesale clients could sustain losses in excess of deposits. Trading CFDs on margin and margin FX does not give you any entitlements or rights to the underlying instruments.
Stratos Global LLC: Our products are traded on leverage which means they carry a high level of risk and you could lose more than your deposits. These products are not suitable for all investors. Please ensure you fully understand the risks and carefully consider your financial situation and trading experience before trading. Seek independent advice if necessary.
Past Performance: Past Performance is not an indicator of future results.
