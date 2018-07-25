import { Component, OnInit, SimpleChanges, Input } from '@angular/core';
import { Observable } from '../../../node_modules/rxjs';

@Component({
  selector: 'app-video-viewer',
  templateUrl: './video-viewer.component.html',
  styleUrls: ['./video-viewer.component.css'],
})
export class VideoViewerComponent implements OnInit {
  player: YT.Player;
  private id = 'cq3NwepDLHY';
  private observable = Observable.create(observer => {
    observer.next('Starting process...');
  });
  private intervalID;

  savePlayer(player) {
    this.player = player;
    console.log('player instance', player);
  }
  onStateChange(event) {
    switch (event.data) {
      case 0:
      /* Video ended */
      case 2:
        /* Video paused */
        clearInterval(this.intervalID);
        break;
      case 1:
        /* Video playing */
        this.intervalID = setInterval(() => {
          console.log('current time', this.player.getCurrentTime().toFixed(0));
        }, 900);
        break;
    }

    // console.log('current time', this.player.getCurrentTime());
    console.log('player state', event.data);
  }
  constructor() {}

  ngOnInit() {}

  ngOnChanges(changes: SimpleChanges): void {
    // Called before any other lifecycle hook. Use it to inject dependencies, but avoid any serious work here.
    // Add '${implements OnChanges}' to the class.
  }
}
