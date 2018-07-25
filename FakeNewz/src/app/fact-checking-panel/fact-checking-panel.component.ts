import { Component, OnInit, OnChanges, SimpleChanges } from '@angular/core';
import { FactCheckService } from '../services/fact-check.service';
import { Observable } from '../../../node_modules/rxjs';

@Component({
  selector: 'app-fact-checking-panel',
  templateUrl: './fact-checking-panel.component.html',
  styleUrls: ['./fact-checking-panel.component.scss'],
})
export class FactCheckingPanelComponent implements OnInit, OnChanges {
  claims: Claim[] = [];
  constructor(private factCheckService: FactCheckService) {}

  ngOnInit() {
    for (let i = 0; i < 35; i++) {
      const claim = this.factCheckService.getClaimAtTime(i);
      if (claim != null) this.claims.push(claim);
    }
  }

  ngOnChanges(changes: SimpleChanges): void {}

  scrollToBottom() {
    const panel = document.getElementById('factPanel');
    panel.scrollTop = Number.MAX_SAFE_INTEGER;
  }
}
