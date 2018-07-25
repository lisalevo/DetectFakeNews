import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-timestamp',
  templateUrl: './timestamp.component.html',
  styleUrls: ['./timestamp.component.css'],
})
export class TimestampComponent implements OnInit {
  @Input() timeStamp: number;
  formattedTime: string;

  constructor() { }

  ngOnInit() {
    this.formattedTime = this.timeFormatter(this.timeStamp);

  }

  timeFormatter(time: number): string {
    var hours = Math.floor(time / 3600);
    time = time - hours * 3600;
    var minutes = Math.floor(time / 60);
    var seconds = time - minutes * 60;

    if (hours > 0) {
      var finalTime = hours.toString() + ':' + this.formatNumber(minutes) + ':' + this.formatNumber(seconds);
    } else {
      var finalTime = minutes.toString() + ':' + this.formatNumber(seconds);
    }
    return finalTime;
  }

  formatNumber(num: number): string {
    var rtn = num.toString();
    if (num < 10) {
      rtn = "0" + rtn;
    }
    return rtn;
  }
}
