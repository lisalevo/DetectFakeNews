import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-timestamp',
  templateUrl: './timestamp.component.html',
  styleUrls: ['./timestamp.component.css'],
})
export class TimestampComponent implements OnInit {
  @Input() timeStamp: number;

  constructor() {}

  ngOnInit() {}
}
