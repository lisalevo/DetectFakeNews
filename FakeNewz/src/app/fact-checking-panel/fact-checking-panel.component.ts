import { Component, OnInit } from '@angular/core';
import { FactCheckService } from '../services/fact-check.service';

@Component({
  selector: 'app-fact-checking-panel',
  templateUrl: './fact-checking-panel.component.html',
  styleUrls: ['./fact-checking-panel.component.scss'],
})
export class FactCheckingPanelComponent implements OnInit {
  claims: Claim[] = [];
  constructor(private factCheckService: FactCheckService) {}

  ngOnInit() {
    this.claims = this.factCheckService.getClaims();
  }

  checkTimeStap() {}
}
