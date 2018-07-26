import { FactCheckService } from './../services/fact-check.service';
import { Component, OnInit, SimpleChanges, Input } from '@angular/core';
import { Observable } from '../../../node_modules/rxjs';
import { YoutubePlayerService } from '../services/youtube-player.service';

@Component({
  selector: 'app-video-viewer',
  templateUrl: './video-viewer.component.html',
  styleUrls: ['./video-viewer.component.css'],
})
export class VideoViewerComponent implements OnInit {
  player: YT.Player;
  private id = 'cq3NwepDLHY';
  private intervalID;

  constructor(private factCheckService: FactCheckService, private YTPlayerService: YoutubePlayerService) {}

  ngOnInit() {}

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
          this.factCheckService.getClaimAtTime(Number(this.player.getCurrentTime().toFixed(0)));
          //console.log('current time', this.player.getCurrentTime().toFixed(0));
        }, 1000);
        break;
    }
    // console.log('player state', event.data);
  }
}
