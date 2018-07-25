import { Component, OnInit, OnChanges, SimpleChanges } from '@angular/core';
import { FactCheckService } from '../services/fact-check.service';
import { Observable } from '../../../node_modules/rxjs';

@Component({
  selector: 'app-fact-checking-panel',
  templateUrl: './fact-checking-panel.component.html',
  styleUrls: ['./fact-checking-panel.component.scss'],
})
export class FactCheckingPanelComponent implements OnInit, OnChanges {
  claims: Observable<Claim[]>;
  _claims: Claim[];
  constructor(private factCheckService: FactCheckService) {}

  ngOnInit() {
    this._claims = this.factCheckService.getClaims();
  }

  ngOnChanges(changes: SimpleChanges): void {
    // Called before any other lifecycle hook. Use it to inject dependencies, but avoid any serious work here.
    // Add '${implements OnChanges}' to the class.

    if (changes['claims'] && this.claims) {
      this.claims.subscribe();
    }
  }
}
