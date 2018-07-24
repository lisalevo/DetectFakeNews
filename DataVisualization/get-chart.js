function search(tags) {

  var url = "https://fred.stlouisfed.org/search?st=";
  var i;
  for(i=0; i < tags.length; i++) {
      url += tags[i]

      if (i < tags.length-1){
          url += "+"
      }
  }
  return url;
}

function getImage(url) {

  var request = require('request');
  var cheerio = require('cheerio');
  var url = search(["unemployment", "rate"]);


  request(url, function (error, response, html) {
    if (!error && response.statusCode == 200) {
      let $ = cheerio.load(html);
    var result = $('#series-pager > tbody > tr:nth-child(1) > td > div.col-xs-12.col-sm-10').html().trim();
      //var result = $('#series-pager > tbody > tr:nth-child(1) > td > div.col-xs-12.col-sm-10').html();
      //var graph_url = result.getElementsByTagName("a")[0].getAttribute("href")
      //var resultJSON = JSON.parse(result);
    var results = result.split(" ")[1]
    var link = results.split('"')[1];
    link = "https://fred.stlouisfed.org" + link
    console.log(link);
    }

  });


}

getImage()
