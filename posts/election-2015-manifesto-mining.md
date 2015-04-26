Title: Election 2015: Manifesto Mining
Abstract: Creating word frequency illustrations from the 2015 election manifestos.
Thumbnail: manifesto-mining-liberal-democrat-sml.png
Published: 2015-03-26 16:39
Updated: 2015-03-26 16:39

With the 2015 General Election just over a week away, I thought I'd read through the manifestos of the various parties, to try and help me make up my mind who should get my vote.

After an embarrassingly short period of time, I got bored and decided to make them into pretty pictures instead. Click on any image below to see the full size version.
 
## Liberal Democrats

[![Liberal Democrats](${cdn2}/img/post/manifesto-mining-liberal-democrat-sml.png "Liberal Democrats")](${cdn2}/img/post/manifesto-mining-liberal-democrat-lge.png)

Most of you will have seen word clouds before, but in case you're one of those who haven't: the bigger the word, the more times it appears in that manifesto.

As this is a developer blog, I'll mention a few technical bits and pieces: I used [PDFMiner](https://github.com/euske/pdfminer) to extract the raw text from the manifesto PDF files, then knocked together a [Python script](https://github.com/markashleybell/manifesto-miner) and a list of stop words to clean up and process the text data. The word clouds themselves are rendered using Tim Chien's [wordcloud2.js](https://github.com/timdream/wordcloud2.js).

## Labour

[![Labour](${cdn2}/img/post/manifesto-mining-labour-sml.png "Labour")](${cdn2}/img/post/manifesto-mining-labour-lge.png)

## Conservatives

[![Conservatives](${cdn2}/img/post/manifesto-mining-green-sml.png "Conservatives")](${cdn2}/img/post/manifesto-mining-green-lge.png)

## Plaid Cymru

[![Plaid Cymru](${cdn2}/img/post/manifesto-mining-plaid-cymru-sml.png "Plaid Cymru")](${cdn2}/img/post/manifesto-mining-plaid-cymru-lge.png)

## Green Party

[![Green Party](${cdn2}/img/post/manifesto-mining-green-sml.png "Green Party")](${cdn2}/img/post/manifesto-mining-green-lge.png)

## SNP

[![SNP](${cdn2}/img/post/manifesto-mining-snp-sml.png "SNP")](${cdn2}/img/post/manifesto-mining-snp-lge.png)

## UKIP

[![UKIP](${cdn2}/img/post/manifesto-mining-ukip-sml.png "UKIP")](${cdn2}/img/post/manifesto-mining-ukip-lge.png)

**These results are not in any way scientific** (or even very useful, arguably); nor do they accurately reflect party policies—although I think we can see where Plaid Cymru are going with theirs fairly unambiguously. They have not been artificially manipulated, and the order in which the illustrations appear does not indicate my support for one particular party over any other*.

 
*UKIP are a bunch of idiots, though.