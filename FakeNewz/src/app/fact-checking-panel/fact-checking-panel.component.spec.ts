import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FactCheckingPanelComponent } from './fact-checking-panel.component';

describe('FactCheckingPanelComponent', () => {
  let component: FactCheckingPanelComponent;
  let fixture: ComponentFixture<FactCheckingPanelComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FactCheckingPanelComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FactCheckingPanelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
