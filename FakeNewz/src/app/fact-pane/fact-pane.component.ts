import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-fact-pane',
  templateUrl: './fact-pane.component.html',
  styleUrls: ['./fact-pane.component.css'],
})
export class FactPaneComponent implements OnInit {
  private timeStamp: number;
  private claimStated: string;
  private supportingDocURL: string;
  private supportingDocSummary: string;
  private supportingImg?: string;

  @Input() claim: Claim;

  constructor() {}

  ngOnInit() {
    this.timeStamp = this.claim.timeStamp;
    this.claimStated = this.claim.claim;
    this.supportingDocURL = this.claim.supportingDocURL;
    this.supportingDocSummary = this.claim.supportingDocSummary;
    this.supportingImg = this.claim.supportingImg;
    // console.log(this.claim);
  }
}
