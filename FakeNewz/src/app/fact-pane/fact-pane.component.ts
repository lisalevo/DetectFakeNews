import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-fact-pane',
  templateUrl: './fact-pane.component.html',
  styleUrls: ['./fact-pane.component.css'],
})
export class FactPaneComponent implements OnInit {
  timeStamp: number;
  claimStated: string;
  supportingDocURL: string;
  supportingDocSummary: string;
  image?: string;

  @Input() claim: Claim;

  constructor() {}

  ngOnInit() {
    this.timeStamp = this.claim.timeStamp;
    this.claimStated = this.claim.claim;
    this.supportingDocURL = this.claim.url;
    this.supportingDocSummary = this.claim.snippet;
    this.image = this.claim.image || '';
    // console.log(this.claim);
  }
}
