import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-speech-viewer',
  templateUrl: './speech-viewer.component.html',
  styleUrls: ['./speech-viewer.component.css'],
})
export class SpeechViewerComponent implements OnInit {
  @Input() verbalClaim: string;

  constructor() {}

  ngOnInit() {}
}
