import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SpeechViewerComponent } from './speech-viewer.component';

describe('SpeechViewerComponent', () => {
  let component: SpeechViewerComponent;
  let fixture: ComponentFixture<SpeechViewerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SpeechViewerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SpeechViewerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
