import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { RoutingModule } from './/routing.module';
import { TimestampComponent } from './timestamp/timestamp.component';
import { VideoViewerComponent } from './video-viewer/video-viewer.component';
import { SpeechViewerComponent } from './speech-viewer/speech-viewer.component';
import { FactSummaryComponent } from './fact-summary/fact-summary.component';
import { PowerbiComponent } from './powerbi/powerbi.component';
import { FactCheckingPanelComponent } from './fact-checking-panel/fact-checking-panel.component';
import { FactPaneComponent } from './fact-pane/fact-pane.component';

import { VgCoreModule } from 'videogular2/core';
import { VgControlsModule } from 'videogular2/controls';
import { VgOverlayPlayModule } from 'videogular2/overlay-play';
import { VgBufferingModule } from 'videogular2/buffering';

@NgModule({
  declarations: [
    AppComponent,
    TimestampComponent,
    VideoViewerComponent,
    SpeechViewerComponent,
    FactSummaryComponent,
    PowerbiComponent,
    FactCheckingPanelComponent,
    FactPaneComponent,
  ],
  imports: [BrowserModule, RoutingModule, VgCoreModule, VgControlsModule, VgOverlayPlayModule, VgBufferingModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
