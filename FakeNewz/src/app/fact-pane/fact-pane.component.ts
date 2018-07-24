import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-fact-pane',
  templateUrl: './fact-pane.component.html',
  styleUrls: ['./fact-pane.component.css'],
})
export class FactPaneComponent implements OnInit {
  @Input() claim: Claim;

  constructor() {}

  ngOnInit() {}
}
