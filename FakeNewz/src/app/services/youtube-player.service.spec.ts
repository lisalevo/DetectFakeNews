import { TestBed, inject } from '@angular/core/testing';

import { YoutubePlayerService } from './youtube-player.service';

describe('YoutubePlayerService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [YoutubePlayerService]
    });
  });

  it('should be created', inject([YoutubePlayerService], (service: YoutubePlayerService) => {
    expect(service).toBeTruthy();
  }));
});
