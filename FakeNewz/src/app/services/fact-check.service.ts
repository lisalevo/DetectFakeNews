// import { Injectable } from '@angular/core';

// @Injectable({
//   providedIn: 'root',
// })

export interface TimeToClaimMap {
  [time: number]: Claim
}

export class FactCheckService {
  claims: Claim[] = [];
  parsedClaims: Claim[] = [];
  map: TimeToClaimMap = {};

  jsonResponse = `
  [{
		"claim": "we are finally seeing rising wages",
		"timeStamp": 2,
		"similarity": 0.5992820158508968,
		"snippet": " To be fair, those making the case for monetary tightening are more thoughtful and less overtly political than the archons of austerity who drove the last wrong turn in policy. But the advice they're giving could be just as destructive.  O.K., where is this coming from?",
		"url": "https://www.nytimes.com/2014/03/14/opinion/krugman-fear-of-wages.html"
	},
	{
		"claim": "African American unemployment stands at the lowest rate ever recorded",
		"timeStamp": 10,
		"similarity": 0.8332253645445977,
		"snippet": " Trump has pushed back against reports and denied he is a racist.  Trump earlier this month tweeted about the African-American and Hispanic unemployment rates shortly after 'Fox & Friends' ran a segment on new unemployment statistics.  African American unemployment is the lowest ever recorded in our country. Trump wrote on Twitter.  The Hispanic unemployment rate dropped a full point in the last year and is close to the lowest in recorded history.Dems did nothing for you but get your vote!#NeverForget @foxandfriends, the president added.  His tweet followed an Associated Press report that included new numbers showing that the African-American unemployment rate reached a record low in December, at 6.8 percent.",
		"url": "http://thehill.com/homenews/administration/371084-trump-fires-back-at-jay-z-black-unemployment-is-at-the-lowest-rate"
	},
	{
		"claim": "and Hispanic American unemployment has also reached the lowest levels in history",
		"timeStamp": 12,
		"similarity": 0,
		"snippet": "None",
		"url": "None"
	},
	{
		"claim": "Small-business confidence is at an all-time high",
		"timeStamp": 15,
		"similarity": 0.8435751759901396,
		"snippet": " The NFIB survey is one of a slew of readings -- such as consumer confidence and manufacturer surveys from the various Federal Reserve branches -- that have improved over the past year. So far, that has contributed to a solid increase in economic activity, but not exceeding the long-term trend for the post-recession recovery.",
		"url": "http://www.businessinsider.com/small-business-optimism-tax-reform-record-level-2018-1"
	},
	{
		"claim": "The stock market has smashed one record after another",
		"timeStamp": 20,
		"similarity": 0.7370673769012361,
		"snippet": " The tech-heavy Nasdaq Composite briefly topped the 7,000-point mark for the first time in mid-day trading on Monday before closing slightly under that milestone. The Nasdaq saw the largest percentage gain on Monday (0.8%, or 58 points) among the three major indices, with streaming device company Roku (up more than 7%) and snack company Snyders - Lance(up 7 % on news of a sale to Campbell Soup) among the notable Nasdaq stocks that saw gains today.",
		"url": "http://fortune.com/2017/12/18/stock-market-record-highs/"
	},
	{
		"claim": "we enacted the biggest tax cuts and reforms in American history",
		"timeStamp": 25,
		"similarity": 0.7841961190130515,
		"snippet": "WASHINGTON -- President Trump on Wednesday proposed sharp reductions in individual and business income tax rates and a radical reordering of the tax code that would significantly benefit the wealthy, but he offered no explanation of how the plan would be financed as he rushed to show progress before the 100-day mark of his presidency.",
		"url": "https://www.nytimes.com/2017/04/26/us/politics/trump-tax-cut-plan.html"
	},
	{
		"claim": "we nearly doubled the standard deduction for everyone",
		"timeStamp": 29,
		"similarity": 0.7317973911795083,
		"snippet": " The top individual rate is expected to be lowered from 39.6 percent to 35 percent, while the lowest rate is expected to be increased from 10 percent to 12 percent. However, the increase in the standard deduction is designed to prevent anyone in the 10 percent bracket from paying more taxes.  The framework document was only developed by Republicans, but Trump has been reaching out to Democrats in an effort to get their support on tax reform as well.  Its time for both parties to come together and do what is right for the American people and the nation that we all love.",
		"url": "https://www.hrblock.com/tax-center/irs/tax-reform/new-child-tax-credit/"
	},
	{
		"claim": "We also doubled the child tax credit.",
		"timeStamp": 30,
		"similarity": 0.7778124613113094,
		"snippet": " Rubio said the credit should be able to count against payroll taxes so taxpayers who don't income tax can still be able to claim the benefit.When President Donald Trump unveiled his tax reform plan Sept.27, he called for a substantially increased child tax credit though he didnt offer any specifics on the number.  He said his plan would cut taxes for the middle class and make the tax code simpler.",
		"url": "https://www.upi.com/Top_News/US/2017/10/25/Ivanka-Trump-Republican-lawmakers-push-double-child-tax-credit/3441508967874/"
	}
]`;
  
  constructor() {
    this.parsedClaims = JSON.parse(this.jsonResponse) as Claim[];
    this.parsedClaims.forEach(claim => {
      this.map[claim.timeStamp] = claim;
    });
  }

  getClaims(): Claim[] {
    return this.claims;
  }

  getClaimAtTime(time: number): Claim {
    return (time in this.map) ? this.map[time] : null;
  }

}
