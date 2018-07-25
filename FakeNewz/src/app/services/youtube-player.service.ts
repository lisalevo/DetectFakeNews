import { Injectable } from '@angular/core';
import { FactCheckService } from './fact-check.service';

@Injectable({
  providedIn: 'root',
})
export class YoutubePlayerService {
  private intervalID;
  constructor(private factCheckService: FactCheckService) {}

  playbackTimeHandler(state: number, player: YT.Player) {
    switch (state) {
      case 0:
      /* Video ended */
      case 2:
        /* Video paused */
        clearInterval(this.intervalID);
        break;
      case 1:
        /* Video playing */
        this.intervalID = setInterval(() => {
          this.factCheckService.getClaimAtTime(Number(player.getCurrentTime().toFixed(0)));
          console.log('current time', player.getCurrentTime().toFixed(0));
        }, 900);
        break;
    }
  }
}
