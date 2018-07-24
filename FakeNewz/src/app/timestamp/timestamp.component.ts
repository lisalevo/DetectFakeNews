import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-timestamp',
  templateUrl: './timestamp.component.html',
  styleUrls: ['./timestamp.component.css'],
})
export class TimestampComponent implements OnInit {
  timeAsserted = '0:00';

  constructor() {}

  ngOnInit() {}
}
