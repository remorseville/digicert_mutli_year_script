<h1 id="multi-year-certificate-life-cycle-management">Multi Year Certificate Life-cycle Management</h1>
<p>Case Usage:</p>
<ul>
<li>You purchase any order from DigiCert and reissue the certificate often to deploy to multiple servers. You are now needing details of all the versions issued and the UI only show the most recent one.</li>
<li>Using a Multi Year order, you can reissue/duplicate and set custom attributes per cert, all under the same order. There are versions with multiple expiration dates and include different “dns_names” as well. You now need every certificates details under that order and there is no single source within the UI.</li>
</ul>
<p>The problem:</p>
<ul>
<li>DigiCert’s certificate management allows the ability to reissue and duplicate certificates, even adjusting the number of names included and/or setting a custom expiration date. They give no way to track this information in one place. Only the most recent version issued will show in some cases.</li>
<li>DigiCert’s new offering of Multi year orders brings another element of management being a 6 year purchase can be made but the maximum validity any certificate can be issued is 397 days. Again, there is no current way to manage all the different versions of certificates under a single order through the UI.</li>
</ul>
<p>The current solution:</p>
<ul>
<li>Through DigiCert’s API you can call both the “reissue” and duplicate" endpoints to get lists of the data you are after. This example uses those methods to create and export a CSV of any certificate details issued from a given order number, along with the order validity date.</li>
</ul>
<p>Pre-requisites:</p>
<ul>
<li>DigiCert API key</li>
<li>DigiCert Order Number</li>
<li>Python Environment</li>
</ul>
<h3 id="csv--output-example">CSV  output example:</h3>

<table>
<thead>
<tr>
<th>#</th>
<th>certificate_id</th>
<th>thumbprint</th>
<th>serial_number</th>
<th>common_name</th>
<th>dns_names</th>
<th>status</th>
<th>valid_till</th>
<th>days_left</th>
<th>type</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>61170668</td>
<td>‘XXXXX8E1DB3F846037173A34E232C9XXXXXXXXXX’</td>
<td>‘XXXXX383EAB199955DB2EAXXXXXXXXXX’</td>
<td>‘<a href="http://domain.com">domain.com</a>’</td>
<td>“‘<a href="http://domain.com">domain.com</a>’  ‘<a href="http://www.domain.com">www.domain.com</a>’”</td>
<td>‘issued’</td>
<td>‘2021-10-23’</td>
<td>384</td>
<td>‘reissue’</td>
</tr>
<tr>
<td>2</td>
<td>66114965</td>
<td>‘XXXXX5C4578BB42DDEF820D4378FE0XXXXXXXXXX’</td>
<td>‘XXXXX2ACF5FCFE144E2725XXXXXXXXXX’</td>
<td>‘<a href="http://domain.com">domain.com</a>’</td>
<td>“‘<a href="http://domain.com">domain.com</a>’  ‘<a href="http://www.domain.com">www.domain.com</a>’”</td>
<td>‘issued’</td>
<td>‘2021-11-02’</td>
<td>394</td>
<td>‘reissue’</td>
</tr>
<tr>
<td>3</td>
<td>66115043</td>
<td>‘XXXXXF0BFA6FEE2E949060F827A44BXXXXXXXXXX’</td>
<td>‘XXXXX8B8CE07828558254XXXXXXXXXX’</td>
<td>‘<a href="http://domain.com">domain.com</a>’</td>
<td>“‘<a href="http://domain.com">domain.com</a>’  ‘<a href="http://www.domain.com">www.domain.com</a>’”</td>
<td>‘approved’</td>
<td>‘2021-11-01’</td>
<td>393</td>
<td>‘duplicate’</td>
</tr>
<tr>
<td>Order Expiration Date: 2021-12-10</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table><h3 id="script">Script:</h3>
<p><a href="https://github.com/remorseville/digicert_mutli_year_script">myp_order_details.py</a></p>

