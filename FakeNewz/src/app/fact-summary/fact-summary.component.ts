import { Component, OnInit, Input } from '@angular/core';
import { FactCheckService } from '../services/fact-check.service';

@Component({
  selector: 'app-fact-summary',
  templateUrl: './fact-summary.component.html',
  styleUrls: ['./fact-summary.component.css'],
})
export class FactSummaryComponent implements OnInit {
  @Input() supportingDocSummary: string;
  constructor() {}

  ngOnInit() {}
}
