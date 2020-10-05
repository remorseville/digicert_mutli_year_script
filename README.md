# Multi Year Certificate Life-cycle Management

Case Usage:
* You purchase any order from DigiCert and reissue the certificate often to deploy to multiple servers. You are now needing details of all the versions issued and the UI only show the most recent one. 
* Using a Multi Year order, you can reissue/duplicate and set custom attributes per cert, all under the same order. There are versions with multiple expiration dates and include different "dns_names" as well. You now need every certificates details under that order and there is no single source within the UI. 

The problem:
* DigiCert's certificate management allows the ability to reissue and duplicate certificates, even adjusting the number of names included and/or setting a custom expiration date. They give no way to track this information in one place. Only the most recent version issued will show in some cases. 
* DigiCert new offering of Multi year orders brings another element of management being a 6 year purchase can be made but the maximum validity any certificate can be issued is 397 days. Again, there is no current way to manage all the different versions of certificates under a single order through the UI. 

The current solution:
* Through DigiCert's API you can call both the "reissue" and duplicate" endpoints to get lists of the data you are after. This example provided uses those methods to export a CSV of any certificate issued from a given order number. 

Pre-requisites:
* DigiCert API key
* DigiCert Order Number


### CSV  output example:

| \#                                  | certificate\_id | thumbprint                                  | serial\_number                      | common\_name       | dns\_names                                   | status      | valid\_till     | days\_left | type         |
|-------------------------------------|-----------------|---------------------------------------------|-------------------------------------|--------------------|----------------------------------------------|-------------|-----------------|------------|--------------|
| 1                                   | 61170668        |  'XXXXX8E1DB3F846037173A34E232C9XXXXXXXXXX' |  'XXXXX383EAB199955DB2EAXXXXXXXXXX' |  'domain\.com' |  "'domain\.com'  'www\.domain\.com'" |  'issued'   |  '2021\-10\-23' | 384        |  'reissue'   |
| 2                                   | 66114965        |  'XXXXX5C4578BB42DDEF820D4378FE0XXXXXXXXXX' |  'XXXXX2ACF5FCFE144E2725XXXXXXXXXX' |  'domain\.com' |  "'domain\.com'  'www\.domain\.com'" |  'issued'   |  '2021\-11\-02' | 394        |  'reissue'   |
| 3                                   | 66115043        |  'XXXXXF0BFA6FEE2E949060F827A44BXXXXXXXXXX' |  'XXXXX8B8CE07828558254XXXXXXXXXX' |  'domain\.com' |  "'domain\.com'  'www\.domain\.com'" |  'approved' |  '2021\-11\-01' | 393        |  'duplicate' |
| Order Expiration Date: 2021\-12\-10 |                 |                                             |                                     |                    |                                              |             |                 |            |              |

### Script:

[myp_order_details.py](https://github.com/remorseville/digicert_mutli_year_script/blob/main/myp_order_details.py)
