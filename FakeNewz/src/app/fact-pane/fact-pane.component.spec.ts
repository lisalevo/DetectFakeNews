import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FactPaneComponent } from './fact-pane.component';

describe('FactPaneComponent', () => {
  let component: FactPaneComponent;
  let fixture: ComponentFixture<FactPaneComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FactPaneComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FactPaneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
