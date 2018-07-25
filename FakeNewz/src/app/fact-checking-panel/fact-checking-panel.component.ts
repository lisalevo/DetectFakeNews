import { Component, OnInit, HostListener, HostBinding, AfterViewChecked } from '@angular/core';
import { FactCheckService } from '../services/fact-check.service';
import { Observable } from '../../../node_modules/rxjs';

@Component({
  selector: 'app-fact-checking-panel',
  templateUrl: './fact-checking-panel.component.html',
  styleUrls: ['./fact-checking-panel.component.scss'],
  // host: { id: 'factPanel' },
})
export class FactCheckingPanelComponent implements OnInit, AfterViewChecked {
  @HostBinding('id') id = 'factPanel';
  claims: Claim[] = [];
  claims$: Observable<Claim[]>;

  @HostListener('window.scrollHeight', ['$event'])
  onscroll(event) {
    console.log(event);
  }

  constructor(private factCheckService: FactCheckService) {}

  ngOnInit() {
    this.claims$ = this.factCheckService.getClaims();
    this.factCheckService.getClaims().subscribe({
      next(claim) {
        const panel = document.getElementById('factPanel');
        panel.scrollTop = Number.MAX_SAFE_INTEGER;
      },
    });
  }

  ngAfterViewChecked() {
    // Called after every check of the component's view. Applies to components only.
    // Add 'implements AfterViewChecked' to the class.
    this.scrollToBottom();
  }

  scrollToBottom() {
    const panel = document.getElementById('factPanel');
    panel.scrollTop = panel.scrollHeight;
  }
}
