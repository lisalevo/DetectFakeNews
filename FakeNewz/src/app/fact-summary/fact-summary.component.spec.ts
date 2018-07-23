import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FactSummaryComponent } from './fact-summary.component';

describe('FactSummaryComponent', () => {
  let component: FactSummaryComponent;
  let fixture: ComponentFixture<FactSummaryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FactSummaryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FactSummaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
